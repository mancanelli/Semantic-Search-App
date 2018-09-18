var rdf = require('rdflib');
var fs = require('fs');

var path = '/home/matteo/Scrivania/Semantic_Web/Ontology';

function myquery(file, queryString) {
    var data = fs.readFileSync(path + file).toString();

    var store = rdf.graph();
    var contentType = 'application/rdf+xml';
    var baseUrl = "http://www.semanticweb.org/matteo/ontologies/project#";

    rdf.parse(data, store, baseUrl, contentType);

    var query = rdf.SPARQLToQuery(queryString, false, store);

    var results = [];

    store.query(query, function(result) {
        var res = {};
        var itemPres = false;

        if(file === "/album_triples.owl") {
            res  = {type: "Music",
                    title: result["?title"].value,
                    artist: result["?artist"].value,
                    year: result["?year"].value,
                    uri: result["?uri"].value.split("#")[1]};

            results.forEach(function(entry) {
                if(entry.uri == res.uri) {
                    var artPres = false;
                    var artists = entry.artist.split(",");

                    artists.forEach(function(a) {
                        if(a.trim() == res.artist.trim())
                            artPres = true;
                    });

                    if(!artPres)
                        entry.artist += ", " + res.artist;

                    itemPres = true;
                    return;
                }
            });
        }
        else if(file === "/book_triples.owl") {
            res  = {type: "Books",
                    title: result["?title"].value,
                    author: result["?author"].value,
                    year: result["?year"].value,
                    uri: result["?uri"].value.split("#")[1]};

            results.forEach(function(entry) {
                if(entry.uri == res.uri) {
                    var autPres = false;
                    var authors = entry.author.split(",");

                    authors.forEach(function(a) {
                        if(a.trim() == res.author.trim())
                            autPres = true;
                    });

                    if(!autPres)
                        entry.author += ", " + res.author;

                    itemPres = true;
                    return;
                }
            });
        }
        else if(file === "/game_triples.owl") {
            res  = {type: "Games",
                    title: result["?title"].value,
                    publisher: result["?publisher"].value,
                    year: result["?year"].value,
                    uri: result["?uri"].value.split("#")[1]};

            results.forEach(function(entry) {
                if(entry.uri == res.uri) {
                    var pubPres = false;
                    var publishers = entry.publisher.split(",");

                    publishers.forEach(function(a) {
                        if(a.trim() == res.publisher.trim())
                            pubPres = true;
                    });

                    if(!pubPres)
                        entry.publisher += ", " + res.publisher;

                    itemPres = true;
                    return;
                }
            });
        }
        else if(file === "/movie_triples.owl") {
            res  = {type: "Movies",
                    title: result["?title"].value,
                    genre: result["?genre"].value,
                    year: result["?year"].value,
                    uri: result["?uri"].value.split("#")[1]};

            results.forEach(function(entry) {
                if(entry.uri == res.uri) {
                    var genPres = false;
                    var genres = entry.genre.split(",");

                    genres.forEach(function(a) {
                        if(a.trim() == res.genre.trim())
                            genPres = true;
                    });

                    if(!genPres)
                        entry.genre += ", " + res.genre;

                    itemPres = true;
                    return;
                }
            });
        }

        if(!itemPres)
            results.push(res);
    });

    return results;
}

module.exports = myquery;
