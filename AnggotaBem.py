from Mahasiswa import Mahasiswa

class AnggotaBem(Mahasiswa):
    __listAnggotaBem = []

    # constructor
    def __init__(self, nama="", jenisKelamin="", NIM="", status="", buku="", laptop=""):
        super().__init__(nama, jenisKelamin, NIM, status, buku, laptop)
        self.__listAnggotaBem.append(nama)

    # show listAnggotaBem
    def showAnggotaBem(self):
        i=0
        for listAnggota in self.__listAnggotaBem:
            print(str(i+1), ". ", listAnggota)
        print("")

    # Bem Method
    def merancangProker(self):
        print(f'{self.getNama()} Sedang Merancang proker..!\n')
    
    def melaksankanProker(self):
        print(f'{self.getNama()} Sedang Melaksanakan proker..!\n')
    
    def menghadiriEvaluasi(self):
        print(f'{self.getNama()} Sedang Menghadiri Evaluasi..!\n')