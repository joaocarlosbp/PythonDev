#1- funçao para imprimir mensagem de boas vindas
def welcome():
    print("Bem-vindo ao nosso Sistema de filmes!")
welcome()

#for i  in range(10):
 #   welcome()

 #2 funçao para calcular a media de notas
 
#def calculate_avarage():
 #   num_ratings = int(input("Quantas notas você quer dar ao flmes? "))
  #  total = 0
   # for i in range(num_ratings):
    #    rating = float(input(f"Digite a nota para o filme: \n"))
     #   total += rating
#
 #   if num_ratings > 0:
  #      average = total / num_ratings
   # else:
    #    average = 0
    #return average
        
        
#print(f"A média das notas é: {calculate_avarage():.2f}")

#funçao para cadastrar filmes

def create_movie():

    print("Vamos cadastrar um novo filme!")
    title_movie = input("Digite o título do filme: ")
    year_movie = input("Digite o ano de lançamento do filme: ")
    genre_movie = input("Digite o gênero do filme: ")
    director_movie = input("Digite o nome do diretor do filme: ")

    movies = {
        "title": title_movie,
        "year": year_movie,
        "genre": genre_movie,
        "director": director_movie
    }
    return movies
movie=create_movie()
print(f"Filme cadastrado com sucesso: {movie['title']} ({movie['year']}) - {movie['genre']} dirigido por {movie['director']}")