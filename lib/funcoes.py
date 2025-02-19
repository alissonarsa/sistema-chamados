import json
import os

# Determinar o diretório base do projeto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Construir o caminho para o arquivo JSON relativo ao diretório base
PATH = os.path.join(BASE_DIR, "../database/chamados.json")


def inicializar_arquivo():
    if not os.path.exists(PATH) or os.path.getsize(PATH) == 0:
        with open(PATH, 'w') as file:
            json.dump({"contador": 0, "chamados": []}, file, indent=4)

def carregar_contador():
    inicializar_arquivo()
    with open(PATH, "r") as f:
        data = json.load(f)
        return data.get("contador", 0)

def salvar_contador(valor):
    inicializar_arquivo()
    with open(PATH, "r") as f:
        data = json.load(f)
    data["contador"] = valor
    with open(PATH, "w") as f:
        json.dump(data, f, indent=4)

def gerar_chamado():
    contador = carregar_contador() + 1
    salvar_contador(contador)
    return f"#{contador:09d}"