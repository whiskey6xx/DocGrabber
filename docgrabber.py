import os, shutil, getpass


username = getpass.getuser()
user_directory = " " 
storage_directory = "D:\" + "\\docgrabber_storage"
word_directory = storage_directory + "\\wordDocs"
pdf_directory = storage_directory + "\\pdfDocs"
txt_directory = storage_directory + "\\txtDocs"
img_directory = storage_directory + "\\imgDocs"
excel_directory = storage_directory + "\\excelDocs"


def back_up():
    if os.path.exists(storage_directory):
        print("storage exists!")
    else:
        os.makedirs(storage_directory)
        print("Storage created!")
    #word
    if os.path.exists(word_directory):
        print("word storage exists!")
    else:
        os.makedirs(word_directory)
        print("word Storage created!")
    #pdf
    if os.path.exists(pdf_directory):
        print("pdf storage exists!")
    else:
        os.makedirs(pdf_directory)
        print("pdf Storage created!")
    #text
    if os.path.exists(txt_directory):
        print("text storage exists!")
    else:
        os.makedirs(txt_directory)
        print("text Storage created!")
    #excel
    if os.path.exists(excel_directory):
        print("excel storage exists!")
    else:
        os.makedirs(excel_directory)
        print("excel Storage created!")



def grab(Directory):
    for root, dirs, files in os.walk(Directory):
        try:
            for i in files:
                split = os.path.splitext(i)
                file_ext = split[1]
                if file_ext == ".docx":
                    print(i)
                    shutil.copy(os.path.join(root, i), word_directory)
                    print(str(i) + " saved to " + str(word_directory))
                elif file_ext == ".pdf":
                    print(i)
                    shutil.copy(os.path.join(root, i), pdf_directory)
                    print(str(i) + " saved to " + str(pdf_directory))
                elif file_ext == ".txt":
                    print(i)
                    shutil.copy(os.path.join(root, i), txt_directory)
                    print(str(i) + " saved to " + str(txt_directory))
                elif file_ext == ".xls":
                    print(i)
                    shutil.copy(os.path.join(root, i), excel_directory)
                    print(str(i) + " saved to " + str(excel_directory))
                else:
                    print(i)
        except PermissionError:
            continue

back_up()

grab(user_directory)


        
