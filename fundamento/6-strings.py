movieName = "Top Gun"
movieName2 = "top Gun"

print(movieName == movieName2)  # False, case-sensitive comparison

movieDescription = "Top Gun é um filme de ação lançado em 1986."
print(movieName)
line = "=" * 20
print(line)
print(movieDescription)

print("top gun" in movieDescription.lower())  # True, case-insensitive search
print("Top Gun" in movieDescription)  # True, case-sensitive search