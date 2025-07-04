#funçao de potencia de um numero
power = lambda num: num ** 2

#funçao que verficia se um numero é par
is_even = lambda x: x % 2 == 0

#funçao que divide dois numeros
div_num = lambda x, y: x / y if y != 0 else "Cannot divide by zero"

#funçao que inverte uma string
invert_string = lambda s: s[::-1]

print(power(5))  # Output: 25
print(is_even(4))  # Output: True
print(is_even(5))  # Output: False
print(div_num(10, 2))  # Output: 5.0
print(div_num(10, 0))  # Output: Cannot divide by zero
print(invert_string("hello"))  # Output: "olleh"


#funcionalidades relacionadas aos filmes
movies_list = ["titanic", "star wars", "matrix", "avengers"]
ratings = {
    "titanic":[7.8, 8.0, 7.5],
    "star wars": [9.5, 9.7, 9.6],
    "matrix": [8.5, 8.8, 8.7],
    "avengers": [6.0, 6.5, 5.5],
}
#função que calcula a média de uma lista de notas
avarage_rating = lambda movie_name: sum(ratings[movie_name]) / len(ratings[movie_name])
print(f"media de avaaliçoes do fime matrix: {avarage_rating('matrix'):.2f}")  # Output: 8.67

#funçao que verifica se um filmes esta na lista
check_movie = lambda movie_name: movie_name in movies_list
print(check_movie("titanic"))  # Output: True

#funçao para recomendar um filme com base na avaliação media

recommend_movie = lambda movie_name: f"recomendo assistir {movie_name} com media de {avarage_rating(movie_name):.2f}"
print(recommend_movie ("star wars"))  # Output: recomendo assistir star wars com media de 9.60