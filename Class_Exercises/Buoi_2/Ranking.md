# Giới thiệu về Ranking
Ranking là việc sắp xếp các tài liệu theo mức độ liên quan để tìm nội dung quan tâm liên quan đến truy vấn. Đây là vấn đề cơ bản của Truy xuất thông tin, được sử dụng trong nhiều trường hợp khác nhau:
- **Công cụ tìm kiếm**: Với hồ sơ người dùng (vị trí, độ tuổi, giới tính,…), một truy vấn dạng văn bản, hãy sắp xếp kết quả trang web theo mức độ liên quan.
- **Hệ thống đề xuất**: Với hồ sơ người dùng và lịch sử mua hàng, hãy sắp xếp các mục khác để tìm các sản phẩm mới có khả năng thú vị cho người dùng.
- **Các công ty du lịch**: Với hồ sơ người dùng và bộ lọc (ngày nhận phòng/trả phòng, số lượng và độ tuổi của khách du lịch,…), hãy sắp xếp các phòng có sẵn theo mức độ liên quan.

# Sử dụng ML trong Ranking
Để xây dựng ML Ranking Model, cần phải xác định đầu vào, đầu ra và hàm mất mát (Loss Function):

- **Input**: Đối với truy vấn q, có n tài liệu D = {d₁, …, dₙ} được xếp hạng theo mức độ liên quan. Các phần tử xᵢ = (q, dᵢ) là đầu vào cho mô hình.
- **Output**: Đối với đầu vào tài liệu truy vấn xᵢ = (q, dᵢ), giả sử tồn tại điểm liên quan thực sự yᵢ. Mô hình đưa ra điểm dự đoán sᵢ = f(xᵢ).

Tất cả các mô hình ML xếp hạng đều sử dụng mô hình học máy cơ sở (ví dụ: Decision Tree hoặc Neural Network) để tính toán s = f(x). Lựa chọn hàm mất mát là yếu tố đặc biệt đối với các model hình Ranking Model.

## Trình bày phương pháp PointWise
- **Mô tả**: Phương pháp PointWise xem xét từng điểm dữ liệu độc lập. Trong ngữ cảnh xếp hạng hoặc học máy, từng điểm dữ liệu được coi như một đơn vị riêng biệt, và mục tiêu là dự đoán điểm hoặc nhãn (label) của từng điểm.
- **Đặc điểm**:
    - Sử dụng các thuật toán học có giám sát thông thường như hồi quy tuyến tính hoặc phân loại.
    - Không quan tâm đến mối quan hệ giữa các điểm dữ liệu hoặc sự tương quan trong tập hợp.
- **Ưu điểm**:
    - Dễ triển khai và hiểu.
    - Hiệu quả khi không cần xem xét mối quan hệ giữa các điểm dữ liệu.
    - Phù hợp với các bài toán đơn giản.
- **Nhược điểm**:
    - Không tận dụng được thông tin từ sự tương quan giữa các điểm dữ liệu.
    - Trong bài toán xếp hạng, không tối ưu hóa trực tiếp thứ hạng toàn cục.
- **Ví dụ**: Dự đoán điểm số hoặc nhãn lớp của một đối tượng (chẳng hạn như dự đoán doanh thu hàng ngày từ dữ liệu).

## Trình bày phương pháp Pairwise
- **Mô tả**: Phương pháp Pairwise so sánh các cặp dữ liệu để học mối quan hệ giữa chúng. Nó thường được sử dụng trong bài toán xếp hạng, trong đó mục tiêu là xác định thứ tự ưu tiên giữa các đối tượng.
- **Đặc điểm**:
    - Tạo ra các cặp dữ liệu từ tập gốc, mỗi cặp thể hiện mối quan hệ giữa hai điểm dữ liệu.
    - Học máy dựa trên mối quan hệ của từng cặp thay vì dựa trên từng điểm độc lập.
- **Ưu điểm**:
    - Hiệu quả trong bài toán xếp hạng vì tận dụng được sự tương quan giữa các điểm dữ liệu.
    - Giảm độ phức tạp so với các phương pháp dựa trên thứ hạng toàn cục (Listwise).
- **Nhược điểm**:
    - Tăng kích thước dữ liệu (số cặp thường lớn hơn nhiều so với số điểm gốc).
    - Đòi hỏi nhiều tài nguyên tính toán hơn so với PointWise.
- **Ví dụ**: Trong xếp hạng kết quả tìm kiếm, so sánh hai tài liệu để xác định tài liệu nào quan trọng hơn.

## Trình bày phương pháp Listwise
- **Mô tả**: Phương pháp Listwise sử dụng toàn bộ danh sách hoặc tập hợp các điểm dữ liệu trong một nhóm (list) để học thứ tự ưu tiên hoặc dự đoán nhãn. Đây là cách tiếp cận toàn diện nhất trong bài toán xếp hạng.
- **Đặc điểm**:
    - Học trên toàn bộ tập hợp dữ liệu thay vì từng điểm hoặc cặp riêng lẻ.
    - Tối ưu hóa trực tiếp thứ hạng toàn cục của dữ liệu.
- **Ưu điểm**:
    - Tận dụng toàn bộ thông tin trong tập dữ liệu.
    - Hiệu quả nhất trong việc tối ưu hóa thứ hạng tổng thể.
- **Nhược điểm**:
    - Phức tạp hơn so với PointWise và Pairwise.
    - Yêu cầu tài nguyên tính toán cao và khó triển khai trên tập dữ liệu lớn.
- **Ví dụ**: Xếp hạng kết quả tìm kiếm cho một truy vấn, tối ưu hóa toàn bộ danh sách các tài liệu liên quan để trả về thứ tự tốt nhất.
