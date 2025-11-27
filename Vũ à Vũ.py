tk="camonvidaden"
mk="anhdadenbenem"
print("moi ban nhap tài khoan")
a=input()
print("moi ban nhap mat khau")
b=input()
for i in range(2):

    if a==tk:
        print("ban dã nhap tai khoan dúng")
        if b==mk:
            print("ban dã dúng")
            break
        else:
            print("ban da nhap sai")
            break
    else:
        print("ban da nhap sai")
        break
        
