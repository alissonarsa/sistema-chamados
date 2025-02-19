import sys
import os

# Adicionar o diretório raiz ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.funcoes import *

while True:
    menu = input(f"""
    
    1 - Novo Chamado
    2 - Buscar Chamado
    3 - Listar Chamados por Prioridade
    4 - Reverter Chamado
    5 - Limpar lista de Chamados
    6 - Status do Chamado
    
    Escolha: """)
    
    if menu == "1":
        print("Vamos abrir seu CHAMADO")
        descricao = input("Descrição: ").lower()
        print("Defina a prioridades: BAIXA, MÉDIA, ALTA")
        prioridade = input("Escolha: ").upper()
        status = "ABERTO"
        gerar_chamado(descricao, prioridade, status)
    elif menu == "2":
        print("Vamos buscar um CHAMADO")
        busca = input("Pesquise seu chamdo: ").lower()
        buscar_chamado(busca)
    elif menu == "3":
        print("Vamos listar os chamados por prioridade")
        chamados_ordenados = prioridade()
        print("Chamados por prioridade:", chamados_ordenados)