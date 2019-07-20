import numpy as np

##single diamension
a=np.array([1,2,3])
print(" \n single Diamension Array")
print(a);
print(type(a))

##multidiamsion

b=np.array([[1,2,3],[4,5,6]])
print(" \n Multi diamensional Array:")
print(b)

##changing datatype

a=np.array([1,3,5,7],complex)
print(" \n Changing the data type:")
print(a)

##finding diamensions
c=np.array([[1,2,3,4],[3,4,4,5],[8,9,5,4]])
print("Array Diamension")
print(c.ndim)

##size of  element
a=np.array([1,9,4,6,3])
print("Each data item contain" ,a.itemsize, " byetes");	

##shape and size

print("Size is=",a.size)
print("shape is=",a.shape)

##reshaping the array

a=np.array([[1,2],[12,34],[44,55],[465,87]])
print("Array before reshaping:")
print(a);
print("Array after reshaping in 2*4:")
print(a.reshape(2,4))

##slicing the Array
print("Element at 0th diamension and 1st position:")
print(a[0,1])

print("Element at 3th diamension and 1st position:")
print(a[3,1])

"""## linespace
N=np.linespace(5,15,10)
print("Linespace:")
print(N)"""

## max ,min ,sum of the array.

a=np.array([1,2,3,7,4,8,0,111,3])
print(a)
print("Maximum Element",a.max())
print("Minimum Element",a.min())
print("sum of  Element",a.sum())

## Numpy for array axis;
## column axis=0;
## row    axis=1;

a=np.array([[1,2,3],[10,20,30]])
print(a);
print("maximum Element at column",a.max(axis=0))
print("minimum Element at column",a.min(axis=1))
print("sum of Element at column",a.max(axis=0))
print("sum of  Element at row",a.max(axis=1))

