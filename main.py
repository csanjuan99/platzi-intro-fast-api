from fastapi import FastAPI

app = FastAPI()

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
async def get_movies():
    return movies
