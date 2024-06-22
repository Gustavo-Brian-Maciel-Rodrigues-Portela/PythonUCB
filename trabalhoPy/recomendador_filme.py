from pre_processamento import PreProcessamento
from aplica_ml import Aplica_ML
import pandas as pd

class RecomendadorFilmes:
    
    def __init__(self, caminho_dados):
        self.preprocessador = PreProcessamento(caminho_dados)
        self.aplicador_ml = None
        self.sig = None
    
    def preparar_dados(self):
        print("Iniciando preparação de dados...")
        self.preprocessador.processa_limpa()
        dados_limpos = self.preprocessador.get_dados_limpos()
        if dados_limpos is not None:
            self.aplicador_ml = Aplica_ML(dados_limpos)
            self.aplicador_ml.tokenizer()
            self.sig = self.aplicador_ml.sigmoid()
            if self.sig is not None:
                print("Dados preparados com sucesso!")
            else:
                print("Erro ao calcular o kernel sigmoid. Verifique os dados.")
        else:
            print("Erro ao obter dados limpos. Verifique o processo de limpeza.")
    
    def give_recommendation(self, title):
        if self.sig is not None and self.aplicador_ml is not None:
            indices = self.aplicador_ml.get_indices()
            dados = self.aplicador_ml.dados_limpos
            if title not in indices:
                print(f"Título '{title}' não encontrado nos dados.")
                return None
            idx = indices[title]
            sig_scores = list(enumerate(self.sig[idx]))
            sig_scores = sorted(sig_scores, key=lambda x: x[1], reverse=True)
            sig_scores = sig_scores[1:8]
            movie_indices = [i[0] for i in sig_scores]
            return dados['title'].iloc[movie_indices]
        else:
            print("Modelo não está preparado. Execute 'preparar_dados' primeiro.")
            return None
