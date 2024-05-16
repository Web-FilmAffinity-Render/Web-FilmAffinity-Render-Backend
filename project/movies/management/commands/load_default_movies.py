from django.core.management.base import BaseCommand
from project.movies.models import Movie
import random

class Command(BaseCommand):
    help = 'Load sample data into Movie model'

    def handle(self, *args, **kwargs):
        # Sample data for creating movies
        titles = [
            "The Shawshank Redemption", "The Godfather", "The Dark Knight", "Pulp Fiction",
            "The Lord of the Rings: The Return of the King", "Schindler's List",
            "Inception", "Forrest Gump", "Fight Club", "The Matrix"
        ]
        years = [1994, 1972, 2008, 1994, 2003, 1993, 2010, 1994, 1999, 1999]
        countries = ["USA", "USA", "USA", "USA", "New Zealand, USA", "USA", "USA, UK", "USA", "USA, Germany", "USA, Australia"]
        directors = [
            "Frank Darabont", "Francis Ford Coppola", "Christopher Nolan", "Quentin Tarantino", "Peter Jackson", "Steven Spielberg", "Christopher Nolan", "Robert Zemeckis", "David Fincher", "The Wachowskis"
        ]
        cast = [
            "Tim Robbins, Morgan Freeman",
            "Marlon Brando, Al Pacino, James Caan",
            "Christian Bale, Heath Ledger, Aaron Eckhart",
            "John Travolta, Uma Thurman, Samuel L. Jackson",
            "Elijah Wood, Ian McKellen, Viggo Mortensen",
            "Liam Neeson, Ben Kingsley, Ralph Fiennes",
            "Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page",
            "Tom Hanks, Robin Wright, Gary Sinise",
            "Brad Pitt, Edward Norton, Helena Bonham Carter",
            "Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss"
        ]

        categories = ["Drama", "Action", "Comedy", "Thriller", "Adventure", "Sci-Fi"]
        genres = [
            "Drama", "Crime, Drama", "Action, Crime, Drama", "Crime, Drama", "Adventure, Drama, Fantasy", "Biography, Drama, History", "Action, Adventure, Sci-Fi", "Drama, Romance", "Drama", "Action, Sci-Fi"
        ]
        rates = [9.3, 9.2, 9.0, 8.9, 8.9, 8.9, 8.8, 8.8, 8.8, 8.7]
        durations = [142, 175, 152, 154, 201, 195, 148, 142, 139, 136]
        plot_descriptions = [
            "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
            "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
            "When the menace known as The Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham.",
            "The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
            "Gandalf and Aragorn lead the World of Men against Sauron's army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring.",
            "In Poland during World War II, Oskar Schindler gradually becomes concerned for his Jewish workforce after witnessing their persecution by the Nazis.",
            "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.",
            "The presidencies of Kennedy and Johnson, the Vietnam War, the Watergate scandal and other historical events unfold from the perspective of an Alabama man with an IQ of 75, whose only desire is to be reunited with his childhood sweetheart.",
            "An insomniac office worker and a devil-may-care soapmaker form an underground fight club that evolves into something much, much more.",
            "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers."
        ]


        for i in range(10):
            movie = Movie.objects.create(
                title=titles[i],
                year=years[i],
                country=countries[i],
                director=directors[i],
                cast=cast[i],
                rate=str(rates[i]),
                genre=genres[i],
                duration=durations[i],
                # image=image_urls[i],
                plot=plot_descriptions[i]
            )
            self.stdout.write(self.style.SUCCESS(f"Created movie: {movie.title}"))