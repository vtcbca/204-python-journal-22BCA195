# write a script list using UDF createlist(). count and print even odd number in the list using UDF evenood().



def evenodd(n):
      even,odd=[],[]
      count1,count2=0,0
      for i in n:
          if i%2==0:
              even.append(i)
              count1+=1
          else:
              odd.append(i)
              count2+=1

      print(f"the even numbers are {count1} and numbers:")
      printlist(even)

      print(f"the odd numbers are {count2} and numbers:")
      printlist(odd)

def printlist(b):
       for i in b:
           print(i)

def createlist():
        a=[]
        b=int(input("how many numbers you want to enter in list:"))
        for i in range(b):
            c=int(input("enter a number:"))
            a.append(c)
        evenodd(a)
createlist()
