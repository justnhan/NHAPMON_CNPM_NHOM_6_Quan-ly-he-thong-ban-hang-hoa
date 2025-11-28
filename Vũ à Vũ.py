tk="camonvidaden"
mk="anhdadenbenem"
print("mời bạn nhập tài khoản")
a=input()
print("mời bạn nhập mật khẩu")
b=input()
for i in range(2):

    if a==tk:
        print("ban dã nhap tai khoan dúng")
        if b==mk:
            print("bạn đã dúng")
            break
        else:
            print("bạn đã nhập sai")
            break
    else:
        print("bạn đã nhập sai sai")
        break
        
