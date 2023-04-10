#write a python program to enter sentence of atleast 10 words. take user input of length of word.
#find the word in user inputed string which has >= lenght od word enter by user and directory where eord is key and its length is value


def makedict(n):
    dic={}
    c=int(input("enter minimum word length:"))
    for i in n:
        if len(i)>=c:
            dic[i]=len(i)
    print(dic)

def input1():
    str=input("enter sentence:")
    a=str.split(" ")
    makedict(a)
input1()
