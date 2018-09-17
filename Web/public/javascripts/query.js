var rdf = require('rdflib');
var fs = require('fs');

var path = '/home/matteo/Scrivania/Semantic_Web/Ontology';

function myquery(media, queryString) {
    var data = fs.readFileSync(path + media).toString();

    var store = rdf.graph();
    var contentType = 'application/rdf+xml';
    var baseUrl = "http://www.semanticweb.org/matteo/ontologies/project#";

    rdf.parse(data, store, baseUrl, contentType);

    var query = rdf.SPARQLToQuery(queryString, false, store);

    var results = [];

    store.query(query, function(result) {
        var res = {};

        if(media === "/small_album_triples.owl") {
            res  = {type: "Music",
                    title: result["?title"].value,
                    artist: result["?artist"].value,
                    year: result["?year"].value,
                    uri: result["?uri"].value.split("#")[1]};
        }
        else if(media === "/book_triples.owl") {
            res  = {type: "Books",
                    title: result["?title"].value,
                    author: result["?author"].value,
                    year: result["?year"].value,
                    uri: result["?uri"].value.split("#")[1]};
        }
        else if(media === "/game_triples.owl") {
            res  = {type: "Games",
                    title: result["?title"].value,
                    publisher: result["?publisher"].value,
                    year: result["?year"].value,
                    uri: result["?uri"].value.split("#")[1]};
        }
        else if(media === "/small_movie_triples.owl") {
            res  = {type: "Movies",
                    title: result["?title"].value,
                    genre: result["?genre"].value,
                    year: result["?year"].value,
                    uri: result["?uri"].value.split("#")[1]};
        }

        results.push(res);
    });

    return results;
}

module.exports = myquery;
