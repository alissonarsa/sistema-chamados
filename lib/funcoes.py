import json
import os

# Determinar o diretório base do projeto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Construir o caminho para o arquivo JSON relativo ao diretório base
PATH = os.path.join(BASE_DIR, "../database/chamados.json")

# funções gerais

def inicializar_arquivo():
    if not os.path.exists(PATH) or os.path.getsize(PATH) == 0:
        with open(PATH, 'w') as file:
            json.dump({"contador": 0, "chamados": []}, file, indent=4)

# funções para o contador

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

# funções para os chamados

def carregar_chamados():
    inicializar_arquivo()
    with open(PATH, "r") as f:
        data = json.load(f)
        return data.get("chamados", [])

def salvar_chamados(chamados):
    inicializar_arquivo()
    with open(PATH, "r") as f:
        data = json.load(f)
    data["chamados"] = chamados
    with open(PATH, "w") as f:
        json.dump(data, f, indent=4)

def buscar_chamado(termo):
    chamados = carregar_chamados()
    resultado = []
    for chamado in chamados:
        if termo in chamado['id'] or termo in chamado['descricao']:
            resultado.append(chamado)
    return resultado

def status_chamado(chamado_id, novo_status):
    chamados = carregar_chamados()
    for chamado in chamados:
        if chamado['id'] == chamado_id:
            chamado['status'] = novo_status
            salvar_chamados(chamados)
            return chamado
    return None

# funções para gerar chamados

def gerar_chamado(descricao, prioridade, status):
    contador = carregar_contador() + 1
    salvar_contador(contador)
    chamado = {
        "id": f"#{contador:09d}",
        "descricao": descricao,
        "prioridade": prioridade,
        "status": status
    }
    chamados = carregar_chamados()
    chamados.append(chamado)
    salvar_chamados(chamados)
    return chamado