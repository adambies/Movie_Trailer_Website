import media
import fresh_tomatoes

# This is where the movie classes are instantiated.

hitmans_bodyguard = media.Movie("The Hitman's Bodyguard", "A hitman hires a bodyguard to protect him.",
                                "https://upload.wikimedia.org/wikipedia/en/2/2d/HitmansBodyguard.jpg",
                                "https://www.youtube.com/watch?v=F4Afusxc2SM")

it = media.Movie("It", "A movie about a killer clown.",
                     "https://upload.wikimedia.org/wikipedia/en/a/a2/It_%282017%29_logo.jpg",
                     "https://www.youtube.com/watch?v=xKJmEC5ieOk")

school_of_rock = media.Movie("School of Rock", "Using rock music to learn",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille", "A rat is a chef in Paris",
                          "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris", "Going back in time to meet authors",
                                "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=atLg2wQQxvU")

# Create the list of movies to be used by the fresh tomatoes file
movies = [hitmans_bodyguard, it, school_of_rock, ratatouille, midnight_in_paris]

# Run the fresh tomatoes function to create the website
fresh_tomatoes.open_movies_page(movies)
