import sys
import os

# Adicionar o diretório raiz ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.funcoes import *

if __name__ == "__main__":
    # Testar a criação de um novo chamado
    chamado = gerar_chamado()
    print("Novo chamado criado:", chamado)
    
    # Testar a sequência
    sequencia = carregar_contador()
    print("Sequência atual:",sequencia)