import random


def conversor (valor_dolar):
    cantidad_moneda = float(input("ingrese cantidad de pesos: "))
    dolares = str(round(cantidad_moneda / valor_dolar, 2))
    print ("tienes $" + dolares + " dolares ")


def primos(numero):
    if numero == 1 or numero == 0:
        return False
    else:
        contador = 0
    if numero < 4:
        return True
    else:
        for i in range(2,numero):
            if numero % i == 0:
                contador += 1
    if contador == 0:
        return True
    else:
        return False


def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False
    

def run():
    respuesta = "s"
    while respuesta == "s" :
        menu = input(""" 
        1-Coversor de monedas
        2-Adivina el numero
        3-Numeros primos
        4-Palindromos
        5-Salir

        Elige una opción: 

        """)


        if menu == 1:
            respuesta_conversor = "s"
            while respuesta_conversor == "s" :
                tipo_moneda = int(input("""
                1-Pesos Argentinos
                2-Pesos Chilenos
                3-Pesos Uruguayos

                Elige una opción: 

                """))

                if tipo_moneda == 1:  
                    conversor (196)   
                elif tipo_moneda == 2:
                    conversor (815) 
                elif tipo_moneda == 3:
                    conversor (42)   
                else:
                    print("Ingresaste una opción incorrecta")
                respuesta_conversor = input("desea continuar (s/n):")
                if respuesta_conversor == "n" :
                    break
                elif respuesta_conversor != "s":
                    respuesta_conversor=input("Ingresaste una opcion incorrecta.desea continuar (s/n):")


        elif menu == 2:
            respuesta_juego = "s"
            while respuesta_juego == "s":
                aleatorio = random.randint(1, 100)
                numero=int(input("ingrese un numero del 1 al 100: "))
                while aleatorio != numero:
                    if  numero < aleatorio:
                        numero = int(input("ingresa un numero mayor: "))
                    else:
                        numero = int(input("ingresa un numero menor: "))
                print("Ganaste")
                respuesta_juego=input("desea jugar nuevamente (s/n): ")
                if respuesta_juego == "n" :
                    break
                elif respuesta_juego != "s":
                    respuesta_juego=input("Ingresaste una opcion incorrecta.desea continuar (s/n):")


        elif menu == 3:
            respuesta_primos = "s"
            while respuesta_primos == "s":
                numero = int(input("ingrese un numero: "))
                if primos(numero):
                    print("es primo")
                else:
                    print("no es primo")
                respuesta_primos=input("desea ingresar otro numero (s/n): ")
                if respuesta_primos == "n" :
                    break
                elif respuesta_primos != "s":
                    respuesta_primos=input("Ingresaste una opcion incorrecta.desea continuar (s/n):")


        elif menu == 4:
            respuesta_palindromos = "s"
            while respuesta_palindromos == "s":
                palabra = input('Escribe una palabra: ')
                es_palindromo = palindromo(palabra)
                if es_palindromo == True:
                    print('Es palíndromo')
                else:
                    print('No es palíndromo')
                respuesta_palindromos=input("desea ingresar otra palabra (s/n): ")
                if respuesta_palindromos == "n" :
                    break
                elif respuesta_palindromos != "s":
                    respuesta_palindromos=input("Ingresaste una opcion incorrecta.desea continuar (s/n):")


        elif menu == 5:
            break
        

        respuesta = input("ingresaste una opcion inconrrecta. Desea continuar (s/n): ")       



if __name__ == "__main__":
    run()
