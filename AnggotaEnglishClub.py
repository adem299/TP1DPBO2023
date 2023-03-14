from Mahasiswa import Mahasiswa

class AnggotaEnglishClub(Mahasiswa):

    __listAnggotaEC = []

    # constructor
    def __init__(self, nama="", jenisKelamin="", NIM="", status="", buku="", laptop=""):
        super().__init__(nama, jenisKelamin, NIM, status, buku, laptop)
        self.__listAnggotaEC.append(nama)


        # show all data in _listAnggotaEC
    def showAnggotaEC(self):
        i=0
        print(">>> Anggota English Club")
        for listAnggota in self.__listAnggotaEC:
            print(str(i+1), ". ", listAnggota, sep="")
            i+=1
        print("")
    
    def belajarEnglish(self):
        print(f'{self.getNama()} Sedang belajar bahasa inggris..!\n')
    
    def merancangProker(self):
        print(f'{self.getNama()} Sedang merancang proker klub bahasa inggris..!\n')