# Semantic-Web

(In corso di sviluppo...)

### Datasets
I dati non sono presenti nel repository.
Sono state utilizzate risorse in formato csv ottenute da https://www.kaggle.com

### ONTOLOGY

1. Protégé
 - myontology.owl
2. Python (rdflib)
  * formatURI.py
  * album_triples.py
  * book_triples.py
  * game_triples.py
  * movie_triples.py
  * main.py

Risultati
  * album_triples.owl
  * book_triples.owl
  * game_triples.owl
  * movie_triples.owl

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
