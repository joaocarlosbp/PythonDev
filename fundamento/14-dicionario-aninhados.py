import pprint
filmsDict ={

    "inception": {
        "director": "Christopher Nolan",
        "year": 2010,
        "cast": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page"]
    },
    "interstellar": {
        "director": "Christopher Nolan",
        "year": 2014,
        "cast": ["Matthew McConaughey", "Anne Hathaway", "Jessica Chastain"]
    },
    "the_dark_knight": {
        "director": "Christopher Nolan",
        "year": 2008,
        "cast": ["Christian Bale", "Heath Ledger", "Aaron Eckhart"]
    }
}
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmsDict)

#1 buscar informaçao dentro de um dicionario aninhado
print(filmsDict["inception"]["director"])

#2 add um novo item
filmsDict["inception"]["rating"] = 8.8
pp.pprint(filmsDict["inception"])