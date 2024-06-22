import pandas as pd

class PreProcessamento:
    
    def __init__(self, caminho_dados):
        self.caminho_dados = caminho_dados
        self.dados = None
        self.dados_limpos = None
        self.carregar_dados()
    
    def carregar_dados(self):
        try:
            self.dados = pd.read_csv(self.caminho_dados, lineterminator='\n')
        except FileNotFoundError:
            print(f"Arquivo não encontrado: {self.caminho_dados}")
    
    def processa_limpa(self):
        if self.dados is not None:
            columns_to_keep = ['id', 'title', 'genres', 'original_language', 'overview']
            self.dados_limpos = self.dados[columns_to_keep]
        else:
            print("Dados não carregados.")
            
    def get_dados_limpos(self):
        if self.dados_limpos is not None:
            return self.dados_limpos
        else:
            print("Dados ainda não processados.")
            return None
