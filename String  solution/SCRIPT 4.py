#write a menudriven list which perform following operation
 #1.create list of string till user choise.
# 2.print string with even character in length.
 #3.replace odd character of string with index no.
 #4.Enter start and end value and extract character from the list of string.
 
 

a=[]
q="y"
while q=="y" or q=="Y":
    print("\n1.Add iteams in list .\n2.print string with even character in length.\n3.replace odd character of string with index no.\n4.enter start and end value and extraxt from the string\n")
    c=int(input("enter your choice!!"))

    if c==1:
        a1="y"
        while a1=="y" or a1=="Y":
            i=input("Enter a string you want to enter:")
            a.append(i)
            a1=input("do you add more string press(y/Y)")

    elif c==2:
        b=[]
        count=0
        for i in a:
            if(len(i)%2==0):
                b.append(i)
                count+=1
        if count>0:
            print(f"string with even character is{b}")
        else:
            print("string had no even character in it...")

    elif c==3:
        p=[]
        for i in a:
            o=[]
            for enu,j in enumerate(a):
                if enu%2==0:
                    o.append(j)
            p.append(o)
        for i in p:
            print(i)


    elif c==4:
        s=int(input("Enter start index:"))
        e=int(input("Enter end index:"))
        res=" ".join([sub for sub in a])[s:e]
        print(f"your string is{res}")

    else:
        print("Enter a valid choice!")

    q=input("do you want to conitinue:(y/Y):")
