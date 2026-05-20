number_list=[1,2,3,4,5,6,7,8,9,10]
numbers_gt5=[num for num in number_list if num>5]
print(numbers_gt5)
numbers_sq=[num**2 for num in number_list]
print(numbers_sq)
numbers_dic={num:num **3 for num in number_list if num<6}
print(numbers_dic)
