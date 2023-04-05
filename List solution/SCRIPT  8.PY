# write  a script to replace list's iteam  with new value if found.take value from user which you want to replace.


def change(n):
    a=[]
    b=int(input("enter value you want to replace:"))
    c=int(input("enter value you want to change with:"))
    for i in n:
        if b==i:
            a.append(c)
        else:
            a.append(i)
    print(a)
def createlist():
    m=[]
    b=int(input("how many numbers you want to enter in list:"))
    for i in range(b):
        c=int(input("enter a number:"))
        m.append(c)
    change(m)
createlist()
