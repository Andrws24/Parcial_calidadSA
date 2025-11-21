Que es ACT?

act es una herramienta la cual nos permite ejecutar de manera local
los workflows de GITBUH ACTIONS, esto sin necesidad de hacer push
en el repositorio.

los requisitos.
Docker:  - Act utiliza de docker para simular los runners de GIT HUB 
         - Debe estar Docker ya instalado
ACT:     - Se puede instalar desde la documentacion oficial : https://github.com/nektos/act
         - Se recomienda usar Versiones anterior ya que son mas estables.


Comando para ejecutar el workflow localmente

act push -P ubuntu-latest=ghcr.io/catthehacker/ubuntu:full-latest
push corresponde al evento que activa tu workflow (on: push).

-P ubuntu-latest=... indica la imagen de Docker para simular el runner ubuntu-latest.

se usar act pull_request si cuando se quiere simular un pull request
