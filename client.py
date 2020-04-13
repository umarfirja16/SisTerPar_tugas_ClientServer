#1. Import socket karena akan digunakan socket IPC
import socket

#2.Buat Socket
s = socket.socket()

#3.Tentukan port server yang akan dituju. Membuka port dibawah 1024 membutuhkan hak akses administrator
port = 12345

#4.Lakukan koneksi ke server dengan socket 127.0.0.1:1234 fungsi connect mempunyai 2 parameter yaitu IP bertipe string dan port bertipe integer
s.connect(('192.168.137.100',port))

#5.Server akan mengirimkan pesan reply sehingga client harus menerimanya ketika menerima pesan, pesan akan disimpan dalam buffer. Ukuran buffer harus ditentukan misal: 1024 atau 2048 atau 4096 (apapun asal 2^n)
print(s.recv(1024).decode())

#6. Tutup koneksi jika telah selesai
s.close()
