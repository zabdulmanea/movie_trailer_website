import webbrowser

class Movie():
    """
    This class provides the structure to store movie information

    Attributes:
        title (str): The movie title
        trailer_youtube_url (str): A link to the movie trailer on youtube
        poster_image_url (str): A link to the movie poster
    """

    # constructor of Movie class, called when an instance of class is created
    def __init__(self, movie_title, movie_poster, movie_trailer):
        self.title = movie_title
        self.trailer_youtube_url = movie_trailer
        self.poster_image_url = movie_poster

    # play the movie trailer in the web
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)