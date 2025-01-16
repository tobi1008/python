#%% Giải phương trình bậc hai 𝑎 𝑥 2 + 𝑏 𝑥 + 𝑐 = 0 ax2 +bx+c=0
import math

# Nhập hệ số a, b, c
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm.")
        else:
            print("Phương trình vô nghiệm.")
    else:
        x = -c / b
        print(f"Phương trình có nghiệm duy nhất: x = {x}")
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Phương trình vô nghiệm.")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Phương trình có nghiệm kép: x = {x}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Phương trình có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}")

# %% Tìm các số có trị tuyệt đối nhỏ hơn 10 
# Nhập ba số thực
num1 = float(input("Nhập số thứ nhất: "))
num2 = float(input("Nhập số thứ hai: "))
num3 = float(input("Nhập số thứ ba: "))

# Tìm các số có trị tuyệt đối nhỏ hơn 10
result = [num for num in [num1, num2, num3] if abs(num) < 10]

# In kết quả
if result:
    print("Các số có trị tuyệt đối nhỏ hơn 10 là:", result)
else:
    print("Không có số nào có trị tuyệt đối nhỏ hơn 10.")

# %% Tìm giá trị lớn nhất và nhỏ nhất trong 5 số thực
# Nhập 5 số thực
numbers = [float(input(f"Nhập số thứ {i+1}: ")) for i in range(5)]

# Tìm giá trị lớn nhất và nhỏ nhất
max_value = max(numbers)
min_value = min(numbers)

# In kết quả
print(f"Giá trị lớn nhất là: {max_value}")
print(f"Giá trị nhỏ nhất là: {min_value}")

# %% Xác định thứ trong tuần của ngày 1/1 của một năm
from math import floor

# Nhập năm
year = int(input("Nhập năm: "))

# Tính thứ trong tuần
day_of_the_week = (year + floor((year - 1) / 4) - floor((year - 1) / 100) + floor((year - 1) / 400)) % 7

# Ánh xạ thứ trong tuần
days = ["Chủ nhật", "Thứ hai", "Thứ ba", "Thứ tư", "Thứ năm", "Thứ sáu", "Thứ bảy"]

# In kết quả
print(f"Ngày 1/1/{year} là {days[day_of_the_week]}")

# %%
