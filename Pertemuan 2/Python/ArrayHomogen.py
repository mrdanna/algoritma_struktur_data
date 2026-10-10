from array import array

nilai = array('i', [90, 85, 70])
nilai.append(100)

print(nilai)        # array('i', [90, 85, 70, 100])
print(nilai[1])     # 85