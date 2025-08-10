#Create an empty list called my_list.
my_lists = []

#Append the following elements to my_list: 10, 20, 30, 40.
my_lists.append(10)
my_lists.append(20)
my_lists.append(30)
my_lists.append(40)

#Insert the value 15 at the second position in the list.
my_lists.insert(1,15)

#Extend my_list with another list: [50, 60, 70].
my_lists.extend([50, 60, 70])

#Remove the last element from my_list.
my_lists.pop(-1)

#Sort my_list in ascending order.
my_lists.sort()

#Find and print the index of the value 30 in my_list.
print(my_lists.index(30))