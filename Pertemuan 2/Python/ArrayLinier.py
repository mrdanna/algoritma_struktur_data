def linear_search(arr, target):
    for i, nilai in enumerate(arr):
        if nilai == target:
            return i
    return -1

data = [10, 20, 30, 40, 50]
print(linear_search(data, 30))  # 2
print(linear_search(data, 99))  # -1