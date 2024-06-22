from recomendador_filme import RecomendadorFilmes

def main():
    caminho = 'movies2.csv' 

    
    recomendador = RecomendadorFilmes(caminho)
    recomendador.preparar_dados()


    while True:
        nome_do_filme = input("Digite o nome do filme para obter recomendações (ou 'sair' para encerrar): ")
        
        if nome_do_filme.lower() == 'sair':
            print("Encerrando o programa...")
            break
        
       
        recomendacoes = recomendador.give_recommendation(nome_do_filme)
        if recomendacoes is not None:
            print(f"\nRecomendações para '{nome_do_filme}':")
            for i, filme in enumerate(recomendacoes, 1):
                print(f"{i}. {filme}")
            print()

if __name__ == "__main__":
    main()
