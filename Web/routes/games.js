var express = require('express');
var router = express.Router();

var file = "/game_triples.owl";
var queryString = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> " +
                    "PREFIX ont: <http://www.semanticweb.org/matteo/ontologies/project#> " +
                    "SELECT ?uri ?title ?publisher ?year " +
                    "WHERE { " +
                    "	?uri rdf:type ont:Game . " +
                    "	?uri ont:game_name ?title . " +
                    "	?uri ont:publishedBy ?puburl . " +
                    "	?puburl ont:org_name ?publisher . " +
                    "   ?uri ont:game_year ?year . " +
                    "} ";

var myquery = require('../public/javascripts/query');
var queryResults = myquery(file, queryString);


router.get('/', function(req, res, next) {
    res.render('table', {data: queryResults});
});


router.get('/*', function(req, res, next) {
    var game = req.url.substring(1, req.url.length);
    var data = {};

    for (var i = 0; i < queryResults.length; i++)
        if (game === queryResults[i].uri)
            data = queryResults[i];

    res.render('info', {data: data});
});

module.exports = router;
