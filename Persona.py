class Persona:
    dna = None
    esMutante = False

    def cargar_dna(self):
        self.dna = []
        contador = 1

        while (contador <= 6):
            lineaDna = input(
                "Ingrese la primer secuencia de ADN, debe contener las letras A, C, G y T y un largo de 6 caracteres: \n").upper() if contador == 1 else input(
                "").upper()

            # La razon de hacerlo verificando con un for es porque no se podía importar librerias, y ante la duda
            # se decidió hacerlo de esta manera. Sin embargo dentro de python se podría importar el paquete 're'
            # que permite trabajar con expresionres regulares, y verificar si matchearia o no con la entrada del usuario
            # de una manera mas eficiente.

            if len(lineaDna) != len([l for l in lineaDna if l == 'A' or l == 'C' or l == 'G' or l == 'T']) or len(
                    lineaDna) != 6:
                print("Datos inválidos, ingrese nuevamente la cadena de adn")
            else:
                contador += 1
                self.dna.append(lineaDna)
                print("Secuencia de DNA válida, continúe hasta llenar la matriz de DNA")
        print("ADN ingresado: ")
        print(self.dna)
        return self.dna

    def encontrarSecuenciasVerticalHorizontal(self):
        secuenciasEncontradas = 0

        # ITERACION HORIZONTAL Y VERTICAL A LA MISMA VEZ
        for i in range(len(self.dna)):

            # Pimero verificamos que las celdas en el centro sean iguales ya que
            # en el caso de que no lo sean implica que no hay secuencia de 4 letras
            # en toda la fila, entonces no es necesario iterar

            if self.dna[i][2] == self.dna[i][3]:
                contador = 1
                for j in range(1, len(self.dna[i])):
                    contador = contador + 1 if self.dna[i][j] == self.dna[i][j - 1] else 1
                    # Si ya pasa la mitad y vuelve a ver desigualdad se sale del bucle
                    if contador == 1 and j == 4: break
                    if contador >= 4:
                        secuenciasEncontradas += 1
                        break

            # Aprovechamos la iteracion y verificamos que las celdas en el centro de las
            # columnas sean iguales para repetir la misma logica de no iterar si no es necesario

            if (self.dna[2][i] == self.dna[3][i]):
                contador = 1
                for j in range(1, len(self.dna)):
                    contador = contador + 1 if self.dna[j][i] == self.dna[j - 1][i] else 1
                    # Si ya pasa la mitad y vuelve a ver desigualdad se sale del bucle
                    if contador == 1 and j == 4: break
                    if contador >= 4:
                        secuenciasEncontradas += 1
                        break
        return secuenciasEncontradas

    def encontrarSecuenciasDiagonales(self):
        secuenciasEncontradas = 0
        diagonales_contadas = set()
        diagonales_contadas_inversas = set()

        for i in range(0, 3):
            for j in range(0, 3):
                if self.dna[i][j] == self.dna[i + 1][j + 1] and self.dna[i + 1][j + 1] == self.dna[i + 2][j + 2] and self.dna[i + 2][j + 2] == \
                        self.dna[i + 3][j + 3]:
                    inicio_diagonal = (i, j)
                    if inicio_diagonal not in diagonales_contadas:
                        diagonales_contadas.add((i, j))
                        diagonales_contadas.add((i + 1, j + 1))
                        diagonales_contadas.add((i + 2, j + 2))
                        diagonales_contadas.add((i + 3, j + 3))
                        secuenciasEncontradas += 1
                    if secuenciasEncontradas > 1: break
            if secuenciasEncontradas > 1: break

            # Utilizamos el mismo for para iterar tambien sobre la diagonal inversa
            for k in range(3, 6):
                if self.dna[i][k] == self.dna[i + 1][k - 1] and self.dna[i + 1][k - 1] == self.dna[i + 2][k - 2] and self.dna[i + 2][k - 2] == \
                        self.dna[i + 3][k - 3]:
                    inicio_diagonal = (i, k)
                    if inicio_diagonal not in diagonales_contadas_inversas:
                        diagonales_contadas_inversas.add((i, k))
                        diagonales_contadas_inversas.add((i + 1, k - 1))
                        diagonales_contadas_inversas.add((i + 2, k - 2))
                        diagonales_contadas_inversas.add((i + 3, k - 3))
                        secuenciasEncontradas += 1
                    if secuenciasEncontradas > 1: break
            if secuenciasEncontradas > 1: break

        return secuenciasEncontradas

    def isMutant(self):

        secuencias = self.encontrarSecuenciasVerticalHorizontal()
        if secuencias > 1:
            self.esMutante = True
        secuencias += self.encontrarSecuenciasDiagonales()

        self.esMutante = True if secuencias > 1 else False
        return self.esMutante