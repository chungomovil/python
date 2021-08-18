## Desplegar programa de automatización de WhatsApp (Ubuntu)

#### **Requisitos:**

`Ubuntu 18.04 o posterior`

`Python 3`

`Navegador Firefox`

`Escritorio remoto 'NoMachine'`

`Código fuente del programa de automatizar`



### Actualización del sistema

Lo primero que debemos hacer será actualizar el sistema:

`sudo apt-get update && sudo apt-get upgrade`

Una vez finalice el proceso de actualización procederemos a verificar que python 3 está instalado en el sistema (debería estar instalado).

`python3 --version`

En caso de no estar instalado:

`sudo apt-get install python3`

Instalamos el gestor de paquetes de python3.

`sudo apt-get install python3-pip`

Ahora instalaremos las librerías de **Selenium** y la de **MySQL**.

`sudo pip3 install --upgrade selenium mysql-connector`



### Escritorio Remoto

El paso inicial será instalar el sistema gráfico "Xorg" que será el encargado de virtualizar nuestra pantalla.

`sudo apt-get install xorg`

A continuación instalamos la librería encargada de simular una pantalla.

`sudo apt-get install xserver-xorg-video-dummy`

Una vez finalizada su instalación, creamos una pantalla virtual, ya que el objetivo es tener este equipo sin pantalla.

**Ruta:** `/etc/X11/xorg.conf`

Creamos el archivo si no existe: `sudo nano /etc/X11/xorg.conf`

Escribimos el siguiente código:

`Section "Device"`
    `Identifier  "Configured Video Device"`
    `Driver      "dummy"`
`EndSection`

`Section "Monitor"`
    `Identifier  "Configured Monitor"`
    `HorizSync 31.5-48.5`
    `VertRefresh 50-70`
`EndSection`

`Section "Screen"`
    `Identifier  "Default Screen"`
    `Monitor     "Configured Monitor"`
    `Device      "Configured Video Device"`
    `DefaultDepth 24`
    `SubSection "Display"`
    `Depth 24`
    `Modes "1366x768"`
    `EndSubSection`
`EndSection`

Entonces es el momento de desactivar el sistema gráfico Wayland **(No se lleva bien con los escritorios remotos).**

`sudo nano /etc/gdm3/custom.conf`

Y descomentamos la línea `WaylandEnable=false`, si no existe la creamos al final del documento.

El siguiente paso será instalar el programa de escritorio remoto 'NoMachine'. **(No instalar Anydesk, debido a que daba problemas al simular una pantalla conectada).**

**URL de descarga:** `https://www.nomachine.com/es/download`

Descargamos el ejecutable **.deb** y procedemos a ejecutarlo en la carpeta donde se haya guardado.

`sudo chmod +x <nombre-ejecutable.deb>`

`sudo dpkg -i <nombre-ejecutable.deb>`

**Nota:** No olvidar poner autologin en el usuario, se puede hacer por interfaz visual.

Reiniciamos ahora el sistema.

**SI TENEMOS UN MONITOR CONECTADO PUEDE QUE NO SE MUESTRE CORRECTAMENTE DESPUÉS DEL REINICIO.**

**SI ACCEDEMOS A TRAVÉS DE "NOMACHINE" SE VERÁ CORRECTAMENTE.**

Desde un ordenador cliente accedemos remotamente con "NoMachine".

El usuario y la clave que nos pedirá será la misma que la del sistema.



### Importar el programa de automatizar

Creamos una carpeta denominada "whatsapp" dentro de `/home/<usuario>` y copiamos los archivos del programa dentro de ella.

Descargamos ahora el driver de selenium para Firefox. Geckodriver.

Descargamos el archivo **.tar.gz** para linux64.

**URL de descarga: ** `https://github.com/mozilla/geckodriver/releases`

Vamos a la ubicación donde se haya descargado y lo descomprimimos:

`tar -xvf geckodriver.tar.gz`

Copiamos ahora el archivo resultante a la ruta `/usr/local/bin`



### Programando ejecución con Crontab

Creamos una rutina con "Crontab" escribiendo el comando:

`crontab -e`

Y al final del documento escribimos:

`00 10 * * * export DISPLAY=:0 && export PATH=$PATH:/usr/local/bin && python3 /home/<usuario>/whatsapp/automatizar_whatsapp.py`

Desglosándolo significaría:

`00 10 * * *`: Se ejecuta todo los días a las 10:00

`export DISPLAY=:0`: Para que crontab sepa que tiene que usar la interfaz gráfica en el monitor "0" (el emulado).

`export PATH=$PATH:/usr/lobal/bin`: Indicamos la ruta del "Geckodriver".

`python3`: El intérprete que lo ejecutará, también se puede poner su ruta absoluta `/usr/bin/python3`.

`/home/<usuario/whatsapp/automatizar_whatsapp.py`: Ruta del ejecutable.

Por último, si queremos saber si ha quedado guardada la configuración ejecutamos el comando:

`crontab -l`
