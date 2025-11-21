Valdación y logs

Como idenfircar fallos en los logs

Linter (pylint) los errores aparecen como codigos ej: E,W,C o F 
si el punraje es bajo, el comando termina con “exit code 2”. 
El workflow se detiene en ese pasos

Pruebas (pytest) Los logs muestran fallas como "FAILED" "ERROR"

Coverage:  si el porcentaje es menor al umbral confugirado. el paso termina con exit code 1.

GENERAL UN RUN FALLIDO  (LINTER)
<img width="949" height="65" alt="image" src="https://github.com/user-attachments/assets/17f9f5e4-075d-4223-a3bc-908dfefea4db" />



VISUALIZAR COBERTURA RUN fallido
<img width="1191" height="340" alt="image" src="https://github.com/user-attachments/assets/35c25893-d412-4252-8b93-cb50853566e5" />


RUN EXITOSO 


<img width="1200" height="381" alt="image" src="https://github.com/user-attachments/assets/0aee9d63-06df-4228-bae1-16dca5c9bdbc" />

la diferencia se que 
la cobertura fallida - estaba en 62% era baja 
la cobertura alta 100% esto quiere decir que ahora todos los casos que se ejecutan estan siendo subierto

