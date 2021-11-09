print("Tugas Pratikum 2")
print()
bil_pertama=int(input("Angka Pertama\t:"))
bil_kedua=int(input("Angka Kedua\t:"))
bil_ketiga=int(input("Angka Ketiga\t:"))
print()
if  bil_pertama > bil_kedua and bil_pertama > bil_ketiga:
    kes = "Angka Pertama Lebih Besar"
elif bil_kedua > bil_ketiga and bil_kedua > bil_pertama:
    kes = "Angka Kedua Lebih Besar"
else :
    kes = "Angka Ketiga Lebih Besar"

print("Kesimpulan\t:" ,kes)