import numpy as np
my_list=[10,22,21,8,9,9,42,3,18,11,5,4,30,12,29,37,31,7,2,26,8,6,4,33,15]
ar = np.array(my_list)
mat = ar.reshape(5,5)
sottrazione = ar - ar.min()
print("I valori sottratti il valore minimo sono: ", sottrazione.reshape(5,5))
divisione = (sottrazione / ar.max()) - ar.min()
print("I valori divisi il massimo e sottratto il minimo sono:", divisione.reshape(5,5))