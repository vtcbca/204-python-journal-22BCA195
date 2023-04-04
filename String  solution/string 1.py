#Write a script to enter any word and check it is palindrom or not

a=input("Enter any string:")
b=a[::-1]
if(a==b):
    print("string is palindrome !")
else:
    print("string is not palindrome !")
    
