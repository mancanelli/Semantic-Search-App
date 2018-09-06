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

import java.util.*;

import entities.*;

public final class MyQuery {
	public static ArrayList<Object> queryExec(OntModel model, String queryString) {
		// setup the default configuration for log4j
		org.apache.log4j.BasicConfigurator.configure(new NullAppender());

		ArrayList<Object> items = new ArrayList<Object>();

		// creazione della query da eseguire
		Query query = QueryFactory.create(queryString);

		// esecuzione della query
		QueryExecution qe = QueryExecutionFactory.create(query, model);
		ResultSet resultSet = qe.execSelect();

		while (resultSet.hasNext()) {
			QuerySolution result = resultSet.next();
			Iterator<String> variables = result.varNames();

			String uri = "";
			Integer year = 0;
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
						art.add(((Literal) value).getLexicalForm());
						break;

					case "genre":
						gen.add(((Literal) value).getLexicalForm());
						break;

					case "year":
						year = Integer.valueOf(((Literal) value).getLexicalForm());
						break;
				}
			}

			Object obj = new Album(uri, year, art, gen);
			boolean itemPres = false;

			for(Object item : items) {
				if(((Album) item).equals(((Album) obj))) {
					boolean artPres = false;
					boolean genPres = false;

					for(String artist : ((Album) item).getArtists())
						if(artist.equals(art.get(0)))
							artPres = true;

					for(String genre : ((Album) item).getGenres())
						if(genre.equals(gen.get(0)))
							genPres = true;

					if(!artPres)
						((Album) item).addArtist(art.get(0));
					if(!genPres)
						((Album) item).addGenre(gen.get(0));

					itemPres = true;
					break;
				}
			}

			if(!itemPres)
				items.add(obj);
		}

		// chiusura della struttura dati per il rilascio di memoria
		qe.close();

		return items;
	}
}
