#Write a script to create a list with 5 string and count total number of string with even number of length with string using UDF

def evenstr(a):
    s=[]
    count=0
    for i in a:
        if(len(i)%2==0):
            s.append(i)
            count=count+1
    if(count>0):
        print(f'The number of even string is {count} and string :{s}')
    else:
        print("No even string avaliable!")

    a=[]
    for i in  range(5):
        b=input(f"Enter string:{i+1}:")
        a.append(b)
    evenstr(a)
                


