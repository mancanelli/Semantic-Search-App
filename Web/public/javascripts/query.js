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

        if(media === "/album_triples.owl") {
            res  = {type: "music",
                    title: result["?title"].value,
                    artist: result["?artist"].value,
                    year: result["?year"].value,
                    album_url: result["?myalbum"].value.split("#")[1]};
        }

        results.push(res);
    });

    return results;
}

module.exports = myquery;

/*
//rating: result["?rating"].value,
//genre: result["?genre"].value,
//label: result["?label"].value,

var stms = store.statementsMatching(undefined, undefined , undefined);
for (var i = 0; i < stms.length; i++) {
    var stm = stms[i];
    console.log(stm);
}
*/
