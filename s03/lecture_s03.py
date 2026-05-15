"""
Author: Youngjae Kim
Date: 2026-05-14
Description: 
    •	Create, access, modify, and delete list items
    •	Extract sublists using slicing
    •	Use the most common list methods confidently
"""

## Array style
print('############### example 1 #################')
fruits = ['apple', 'banana', 'cherry']
print(fruits[1])
print(len(fruits)) # how to get length(size) of list
print(fruits[len(fruits)- 1]) #print out the value of the last index in the list
print('the first value: ' + fruits[0] + ' || the last value: ' + fruits[-1]) # this is python way.(Recommendation)

print()
print('############### example 2 #################')
fruitList = []
fruitList.append('apple')
fruitList.append('banana')
fruitList.append('cherry')
print(fruitList[0]) # prints 1
print(fruitList[1]) # prints 2
print(fruitList[2]) # prints 3

# it should be done after learning loop
print('========= loop ======')
for x in fruitList:
    print(x)


###########################################
# list slicing
###########################################
print()
print('#################### list slicing ################')

slicinglist = [0, 1, 2, 3, 4, 5]
print(slicinglist[1:4])
print(slicinglist[:3])
print(slicinglist[2:])
print(slicinglist[2:-1])
print(slicinglist[2:-2])
print(slicinglist[:])
print(slicinglist)
print(slicinglist[::2])

# minus index.
print(slicinglist[-3:])
print(slicinglist[::-1]) ## reverse, oiginal list won't be changed


################################################
# copy list
###############################################
print()
print('#################### copy list ################')
newlist = slicinglist[:] ## Shallow Copy
anotherlist = slicinglist ## Reference assignment (memory address) - little bit explain
print(newlist)
print(anotherlist)

slicinglist.append(7)
print(newlist)  
print(anotherlist)


########################################################
# list operator=>append(), sort(), len() 
########################################################
print()
print('#################### list operator=>append(), sort(), len() ################')
operationList = [1, 0, 2, 4, 3, 5]
operationList.append(6)
print(operationList)

operationList.sort() #assending
print(operationList)

operationList.sort(reverse=True) #decending
print(operationList)

print(len(operationList))

reverseList = ['x1', 'x2', 'x4', 'x3'] #Revverse list value
reverseList.reverse()
print(reverseList)


##############################################################
# remove(), pop(), del()
##############################################################
print()
print('#################### list operator=> remove(), pop(), del() ################')
operationList = [1, 0, 2, 4, 3, 5]
operationList.remove(3) # This is good when you know only value, but not sure the index.
print(operationList)

operationList = [1, 0, 2, 4, 3, 5]
operationList.pop(3) # This is good when you know the index when you want to delete.
print(operationList)

operationList = [1, 0, 2, 4, 3, 5]
del operationList[0:4] # This is good if you want to delete from one index to another (range)
print(operationList)


##############################################################
# list in
##############################################################
operationList = [1, 0, 2, 4, 3, 5] ## validate if the certain value does exist. 
print(3 in operationList)
print(6 in operationList)
print(6 not in operationList)

### all casesenstive.
users = ["Alice", "Bob", "Charlie"]
if "Alice" in users:
    print("Alice is a user")

if "alice" in users:
    print("Alice is a user")