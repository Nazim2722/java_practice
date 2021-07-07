a=int(input("enter a "))
b=int(input("enter b "))
c=int(input("enter c "))
if a>b and a>c and b>c:
  print("number in descending order are:",a,b,c)
elif b>c and c>a:
  print("number in descending order are:",b,c,a)
