import pyAesCrypt
import glob


def encrypt(in_file,out_file):

    #Buffer Size
    buffersize = 64 * 1024

    #Password for decrypt
    password = ""   #Put here your password

    #Encrypt Proccess
    try:
        pyAesCrypt.encryptFile(r"{0}".format(in_file),out_file,password,buffersize)
    except:
        print("Something went wrong")


FileNames = []

#All PDF files in current directory 
PdfFilenamesList = glob.glob('*.pdf')

#Takes All file names
for i in PdfFilenamesList:
    FileNames.append(i[:-4])

#Encrypt all Files
for j in range(len(PdfFilenamesList)):
    encrypt(PdfFilenamesList[j],FileNames[j])

print(FileNames)
print(PdfFilenamesList)

#Tomer Shweika