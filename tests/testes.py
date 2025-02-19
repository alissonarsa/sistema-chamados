import sys
import os

# Adicionar o diretório raiz ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.funcoes import *

if __name__ == "__main__":
    # Testar a sequência
    sequencia = carregar_contador()
    print("Sequência atual:",sequencia)

    # Testar a listagem de chamados
    chamados = carregar_chamados()
    print("Lista de chamados:", chamados)

    # Testar a criação de um novo chamado
    chamado = gerar_chamado("Exemplo de descrição", "alta", "aberto")
    print("Novo chamado criado:", chamado)

    # Testar a função buscar_chamado
    termo = "não"
    resultados = buscar_chamado(termo)
    print(f"Resultados da busca por '{termo}':", resultados)

    # Testar a função status_chamado
    chamado_id = "#000000010"
    novo_status = "FINALIZADO"
    chamado_atualizado = status_chamado(chamado_id, novo_status)
    print(f"Chamado atualizado com novo status '{novo_status}':", chamado_atualizado)

    # Testar a função mover_chamado
    chamado_movido = mover_chamado()
    print(f"Chamado movido para finalizados:", chamado_movido)
    
    # Testar a função prioridade
    chamados_ordenados = prioridade()
    print("Chamados ordenados por prioridade:", chamados_ordenados)