var express = require('express');
var router = express.Router();

var media = "/album_triples.owl";
var queryString = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> " +
                    "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> " +
                    "PREFIX owl: <http://www.w3.org/2002/07/owl#> " +
                    "PREFIX ont: <http://www.semanticweb.org/matteo/ontologies/project#> " +
//                  "SELECT ?myalbum ?title ?artist ?year ?rating ?reviewurl ?review ?genre ?reviewer ?label " +
                    "SELECT ?myalbum ?title ?artist ?year " +
                    "WHERE { " +
                    "	?myalbum rdf:type ont:Album . " +
                    "	?myalbum ont:album_title ?title . " +
                    "	?myalbum ont:recordedBy ?arturl . " +
                    "	?arturl ont:person_name ?artist . " +
                    "   ?myalbum ont:album_year ?year . " +
/*
                    "   ?myalbum ont:album_rating ?rating . " +
                    "   ?myalbum ont:review_url ?reviewurl . " +
                    "   ?myalbum ont:review_date ?reviewdate . " +
                    "   ?myalbum ont:album_review ?review . " +
                    "	?myalbum ont:album_genre ?genre . " +
                    "	?myalbum ont:reviewedBy ?reviewerurl . " +
                    "	?reviewerurl ont:person_name ?reviewer . " +
                    "	?myalbum ont:labeledBy ?labelurl . " +
                    "	?labelurl ont:org_name ?label . " +
*/
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
        if (alb === queryResults[i].album_url)
            data = queryResults[i];

    res.render('info', {data: data});
});

module.exports = router;

/*
var queryString = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> " +
                    "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> " +
                    "PREFIX owl: <http://www.w3.org/2002/07/owl#> " +
                    "PREFIX ont: <http://www.semanticweb.org/matteo/ontologies/project#> " +
//                    "SELECT ?myalbum ?title ?artist ?year ?rating ?genre ?label " +
                    "SELECT ?myalbum ?title ?artist ?year " +
                    "WHERE { " +
                    "	?myalbum rdf:type ont:Album . " +
                    "	?myalbum ont:album_title ?title . " +
                    "	?myalbum ont:recordedBy ?arturl . " +
                    "	?arturl ont:person_name ?artist . " +
                    "   ?myalbum ont:album_year ?year . " +
                    "   ?myalbum ont:album_rating ?rating . " +
                    "	?myalbum ont:album_genre ?genre . " +
                    "	?myalbum ont:labeledBy ?labelurl . " +
                    "	?labelurl ont:org_name ?label . " +
                    "} ";
*/
