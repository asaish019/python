def age(a1,a2,a3,aavg=20):
    total=a1+a2+a3
    avg=total/3
    if avg>aavg:
        print("u can go for ride")
    else:
        print("Sorry")
    return

father=int(input("father age: "))
son=int(input("son age: "))
daughter=int(input("daughter age: "))
age(father,son,daughter,50)
