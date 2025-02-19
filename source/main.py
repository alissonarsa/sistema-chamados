import sys
import os

# Adicionar o diretório raiz ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.funcoes import *

while True:
    print("""
    
    1 - Novo Chamado
    2 - Buscar Chamado
    3 - Listar Chamados por Prioridade
    3 - Reverter Chamado
    5 - Limpar lista de Chamados
    
    """)