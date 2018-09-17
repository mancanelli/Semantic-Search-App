var express = require('express');
var router = express.Router();

var media = "/small_movie_triples.owl";
var queryString = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> " +
                    "PREFIX ont: <http://www.semanticweb.org/matteo/ontologies/project#> " +
                    "SELECT ?uri ?title ?genre ?year " +
                    "WHERE { " +
                    "	?uri rdf:type ont:Movie . " +
                    "	?uri ont:movie_title ?title . " +
                    "	?uri ont:movie_genre ?genre . " +
                    "   ?uri ont:movie_date ?year . " +
/*
                    "   ?uri ont:runtime ?runtime . " +
                    "   ?uri ont:budget ?budget . " +
                    "   ?uri ont:movie_rating ?rating . " +
                    "   ?uri ont:revenue ?revenue . " +
                    "   ?uri ont:collection ?collection . " +
                    "   ?uri ont:movie_original_title ?original_title . " +
                    "   ?uri ont:language ?language . " +
                    "   ?uri ont:prod_country ?prod_country . " +
                    "	?uri ont:productedBy ?produri . " +
                    "	?produri ont:org_name ?prodcomp . " +
                    "	?uri ont:starring ?acturi . " +
                    "	?acturi ont:org_name ?actor . " +
                    "	?uri ont:directedBy ?diruri . " +
                    "	?diruri ont:person_name ?director . " +
                    "	?uri ont:editedBy ?edituri . " +
                    "	?edituri ont:perso_name ?editor . " +
                    "	?uri ont:screenplayBy ?screenuri . " +
                    "	?screenuri ont:person_name ?screenwriter . " +
*/
                    "} ";

var myquery = require('../public/javascripts/query');
var queryResults = myquery(media, queryString);

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
