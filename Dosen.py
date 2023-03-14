from Human import Human;

class Dosen(Human):

    # constructor
    def __init__(self, nama="", jenisKelamin="", nip="", spidol="", laptop=""):
        super().__init__(nama, jenisKelamin)
        self.__NIP = nip
        self.__spidol = spidol
        self.__laptop = laptop
        self.__asisten = ""

    # setter and getter
    def setNIP(self, nip):
        self.__NIP = nip

    def setSpidol(self, spidol):
        self.__spidol = spidol

    def setLaptop(self, laptop):
        self.__laptop = laptop

    # assume lecturer only have 1 asisten which student contain NIM "6969"
    def setAsisten(self, prodi):
        for mhs in prodi.getListMhs():
            if mhs.getNIM() == "6969":
                self.__asisten = mhs.getNama()

    def getNIP(self):
        return self.__NIP
    
    def getSpidol(self):
        return self.__spidol
    
    def getLaptop(self):
        return self.__laptop
    
    def getAsisten(self):
        return self.__asisten
    
    def mengajar(self):
        print(f"{self.__nama} sedang mengajar!")
    
    def memberiTugas(self):
        print(f"{self.__nama} memberi tugas!")

    # method give grades for student
    def memeberiNilai(self, prodi):
        nama = input('Input student name : ')
        # after nama is inputed
        for mhs in prodi.getListMhs():
            # every student must have nilaiAsisten before lecturer input the grades
            if mhs.getNama() == nama:
                # assume asisten not have nilaiAsisten but they have nilai/grades from lecturer 
                if mhs.getNIM() == "6969":
                    nilai = input('Input grades: ')
                    mhs.setNilai(nilai)
                    print(f"Grades for {mhs.getNama()} was successfully inputed.\n")
                elif mhs.getNilaiAsisten() != "-":
                    nilai = input('Input grades: ')
                    mhs.setNilai(nilai)
                    print(f"Grades for {mhs.getNama()} was successfully inputed.\n")
                else:
                    print("Please wait until Asisten inputed the Grades..!\n")
                    break

    # method showData Lecturer
    def showData(self):
        print(">>> Lecturer Data Card")
        print("Name:", self.getNama())
        print("Gender:", self.getJenisKelamin())
        print("NIP:", self.getNIP())
        print("Laptop:", self.getLaptop())
        print("Asisten:", self.getAsisten())
        print("Spidol Collection:")
        for i in self.getSpidol():
            print(">", i)
        print("")

