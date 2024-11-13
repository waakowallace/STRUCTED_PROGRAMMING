#list 
#NO 1 
#finding the sum of items in a  list 
list=[2,3,10,11,12]
sum_list=sum(list)
print("the sum of  numbers in the list is ",sum_list)

# NO 2
#multyping the numbers in a list .come up with a list 
numbers=[2,3,4,5,]
product=1
for i in numbers:
    product*=i
    print(product)

#NO 3
#finding the largest number in the list 
numbers=[17,50,14,12,1]
largest_number=max(numbers)
print("the largest number is :",largest_number)


#NO 4 finding the smallest number
numbers=[17,50,14,12,1]
smallest_num=min(numbers)
print("the smallest number is :",smallest_num)
"""
#NO 7 
# removing from a duplicate
my_list = [1,2,2, 6]
unique_list = list(my_list)
print("List without duplicates:", unique_list)"""

#NO 8
#seeing if a list is empty
list=[2]
if not list:
    print("the list is empty ")
else:
    print("the list is not empty")

#NO 9 
#copying a list 
fruits=['mango','apple','pinapple']
copying_list=fruits.copy()
print("cloned list :",copying_list)

#NO 10
#words longer than a given character
words = ["wallace", "waako", "william", ]
# length threshold
n = 5
# finding words longer than n
long_words = [word for word in words if len(word) > n]
# printing the list of long words
print("Words longer than", n, ":", long_words)

#NO 22 appanding two list 
list1=[1,2,3,4]
list2=[4,6,7,8]
#appand the lists 
list2.append(list1)
print("the appanded list :",list2)

#NO 23
my_list = [12, 45, 7, 23, 56, 89, 34]
sorted_list = sorted(my_list)
second_smallest = sorted_list[1]
# printing the second smallest number
print("The second smallest number in the list is:",second_smallest)

# dictionaries 
#no3
my_dict = {'a': 1, 'b': 2, 'c': 3}
key = 'b'
# checking if the key exists in the dictionary
if key in my_dict:
    print(f"The key '{key}' exists in the dictionary.")
else:
    print(f"The key '{key}' does not exist in the dictionary.")


#NO4
# iterating of loops
dict = {'a': 1, 'b': 2, 'c': 3}

# iterating over the dictionary using a for loop
for key, value in dict.items():
    print(f"Key: {key}, Value: {value}")

#TUPLES 
#NO1 CREATING A TUPLE
tuple=(2,3,7,8,10)
print(tuple)




ss





