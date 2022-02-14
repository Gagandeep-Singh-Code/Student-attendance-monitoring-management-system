from subprocess import run
import sys
import os, shutil, glob


while True:
    print("****************Menu*****************")
    print("1. Add new student")
    print("2. Take attendance")
    print("3. Exit")
    x = int(input("Enter your choice: "))

    folderPath = './dataset'
    if x == 1:
        os.system("python add_student.py")                                                              #To add new student data
        a = int(input("Enter 1 to create new Person Group or 0 to use existing: "))
        if a == 1:
            os.system("python create_person_group.py")                                                  #To create new person group
        elif a == 0:
            pass
        else:
            print("Invalid choice.")
            pass
        os.system("python create_person.py " + max(glob.glob(os.path.join(folderPath, '*/')), key=os.path.getmtime))
        os.system("python add_person_faces.py " + max(glob.glob(os.path.join(folderPath, '*/')), key=os.path.getmtime))
        os.system("python train.py")
        os.system("python get_status.py")

    elif x == 2:
        os.system("python take_attendance.py")

        folder = './attendance'
        latest_folder = max(glob.glob(os.path.join(folder, '*/')), key=os.path.getmtime)
        croppedFol = './cropped'
        for image in os.listdir(latest_folder):
            if os.path.exists(croppedFol):
                shutil.rmtree(croppedFol)
            os.makedirs(croppedFol)
            os.system("python detect.py " + os.path.join(latest_folder, image))
            os.system("python spreadsheet.py ")
            os.system("python identify.py ")

    elif x == 3:
        print("Bye, have a great day!")
        break
    else:
        print("Invalid choice.")