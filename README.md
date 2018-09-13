# Semantic-Web

(In corso di sviluppo...)

### Datasets
I dati non sono presenti nel repository.

Sono state utilizzate risorse in formato csv ottenute da https://www.kaggle.com

### ONTOLOGY

1. Protégé
   * myontology.owl
2. Python (rdflib)
   * formatURI.py
   * album_triples.py
   * book_triples.py
   * game_triples.py
   * movie_triples.py
   * main.py
3. Risultati
   * album_triples.owl
   * book_triples.owl
   * game_triples.owl
   * movie_triples.owl

### Recommendation

1. Java (Jena)
   * entities
     - Album.java
     - Book.java
     - Game.java
     - Movie.java
   * similarity
     - TFIDF.java
     - Similarity.java
   * recommender
     - Recommender.java
   * query
     - MyQuery.java
   * main
     - Main.java
2. Risultati (da generare)
   * album_rec.owl
   * book_rec.owl
   * game_rec.owl
   * movie_rec.owl

### Web

1. Node.js (Express)
   * app.js
   * routes
     - index.js
     - music.js
     - books.js
     - games.js
     - movies.js
   * public/javascripts
     - query.js (rdflib)
   * views
     - index.ejs
     - error.ejs
     - music.ejs
     - books.ejs
     - games.ejs
     - movies.ejs
     - info.ejs
   * public/stylesheets
     - index.css
     - music.css
     - books.css
     - games.css
     - movies.css
     - info.css

### Esecuzione
node app.js
localhost:3000/
