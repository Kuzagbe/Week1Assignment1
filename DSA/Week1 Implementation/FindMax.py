# # This just a list of numbers
# list1 = [10, 20, 4, 45, 99, 102, 100]
#
# # this code is to sort the list above
# list1.sort()
#
# #the code here is to help print the last element from behind since
# # the List1[-1] is telling it tomprint from the last elemet which is the
# print("Largest element is:", list1[-1])


# Another way of doing this is below so please grayout the top one to get the down part

print("============================================================================")

# creating empty list.
# This is an empty list that will be filled by the user later on in the code
list1 = []

# This algorithm asks the user how many element will he or she want in the list
SuggestedNum = int(input("Enter the number of elements you want in your list: "))

# This algorithm also help iterate till it gets to the suggestedNum by appending the list
for i in range(1, SuggestedNum + 1):
    SuggestedElements = int(input("Enter a number to put in your list: "))
    list1.append(SuggestedElements)

# This print method help print the largest number
print("Largest element is:", max(list1))