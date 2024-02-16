'''
9) Create a dictionary named movie-ratings with 
at least five movies as keys and their ratings (out of 10) as values. 
Ask the user for a movie title. Write a function named recommend_movie 
that takes the movie_rating dictionary and the movie title as arguments. 
The function should check if the movie is in the dictionary and recommend 
the movie if it has a rating of 8 or higher. Otherwise, suggest movie titles 
that have a rating of 8 or higher. 
If the movie is not found in the dictionary, 
it should still recommend movies that are rated 8 or higher.
'''

def recommend_movie(movie_ratings, movie_title):
    #create empty list
    rec_movies = []

    #if input in list
    if movie_title in movie_ratings:

        #if rating greater than equal to 8
        if movie_ratings[movie_title] >= 8:
            print(f"Good Choice! I recommend watching {movie_title}")
        else:
            print(f"I recommend watching:")

            #appened for ones less than 8
            for title, rating in movie_ratings.items():
                if rating >= 8:
                    rec_movies.append(title)
            print(*rec_movies, sep = ', ')
    
    #if input not in list
    else:
        print(f"Bad Choice! I recommend watching:")

        #appened for ones less then 8
        for title, rating in movie_ratings.items():
            if rating >= 8:
                rec_movies.append(title)
        print(*rec_movies, sep = ', ')


#Create dictionary
movie_ratings = {"The Godfather": 9,
                 "The Godfather Part II": 9,
                 "Goodfellas": 10,
                 "Casino":7,
                 "The Departed": 8}

#ask for title
movie_title = input("Enter movie title: ")

recommend_movie(movie_ratings,movie_title)