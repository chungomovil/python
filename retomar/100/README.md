## Preparativos para los ejercicios

### Paso I
El primer paso sera crear una base de datos nueva llamada **pythonya** y dentro de ella creamos la tabla **articulos** con las siguientes inserciones:

*CREATE TABLE `articulos` (*
  *`codigo` int(11) NOT NULL AUTO_INCREMENT,*
  *`descripcion` varchar(50) DEFAULT NULL,*
  *`precio` float DEFAULT NULL,*
  *PRIMARY KEY (`codigo`)*
*);*

*insert into `articulos` values (1,'papas',15);*
*insert into `articulos` values (2,'manzanas',24)*;
*insert into `articulos` values (3,'peras',45.3);*
*insert into `articulos` values (4,'naranjas',22);*
*insert into `articulos` values (5,'pomelos',29);*
*insert into `articulos` values (6,'frutillas',130);*
*insert into `articulos` values (7,'anana',75);*


### Paso II

Seguidamente procedemos a codificar el siguiente archivo PHP llamado **retornararticulos.php** que se conecta a la base de datos **pythonya**, recupera todas las filas de la tabla **articulos** y finalmente retorna todos los datos en formato JSON:

*<?php*
*header('Content-Type: application/json');*

*$server="localhost";*
*$usuario="root";*
*$clave="";*
*$base="pythonya";*
*$conexion=mysqli_connect($server,$usuario,$clave,$base) or die("problemas") ;*
*mysqli_set_charset($conexion,'utf8');*

*$datos = mysqli_query($conexion, "SELECT codigo, descripcion, precio from articulos");*
*$resultado = mysqli_fetch_all($datos, MYSQLI_ASSOC);*
*echo json_encode($resultado);*
*?>*

### Paso III

Codificaremos ahora otro archivo PHP denominado **retornararticulo.php** que se conectará a la base de datos, pero solo extraerá el archivo con el codigo que se le envíe como parámetro.

*<?php*
*header('Content-Type: application/json');*

*$server="localhost";*
*$usuario="root";*
*$clave="";*
*$base="pythonya";*
*$conexion=mysqli_connect($server,$usuario,$clave,$base) or die("problemas") ;*
*mysqli_set_charset($conexion,'utf8');*

*$datos = mysqli_query($conexion, "SELECT codigo, descripcion, precio from articulos where codigo=$_GET[codigo]");*
*$resultado = mysqli_fetch_all($datos, MYSQLI_ASSOC);*
*echo json_encode($resultado);*
*?>*

