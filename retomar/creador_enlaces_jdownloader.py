from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

#enlace_padre=input("Enlace de la lista de reproducción: ")
enlace_padre=input("Enlace: ")
navegador_opciones=Options()
#Indicamos la ruta DESTINO de la carpeta donde se almacenarán la cookies de chrome
navegador_opciones.add_argument("--user-data-dir=C:\\environments\\selenium")
#Indicamos donde esta el ejecutable "chromedriver" (necesario descargarlos para emular la ejecucion de chrome con selenium) y le agregamos la carpeta de las cookies
navegador=webdriver.Chrome("C:\chromedriver\chromedriver.exe", options=navegador_opciones)
navegador.get(enlace_padre)
time.sleep(4)
busqueda=bs(navegador.page_source, "lxml")
lista_etiqueta_enlace=busqueda.find_all(id="video-title")
for etiqueta_enlace in lista_etiqueta_enlace:
    enlace=etiqueta_enlace.get("href")
    
#<---PENDIENTE DE PONER UN ENTORNO GRAFICO, BUSCAR COMO BAJAR COMPLETAMENTE LA PAGINA (haciendo scroll) CON SELENIUM Y CERRARLO DESDE LA INTERFAZ VISUAL COPIANDO TODOS LOS ENLACES--->
