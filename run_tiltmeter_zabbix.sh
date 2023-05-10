#!/bin/bash

# Define variables
CONDA_PATH="/home/seiscomp/anaconda3/bin"
CONDA_ENV="soh_zabbix"
SCRIPT_PATH="/home/seiscomp/eclipse-workspace/soh_zabbix"
PYTHON_SCRIPT="soh_reftek.py"
CONFIG_FILE="configuration.txt"

# Carga el entorno de Conda dentro de la shell de bash
eval "$(${CONDA_PATH}/conda shell.bash hook)"

# Activa el ambiente Conda
conda activate ${CONDA_ENV}

# Navega hacia el directorio del script Python
cd ${SCRIPT_PATH}

# Ejecuta el script Python con el archivo de configuración y redirige la salida estándar a la salida de error
python ./${PYTHON_SCRIPT} ./${CONFIG_FILE} >&2

