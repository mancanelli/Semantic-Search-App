# Semantic-Web

(In corso di sviluppo...)

### Datasets
I dati non sono presenti nel repository.
Sono state utilizzate risorse in formato csv ottenute da https://www.kaggle.com

### ONTOLOGY

* Protégé
  1. myontology.owl
* Python (rdflib)
  1. formatURI.py
  2. album_triples.py
  3. book_triples.py
  4. game_triples.py
  5. movie_triples.py
  6. main.py

Risultati
  1. album_triples.owl
  2. book_triples.owl
  3. game_triples.owl
  4. movie_triples.owl

### Recommendation

* Java (Jena)
  1. entities
    - Album.java
    - Book.java
    - Game.java
    - Movie.java
  2. similarity
    - TFIDF.java
    - Similarity.java
  3. recommender
    - Recommender.java
  4. query
    - MyQuery.java
  5. main
    - Main.java

Risultati (da generare)
  1. album_rec.owl
  2. book_rec.owl
  3. game_rec.owl
  4. movie_rec.owl

## Web

* Node.js (Express)
  1. app.js
  2. routes
    - index.js
    - music.js
    - books.js
    - games.js
    - movies.js
  3. public/javascripts
    - query.js (rdflib)
  4. views
    - index.ejs
    - error.ejs
    - music.ejs
    - books.ejs
    - games.ejs
    - movies.ejs
    - info.ejs
  5. public/stylesheets
    - index.css
    - music.css
    - books.css
    - games.css
    - movies.css
    - info.css
    
Esecuzione
  1. node app.js
  2. localhost:3000/
