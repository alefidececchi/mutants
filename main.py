from Persona import Persona

continuarPrograma = True

while continuarPrograma:
    persona = Persona()
    dna = persona.cargar_dna()
    print("Buscando secuencias...")
    resultado = persona.isMutant()
    print("La invocacion del metodo isMutant() devolvió: " + str(resultado))

    print("El adn cargado es mutante") if persona.esMutante else print("El adn cargado no es mutante")
    lectura = input('Desea cargar el adn de otra persona? "S" para continuar, o presione cualquier otra tecla para salir ').upper()
    continuarPrograma = lectura == "S"

