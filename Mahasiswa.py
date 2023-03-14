from Human import Human

class Mahasiswa(Human):
    # constructor
    def __init__(self, nama="", jenisKelamin="", NIM="", status="", buku="", laptop="", nilai="-", nilaiAsisten="-"):
        super().__init__(nama, jenisKelamin)
        self.__NIM = NIM
        self.__status = status
        self.__buku = buku
        self.__laptop = laptop
        self.__nilai = nilai
        self.__nilaiAsisten = nilaiAsisten

    # setter and getter
    def setNIM(self, NIM):
        self.__NIM = NIM

    def setStatus(self, status):
        self.__status = status

    def setBuku(self, buku):
        self.__buku = buku

    def setLaptop(self, laptop):
        self.__laptop = laptop

    def setNilai(self, nilai):
        self.__nilai = nilai

    def setNilaiAsisten(self, nilai):
        self.__nilaiAsisten = nilai

    def getNIM(self):
        return self.__NIM
    
    def getStatus(self):
        return self.__status
    
    def getBuku(self):
        return self.__buku
    
    def getLaptop(self):
        return self.__laptop
    
    def getNilai(self):
        return self.__nilai
    
    def getNilaiAsisten(self):
        return self.__nilaiAsisten
    
    # method student
    def belajar(self):
        print(f"{self.getNama()} sedang belajar..!\n")

    # method show all data student
    def showData(self):
        print(">>> Student Data Card")
        print("Nama:", self.getNama())
        print("JenisKelamin:", self.getJenisKelamin())
        print("NIM:", self.getNIM())
        print("Nilai:", self.getNilai())
        print("Status:", self.getStatus())
        print("NilaiAsisten:", self.getNilaiAsisten())
        print("Jenis Laptop:", self.getLaptop())
        print("List Books:")
        for i in self.getBuku():
            print(">", i)
        print("")