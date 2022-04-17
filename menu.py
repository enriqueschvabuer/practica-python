import random


def conversor (valor_dolar):
    cantidad_moneda = float(input("ingrese cantidad de pesos: "))
    dolares = str(round(cantidad_moneda / valor_dolar, 2))
    print ("tienes $" + dolares + " dolares ")
    

def run():
    respuesta = "s"
    while respuesta == "s" :
        menu = int(input(""" 
        1-Coversor de monedas
        2-adivina el numero
        3-Pesos Uruguayos

        Elige una opción: 

        """))


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


if __name__ == "__main__":
    run()
