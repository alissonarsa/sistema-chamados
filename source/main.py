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
    4 - Reverter e limpar a lista de Chamados
    5 - Status do Chamado
    
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
    elif menu == "4":
        print("Revertendo e limpando a lista de chamados")
        chamados_revertidos = reverter_e_limpar()
        print("Chamados revertidos e lista limpa:", chamados_revertidos)
    elif menu == "5":
        print("Alterando status do chamado")
        chamado_id = input("Digite o ID do chamado: ").lower()
        novo_status = input("Digite o novo status (aberto, em andamento, fechado, concluído): ").lower()
        chamado = status_chamado(chamado_id, novo_status)
        if chamado:
            print("Status do chamado alterado com sucesso!")
        else:
            print("Chamado não encontrado.")
    else:
        print("Opção inválida. Tente novamente.")