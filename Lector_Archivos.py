import os
Lista_archivos = os.listdir()
for Archivo in Lista_archivos:
  with open(Archivo, "r") as archivo:
    print(archivo.read()+"\n")
