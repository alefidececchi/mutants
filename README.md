# Mutants
* Nombre y Apellido: Alejandro Fidececchi
* DNI: 38372000
* Email: ale.fidececchi@gmail.com
## De que va el proyecto
El desafío consiste en encontrar personas las cuales cuentan con un ADN mutante.
El ADN está conformado por una matriz de 6 x 6, la cual contiene letras A, C, G y T. Cómo saber si una persona tiene un ADN mutante? Encontrando secuencias de 4 letras iguales tanto horizontal, vertical y diagonalmente en ambos sentidos.
Si hay 2 o más secuencias, quiere decir que la persona portadora de ese ADN es mutante.
...
## Como lo resolví
Primero me tomé un buen tiempo antes de ponerme a codear. Pensé en cual es la manera más eficiente, por lo que tuve que buscar en qué consiste un código eficiente. Me encontré con muchos factores a la hora de clasificar si un código es tal o no. El manejo de memoria, hacer lo posible por no anidar bucles. Teniendo esto en mente, intenté encontrar el algoritmo perfecto, el cual después de varios días supuse que no existía. Así que al no poder escapar del anidamiento de bucles ya que estamos hablando de una matriz, pensé en cuál sería una forma para recorrerla lo menos posible y aún así encontrar un buen resultado. La forma que se me occurrió fue pensar en qué celdas tendrían en común si una secuencia se ubica en un extremo, y otra secuencia estaría ubicada en el otro extremo, por lo que me encontre que para las filas las celdas compartidas son las que corresponden al indice de las columnas 2 y 3, de esta manera si estas celdas no son iguales, ya no es necesario recorrer todas sus columnas buscando la secuencia. Lo mismo sucede con las columnas, solo que estos valores se aplican a las filas. Para las diagonales sucede lo mismo, pero el algoritmo se acomplejiza. Además de pensar en estas coincidencias, también es necesario corroborar siempre que se pueda si lo que va del programa hay al menos dos secuencias, ya que de ser así el adn sería mutante y no tendría sentido seguir recorriendo la matriz. 
...
## Como correrlo
### En Linux:
1. No es necesario descargar Python ya que viene instalado por default, pero si es necesario que lo tengas actualizado, podes checkear la version con:
```
$ python --version
// o
$ python3 --version
```
2. Si la version es menor a 3.10 te sugiero que la actualices:
```
$ sudo apt update
$ sudo apt upgrade && apt-get upgrade python3
```
3. Ubicate en algun directorio vacío y clona el respositorio con
```
$ git clone https://github.com/alefidececchi/mutants.git
```
4. Ejecutá:
```
$ python3 main.py
// o
$ python main.py
```
### En windows:
1. Debes tener instalado Python 3.10, de no ser así podés acá hay una guía paso a paso para poder instalarlo correctamente: https://www.digitalocean.com/community/tutorials/install-python-windows-10
2. Clona el repositorio en alguna carpeta vacía (usa el comando descrito anteriormente).
3. Ejecutá:
```
$ python3 main.py
// o
$ python main.py
```
## Casos de prueba
Mutante = "ATGCGA", "CAGTGC", "TTATGT", "AGTTGG", "CTCTTA", "TCACTG"
<p>No mutante = "ATGCGA", "CAGTGC", "ATGCTA", "TTATGT", "CCCTCC", "AATCAG"</p>  
