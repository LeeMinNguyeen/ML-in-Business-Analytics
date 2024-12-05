<h1 align="center">
<strong>CÂU HỎI THẢO LUẬN</strong>
</h1>



# Câu 1: Trình bày ưu điểm và nhược điểm của Filtering Out Missing Data và Filling In Missing Data
## Filtering Out Missing Data
- **Mô tả**: Loại bỏ các hàng hoặc cột chứa giá trị thiếu (missing values).
- **Ưu điểm**:
    - Đơn giản, dễ thực hiện.
    - Tránh các sai lệch hoặc kết quả không chính xác do sử dụng dữ liệu thiếu.
    - Phù hợp khi tỷ lệ dữ liệu thiếu rất nhỏ và không gây mất mát thông tin quan trọng.
- **Nhược điểm**:
    - Làm mất một phần dữ liệu, có thể dẫn đến mất thông tin quan trọng hoặc làm giảm kích thước mẫu.
    - Không phù hợp khi tỷ lệ dữ liệu thiếu lớn, vì sẽ gây giảm chất lượng phân tích.

## Filling In Missing Data
- **Mô tả**: Điền giá trị thay thế vào chỗ thiếu bằng cách sử dụng giá trị trung bình, giá trị thường gặp nhất (mode), giá trị từ một mô hình dự đoán, hoặc các phương pháp khác.
- **Ưu điểm**:
    - Giữ lại toàn bộ dữ liệu gốc, không làm giảm kích thước mẫu.
    - Phù hợp khi dữ liệu thiếu ở mức độ trung bình và có sự nhất quán.
    - Có thể cải thiện kết quả phân tích nếu điền dữ liệu đúng cách.
- **Nhược điểm**:
    - Nếu giá trị được điền không phản ánh thực tế, có thể gây sai lệch cho kết quả phân tích.
    - Một số phương pháp (như dự đoán bằng mô hình) có thể phức tạp và tốn tài nguyên tính toán.
    - Dữ liệu sau khi được điền không còn phản ánh chính xác bản chất của dữ liệu gốc.

# Câu 2: Trình bày phương pháp PointWise
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

# Câu 3: Trình bày phương pháp Pairwise
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

# Câu 4: Trình bày phương pháp Listwise
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

# Câu 5: Trình bày mô hình Machine Translation của Amazon
<img src="./Images/Machine_Translation_Amazon.png"/>

- Dịch vụ **Amazon Translate** sử dụng công nghệ máy học tiên tiến (machine learning) để thực hiện dịch thuật văn bản tự động, chất lượng cao, theo nhu cầu.
- Dịch vụ hỗ trợ hơn **5,500 cặp ngôn ngữ dịch** khác nhau.
- Tài liệu hoặc văn bản được dịch có thể được lưu trữ trên **Amazon S3**, duy trì nguyên vẹn định dạng.

## **Quy trình chính**

1. **Upload tài liệu**
    - Tài liệu được tải lên Amazon S3 trong định dạng UTF-8.
    - Các tài liệu này có thể là văn bản đơn giản hoặc tài liệu phức tạp với định dạng rõ ràng.

2. **Amazon Translate xử lý tài liệu**
Amazon Translate thực hiện quá trình dịch tự động với các tính năng:
    - **Document Translation:** Hỗ trợ dịch toàn bộ tài liệu, giữ nguyên định dạng ban đầu.
    - **Active Custom Translation:** Cho phép người dùng tùy chỉnh quá trình dịch theo nhu cầu, chẳng hạn như thay đổi cách dịch thuật ngữ chuyên ngành.
    - **Custom Terminology:** Người dùng có thể định nghĩa bộ từ điển riêng để Amazon Translate ưu tiên sử dụng các thuật ngữ đã định nghĩa.
    - **Profanity Masking:** Lọc các từ ngữ không phù hợp (ví dụ: từ ngữ tục tĩu) trong văn bản đầu ra.
    - **Formality Configuration:** Điều chỉnh mức độ trang trọng (formality level) của văn bản được dịch.
    - **Automatic Source Language Detection:** Tự động nhận diện ngôn ngữ của văn bản nguồn mà không cần chỉ định trước.

3. **Trả kết quả**
    - Dịch vụ trả về tài liệu đã dịch trong định dạng UTF-8.
    - Các tài liệu đã dịch có thể được lưu trên Amazon S3 với định dạng, bố cục được giữ nguyên, hoặc chỉ trả về dưới dạng văn bản thuần túy.

## **Ưu điểm chính của Amazon Translate**
- **Chất lượng dịch thuật cao:** Sử dụng công nghệ học sâu để tối ưu hóa chất lượng dịch thuật.
- **Tùy chỉnh mạnh mẽ:** Hỗ trợ các tính năng tùy chỉnh như thuật ngữ riêng, độ trang trọng, và lọc ngôn ngữ.
- **Tính tự động:** Tích hợp liền mạch với các dịch vụ AWS khác, tự động hóa quy trình dịch và lưu trữ.
- **Khả năng mở rộng:** Hỗ trợ số lượng lớn dữ liệu và ngôn ngữ, phù hợp với các tổ chức lớn.
- **Bảo toàn định dạng:** Dịch thuật tài liệu mà không làm mất định dạng gốc, rất hữu ích cho các tài liệu kinh doanh hoặc kỹ thuật.

## **Ứng dụng thực tế**
- **Thương mại điện tử:** Dịch mô tả sản phẩm cho khách hàng quốc tế.
- **Dịch vụ khách hàng:** Hỗ trợ tự động dịch nội dung email hoặc tài liệu.
- **Truyền thông đa ngôn ngữ:** Tạo nội dung cho nhiều thị trường trên toàn cầu.

# Câu 6: Trình bày mô hình Machine Translation của Google
<img src="./Images/Machine_Translation_Google.png"/>

Google Translate sử dụng các công nghệ hiện đại như **Neural Machine Translation (NMT)** và **Speech-to-Text Translation (ST)** để thực hiện dịch thuật. Hệ thống này hỗ trợ nhiều nguồn đầu vào khác nhau và trả về các loại đầu ra phù hợp với mục đích sử dụng.

## **Quy trình chính và thành phần**
1. **Đầu vào**
    - **Text (Văn bản)**: Văn bản thông thường do người dùng nhập.
    - **Pen (Viết tay)**: Sử dụng công nghệ OCR để nhận diện và chuyển đổi chữ viết tay thành văn bản.
    - **Mic (Âm thanh)**: Dùng công nghệ nhận diện giọng nói (Speech Recognition) để chuyển lời nói thành văn bản.
    - **Camera**: Xử lý văn bản trong hình ảnh thông qua **Scene Text OCR**.
    - **Conversation (Hội thoại)**: Dịch trực tiếp các cuộc hội thoại thời gian thực.
    - **Transcribe (Ghi âm)**: Chuyển đổi lời nói ghi âm thành văn bản và dịch.

2. **Xử lý dữ liệu**: Google Translate sử dụng hai công nghệ chính:
    - **Neural Machine Translation (NMT):**
        - Đây là cốt lõi của Google Translate, sử dụng mạng nơ-ron sâu (Deep Neural Network) để thực hiện dịch thuật văn bản một cách chính xác và tự nhiên.
        - NMT học từ ngữ cảnh và cấu trúc của câu để cung cấp bản dịch chất lượng cao.
    - **Speech-to-Text Translation (ST):**
        - Chuyển đổi giọng nói thành văn bản và sau đó áp dụng NMT để dịch ngôn ngữ.

3. **Các tính năng bổ sung**
    - **GAN (Generative Adversarial Networks):**
        - Được sử dụng trong xử lý hình ảnh và dịch văn bản trực tiếp trên ảnh (Text-over-Image).
        - **Ví dụ**: Dịch một đoạn văn bản trong ảnh và trả kết quả ngay trên ảnh gốc.
   
    - **Text-to-Speech Synthesis:**
        - Sau khi dịch, hệ thống chuyển văn bản dịch thành giọng nói, hỗ trợ giao tiếp bằng lời.

4. **Đầu ra**
    - **Text (Văn bản)**: Trả về văn bản đã dịch.
    - **Text-over-Image**: Văn bản được dịch trực tiếp hiển thị trên hình ảnh ban đầu.
    - **Speech (Âm thanh)**: Đọc bản dịch dưới dạng âm thanh.

## **Ưu điểm chính của mô hình Google Translate**
- **Hỗ trợ đa dạng đầu vào:** Văn bản, giọng nói, hình ảnh, và chữ viết tay.
- **Neural Machine Translation (NMT):** Dịch thuật chính xác và tự nhiên hơn so với các phương pháp truyền thống.
- **Tích hợp mạnh mẽ:** Kết hợp OCR, nhận diện giọng nói, và GAN để mở rộng ứng dụng trong nhiều ngữ cảnh thực tế.
- **Đa ngôn ngữ:** Hỗ trợ hơn 100 ngôn ngữ.
- **Thời gian thực:** Có khả năng dịch nhanh chóng, bao gồm hội thoại trực tiếp.

## **Ứng dụng thực tế**
- **Du lịch:** Dịch biển hiệu, menu, hoặc hội thoại trong thời gian thực.
- **Học tập:** Dịch tài liệu nghiên cứu hoặc bài viết.
- **Truyền thông:** Hỗ trợ dịch các bài viết, email, và thông tin truyền thông.
- **Công việc hàng ngày:** Dịch các cuộc hội thoại hoặc nội dung viết tay.

# Câu 7: Hãy sử dụng Python triệu gọi Google API để viết App dịch một đoạn văn
> https://codelabs.developers.google.com/codelabs/cloud-translation-python3#0 

# Câu 8: Tìm hiểu Looker
> https://cloud.google.com/looker?hl=en

Looker là nền tảng trí tuệ kinh doanh (BI) của Google Cloud, giúp người dùng khám phá, phân tích và chia sẻ dữ liệu để đưa ra quyết định kinh doanh thông minh hơn. Nó cung cấp các công cụ mạnh mẽ để tạo báo cáo và bảng điều khiển tương tác, cho phép người dùng trực quan hóa dữ liệu từ nhiều nguồn khác nhau. 

## **Các tính năng chính của Looker:**

- **Khám phá và phân tích dữ liệu:** Looker cho phép người dùng truy cập và phân tích dữ liệu theo thời gian thực, cung cấp một nguồn sự thật duy nhất cho tổ chức. 

- **Tích hợp đa dạng nguồn dữ liệu:** Người dùng có thể kết nối Looker với nhiều nguồn dữ liệu khác nhau, bao gồm cơ sở dữ liệu đám mây và tại chỗ, để tạo báo cáo và bảng điều khiển tùy chỉnh. 

- **Tùy chỉnh và chia sẻ báo cáo:** Looker cung cấp các công cụ để tạo báo cáo và bảng điều khiển tùy chỉnh, cho phép người dùng chia sẻ thông tin chi tiết với nhóm hoặc toàn bộ tổ chức. 

- **Bảo mật và quản trị dữ liệu:** Nền tảng cung cấp các tính năng quản trị và bảo mật mạnh mẽ, đảm bảo rằng dữ liệu được quản lý và truy cập một cách an toàn. 

**Lợi ích của việc sử dụng Looker:**

- **Ra quyết định dựa trên dữ liệu:** Looker giúp các tổ chức đưa ra quyết định kinh doanh thông minh hơn bằng cách cung cấp thông tin chi tiết dựa trên dữ liệu. 

- **Cải thiện hiệu quả hoạt động:** Bằng cách cung cấp quyền truy cập vào dữ liệu theo thời gian thực, Looker giúp cải thiện hiệu quả hoạt động và thúc đẩy sự hợp tác trong tổ chức. 

- **Tăng cường bảo mật dữ liệu:** Với các tính năng bảo mật và quản trị tích hợp, Looker đảm bảo rằng dữ liệu của tổ chức được bảo vệ và tuân thủ các quy định. 

## **Looker Studio:**

Looker Studio, trước đây gọi là Google Data Studio, là một công cụ miễn phí cho phép người dùng tạo báo cáo và bảng điều khiển tương tác từ nhiều nguồn dữ liệu khác nhau. Nó cung cấp giao diện kéo và thả dễ sử dụng, giúp người dùng trực quan hóa dữ liệu một cách hiệu quả. 

## **Tài nguyên bổ sung:**

- [Giới thiệu về Looker](https://cloud.google.com/looker/docs/intro)
- [Looker cho trí tuệ kinh doanh](https://cloud.google.com/looker-bi/)
- [Looker Studio](https://cloud.google.com/looker-studio)

# Câu 9: Tìm hiểu Apache Spark
> https://spark.apache.org 

Apache Spark là một công cụ phân tích dữ liệu mã nguồn mở, được thiết kế để xử lý dữ liệu lớn với tốc độ cao và khả năng mở rộng linh hoạt. Nó cung cấp các API cấp cao cho nhiều ngôn ngữ lập trình như Scala, Java, Python và R, cho phép thực hiện các tác vụ xử lý dữ liệu, khoa học dữ liệu và học máy trên cả máy đơn lẻ và cụm máy tính. 

## **Kiến trúc và tính năng:**

- **Resilient Distributed Dataset (RDD):** Là nền tảng của Spark, RDD là tập hợp dữ liệu chỉ đọc, được phân tán trên nhiều máy và có khả năng chịu lỗi cao. 

- **Spark SQL:** Cung cấp giao diện để thực hiện các truy vấn SQL phân tán nhanh chóng, hỗ trợ phân tích dữ liệu và báo cáo. 

- **Spark Streaming:** Cho phép xử lý dữ liệu streaming theo thời gian thực, hữu ích cho các ứng dụng yêu cầu phân tích dữ liệu liên tục. 

- **MLlib:** Thư viện học máy tích hợp, cung cấp các thuật toán và công cụ để xây dựng mô hình học máy trên dữ liệu lớn. 

- **GraphX:** API để xử lý và phân tích đồ thị, cho phép thực hiện các tính toán phức tạp trên cấu trúc dữ liệu đồ thị. 

## **Ưu điểm của Apache Spark:**

- **Tốc độ cao:** Sử dụng cơ chế lưu trữ trong bộ nhớ và tối ưu hóa truy vấn, Spark có thể thực hiện các truy vấn phân tích nhanh chóng trên dữ liệu có kích thước bất kỳ. 

- **Hỗ trợ đa ngôn ngữ:** Spark hỗ trợ các ngôn ngữ lập trình phổ biến như Java, Scala, R và Python, giúp lập trình viên dễ dàng xây dựng ứng dụng. 

- **Xử lý đa dạng tác vụ:** Spark có khả năng xử lý nhiều loại tác vụ khác nhau như truy vấn tương tác, phân tích thời gian thực, học máy và xử lý đồ thị, tất cả trong một nền tảng duy nhất. 

## **Ứng dụng thực tế:**

Apache Spark được sử dụng rộng rãi trong nhiều lĩnh vực như phân tích dữ liệu lớn, học máy, xử lý dữ liệu thời gian thực và phân tích đồ thị. Nhiều công ty và tổ chức đã áp dụng Spark để tối ưu hóa quy trình xử lý dữ liệu và đưa ra quyết định kinh doanh thông minh hơn. 

## **Tài nguyên bổ sung:**

- [Tài liệu chính thức của Apache Spark](https://spark.apache.org/docs/latest/)

- [Hướng dẫn bắt đầu nhanh với Apache Spark](https://spark.apache.org/docs/latest/quick-start.html)

- [Kho mã nguồn Apache Spark trên GitHub](https://github.com/apache/spark)

Apache Spark tiếp tục phát triển và đóng vai trò quan trọng trong hệ sinh thái xử lý dữ liệu lớn, cung cấp các công cụ mạnh mẽ cho việc phân tích và xử lý dữ liệu hiệu quả. 


<h1 align="center">
<strong>CÂU HỎI ÔN TẬP</strong>
</h1>

# Câu 1: Hãy trình bày ứng dụng máy học liên quan tới Completion

# Câu 2: Hãy trình bày ứng dụng máy học liên quan tới Machine Translation

# Câu 3: Phân tích kinh doanh là gì?

# Câu 4: Trình bày các Công cụ phân tích kinh doanh phổ biến

# Câu 5: Trình bày ứng dụng của máy học trong phân tích kinh doanh, cho ví dụ minh họa

# Câu 6: Trình bày Ưu điểm và nhược điểm của máy học, cho ví dụ minh họa