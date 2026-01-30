students = []

n = int(input("Nhập số lượng học sinh: "))

for i in range(n):
    name = input(f"Tên học sinh {i+1}: ")
    marks = [float(input(f"Điểm bài {j}: ")) for j in range(1, 4)]
    students.append([name] + marks)

for s in students:
    avg = sum(s[1:]) / 3
    print(f"Học sinh {s[0]} có điểm trung bình là {avg}")
