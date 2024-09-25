
my_list = [1, 2, 3, 'apple', 'lemon']

#-------------------------------------------------------------------------------------------------
# first_element = my_list[3]
# print(first_element)

# my_list[2] ="watermelon"
# print(my_list)
#-------------------------------------------------------------------------------------------------
my_list.append(6) # to insert the value at the end
print(my_list)

#insert
my_list.insert(1, 20)
print(my_list)
print()

#pop
poped_element = my_list.pop()
print(my_list)
print()

#short
my_list.sort(key=str)
print(my_list)
print()

#reverse
my_list.reverse()
print(my_list)
print()