import array
def move(arr):
    zero_i = 0
    for index, n in enumerate(arr):
        if n != 0:
            arr[zero_i] = n
            if zero_i != index:
                arr[index] = 0
            zero_i += 1
    return arr

# arr = array.array('i',[99, 0, -7, 0, 16])
# 파이썬은 메모리 절약을 위해 일정범위 안에 값의 id를 같게 사용

# for i in range(len(arr)):
#     print(f"{arr[i]:5} {id(arr[i])}")

# l = [99, 99]
# print(id(l[0]), id(l[1]))
arr = [99, 0, -7, 0, 16]
move(arr)
print(arr)

