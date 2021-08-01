from distutils.core import setup
import py2exe
import proyecto_estimaciones
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st
import os
import sys

archivo=os.path.dirname(__file__)
imagenes=str(archivo)+"\\images"

my_data_files=[]

for archivo in os.listdir(imagenes):
    imagen="images", [os.path.join(imagenes, archivo)]
    my_data_files.append(imagen)

setup(
    data_files=my_data_files,
    windows=["proyecto_estimaciones.py"],
    options = {"py2exe": {"compressed": 1, "optimize": 2,"dll_excludes": "w9xpopen.exe", "ascii": 0, "bundle_files": 1}},
    zipfile = None)
