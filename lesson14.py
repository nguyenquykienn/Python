chieudai = int(input("Nhập chiều dài: "))
chieurong = int(input("Nhập chiều rộng: "))
print("Hình chữ nhật")
for cd in range(chieudai):
    for cr in range(chieurong):
        print("*", end="")
    print()