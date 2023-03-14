class Human():

    # constructor
    def __init__(self, nama="", jenisKelamin=""):
        self.__nama = nama
        self.__jenisKelamin = jenisKelamin

    # Setter methods
    def setNama(self, nama):
        self.__nama = nama

    def setJenisKelamin(self, jenisKelamin):
        self.__jenisKelamin = jenisKelamin

        # Getter methods
    def getNama(self):
        return self.__nama

    def getJenisKelamin(self):
        return self.__jenisKelamin
    
    def makan(self):
        print(f"{self.__nama} sedang makan..!\n")
    
    def minum(self):
        print(f"{self.__nama} sedang minum..!\n")
    
    def tidur(self):
        print(f"{self.__nama} sedang tidur..!\n")