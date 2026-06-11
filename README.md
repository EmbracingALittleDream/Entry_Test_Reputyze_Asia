# Bài test đầu vào của Công ty TNHH Lửa Á Châu (Reputyze Asia) vị trí Data Analysis Social Media Intern

## Objective
Phân tích dữ liệu mạng xã hội của TCBS với các yêu cầu sau:
1. Định nghĩa các trường thông tin của dữ liệu
2. Kiểm tra và xử lý lại sắc thái (sentiment) của từng bài viết / bình luận cho chính xác
3. Xử lý dữ liệu mẫu: nội dung mỗi bài viết và bình luận đang thể hiện khía cạnh gì? Có 4 khía cạnh sau
  - Thương hiệu: nội dung nói về thương hiệu TCBS
  - Sản phẩm: nội dung nói về các sản phẩm - dịch vụ của TCBS
  - Chương trình khuyến mãi: nội dung nói về khuyễn mãi của TCBS
  - Khác: nội dung nói về những khía cạnh khác
4. Thống kê các chỉ số:
  - Tổng số bài đăng (post)
  - Tổng số bình luận (cmt)
  - Tổng số tương tác (engagement)
5. Vẽ biểu đồ xu hướng thảo luận (mention) và tương tác (egagement) theo thời gian. Cho thấy được lượng thảo luận và tương tác mỗi ngày là bao nhiêu.
6. Vẽ biểu đồ thể hiện tỉ lệ thảo luận trên từng nền tảng (platforms)
7. Vẽ biểu đồ thể hiện tỉ lệ sắc thái thảo luận (sentiment)
8. Top 5 chủ đề (nội dung) có nhiều thảo luận nhất trong bảng dữ liệu và tỉ lệ phần trăm thảo luận của từng chủ đề (nội dung).
9. Đánh giá chung về dữ liệu

## Dataset
- Number of rows/columns: 291 quan trắc - 18 biến
- Variables description
1. Platform     :           Nền tảng số mà thông tin được đăng tải
2. Type         :           Loại bài viết được ghi nhận (post hoặc comment)
3. Title        :           Tiêu đề của thông tin được đăng tải
4. Content      :           Tóm tắt nội dung của thông tin được đăng tải
5. Created Date :           Ngày - tháng - năm thông tin được đăng tải
6. Sentiment    :           Sắc thái - phản hồi mà bài viết nhận được
7. Author       :           Tác giả của bài viết
8. Author URL   :           path - đường link dẫn đến bài viết
9. Reaction     :           Số lượt xem của bài viết
10. Comments    :           Số lượt bình luận bài viết nhận được
11. Shares      :           Số lượt chia sẻ của bài viết
12. Like        :           Số lượt thích bài viết nhận được
13. Love        :           Số lượt thả tim bài viết nhận được
14. Haha        :           Số lượt thả haha bài viết nhận được
15. Wow         :           Số lượt thả wow bài viết nhận được
16. Sad         :           Số lượt phản hồi buồn sau khi đọc bài viết
17. Angry       :           Số lượt phản hồi tức giận sau khi đọc bài viết
18. Care        :           Số lượt phản hồi quan tâm sau khi đọc bài viết
    
## Tools Used
- Python
- Pandas
- NumPy
- Matplotlib

## Project Files
- report: [Markdown Report](report/Test_Entry.ipynb)
- report: [PDF Report](Report_Entry_Test.pdf)
