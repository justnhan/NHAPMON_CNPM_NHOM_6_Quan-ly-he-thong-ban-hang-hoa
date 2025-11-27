ad="NHAN"
ps= "123"
print("Chao mung ban da den!")
print("---------------------------------------------")
for i in range (3):
    print ("Moi ban nhap ten dang nhap:")
    a= input()
    print("moi ban nhap mat khau:")
    b= input()
    if a==ad:
        for j in range (3):
            if b==ps:
                flag=True
                print ("Chao mung ban da den voi nha camon!")
                break
            else:
                flag=False
                print("sai mat khau, vui long nhap lai!")
                b=input()
        if flag==True:
            break
        else:
            print("sai qua nhieu lan, ban da het luot nhap! Vui long tao lai.")
            break
    else:
        print("Tai khoan khong ton tai! Vui long dang nhap lai")
print("đã sửa!")
