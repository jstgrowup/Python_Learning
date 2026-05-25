# 1.
# numbers=[1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
# count=0
# for num in numbers:
#     if num>0:
#         count+=1

# print(count)

# 2

# num=input("Please enter the number: ")
# sum_even=0
# for n in range(1,num+1):
#     if n%2==0:
#         sum_even+=n
# print(sum_even)

# 3
# user_num=int(input("Please enter the number: "))
# for num in range(1,11):
#     if num==5:
#         continue
#     else:
#         print(num*user_num)

# 4
# user_str=input("Please enter the string: ")
# reversed_str=""
# for char in user_str:
#     reversed_str=char+reversed_str
# print(reversed_str)

# 5
# str="acdacds"
# for char in str:
#     if str.count(char)==1:
#         print(char)
#         break

number =5
factorial=1
while number >0:
    factorial*= number
    number-=1

print(factorial)

