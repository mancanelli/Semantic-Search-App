from album_triples import addAlbumTriples
from book_triples import addBookTriples
from movie_triples import addMovieTriples
from game_triples import addGameTriples

import rdflib

if __name__ == "__main__":
    graph = rdflib.Graph()
    graph.parse("myontology.owl", format="xml")

    ontURI = "http://www.semanticweb.org/matteo/ontologies/project"

    addBookTriples(graph, ontURI)
    addAlbumTriples(graph, ontURI)
    addMovieTriples(graph, ontURI)
    addGameTriples(graph, ontURI)

    file = open("triples.owl", "wb")
    file.write(graph.serialize(format='xml'))
    file.close()
