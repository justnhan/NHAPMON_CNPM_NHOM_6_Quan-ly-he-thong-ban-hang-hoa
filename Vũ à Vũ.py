tk="camonvidaden"
mk="anhdadenbenem"
print("moi ban nhap tài khoan")
a=input()
print("moi ban nhap mat khau")
b=input()
for i in range(3):

    if a==tk:
        print("ban dã nhap tk dúng")
        if b==mk:
            print("ban dã dúng")
            break
        else:
            print("m ngu")
            break
    else:
        print("m ngu")
        break
        
