movieName = "top gun"
movieDescription = "A movie about a fighter pilot"

print(movieName.upper())  # 'TOP GUN'
print(movieName.lower())  # 'top gun'
print(movieName.title())  # 'Top Gun'
print(movieName.capitalize())  # 'Top gun'
print(movieName.count("o"))  # 1
print(movieName.find("u"))  # 4
print(movieName.center(20, "*"))  # '****top gun*****'
print(movieName.replace("top", "Shoti"))  # 'Shoti gun'
print(movieDescription.split(" "))  # ['A', 'movie', 'about', 'a', 'fighter', 'pilot']