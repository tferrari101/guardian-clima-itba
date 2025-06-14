from ia_consejera import obtener_consejo_ia_gemini
from acerca import mostrar_info_acerca_de
import config 

def obtener_ultima_consulta_usuario(usuario):
    """
    Devuelve una consulta de ejemplo se puede conectar con historial_global.csv.
    """
    return {
        'temperatura': x,
        'condicion_clima': "x+1",
        'viento': x+2,
        'humedad': x+3
    }

def mostrar_menu_principal(usuario):
    while True:
        print("\n=== MENÚ PRINCIPAL DE GUARDIÁNCLIMA ITBA ===")
        print("1. Consultar clima")
        print("2. Ver historial")
        print("3. Estadísticas globales")
        print("4. Consejo IA")
        print("5. Acerca de...")
        print("6. Cerrar sesión")

        opcion = input("Elige una opción: ")
        if opcion == "1":

          ...
        elif opcion == "2":

          ...
        elif opcion == "3":

          ...
        
        elif opcion == "4":
            
            datos = obtener_ultima_consulta_usuario(usuario)

            consejo = obtener_consejo_ia_gemini(
                config.API_KEY_GEMINI, #Configurar convenientemente de la API
                datos['temperatura'],
                datos['condicion_clima'],
                datos['viento'],
                datos['humedad']
            )
            
            print("\n Consejo de vestimenta:")
            print(consejo)

        elif opcion == "5":
            mostrar_info_acerca_de(
                nombre_grupo="Grupo 92",
                integrantes=["Nombre 1", "Nombre 2", "Nombre 3"]
            )

        elif opcion == "6":
            print("\nCerrando sesión... ¡Hasta pronto!")
            break
        else:
            print("Esa opción aún no está implementada. Por favor ingrese una opción correcta") #Por si el usuario ingresa una opción por encima del número 6


if __name__ == "__main__":
    usuario_logueado = "ingreso"  
    mostrar_menu_principal(usuario_logueado) # Esto es solo un ejemplo, despues se va a conectar con el sistema de usuarios

