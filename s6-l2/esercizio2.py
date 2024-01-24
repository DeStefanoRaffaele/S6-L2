import numpy as np
linear_data = np.array([x for x in range(27)])
reshaped_data = linear_data.reshape((3,3,3))
print(linear_data)
print(reshaped_data)
print("La dimensione è: ", reshaped_data.size)