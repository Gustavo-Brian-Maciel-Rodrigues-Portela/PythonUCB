import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import sigmoid_kernel

class Aplica_ML:
    
    def __init__(self, dados_limpos):
        self.dados_limpos = dados_limpos
        self.tfv_matrix = None
        self.sig = None
        self.indices = None
    
    def tokenizer(self):
        tfv = TfidfVectorizer(min_df=3, max_features=None,
                              strip_accents='unicode', analyzer='word', token_pattern=r'\w{1,}',
                              ngram_range=(1, 3),
                              stop_words='english')
        try:
            self.dados_limpos['overview'] = self.dados_limpos['overview'].fillna('')
            self.tfv_matrix = tfv.fit_transform(self.dados_limpos['overview'])
            print("Matriz TF-IDF criada com sucesso.")
        except Exception as e:
            print(f"Erro ao criar a matriz TF-IDF: {e}")
    
    def sigmoid(self):
        try:
            if self.tfv_matrix is not None:
                self.sig = sigmoid_kernel(self.tfv_matrix, self.tfv_matrix)
                self.indices = pd.Series(self.dados_limpos.index, index=self.dados_limpos['title']).drop_duplicates()
                print("Kernel sigmoid calculado com sucesso.")
                return self.sig
            else:
                print("Matriz TF-IDF não foi criada. Execute 'tokenizer' primeiro.")
        except Exception as e:
            print(f"Erro ao calcular o kernel sigmoid: {e}")
            return None
    
    def get_sig(self):
        if self.sig is not None:
            return self.sig
        else:
            print("Kernel sigmoid não calculado.")
            return None
    
    def get_indices(self):
        if self.indices is not None:
            return self.indices
        else:
            print("Índices não encontrados.")
            return None
