books = [
    ["Ready Player One", "Scifi"],
    ["Hitch Hikers Guide to the Galaxy", "Scifi"],
    ["Restuarnt at the end of the Universe", "Scifi"],
    ["Life the Universe and Everything", "Scifi"],
    ["The Hobbit", "Fantasy"],
    ["Lord of the Rings, The fellowship of the Ring", "Fantasy"],
    ["Lord of the Rings, The Two Towers", "Fantasy"],
    ["Lord of the Rings, The Return of the King", "Fantasy"],
    ["The Outsider", "Thriller"],
    ["In a House of Lies", "Thriller"],
    ["The Girl on the Train", "Thriller"],
    ["In a dark dark Wood", "Thriller"]
    ["Diary of a Wimpy Kid", "Kids"]

]

def findbook(search):
    for i in books:
        if search.lower() == i[1].lower():
            print(i[0])


search = input("What genre are you looking for? ")
findbook(search)
