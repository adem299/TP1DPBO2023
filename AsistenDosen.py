from Mahasiswa import Mahasiswa
class AsistenDosen(Mahasiswa):
    def __init__(self, nama="", jenisKelamin="", nim="", status="", buku="", spidol="", laptop=""):
        super().__init__(nama, jenisKelamin, nim, status, buku, laptop)
        self.spidol = spidol

    # get set
    def setSpidol(self, spidol):
        self.spidol = spidol

    def getSpidol(self):
        return self.spidol
    
    def membantuMengajar(self):
        print(f'{self.getNama()} Sedang mengajar..!\n')

    # show all Asisten collection Markers 
    def collectionMarkers(self):
        print("Markers Collection: ")
        for i in self.getSpidol():
            print(">>", i)
        print("")
    
    # give asisten grades for student
    def memeberiNilaiAsisten(self, prodi):
        nama = input('Masukan nama Mahasiswa: ')

        # take data from Prodi and looping
        for mhs in prodi.getListMhs():
            # if nama found from getList, input grades for that student
            if mhs.getNama() == nama:
                nilai = input('Masukan nilai asisten: ')
                mhs.setNilaiAsisten(nilai)
                print(f"Grades for {mhs.getNama()} was successfully inputed.\n")
