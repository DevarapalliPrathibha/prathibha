
import numpy as np
list_a = [1,2,3,4]
list_b = [5,6,7,8]
print(list_a + list_b)
numpy_a = np.array([1,2,3,4])
numpy_b = np.array([5,6,7,8])
print(numpy_a)
print(numpy_a * numpy_b)
print("\n")
#common properties
numpyBasic_array = np.array([1,2,3,4,5,6.2,"a"])
print(numpyBasic_array.dtype)
print(numpyBasic_array.itemsize)
print(numpyBasic_array.size)
print("\n")

numpyBasic_array1 = np.array([1,2,3,4,5,6.2])
print(numpyBasic_array1.dtype)
print(numpyBasic_array1.itemsize)
print(numpyBasic_array1.size)
print("\n")
#2d arrays

array_2D = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array_2D)
print("dimensions: {}".format(array_2D.ndim))
print("shape: {}".format(array_2D.shape))
print("array Dtype: {}".format(array_2D.dtype))
print("\n")
#3d arrays
array_3D = np.array(([[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9,]]]))
print(array_3D)
print("dimensions: {}".format(array_3D.ndim))
print("shape: {}".format(array_3D.shape))
print("array Dtype: {}".format(array_3D.dtype))
print("\n")

array_2D = np.array([1,2,3,4],dtype = 'float32')
print(array_2D)
print(array_2D.itemsize)
print(array_2D.dtype)
print("\n")
array_2D = np.array([1,2,3,4],dtype = 'float64')
print(array_2D)
print(array_2D.itemsize)
print(array_2D.dtype)
print("\n")
array_2D = np.array([1,2,3,4],dtype = 'int64')
print(array_2D)
print(array_2D.itemsize)
print(array_2D.dtype)
print("\n")
#accessing arrays
array_a = np.array([[1,2,3,8,0],[4,5,6,9,7]])
print(array_a)
print(array_a.size)
print(array_a[1,2])
print(array_a[0,2])
print(array_a[:, 2])
print(array_a[:, -3])
print("\n")
#step - start :end: stepsize
print(array_a[0, 0: 4: 2])
print(array_a[:, 0: 4: 2])

array_a[0,2] = 10
array_a[: ,2] = 10
print(array_a)
print("\n")

array_3D = np.array([[[2,3],[7,8]],[[1,3],[4,5]]])
print(array_3D)
print(array_3D[0,1,0])
print(array_3D[:, 1,0])
print("\n")

#updating 3d array
array_3D[:,0,:] = 20
print(array_3D)
array_3D[:, 0, :] = [[5,5],[10,10]]
print(array_3D)
print("\n")
#common arrays
#ones twos empty
print(np.zeros(3))
print("\n")

print(np.ones(3))
print("\n")
two_d = np.zeros((3,3))
print(two_d)
print("\n")
three_d = np.zeros((2,3,3))
print(three_d)
print("\n")
four_d = np.zeros((2,3,3,2))
print(four_d)
print("\n")
print(np.zeros((3,3)))
print("\n")
print(np.full((2,2),[1,2]))
print("\n")
print(np.full((3,3),[1,2,3]))
print("\n")
print(np.full((3,3),[1,2,3],dtype = "float32"))
print("\n")
array_b = [1,2,3,5,8]
print(np.full_like(array_b, 4))
print("\n")
#repeat
array_c = [[1,2,3],[4,5,6]]
array_repeat = np.repeat(array_c,2, axis =1)
print(array_repeat)
print("\n")
array_c = [[1,2,3],[4,5,6]]
array_repeat = np.repeat(array_c,2)
print(array_repeat)
print("\n")
array_d = np.zeros((3,3))
array_d[1,1] = 7
print(array_d)
print("\n")
update_array = np.zeros((5,5))
update_array[1:-1, 1:-1] = array_d
print(update_array)
print("\n")
#copying arrays
#array_e = np.array([1,2,3,4])
#array_f = array_e
#math operations
array_math = np.array([1,2,3])
print(np.sin)
print("declared array: {}".format(array_math))
print("add 10 to array array: {}".format(array_math+10))
print("sub 2 from array: {}".format(array_math-2))
print("raise to pow array array: {}".format(array_math**2))
print("multiply array: {}".format(array_math*5))
print("divide array by 2: array: {}".format(array_math/2))
print("\n")
#algebra with numpy
arr_a = np.ones((2,3))
arr_b = np.full((3,2),2)
print(arr_a)
print(arr_b)
#print(arr_a * arr_b)
print(np.matmul(arr_a,arr_b))
#statics
# statistics
print("\n")
n_a = [[1,1,1,1], [0,0,0,0,0,0,0]]
print(n_a)
print("\n")

array_stats = [[1,2,3], [4,5,-6]]     #access - 1 = row(horizontal)
                                      #access - 0 = column(vertical) comparing (1,4)(2,5) (3,-6)
print(np.min(array_stats))
print(np.min(array_stats, axis= 0))
print(np.min(array_stats, axis= 1))

#print(np.max(array_stats))
print(np.max(array_stats, axis= 0))
print(np.max(array_stats, axis= 1))

print(np.max(array_stats))
print(np.sum(array_stats, axis=0))
print(np.sum(array_stats, axis=1))
print("\n")
# stacking

a_v1 = np.array([1,2,3,4])

a_v2 = np.array([1,2,3,4])

print(np.array([a_v1, a_v2]))


print(np.hstack([a_v1, a_v2]))
print("\n")

#arange - array range
one_d = np.arange(6)
print(one_d)
print("\n")
two_d = np.arange(12).reshape(4,3)
print(two_d)
print(two_d.shape)
print("\n")
three_d = np.arange(24).reshape(2,3,4)
print(three_d)
print(three_d.shape)
print("\n")
four_d = np.arange(144).reshape(2,4,3,6)
print(four_d)
print(four_d.shape)
print("\n")
data_from_Text_File = np.genfromtxt('textfile_1.txt',delimiter=',')
print(data_from_Text_File)
data_from_Text_File = data_from_Text_File.astype('int32')
print(data_from_Text_File)
print(data_from_Text_File>7)
print("\n")
def numpy_function(a,b):
    return 10 * a + b
c = np.fromfunction(numpy_function, (2, 3), dtype=int)
print(c)
print("\n")
def numpy_function(a,b,d):
    return 10 * a - b - d
c = np.fromfunction(numpy_function, (2, 3, 4), dtype=int)
print(c)



















