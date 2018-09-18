var express = require('express');
var router = express.Router();

var file = "/movie_triples.owl";
var queryString = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> " +
                    "PREFIX ont: <http://www.semanticweb.org/matteo/ontologies/project#> " +
                    "SELECT ?uri ?title ?genre ?year " +
                    "WHERE { " +
                    "	?uri rdf:type ont:Movie . " +
                    "	?uri ont:movie_title ?title . " +
                    "	?uri ont:movie_genre ?genre . " +
                    "   ?uri ont:movie_date ?year . " +
                    "} ";

var myquery = require('../public/javascripts/query');
var queryResults = myquery(file, queryString);

router.get('/', function(req, res, next) {
    res.render('table', {data: queryResults});
});

router.get('/*', function(req, res, next) {
    var movie = req.url.substring(1, req.url.length);
    var data = {};

    for (var i = 0; i < queryResults.length; i++)
        if (movie === queryResults[i].uri)
            data = queryResults[i];

    res.render('info', {data: data});
});

module.exports = router;
