tk="camonvidaden"
mk="anhdadenbenem"
print("m?i b?n nh?p tài kho?n")
a=input()
print("m?i b?n nh?p m?t kh?u")
b=input()
for i in range(3):

    if a==tk:
        print("b?n dã nh?p tk dúng")
        if b==mk:
            print("b?n dã dúng")
            break
        else:
            print("m ngu")
            break
    else:
        print("m ngu")
        break
        
