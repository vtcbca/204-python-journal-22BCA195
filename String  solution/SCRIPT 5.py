# write a script 2 udf input() to take input string and call strsymmetric() by passing string.
# strsymmetric() chrck string is summetric or not . a string is said to be symmetric if bith the halves of the string are the same.


def symmetric(n):
    half=(len(n)//2)
    first=n[:half]
    second=n[half:]
    if first==second:
        print(f"string {n} is symmetric!!!")
    else:
        print(f" string {n} is not symmetric!!!")
def input1():
    a=input("enter a string:")
    symmetric(a)
input1()
