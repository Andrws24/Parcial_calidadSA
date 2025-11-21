import re

def validar_correo (email: str) -> bool:


   # Validad si el correo tiene un formato correcto.
   # retornar True si es valido, false si no.

   
   patron = r'^[a-zAzZ0-9_.+-]+@[a-zA-Z0-9-]+\. [a-zA-Z0-9-.]+$'
   return re.match (patron,email) is not None


  if __name__ == "__main__":
   
    prueba= [" prueba@gmail.com", "mal_correo", "otro@gmail.org" ]
    for correo in prueba:

        print (f"{correo}: {'Valido'if validar_correo(correo) else 'Invalido'}")