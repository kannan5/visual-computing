import numpy as np

# a = np.full((1, 3, 5), 6)
# b = np.empty((2, 3, 5), dtype=np.uint8)
# c = np.array([1, 2, 3 [2, 5, 5, [55, 88, 77]]])
a = np.array([[[1, 2, 32],
               [5, 5, 55],
               [88, 77, 22]]])
b = np.array([[[1, 2, 32],
               [55, 75, 55],
               [111, 77, 122]]])


def array_add(array1, array2):
    add_array = np.add(array1, array2)
    val = add_array > 255
    if np.sum(val):
     for i in val:
        add_array[val] = array_slicing(add_array[val],i)
    print(add_array)


def array_sub(array1, array2):
    sub_array = np.subtract(array1, array2)
    val = sub_array < 0
    if np.sum(val):
     for i in sub_array:
      sub_array[val] = array_slicing(sub_array[val],i)
    print(sub_array)


def array_multiply(array1, array2):
    mul_array = np.multiply(array1, array2)
    val = mul_array >= 255
    if np.sum(val):
     for i in val:
      mul_array[val] = array_slicing(mul_array[val], i)
    print(mul_array)


def array_divide(array1, array2):
    # print(array1.shape)
    divide_array = np.divide(array1, array2)
   # val = ((divide_array > 0).all() and (divide_array < 0).all())
    val = np.where(np.logical_and(divide_array >= 0, divide_array <= 255))
    if np.sum(val):
     for i in val:
        divide_array[val] = array_slicing(divide_array[val], i)
    divide_array = divide_array.astype(int)
    print(divide_array)


def array_slicing(array_val, current_val):
    min_val = np.min(array_val)
    max_val = np.max(array_val)
    new_min = 0
    new_max = 255
    old_range = (max_val - min_val)
    if old_range == 0 :
      new_val = new_min
      array_val = new_val
    else:
     new_range = (new_max - new_min)
     new_val = (((array_val - min_val) * new_range) / old_range)+new_min
     array_val = new_val
    return array_val

# print(a.ndim)

# print(b.ndim)


array_add(a, b)

array_sub(a, b)


array_multiply(a, b)

array_divide(a, b)

