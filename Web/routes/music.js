var express = require('express');
var router = express.Router();

var media = "/small_album_triples.owl";
var queryString = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> " +
                    "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> " +
                    "PREFIX owl: <http://www.w3.org/2002/07/owl#> " +
                    "PREFIX ont: <http://www.semanticweb.org/matteo/ontologies/project#> " +
                    "SELECT ?uri ?title ?artist ?year " +
                    "WHERE { " +
                    "	?uri rdf:type ont:Album . " +
                    "	?uri ont:album_title ?title . " +
                    "	?uri ont:recordedBy ?arturl . " +
                    "	?arturl ont:person_name ?artist . " +
                    "   ?uri ont:album_year ?year . " +
                    "} ";

var myquery = require('../public/javascripts/query');
var queryResults = myquery(media, queryString);

router.get('/', function(req, res, next) {
    res.render('music', {title: 'Music', data: queryResults});
});

router.get('/*', function(req, res, next) {
    var alb = req.url.substring(1, req.url.length);
    var data = {};

    for (var i = 0; i < queryResults.length; i++)
        if (alb === queryResults[i].album_uri)
            data = queryResults[i];

    res.render('info', {data: data});
});

module.exports = router;
