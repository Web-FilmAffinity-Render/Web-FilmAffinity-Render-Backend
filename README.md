# Web-FilmAffinity-Render-Backend

Backend server for our web project. As a Django-based server, it is divided into applications, a settings directory and the manage.py. The rest of the files are complementary.

## Project

`/project` is the main folder for the project. Here we speciffy the settings, urls and interfaces for our server, managing its overall structure and behaviour.

### Databases

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

For any further doubts abou the PostgresSQL database see [Render's official documentation](https://docs.render.com/databases)

### Credentials

### Middleware

#### WhiteNoise

## Apps

### movies

### users

### reviews

## Deployment

We will be deploying the server on render.