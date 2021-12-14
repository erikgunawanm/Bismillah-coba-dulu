#Nama       : M. Erik Gunawan
#NIM        : 12220104

while True :
    fname = input ("Masukkan nama file : ")
    try :
        fhand = open (fname)
        break
    except :
        print ("File tidak ditemukan. Sila masukkan kembali _/\_")
        continue
count = 0
for line in fhand :
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split ()
    email = words[1]
    print (email)
    count = count + 1 
print ("Ada ", count, "baris yang diawali kata 'From '")