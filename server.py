#1.Import socket karena akan digunakan socket IPC
import socket

#2.Buat socket. Tipe socket client & server seharusnya sama
s = socket.socket()
print("Socket berhasil dibuat")

#3.Definisi IP & Port dari server untuk binding
ip = "127.0.0.1"
port = 12345

#4.Lakukan binding pada IP & port yang telah ditenukan
s.bind((ip,port))
pesan = "socket bind ke alamat "+ip+" dan port "+str(port)
print(pesan)

#5.Socket dalam keadaan mendengar & siap menerima koneksi
s.listen(5)
print("socket dalam state mendengarkan")

#selama socket mendengar
while True:
    
    #7.socket akan menerima koneksi
    c, addr =s.accept()
    print('Mendapat koneksi dari', addr)
    
    #8.socket server akan mengirmkan pesan ke client. Pada python, pesan akan didecode ketika akan dikirimkan & didecode ketika diterima. Encoding & decoding diperlukan agar mempunyai representasi yang sama
    pesan = "halo "+str(addr) + "Anda telah berhasil terkoneksi ke server"
    c.send(pesan.encode())
    
    #9.socket menutup koneksi & siap menerima koneksi lainnya
    c.close()