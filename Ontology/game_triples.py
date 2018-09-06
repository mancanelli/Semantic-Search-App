from rdflib import URIRef, Literal, RDF
from formatURI import formatURI
import csv


def addGameTriples(graph, ontURI):
    with open('../Data/games.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        flag = True

        for row in csv_reader:
            if flag:
                flag = False
                continue

            # Game
            title = formatURI(str(row[0]))
            graph.add((URIRef(ontURI + title), RDF.type, URIRef(ontURI + "#Game")))

            # Title
            graph.add((URIRef(ontURI + title), URIRef(ontURI + "#game_name"), Literal(str(row[0]))))

            # Platform
            if row[1]:
                graph.add((URIRef(ontURI + title), URIRef(ontURI + "#platform"), Literal(str(row[1]))))

            # Year
            if row[3]:
                graph.add((URIRef(ontURI + title), URIRef(ontURI + "#game_year"), Literal(row[3])))

            # Genre
            if row[4]:
                graph.add((URIRef(ontURI + title), URIRef(ontURI + "#game_genre"), Literal(str(row[4]))))

            # ESRB
            if row[6]:
                graph.add((URIRef(ontURI + title), URIRef(ontURI + "#esrb"), Literal(str(row[6]))))

            # Sales
            if row[7]:
                graph.add((URIRef(ontURI + title), URIRef(ontURI + "#na_sales"), Literal(float(row[7]))))

            if row[8]:
                graph.add((URIRef(ontURI + title), URIRef(ontURI + "#eu_sales"), Literal(float(row[8]))))

            if row[9]:
                graph.add((URIRef(ontURI + title), URIRef(ontURI + "#jp_sales"), Literal(float(row[9]))))

            if row[10]:
                graph.add((URIRef(ontURI + title), URIRef(ontURI + "#glob_sales"), Literal(float(row[10]))))

            # Rating
            if row[11]:
                graph.add((URIRef(ontURI + title), URIRef(ontURI + "#critic_score"), Literal(float(row[11]) % 10)))

            if row[12]:
                graph.add((URIRef(ontURI + title), URIRef(ontURI + "#user_score"), Literal(float(row[12]))))

            # Publisher
            if row[2]:
                pub = formatURI(str(row[2]))
                graph.add((URIRef(ontURI + pub), RDF.type, URIRef(ontURI + "#GamePublisher")))

                graph.add((URIRef(ontURI + pub), URIRef(ontURI + "#org_name"), Literal(str(row[2]))))

                graph.add((URIRef(ontURI + title), URIRef(ontURI + "#publishedBy"), URIRef(ontURI + pub)))

            # Developer
            if row[5]:
                for elem in row[5].split(", "):
                    dev = formatURI(elem)
                    graph.add((URIRef(ontURI + dev), RDF.type, URIRef(ontURI + "#GameDeveloper")))

                    graph.add((URIRef(ontURI + dev), URIRef(ontURI + "#org_name"), Literal(elem)))

                    graph.add((URIRef(ontURI + title), URIRef(ontURI + "#developedBy"), URIRef(ontURI + dev)))
