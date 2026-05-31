# List: Dynamic array, contiguous block of memory that contains pointers to your objects and it dynamically resizes itself by doubling its capacity whenever filled

#index access O(1)

test_list = [3231, 344, 2, 6, 3]

print(test_list[0])

# appending to right O(1)
# appending to left O(N) .insert(0, val)



import time

# Let's test an O(1) Right Append
start_time = time.time()
right_list = []
for i in range(100000):
    right_list.append(i) # O(1) operation
print(f"Right Append Time: {time.time() - start_time} seconds")

# Let's test an O(N) Left Insert
start_time = time.time()
left_list = []
for i in range(100000):
    left_list.insert(0, i) # O(N) operation inside a loop!
print(f"Left Insert Time: {time.time() - start_time} seconds")

