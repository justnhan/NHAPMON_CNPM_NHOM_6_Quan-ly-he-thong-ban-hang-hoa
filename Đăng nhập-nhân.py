ad="NHAN"
ps= "123"
print("Chào m?ng b?n dã d?n!")
print("---------------------------------------------")
for i in range (3):
    print ("M?i b?n nh?p tên dang nh?p:")
    a= input()
    print("m?i b?n nh?p m?t kh?u:")
    b= input()
    if a==ad:
        for j in range (3):
            if b==ps:
                flag=True
                print ("Chào m?ng b?n dã d?n v?i nhà camon!")
                break
            else:
                flag=False
                print("sai m?t kh?u, vui lòng nh?p l?i!")
                b=input()
        if flag==True:
            break
        else:
            print("Sai quá nhi?u l?n, dã h?t lu?t nh?p! Vui lòng t?o l?i.")
            break
    else:
        print("Tài kho?n không t?n t?i, vui lòng nh?p l?i!")
print("chưa được sửa!")
