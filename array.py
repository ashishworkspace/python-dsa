import array as arr


num_array = arr.array('i', [1,2,6,33])

print(num_array)

print(num_array[0]) # getting data using array indexing has time complexity is O(1) 
print(num_array.buffer_info()) # buffer_info is function used to get the location of the array

# append function has time complexity O(n) and space complexity is  O(1)
num_array.append(26)
print(num_array)
print(num_array.buffer_info()) # location of array is changed from above position 
# So CPU required time to reallocate the memory and transfer every data in the array to a new position.
# So append fuction has time complexity O(n) and space complexity O(1) as it does not require to reallocate any new space in memory.

# pop function has time complexity O(1) and space complexity is O(1)
num_array.pop()
print(num_array)
print(num_array.buffer_info()) # same position in memory as above



 