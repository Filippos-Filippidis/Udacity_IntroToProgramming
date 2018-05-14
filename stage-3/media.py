import webbrowser


# webbrowser module provides a high-level
# interface to allow displaying Web-based documents to users


class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, rating_image_url):
        """
        Initialize the movie instance.
        Arguments:
        title: title of the movie
        storyline: story of the movie
        poster_image: movie poster
        trailer: movie trailer
        rating: movie rating
        ...
        Returns:
        None
        """

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating_image_url = rating_image_url

    def show_trailer(self):
        """
        Function to play trailer in a web browser.

        Returns:
        None
        """

        # Display url using the default browser
        webbrowser.open(self.trailer_youtube_url)
