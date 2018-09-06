from rdflib import URIRef, Literal, RDF
from formatURI import formatURI
import csv


def addBookTriples(graph, ontURI):
    with open('../Data/books.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        flag = True

        for row in csv_reader:
            if flag:
                flag = False
                continue

            # Book
            title = formatURI(str(row[2]))
            graph.add((URIRef(ontURI + title), RDF.type, URIRef(ontURI + "#Book")))

            # Title
            graph.add((URIRef(ontURI + title), URIRef(ontURI + "#book_title"), Literal(str(row[2]))))

            # Series
            if row[3]:
                graph.add((URIRef(ontURI + title), URIRef(ontURI + "#series"), Literal(str(row[3]))))

            # Num Series
            if row[4]:
                graph.add((URIRef(ontURI + title), URIRef(ontURI + "#num_series"), Literal(str(row[4]))))

            # Original Title
            if row[5]:
                graph.add((URIRef(ontURI + title), URIRef(ontURI + "#book_original_title"), Literal(str(row[5]))))

            # Year
            if row[6]:
                graph.add((URIRef(ontURI + title), URIRef(ontURI + "#book_year"), Literal(int(row[6]))))

            # Rating
            if row[7]:
                graph.add((URIRef(ontURI + title), URIRef(ontURI + "#book_rating"), Literal(float(row[7]) * 2)))

            # Image
            if row[8]:
                graph.add((URIRef(ontURI + title), URIRef(ontURI + "#cover_image"), URIRef(str(row[8]))))

            # Author
            if row[1]:
                author = formatURI(str(row[1]))
                graph.add((URIRef(ontURI + author), RDF.type, URIRef(ontURI + "#Author")))

                graph.add((URIRef(ontURI + author), URIRef(ontURI + "#person_name"), Literal(str(row[1]))))

                graph.add((URIRef(ontURI + title), URIRef(ontURI + "#writtenBy"), URIRef(ontURI + author)))
