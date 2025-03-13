from flask import Flask, jsonify, request, render_template
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import pandas as pd

from ConnectMySQL import Connector
import io
import base64

app = Flask(__name__)

# Database connection
conn = Connector(
    server='localhost',
    port=3306,
    database='sakila',
    username='root',
    password="nguyin"
)
conn.connect()

# Load data
customer = conn.GetTableData('customer')
film = conn.GetTableData('film')
inventory = conn.GetTableData('inventory')
rental = conn.GetTableData('rental')

# Merge the necessary tables to get the required information
customer_rental = pd.merge(customer, rental, on='customer_id', suffixes=('_customer', '_rental'))
customer_rental_inventory = pd.merge(customer_rental, inventory, on='inventory_id', suffixes=('_rental', '_inventory'))
customer_rental_inventory_film = pd.merge(customer_rental_inventory, film, on='film_id', suffixes=('_inventory', '_film'))

# Calculate total payment
total_payment = customer_rental_inventory_film.groupby('customer_id')['rental_rate'].sum().reset_index()
total_payment.columns = ['customer_id', 'TotalPayment']

# Calculate rental frequency
rental_frequency = customer_rental_inventory_film.groupby('customer_id')['rental_id'].count().reset_index()
rental_frequency.columns = ['customer_id', 'RentalFrequency']

# Calculate average film length
average_film_length = customer_rental_inventory_film.groupby('customer_id')['length'].mean().reset_index()
average_film_length.columns = ['customer_id', 'AverageFilmLength']

# Calculate favorite rating
favorite_rating = customer_rental_inventory_film.groupby(['customer_id', 'rating']).size().reset_index(name='count')
favorite_rating = favorite_rating.loc[favorite_rating.groupby('customer_id')['count'].idxmax()]
favorite_rating = favorite_rating[['customer_id', 'rating']]
favorite_rating.columns = ['customer_id', 'FavoriteRating']

# Merge all the calculated data
df = pd.merge(customer[['customer_id', 'first_name', 'last_name']], total_payment, left_on="customer_id", right_on="customer_id")
df = pd.merge(df, rental_frequency, on='customer_id')
df = pd.merge(df, favorite_rating, on='customer_id')
df = pd.merge(df, average_film_length, on='customer_id')

# Rename columns
df.columns = ['CustomerId', 'FirstName', 'LastName', 'TotalPayment', 'RentalFrequency', 'FavoriteRating', 'AverageFilmLength']

# Create a mapping dictionary for favorite ratings
rating_mapping = {
    'G': 1,
    'PG': 2,
    'PG-13': 3,
    'R': 4,
    'NC-17': 5
}

# Map the favorite ratings to numbers
df['FavoriteRatingNumber'] = df['FavoriteRating'].map(rating_mapping)

# Standardize the data
scaler = StandardScaler()
cluster_columns = ['TotalPayment', 'RentalFrequency', 'FavoriteRatingNumber', 'AverageFilmLength']
X = scaler.fit_transform(df[cluster_columns])

# Find optimal clusters
def find_optimal_clusters(X, max_k=10):
    inertia = []
    silhouette_scores = []
    for k in range(2, max_k + 1):
        kmeans = KMeans(n_clusters=k, init='k-means++', max_iter=500, random_state=42)
        kmeans.fit(X)
        inertia.append(kmeans.inertia_)
        if k > 1:
            score = silhouette_score(X, kmeans.labels_)
            silhouette_scores.append(score)

    return inertia, silhouette_scores

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# Route to find optimal clusters
@app.route('/find_optimal_clusters')
def optimal_clusters():
    inertia, silhouette_scores = find_optimal_clusters(X)
    import matplotlib.pyplot as plt

    # Plot inertia
    plt.figure(figsize=(10, 6))
    plt.plot(range(2, len(inertia) + 2), inertia, marker='o', linestyle='--')
    plt.title('Inertia vs. Number of Clusters')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Inertia')
    inertia_img = io.BytesIO()
    plt.savefig(inertia_img, format='png')
    inertia_img.seek(0)
    with open('SakilaMachineLearning\\templates\\images\\inertia_plot.png', 'wb') as f:
        f.write(inertia_img.getvalue())
    
    # Plot silhouette scores
    plt.figure(figsize=(10, 6))
    plt.plot(range(3, len(silhouette_scores) + 3), silhouette_scores, marker='o', linestyle='--')
    plt.title('Silhouette Score vs. Number of Clusters')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Silhouette Score')
    silhouette_img = io.BytesIO()
    plt.savefig(silhouette_img, format='png')
    silhouette_img.seek(0)
    silhouette_plot_url = base64.b64encode(silhouette_img.getvalue()).decode()

    return render_template("optimal_cluster.html")
# Route to perform clustering
@app.route('/perform_clustering', methods=['POST'])
def perform_clustering():
    cluster = request.json.get('cluster', 3)
    kmeans = KMeans(n_clusters=cluster, init='k-means++', max_iter=500, random_state=42)
    y_kmeans = kmeans.fit_predict(X)
    centroids = scaler.inverse_transform(kmeans.cluster_centers_)
    df['cluster'] = y_kmeans
    
    import matplotlib.pyplot as plt

    # Plot the clusters
    plt.figure(figsize=(10, 6))
    plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='red', marker='X')
    plt.title('Customer Clusters')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')

    # Save the plot to a BytesIO object
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return jsonify({'centroids': centroids.tolist(), 'clusters': y_kmeans.tolist(), 'plot_url': plot_url})

# Route to get customer by cluster
@app.route('/get_customer_by_cluster/<int:cluster_id>')
def get_customer_by_cluster(cluster_id):
    if cluster_id not in df["cluster"].unique():
        return jsonify({'error': f"Cluster {cluster_id} does not exist."}), 404
    cluster_data = df[df["cluster"] == cluster_id]
    return cluster_data[['CustomerId', 'TotalPayment', 'RentalFrequency', 'FavoriteRating', 'cluster']].to_json(orient='records')

if __name__ == '__main__':
    app.run(debug=True)
