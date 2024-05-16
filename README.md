**Web-FilmAffinity-Render-Backend**
==================================

Backend server for our web project. As a Django-based server, it is divided into applications, a settings directory and the manage.py. The rest of the files are complementary.

# Structure

```
|-- Web-FilmAffinity-Render-Backend
|   |-- .gihub
|   |   |-- workflows
|   |   |   |-- django.yml
|   |-- project
|   |   |-- movies
|   |   |   |-- management
|   |   |   |   |-- __init__.py
|   |   |   |   |-- commands
|   |   |   |   |   |-- __init__.py
|   |   |   |   |   |-- load_default_movies.py
|   |   |   |-- migrations
|   |   |   |   |-- ...
|   |   |   |-- __init__.py
|   |   |   |-- admin.py
|   |   |   |-- apps.py
|   |   |   |-- models.py
|   |   |   |-- serializers.py
|   |   |   |-- tests.py
|   |   |   |-- views.py
|   |   |-- reviews
|   |   |   |-- migrations
|   |   |   |   |-- ...
|   |   |   |-- __init__.py
|   |   |   |-- admin.py
|   |   |   |-- apps.py
|   |   |   |-- models.py
|   |   |   |-- serializers.py
|   |   |   |-- tests.py
|   |   |   |-- views.py
|   |   |-- users
|   |   |   |-- migrations
|   |   |   |   |-- ...
|   |   |   |-- __init__.py
|   |   |   |-- admin.py
|   |   |   |-- apps.py
|   |   |   |-- models.py
|   |   |   |-- serializers.py
|   |   |   |-- tests.py
|   |   |   |-- views.py
|   |   |-- __init__.py
|   |   |-- asgi.py
|   |   |-- settings.py
|   |   |-- urls.py
|   |   |-- wsgi.py
|   |-- .gitignore
|   |-- build.sh
|   |-- manage.py
|   |-- README.md
|   |-- requirements.txt
```

# Project


`/project` is the main folder for the project. Here we speciffy the settings, urls and interfaces for our server, managing its overall structure and behaviour. Inside it we can also find our applications. These could have been placed outside, since its only a matter of how is it deffined in the settings, but we found this more compact approach more suitable.

## Databases

For our default database, we will use a PostgresSQL database deployed from render. We have chosen this approach since is more suitable for a real-case scenario as well as more secure. Since this project was concieved as an academic task, we have deployed a PostgresSQL database in render that will serve our purpose, but will cease to exist eventually, and it won't be valid for this project anymore.

Therefore, here we provide a series of steps to modify in case of need.

1. Deploy your own PostgresSQL instance. We will follow with the deployment on render but the database could be running anywhere, in theory.

2. In the settings.py file, go to the databases secription. It should be something similar to:

```python

DATABASES = {
    'default': dj_database_url.config(
        default='postgres://admin:a6LIy1wKUsPTBgDas3D80HFzhtNI2xo0@dpg-cp1igp8l5elc73ettn70-a.frankfurt-postgres.render.com/default_u7ug',
        conn_max_age=600
    )
}

```

3. Change the `default` URL as needed. Notice here we are following the pattern ``postgres://USER:PASSWORD@INTERNAL_HOST:PORT/DATABASE``. This does not hide the user nor the password or any other sensitive information as it is not a critical requirement for our project. If it were the case, another approach would be needed.

For any further doubts about the PostgresSQL database see [Render's official documentation](https://docs.render.com/databases)

## Credentials

## Middleware

### WhiteNoise

# Apps

As metioned above, all the apps are located inside the `/project` folder. Following this schema, the apps are named, all with the same structure, as `project.<name of the app>`.

## movies

### API


| Method | Route              | Description                                   | Response                                               |
|:--------|:----------------:|:---------------------------------------------:|--------------------------------------------------------:|
| GET    | /movies/                | Obtains entire list of movies                 | 200 + List of JSONs if OK                                 |
| GET    | /movies/<int:pk>        | Obtains movie with id `pk`                    | 200 + JSON if OK                                        |
| POST   | /movies/create          | If superuser, creates a new movie             | 201 if OK, 401 if incorrect credentials                 |
| PUT    | /movies/update/<int:pk> | If superuser, updates movie data              | 200 if OK, 401 if incorrect credentials                 |
| DELETE | /movies/delete/<int:pk> | If superuser, removes the selected movie      | 204 if OK, 401 if incorrect credentials                 |

### Models

#### Movie

The model is a representation of a movie with all the relevant information

##### Fields

- **title**: The title of the movie.
- **year**: The release year of the movie.
- **country**: The country of origin for the movie.
- **director**: The director(s) of the movie.
- **cast**: The cast members of the movie.
- **rate**: The average rating of the movie.
- **genre**: The genre(s) of the movie.
- **duration**: The duration of the movie in minutes.
- **plot**: The plot summary of the movie.

### Serializers

#### MovieSerializer

The `MovieSerializer` is used to serialize and deserialize movie data for detailed representations.

##### Methods

- `create`: Creates a new movie instance using the provided data. It calls the custom manager method `create_movie` to create the movie.

- `update`: Updates an existing movie instance with the provided data.

#### MovieListSerializer

The `MovieListSerializer` is used to serialize and deserialize movie data for list representations.

##### Methods

- `create`: Creates a new movie instance using the provided data.

### Views

#### MovieListView

- **Purpose**: This view is responsible for listing movies based on query parameters such as title, plot, minimum and maximum rate, and genre.

#### MovieView

- **Purpose**: This view is responsible for retrieving a specific movie by its primary key.

#### CreateMovieView

- **Purpose**: This view is responsible for creating a new movie instance.

#### UpdateMovieView

- **Purpose**: This view is responsible for updating an existing movie instance.

#### DestroyMovieView

- **Purpose**: This view is responsible for deleting an existing movie instance.

<br>
<br>

> **Authentication**: 
> All views require authentication by checking the user's token retrieved from the session cookie. Except for `MovieListView` and `MoviewView` that doesnt require authentication.

## users

### API


| Method  | Route         | Description                                                                   | Response         |
|:--------|:-------------:|:-----------------------------------------------------------------------------:|-----------------:|
| POST   | /users/signin  | Creates a new user with the incoming JSON: {"email": "\*", "password": "\*", ...}. Allows any fields, "email" and "password" are required. | 201 if OK, 400 if required fields are missing, 409 if there is already a user with that email |
| POST   | /users/login   | Creates a session which allows access to other resources of the API in regard to the user indicated in the JSON: {"email": "\*", "password": "\*"} | 201 if OK, 401 if incorrect credentials                                                       |
| GET    | /users/me      | Obtains the profile data from the logged user                                 | 200 + profile JSON if OK, 401 if not logged                                                   |
| PUT    | /users/me      | Updates profile of the logged user with the provided data (JSON)              | 200 + updated profile JSON if OK, 401 if not logged                                           |
| DELETE | /users/me      | Removes logged user                                                           | 204 if OK, 401 if not logged                                                                   |
| DELETE | /users/logout  | Terminates user session                                                       | 204 if OK, 401 if not logged                                                                   |


### Models

#### User

The model is a simple representation of a user with a name, an email and a password

##### Fields

- **name**: The name of the user.
- **email**: The email address of the user.
- **password**: The hashed password of the user.

### Serializers

#### UserSerializer

The `UserSerializer` is used to serialize and deserialize user data, particularly for creating and updating user accounts.

The serializer includes a validation method `validate_password` that ensures the password meets a specific format using a regular expression pattern.

#### LoginSerializer

The `LoginSerializer` is used to validate login credentials and authenticate users.

The serializer validates the login credentials by attempting to authenticate the user using Django's `authenticate` function.

### Views

#### SigninView

- **Purpose**: This view is responsible for creating a new user account.

#### LoginView

- **Purpose**: This view is responsible for logging in a user and generating a session token.

#### UserView

- **Purpose**: This view is responsible for retrieving, updating, or deleting the user's own account.

#### LogoutView

- **Purpose**: This view is responsible for logging out a user by deleting the session token.

## reviews

### API

| Method  | Route                                 | Description                            | Response                                |
|:--------|:-------------------------------------:|:---------------------------------------|----------------------------------------:|
| GET     | /reviews/?movie_title=<movie title>   | Obtains list of reviews for the specified movie title               | 200 + List of review JSONs if OK, 400 if `movie_title` not provided |
| POST    | /reviews/new                          | Creates a review for the logged user with the provided JSON         | 201 if OK, 401 if not logged, 404 if movie not found                      |

### Models

#### Review

The model consists in a representation of a review identifying the user and the movie it is reviewing

##### Fields

- **movie_title**: The title of the movie being reviewed.
- **user_username**: The username or email of the user who wrote the review.
- **review_text**: The text content of the review.
- **review_rate**: The rating given to the movie in the review.

### Serializers

#### ReviewSerializer

The `ReviewSerializer` is used to serialize and deserialize review data.

##### Methods

- `create`: Creates a new review instance using the provided data.

### Views

#### ListReviewView

- **Purpose**: This view is responsible for listing reviews for a specific movie.

#### CreateReviewView

- **Purpose**: This view is responsible for creating a new review for a movie.

The `CreateReviewView` ensures that only logged-in users can create reviews by retrieving the user based on the session token.


## Deployment

We will be deploying the server on Render.

### .env