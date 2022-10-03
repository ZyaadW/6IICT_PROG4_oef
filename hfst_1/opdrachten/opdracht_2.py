films = [ "Monty Python and the Holy Grail",
          "Monty Python's Life of Brian",
          "Monty Python's Meaning of Life",
          "And Now For Something Completely Different"]

scores = [
    [ 9, 10, 9.5, 8.5, 3, 7.5 ,8 ], # Grail
    [ 10, 10, 0, 9, 1, 8, 7.5, 8, 6, 9 ], # Brian
    [ 7, 6, 5 ], # Life
    [ 6, 5, 6, 6 ] # Different
] 
film_ratings = {}
for index, film in enumerate(films):
    film_ratings[film] = scores[index]
    
print(film_ratings)

film_gemiddelde = {}
for key, scores in film_ratings.items():
    film_gemiddelde = sum(scores)/len(scores)

print(film_gemiddelde)    

     