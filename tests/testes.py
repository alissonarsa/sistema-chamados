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