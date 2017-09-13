import webbrowser


class Movie(object):
    """ This class provides a way to store movie related information."""

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """This constructor creates space to store movie
         information.

         Args:
             movie_title (str): The title of the movie.
             movie_storyline (str): Short description of movie's plot.
             poster_image (str): Link to the poster image for the movie.
             trailer_youtube (str): Link to the movie trailer on Youtube.

        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """The show_trailer function opens a web browser and loads the trailer
        from the url.
        """
        webbrowser.open(self.trailer_youtube_url)


    def show_poster(self):
        """The show poster function opens a web browser and loads the poster
        image from the url.
        """
        webbrowser.open(self.poster_image_url)


