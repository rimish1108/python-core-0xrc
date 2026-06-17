list1 = [1,2,3,2,1]
copy_list1 = list1.copy()
print(copy_list1)
copy_list1.reverse()
if(copy_list1 == list1):
    print("This list is palindrome")
else:
    print("This list is not palinddrome")


list2 = [1, "abc", "abc", 1]
copy_list2 = list2.copy()
copy_list2.reverse()
if(copy_list2==list2):
    print("The list is palindrome")
else:
    print("The list is not palinddrome!")