def mostrar_info_acerca_de(nombre_grupo, integrantes):
    """
    Muestra la información de la aplicación GuardiánClima ITBA y los créditos del equipo.
    """

    print("\n  Acerca de GuardiánClima ITBA")
    print("-" * 50)
    print("""
Guardián Clima ITBA es una aplicación desarrollada en Python
que te permite consultar el clima actual, guardar tus búsquedas, 
generar estadísticas globales y recibir consejos personalizados de vestimenta
gracias a una IA conectada a Google Gemini.

La aplicación provee un entorno seguro de registro e inicio de sesión, 
validando contraseñas según criterios de seguridad estudiados en el 
módulo 4. También permite acceder a un menú completo de funciones útiles 
del clima para el usuario.

Funcionalidades del Menú Principal:
1. Consultar clima actual (OpenWeatherMap) y guardar en historial.
2. Ver tu historial personal de consultas.
3. Obtener estadísticas globales de todas las consultas.
4. Recibir consejos personalizados de vestimenta por IA.
5. Ver esta sección con la descripción y créditos del grupo.
6. Cerrar sesión.

Tecnología usada:
- Python 3.x
- API de clima: OpenWeatherMap
- API de IA generativa: Google Gemini
- Manejo de archivos CSV (usuarios e historial)
- Librerías: requests, csv, google-generativeai
""")

    print("Desarrollado por el grupo:", nombre_grupo)
    print("Integrantes:")
    for integrante in integrantes:
        print(f"- {integrante}")
