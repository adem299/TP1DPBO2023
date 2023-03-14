# TP1DPBO2023
Saya Ade Mulyana NIM 2108799 mengerjakan TP1 dalam mata kuliah Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.

# Desain Program
![DiagramTp1](https://user-images.githubusercontent.com/100661834/225004371-5a858c15-a4d0-475d-957d-22e3ff159d53.png)

Berdasarkan Diagram diatas dapat disimpulkan:
Terdapat 7 class diantaranya:
1. Human
   Terdiri dari 2 attribute nama dan jeniKelamin, juga terdapat beberapa method diantaranya get()set() makan(), minum() dan tidur(). Human merupakan root class
2. Dosen
   Tambahan 4 attribute diantaranya NIP, spidol[], laptop dan asisten, juga terdapat beberapa method get()set() diantaranya mengajar(), memberiTugas(), memberiNilai(Prodi), dan showData(). Class Dosen merupakan child class dari Human dimana terdapat attribute tambahan selain dari attribute parent class. Class Dosen juga mengcomposite Prodi untuk mendapatkan data seluruh mahasiswa, selain itu class Dosen juga has a atau mempunyai class AsistenDosen.
3. Mahasiswa
   Tambahan 6 attribute diantaranya NIM, status, buku[], laptop, nilai dan nilaiAsisten juga terdapat beberapa method diantaranya get()set(), belajar(), dan showData(). class Mahasiswa merupakan child class dari Human dimana terdapat attribute tambahan dan prilaku yang sama seperti class Human.
4. AsistenDosen
   Terdapat 1 attribute spidol dan beberapa method yaitu get(),set(), membantuMengajar(), collectionMarkers(), memberiNilaiAsisten(Prodi). Class ini merupakan turunan dari class Mahasiswa, seperti pada umunya Asisten adalah seorang Mahasiswa. Asumsi untuk atribut nilaiAsisten berisi null / "-" dikarenakan AsistenDosen tidak bisa mengisi sendiri nilaiAsisten nya.
5. AnggotaEnglishClub
   Terdapat attribute listAnggotaEnglishClub dan beberapa method seperti belajarEnglish(), merancangProke(), dan showAnggota(). Sama sepeti AsistenDosen class AnggotaEnglishClub juga merupakan Mahasiswa, dimana class ini merupakan child class dari class Mahasiswa.
6. AnggotaBem
   Terdapat attribute listAnggotaBem dan beberapa method seperti merancangProker(), melaksankanProker(), dan showAnggotaBem(). Sama sepeti AsistenDosen class, AnggotaBem juga merupakan Mahasiswa, dimana class ini merupakan child class dari class Mahasiswa.
8. Prodi
   Terdiri dari attribut listMahasiswa[], dan namaProdi juga terdapat beberapa methode seperti get(),set(), dan showListMhs(). Class ini mengcomposite class Mahasiswa untuk mendapatkan semua data Mahasiswa.

# Alur Program
1. Program menampilkan Menu

![Screenshot from 2023-03-14 19-18-03](https://user-images.githubusercontent.com/100661834/225012014-3f0257b9-3845-4b60-b3ef-853167e66cc9.png)

2. Jika opsi 1 di pilih program akan menampilkan list Mahasiswa prodi Ilmu Komputer

![Screenshot from 2023-03-14 19-19-16](https://user-images.githubusercontent.com/100661834/225012547-e54ae9e0-029f-4f3a-a6a2-3dfbc7b330a0.png)

3. Jika opsi 1 di pilih program akan menampilkan Student data card dimana nilai dan nilaiAsisten masih null "-" dikarenakan belum ada inputan

![Screenshot from 2023-03-14 19-24-08](https://user-images.githubusercontent.com/100661834/225013304-46e2bba8-6115-4f06-8db3-56e37b4b0a79.png)

4. Ketika opsi 5 dipilih yang merupakan AsistenDosen lalu opsi 7 dipilih untuk memberi nilaiAsisten program akan meminta inputan Nama mahasiswa dan nilaiAsisten, nilaiAsisten Mahasiswa tersebut sekarang telah terisi.

![Screenshot from 2023-03-14 19-31-06](https://user-images.githubusercontent.com/100661834/225014491-756417b0-8244-4c1c-b03c-1e8337437045.png)

5. Ketika opsi 2 dari menu awal dipilih program akan menampilkan menuLecturer

![Screenshot from 2023-03-14 19-32-02](https://user-images.githubusercontent.com/100661834/225014811-4063121b-21a8-4e96-a07b-ddcef0213f0b.png)

6. Jika opsi 2 dari menuLecturer dipilih program akan meminta inputan Untuk mengisi nilai sesuai nama yang di input, sekarang Mahasiswa tersebut sudah memiliki nilai pada attribute nilai nya.

![Screenshot from 2023-03-14 19-33-03](https://user-images.githubusercontent.com/100661834/225015909-b241780d-c3b3-4c0f-94d1-845417ebeae6.png)
![Screenshot from 2023-03-14 19-33-43](https://user-images.githubusercontent.com/100661834/225016500-b7446d64-0a1b-4e39-acbe-45af6a27bd07.png)

7. Bonus case, jika Dosen input nilai ke mahasiswa yang nilaiAsisten nya masih null "-" program akan meminta dosen untuk menunggu nilaiAsisten di isi terlebih dahulu.

![Screenshot from 2023-03-14 19-34-28](https://user-images.githubusercontent.com/100661834/225017256-d2b71d73-873c-4039-ace2-7ccf0c2f287d.png)

