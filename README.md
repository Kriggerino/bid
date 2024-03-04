# BID - So sánh tuyên bố đáp ứng với vendor datasheet

## Danh sách công việc và hướng dẫn thực hiện:

- Đọc và trích xuất các thông tin được đưa ra trong tuyên bố đáp ứng.
- Tải datasheet của từng sản phẩm được đưa ra trong tuyên bố đáp ứng.
- Đọc và trích xuất thông tin trong datasheet, lưu trữ dưới dạng phù hợp.
- Loop và so sánh thông tin trong tuyên bố đáp ứng với tài liệu tương ứng.
- Tổng hợp kết quả và hiển thị.

## Tài liệu liên quan:

- Tài liệu đáp ứng của SeaBank - Yêu cầu không chia sẻ.

## Tiêu chuẩn coding:

- Sử dụng PEP8 để format.
- Luôn đặt tên biến dễ hiểu và có ý nghĩa, ưu tiên độ dễ hiểu.
- Luôn viết docstring bằng dấu nháy, docstring có thể viết dưới dạng markdown, hãy format khi cần thiết.
- ... sẽ cập nhật sau

## Current Issues:
- Tốc độ chậm do sử dụng nhiều API bên thứ 3, do thiết kế phân mảnh dễ scale lên
- Fix cứng folder lưu pdf tải về trong documents, sẽ sửa lại
- Chỉ thực hiện được query trên 1 file thông báo kỹ thuật, cần mở rộng thuật toán (Hoặc tạo thêm nhiều worker để thực hiện cho nhiều document)
- Một số link đường dẫn trung gian làm ảnh hưởng đến việc tải tài liệu (datasheets)
- New Repository