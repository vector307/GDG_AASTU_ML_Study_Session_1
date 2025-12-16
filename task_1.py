import numpy as np

# step 1:
my_list = [1,2,3,4,5]

# step 2:
arr = np.array(my_list)

# step 3:
mean = arr.mean()
maximum_value = arr.max()
sum = arr.sum()

# step 4:
print(f"the mean arr: {mean}")
print(f"the maximum value of arr: {maximum_value}")
print(f"the sum of arr: {sum}")