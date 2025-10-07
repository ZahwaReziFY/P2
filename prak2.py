a = float(input("Masukan angka pertama: "))
b = float(input("Masukan angka kedua: "))
c = float(input("Masukan angka ketiga: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Angka terbesar adalah:", largest)