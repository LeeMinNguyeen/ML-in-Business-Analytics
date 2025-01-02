# Trình bày phương pháp PointWise
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

# Trình bày phương pháp Pairwise
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

# Trình bày phương pháp Listwise
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
