class Prodi():
    __listMahasiswa = []

    def __init__(self, mhs, namaProdi=""):
        self.__listMahasiswa.append(mhs)
        self.__namaProdi = namaProdi

    def setNamaProdi(self, namaProdi):
        self.__namaProdi = namaProdi

    def setListMhs(self, mhs):
        self.__listMahasiswa.append(mhs)

    def getNamaProdi(self):
        return self.__namaProdi

    def getListMhs(self):
        return self.__listMahasiswa

    # method show All list Studunt in this Prodi
    def showListMhs(self):
        i=0
        print(">>> List Mahasiswa Prodi", self.__namaProdi)
        for mhs in self.__listMahasiswa:
            print((i+1),". ", mhs.getNama(), sep="")
            i+=1