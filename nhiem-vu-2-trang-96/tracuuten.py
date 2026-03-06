input_file = open("diem.inp", encoding="utf-8") #encoding để đọc được tiếng Việt có dấu
ten_list = []
diem_list = []
for line in input_file.readlines():
    ten,diem =line.split()
    ten_list.append(ten)
    diem_list.append(float(diem))
ten=''
while(ten!='end'):
    ten = input('Nhập tên học sinh cần tra cứu, nhập từ khóa end để kết thúc:')
    if (ten!='end'):
        vitri=1
        for i in range(0,len(ten_list)):
            if ten==ten_list[i]:
                vitri=i
            if vitri==-1:
                print('Khong tim thay hoc sinh trong danh sach')
            else:
                print('Diem so cua hoc sinh la:' ,diem_list[vitri])