#1- funçao para imprimir nomes completos
def full_name(first_name, last_name):
    print(f"Nome completo: {first_name} {last_name}")
full_name("João", "Silva")

#2- funçao para calcular a soma de dois numeros
def sum_numbers(num1, num2):
    return num1 + num2
result = sum_numbers(10, 5)
print(f"Soma: {result}")

#3- funçao com parametro default
def address(country="brasil"):
    print(f"País: {country}")
address()  # Usa o valor padrão
address("Portugal")  # Usa o valor fornecido

#4- funçao para avaliar filme
def rate_movie(num_ratings,movie_name):
    total = 0
    for i in range(num_ratings):
        note = float(input(f"Digite a nota do filme:\n "))
        total += note
    if num_ratings > 0:
        average = total / num_ratings
    else:
        average = 0
    print(f"A média de avaliações do filme {movie_name} é: {average:.2f}")
rate_movie(3, "O Senhor dos Anéis")