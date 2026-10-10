def insert_at(arr, index, value):
    arr.append(None)  # memperbesar array
    for i in range(len(arr) - 1, index, -1):
        arr[i] = arr[i - 1]
    arr[index] = value

def delete_at(arr, index):
    if index < 0 or index >= len(arr):
        raise IndexError("Indeks di luar jangkauan")

    for i in range(index, len(arr) - 1):
        arr[i] = arr[i + 1]

    arr.pop()

data = [10, 20, 30, 40]
insert_at(data, 2, 25)
print(data)  # [10, 20, 25, 30, 40]

delete_at(data, 2)
print(data)  # [10, 20, 30, 40]