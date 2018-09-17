package main;

import org.apache.jena.query.Query;
import org.apache.jena.query.QueryExecution;
import org.apache.jena.query.QueryExecutionFactory;
import org.apache.jena.query.QueryFactory;
import org.apache.jena.query.QuerySolution;

import org.apache.jena.query.ResultSet;
import org.apache.jena.query.ResultSetFormatter;

import org.apache.jena.ontology.Individual;
import org.apache.jena.ontology.OntClass;
import org.apache.jena.ontology.OntModel;

import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.ModelFactory;
import org.apache.jena.rdf.model.Property;
import org.apache.jena.rdf.model.Resource;
import org.apache.jena.rdf.model.Literal;
import org.apache.jena.rdf.model.RDFNode;

import org.apache.log4j.varia.NullAppender;

import java.io.*;
import java.util.*;

import entities.*;
import query.MyQuery;
import recommender.Recommender;

public class Main {
	public static void main(String[] args) {
		org.apache.log4j.BasicConfigurator.configure(new NullAppender());

		String ontURI = "http://www.semanticweb.org/matteo/ontologies/project#";
		String prop = "correlatedWith";

		String queryString = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> " +
							 "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> " +
							 "PREFIX owl: <http://www.w3.org/2002/07/owl#> " +
							 "PREFIX ont: <http://www.semanticweb.org/matteo/ontologies/project#> " +
							 "SELECT ?myalbum ?artist ?genre ?year " +
							 "WHERE { " +
							 "	?myalbum rdf:type ont:Album . " +
							 "	?myalbum ont:recordedBy ?art . " +
							 "	?art ont:person_name ?artist . " +
							 "	?myalbum ont:album_genre ?genre . " +
							 "	?myalbum ont:album_year ?year . " +
							 "} ";

		try {
			//OntModel model = ModelFactory.createOntologyModel();
			OntModel model = ModelFactory.createOntologyModel();
			model.read("../Ontology/small_album_triples.owl", "RDF/XML");

			Property correlated = model.getProperty(ontURI, prop);

			ArrayList<Object> items = MyQuery.queryExec(model, queryString);
			ArrayList<Object> recommended = new ArrayList<Object>();
			Recommender recom = new Recommender(items);

			int i = 0;

			for(Object item : items) {
				recommended = recom.recommendation(item);

				for(Object obj : recommended) {
					Resource firstResource = model.getResource(((Album) item).getUri());
					Resource secondResource = model.getResource(((Album) obj).getUri());

					firstResource.addProperty(correlated, secondResource);
				}

				System.out.println(i++);
			}

			model.write(new PrintWriter("album_recom.owl", "UTF-8"), "RDF/XML");
		}
		catch (Exception e) {
			System.out.println("Something went wrong: " + e);
		}
	}
}
