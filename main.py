from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

# Models with pydantic
class Movie(BaseModel):
    id: int
    name: str
    year: int
    genre: str
    director: str
    imdb_score: float
    popularity: int


# Documentation
app.title = "Platzi - Introduction to FastAPI"
app.version = "0.0.1"

movies = [
    {
        "id": 1,
        "name": "The Shawshank Redemption",
        "year": 1994,
        "genre": "Drama",
        "director": "Frank Darabont",
        "imdb_score": 9.3,
        "popularity": 100,
    },
    {
        "id": 2,
        "name": "The Godfather",
        "year": 1972,
        "genre": "Crime, Drama",
        "director": "Francis Ford Coppola",
        "imdb_score": 9.2,
        "popularity": 150,
    },
    {
        "id": 3,
        "name": "The Godfather: Part II",
        "year": 1974,
        "genre": "Crime, Drama",
        "director": "Francis Ford Coppola",
        "imdb_score": 9.0,
        "popularity": 70,
    },
    {
        "id": 4,
        "name": "The Dark Knight",
        "year": 2008,
        "genre": "Action, Crime, Drama",
        "director": "Christopher Nolan",
        "imdb_score": 9.0,
        "popularity": 200,
    }
]


@app.get("/", tags=["root"])
async def root():
    return {"message": "Hello World"}


@app.get("/movies", tags=["movies"])
async def get_movies(popularity: int = None):
    if popularity:
        filter_movies = list(filter(lambda m: m["popularity"] > popularity, movies))
        return filter_movies
    return movies


@app.get("/movies/{id}", tags=["movies"])
async def get_movie(id: int):
    movie = list(filter(lambda m: m["id"] == id, movies))[0]
    return movie


@app.post("/movies", tags=["movies"])
async def create_movie(movie: Movie = Body(...)):
    movies.append(movie)
    return movies


@app.put("/movies/{id}", tags=["movies"])
async def update_movie(id: int, update_movie: Movie = Body(...)):
    for movie in movies:
        if movie["id"] == id:
            movie["name"] = update_movie.name
            movie["year"] = update_movie.year
            movie["genre"] = update_movie.genre
            movie["director"] = update_movie.director
            movie["imdb_score"] = update_movie.imdb_score
            movie["popularity"] = update_movie.popularity
            return movie


@app.delete("/movies/{id}", tags=["movies"])
async def delete_movie(id: int):
    for movie in movies:
        if movie["id"] == id:
            movies.remove(movie)
            return {"message": "Movie deleted"}
    return {"message": "Movie not found"}
    