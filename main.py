# Saya Ade Mulyana NIM 2108799 mengerjakan TP1 dalam mata kuliah Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.

from Prodi import Prodi
from Dosen import Dosen
from AnggotaBem import AnggotaBem
from AnggotaEnglishClub import AnggotaEnglishClub as AnggotaEC 
from AsistenDosen import AsistenDosen as asdos
from Mahasiswa import Mahasiswa

## Declare Every environment needed
booksOfScience = ["Physics", "Chemistry", "Astronomy"]
booksOfEarth = ["Geophysics", "Geology"]
booksOfTeyvat = ["Archon wars", "Story of Khanneriah", "Wonderful Inazuma", "Dawn Winery ASMR Songs"]
markersPrimary = ["Black", "Red", "Blue"]
markersRGB = ["Red", "Green", "Blue"]


Rose = Dosen("Rose", "Female", "1234", markersPrimary, "Acer")

Resyad = Mahasiswa("Resyad", "Male", "1123", "Mahasiswa biasa", booksOfEarth, "Lenovo")
Pahri = AnggotaBem("Pahri", "Male", "8890", "Anggota BEM", booksOfScience, "Advan")
Angga = AnggotaEC("Angga", "Male", "1124", "Anggota English Club", booksOfEarth, "Huawei")
Getsby = AnggotaEC("Getsby", "Male", "1198","Anggota English Club", booksOfTeyvat, "Acer")

Mila = asdos("Mila", "Female", "6969","Asisten", booksOfTeyvat, markersRGB, "Toshiba")


ilkom = Prodi(Resyad, "Ilmu Komputer")
ilkom.setListMhs(Angga)
ilkom.setListMhs(Pahri)
ilkom.setListMhs(Getsby)
ilkom.setListMhs(Mila)

# set asisten
Rose.setAsisten(ilkom)

## Main Menu functions
def menuMain():
    print("""
===========================
+++---Halu University---+++
|| 1. Show All Mahasiswa ||
|| 2. Show Dosen         ||
|| 3. Close Program      ||
+++---------------------+++
============================
    """)

## Student Menu functions
def menuStudent():
    print("======================")
    print(" 1. Show Id Card      ")
    print(" 2. Makan             ")
    print(" 3. Minum             ")
    print(" 4. Tidur             ")
    print(" 5. Belajar           ")
    print("======================")

## Lecturer menu Functions
def menuLecturer(lecture):
    print("======================")
    print("This is Lecturer", lecture.getNama())
    print("----------------------")
    print(" 1. Show data Card    ")
    print(" 2. Gives a Grades    ")
    print(" 3. Makan             ")
    print(" 4. Minum             ")
    print(" 5. Tidur             ")
    print(" 0. Back to main Menu ")
    print("======================")

## English Club Member menu Function
def ecMenu(objStudent):
    print(f"Special action for {objStudent.getStatus()}")
    print("======================")
    print(" 6. Belajar Bahasa Inggris")
    print(" 7. Merancang proker")
    print(" 8. Show English Club Member ")
    print(" 0. Back to main Menu ")
    print("======================")

## BEM member menu functions
def bemMenu(objStudent):
    print(f"Special action for {objStudent.getStatus()}")
    print("======================")
    print(" 6. Sedang Merancang proker")
    print(" 7. Sedang Melaksanakan proker")
    print(" 8. Sedang Menghadiri Evaluasi")
    print(" 0. Back to main Menu ")
    print("======================")

## Asisten menu functions
def asistenMenu(objStudent):
    print(f"Special action for {objStudent.getStatus()}")
    print("======================")
    print(" 6. Membantu Dosen mengajar")
    print(" 7. Memberi nilaiAsisten")
    print(" 0. Back to main Menu ")
    print("======================")


## Student Action functions
def studentAction(ypt, objStudent):
    if ypt == "1":
        objStudent.showData()
        # show markers collection only for Asisten
        if objStudent.getNIM() == "6969":
            objStudent.collectionMarkers()
    elif ypt == "2":
        objStudent.makan()
    elif ypt == "3":
        objStudent.minum()
    elif ypt == "4":
        objStudent.tidur()
    elif ypt == "5":
        objStudent.belajar()
    else:
        print("Please input the Correct Action!")


## Start program
ans = True
while ans:
    # show main menu
    menuMain()
    ipt = input('Select option: ')

    if ipt == "1":
        flag = False 
        # show all list mhs
        ilkom.showListMhs()
        print("0. Back to main Menu")
        # take input from user for action
        xpt = input('Choose student: ')
        if xpt == "0":
            continue
        elif xpt == "1": # this action for Resyad
            # while flag not true, looping this step
            while flag!= True:
                # show menu for student
                menuStudent()
                print(" 0. Back to main Menu")

                ypt = input('Choose action: ')
                # if action = 0, the program will go back to the main menu 
                if ypt == "0":
                    flag = True
                else:
                    studentAction(ypt, Resyad)

        elif xpt == "2": # this action for Angga (EngClub)
            while flag!= True:
                # show menu for student and EncLub member
                menuStudent()
                ecMenu(Angga)
                
                ypt = input('Choose action: ')
                # if action = 0, the program will go back to the main menu 
                if ypt == "0":
                    flag = True
                elif ypt == "6":
                    Angga.belajarEnglish()
                elif ypt == "7":
                    Angga.merancangProker()
                elif ypt == "8":
                    Angga.showAnggotaEC()
                else:
                    studentAction(ypt, Angga)

        elif xpt == "3":
            while flag!= True:
                # show menu for student and Bem member
                menuStudent()
                bemMenu(Pahri)
                
                ypt = input('Choose action: ')
                # if action = 0, the program will go back to the main menu 
                if ypt == "0":
                    flag = True
                elif ypt == "6":
                    Pahri.merancangProker()
                elif ypt == "7":
                    Pahri.melaksankanProker()
                elif ypt == "8":
                    Pahri.menghadiriEvaluasi()
                else:
                    studentAction(ypt, Angga)

        elif xpt == "4":
            while flag!= True:
                # show menu for student and EncLub member
                menuStudent()
                ecMenu(Getsby)
                
                ypt = input('Choose action: ')
                # if action = 0, the program will go back to the main menu 
                if ypt == "0":
                    flag = True
                elif ypt == "6":
                    Getsby.belajarEnglish()
                elif ypt == "7":
                    Getsby.merancangProker()
                elif ypt == "8":
                    Getsby.showAnggotaEC()
                else:
                    studentAction(ypt, Getsby)

        elif xpt == "5":
            while flag!= True:
                # show menu for student and asisten
                menuStudent()
                asistenMenu(Mila)
                ypt = input('Choose action: ')
                # if action = 0, the program will go back to the main menu 
                if ypt == "0":
                    flag = True
                elif ypt == "6":
                    Mila.membantuMengajar()
                elif ypt == "7":
                    Mila.memeberiNilaiAsisten(ilkom)
                else:
                    studentAction(ypt, Mila)
                    
    elif ipt == "2":
        # this is lecturer program
        flag = False
        # run this state while flag still false
        while flag!= True:
            # show menu for lecturer
            menuLecturer(Rose)
            # take input from user
            xpt = input('Choose action: ')
            if xpt == "0":
                flag = True
            elif xpt == "1":
                Rose.showData()
            elif xpt == "2":
                Rose.memeberiNilai(ilkom)
            elif xpt == "3":
                Rose.makan()
            elif xpt == "4":
                Rose.minum()
            elif xpt == "5":
                Rose.tidur()
            else:
                print("Please input the Correct Action!")

    elif ipt == "3":
        # close program
        print("Thanks, see you next time...\n")
        ans = False
    else:
        print("Please input the correct option!")
    
        

