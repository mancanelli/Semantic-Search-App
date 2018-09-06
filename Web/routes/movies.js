var express = require('express');
var router = express.Router();

var media = "/book_triples.owl"; // DA MODIFICARE
var queryString = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> " +
                    "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> " +
                    "PREFIX owl: <http://www.w3.org/2002/07/owl#> " +
                    "PREFIX ont: <http://www.semanticweb.org/matteo/ontologies/project#> " +
                    "SELECT ?myalbum ?title ?artist ?year " +
                    "WHERE { " +
                    "	?myalbum rdf:type ont:Album . " +
                    "	?myalbum ont:album_title ?title . " +
                    "	?myalbum ont:recordedBy ?arturl . " +
                    "	?arturl ont:person_name ?artist . " +
                    "   ?myalbum ont:album_year ?year . " +
                    "} ";

var myquery = require('../public/javascripts/query');
var queryResults = myquery(media, queryString);

router.get('/', function(req, res, next) {
    res.render('movies', {title: 'Movies', data: queryResults});
});

router.get('/*', function(req, res, next) {
    var movie = req.url.substring(1, req.url.length);
    var data = {};

    for (var i = 0; i < queryResults.length; i++)
        if (movie === queryResults[i].movie_url)
            data = queryResults[i];

    res.render('info', {title: 'Movies', data: data});
});

module.exports = router;
