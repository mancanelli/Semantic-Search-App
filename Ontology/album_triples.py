from rdflib import URIRef, Literal, RDF
from formatURI import formatURI
from ast import literal_eval
import csv


def addAlbumTriples(graph, ontURI):
    with open('../Data/album.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')

        for row in csv_reader:
            # Album
            if row[8]:
                title = formatURI(str(row[0])) + "_" + str(row[8])
            else:
                title = formatURI(str(row[0]))

            graph.add((URIRef(ontURI + title), RDF.type, URIRef(ontURI + "#Album")))

            # Title
            graph.add((URIRef(ontURI + title), URIRef(ontURI + "#album_title"), Literal(str(row[0]))))

            # Rating
            if row[3]:
                graph.add((URIRef(ontURI + title), URIRef(ontURI + "#album_rating"), Literal(float(row[3]))))

            # Album Year
            if row[8]:
                graph.add((URIRef(ontURI + title), URIRef(ontURI + "#album_year"), Literal(int(row[8]))))

            # Label
            if row[7]:
                for elem in literal_eval(row[7]):
                    lab = formatURI(elem)
                    graph.add((URIRef(ontURI + lab), RDF.type, URIRef(ontURI + "#Label")))

                    graph.add((URIRef(ontURI + lab), URIRef(ontURI + "#org_name"), Literal(elem)))

                    graph.add((URIRef(ontURI + title), URIRef(ontURI + "#labeledBy"), URIRef(ontURI + lab)))

            # Artist
            if row[1]:
                for elem in row[1].split(", "):
                    art = formatURI(elem)
                    graph.add((URIRef(ontURI + art), RDF.type, URIRef(ontURI + "#Artist")))

                    graph.add((URIRef(ontURI + art), URIRef(ontURI + "#person_name"), Literal(elem)))

                    graph.add((URIRef(ontURI + title), URIRef(ontURI + "#recordedBy"), URIRef(ontURI + art)))

            # Genre
            if row[6]:
                for elem in literal_eval(row[6]):
                    graph.add((URIRef(ontURI + title), URIRef(ontURI + "#album_genre"), Literal(elem)))
