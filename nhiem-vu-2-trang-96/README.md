Vấn đề chính khi hệ thống in ra kết quả nhiều lần:
Lỗi như sau:

/workspaces/py/nhiem-vu-2-trang-96 (main) $ python tracuuten.py 
Nhập tên học sinh cần tra cứu, nhập từ khóa end để kết thúc:Minh
Diem so cua hoc sinh la: 5.6
Diem so cua hoc sinh la: 5.6
Diem so cua hoc sinh la: 5.6
Diem so cua hoc sinh la: 5.6
Diem so cua hoc sinh la: 5.6
Diem so cua hoc sinh la: 5.6

vitri được khởi tạo là 1 thay vì -1, nên khi không tìm thấy vẫn in giá trị hợp lệ.
Khối if vitri==-1 và else nằm trong vòng for, nên được kiểm tra và in mỗi lần lặp — dẫn đến in nhiều lần.

