# Verificar donde esta python y pip

-which python3

-which pip3

# Si estas en linus o wsl debes instalar

sudo apt install -y python3-venv

# Poner cada proyecto en su propio ambiente, entrar en cada carpeta.

python3 -m venv env

# Activar el ambiente# 

source env/bin/activate

# Salir del ambiente virtual

deactivate

# Podemos instalar las librerias necesarias en el ambiente virtual como por ejemplo

pip3 install matplotlib==3.5.0

# Verificar las instalaciones

pip3 freeze

# Generar el archivo con el siguiente comando

pip3 freeze > requirements.txt

# Revisar lo que hay dentro del archivo

cat requirements.txt

# Instalar las dependencias necesarias para contribuir más rápido en proyectos

pip3 install -r requirements.txt

# Preparar archivo para contribución

# App Project

```sh
git clone
cd app
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
python3 main.py

```