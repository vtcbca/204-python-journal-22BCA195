#write a script to check if the list contains three consecutive common numbers in python using udf.



def consecutivecommon(n):
    count=0
    b=[]
    for i in range(len(n)-2):
        if n[i]==n[i+1] and n[i+1]==n[i+2]:
            b.append(n[i])
            count+=1
    if count>0:
        print(f"consecutive common number in list {n} as follow:{b}")
    else:
        print("no consecutive number in list!!")
def takeinput():
    a=[]
    b=int(input("how many you want to enter in list:"))
    for i in range(b):
        c=int(input("enter value:"))
        a.append(c)
    consecutivecommon(a)
takeinput()
