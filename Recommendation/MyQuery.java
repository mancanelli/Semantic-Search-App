package query;

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

import entities.Movie;

public final class MyQuery {
	public static ArrayList<Movie> queryExec() {
		// setup the default configuration for log4j
		org.apache.log4j.BasicConfigurator.configure(new NullAppender());
		
		ArrayList<Movie> movies = new ArrayList<Movie>();
		
		// creazione di un modello in memoria
		OntModel model = ModelFactory.createOntologyModel();
		model.read("only_album.owl", "RDF/XML");
		
		// creazione della query da eseguire
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
		
		Query query = QueryFactory.create(queryString);
		
		// esecuzione della query
		QueryExecution qe = QueryExecutionFactory.create(query, model);
		ResultSet resultSet = qe.execSelect();
		
		while (resultSet.hasNext()) {
			QuerySolution result = resultSet.next();
			Iterator<String> variables = result.varNames();
			
			String uri;
			Integer year;
			ArrayList<String> art = new ArrayList<String>();
			ArrayList<String> gen = new ArrayList<String>();

			while (variables.hasNext()) {
				String var = (String) variables.next();
				RDFNode value = result.get(var);
				
				switch(var) {
					case "myalbum":
						uri = ((Resource) value).getURI();
						break;
					
					case "artist":
						art.add(value);
						break;
					
					case "genre":
						gen.add(value);
						break;
						
					case "year":
						year = Integer.valueOf(value);
						break;
				}
			}
			
			Movie m = new Movie(uri, year, art, gen);
			movies.add(m);
		}
		
		// chiusura della struttura dati per il rilascio di memoria
		qe.close();
		
		return movies;
	}
}
