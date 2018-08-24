import rdflib


g = rdflib.Graph()
g.parse("populated.owl", format="xml")


book_query = g.query(
	"""
	PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
	PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
	PREFIX owl: <http://www.w3.org/2002/07/owl#>
	PREFIX ont: <http://www.semanticweb.org/matteo/ontologies/project#>

	SELECT ?title

	WHERE {
		?mybook rdf:type ont:Book .
		?mybook ont:book_title ?title .
	}
	""")

second_query = g.query(
	"""
	PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
	PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
	PREFIX owl: <http://www.w3.org/2002/07/owl#>
	PREFIX ont: <http://www.semanticweb.org/matteo/ontologies/project#>

	SELECT ?title ?name

	WHERE {
		?mybook rdf:type ont:Book .
		?mybook ont:book_title ?title .
		?mybook ont:writtenBy ?aut .
		?aut ont:person_name ?name
	}
	""")


for row in book_query:
	print('book_title: ' + str(row[0]))
	print("--------------------------")

for row in second_query:
	print('book_title: ' + str(row[0]))
	print('author: ' + str(row[1]))
	print("--------------------------")
	
