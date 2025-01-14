import os
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))  # Diretório do script
file_path = os.path.join(script_dir, "produtos.csv")     # Caminho completo do arquivo

tabela = pd.read_csv(file_path)
print(tabela)