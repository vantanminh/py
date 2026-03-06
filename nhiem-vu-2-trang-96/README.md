## Vấn đề và Cách Sửa

### Vấn đề ban đầu
Hệ thống in ra kết quả nhiều lần thay vì một lần:

```
Nhập tên học sinh cần tra cứu, nhập từ khóa end để kết thúc:Minh
Diem so cua hoc sinh la: 5.6
Diem so cua hoc sinh la: 5.6
Diem so cua hoc sinh la: 5.6
Diem so cua hoc sinh la: 5.6
Diem so cua hoc sinh la: 5.6
Diem so cua hoc sinh la: 5.6
```

### Nguyên nhân
1. Khối `if vitri==-1` và `else` nằm **bên trong** vòng `for`
2. Nên mỗi lần lặp một phần tử, chương trình sẽ kiểm tra và in kết quả
3. Nếu có 6 phần tử trong danh sách → in 6 lần

### Cách sửa
✅ **Đã sửa**: 
- Đưa khối `if-else` **ra ngoài** vòng `for`
- Thêm `break` để thoát vòng khi tìm thấy học sinh
- Bây giờ chỉ in kết quả **một lần duy nhất**

