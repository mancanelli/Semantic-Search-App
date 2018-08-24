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
import org.apache.jena.rdf.model.RDFNode;

import org.apache.log4j.varia.NullAppender;

import java.io.*;
import java.util.*;


public class MyQuery {
	
	public static void main(String[] args) {
		
		// setup the default configuration for log4j
		org.apache.log4j.BasicConfigurator.configure(new NullAppender());
		
		// creazione di un modello in memoria
		OntModel model = ModelFactory.createOntologyModel();
		model.read("populated.owl", "RDF/XML");
		
		// creazione della query da eseguire
		String queryString = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> " +
							 "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> " +
							 "PREFIX owl: <http://www.w3.org/2002/07/owl#> " +
							 "PREFIX ont: <http://www.semanticweb.org/matteo/ontologies/project#> " +
							 "SELECT ?title ?name " +
							 "WHERE { " +
							 "	?mybook rdf:type ont:Book . " +
							 "	?mybook ont:book_title ?title . " +
							 "	?mybook ont:writtenBy ?aut . " +
							 "	?aut ont:person_name ?name " +
							 "} " +
							 "LIMIT 10";
		
		Query query = QueryFactory.create(queryString);
		
		// esecuzione della query
		QueryExecution qe = QueryExecutionFactory.create(query, model);
		ResultSet results = qe.execSelect();
		
		// stampa
		ResultSetFormatter.out(System.out, results, query);
		
		// chiusura della struttura dati per il rilascio di memoria
		qe.close();
	}
}

