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
