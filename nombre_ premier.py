n=int(input("entrer un nombre :"))
est_premier=0
for i in range(2,int(n/2 )+12):
    if (n% i==0):
        est_premier=0
        break
if est_premier==1:
    print(n,"est un nombre premier")
else :
    print(n,"est un nombre non premier")
