from rdflib import URIRef, Literal, RDF
from formatURI import formatURI
from ast import literal_eval
import csv


def addMovieTriples(graph, ontURI):
    with open('../Data/movies.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        flag = True

        for row in csv_reader:
            if flag:
                flag = False
                continue

            # Movie
            if row[8]:
                title = formatURI(str(row[1])) + "_" + str(row[8]).split("-")[0]
            else:
                title = formatURI(str(row[1]))

            graph.add((URIRef(ontURI + title), RDF.type, URIRef(ontURI + "#Movie")))

            # Title
            graph.add((URIRef(ontURI + title), URIRef(ontURI + "#movie_title"), Literal(str(row[1]))))

            # Genre
            if row[4]:
                for elem in literal_eval(row[4]):
                    graph.add((URIRef(ontURI + title), URIRef(ontURI + "#movie_genre"), Literal(elem)))

            # Runtime
            if row[5]:
                graph.add((URIRef(ontURI + title), URIRef(ontURI + "#runtime"), Literal(int(row[5]))))

            # Budget
            if row[7]:
                graph.add((URIRef(ontURI + title), URIRef(ontURI + "#budget"), Literal(int(row[7]))))

            # Year
            if row[8]:
                graph.add((URIRef(ontURI + title), URIRef(ontURI + "#movie_date"), Literal(str(row[8]).split("-")[0])))

            # Revenue
            if row[9]:
                graph.add((URIRef(ontURI + title), URIRef(ontURI + "#revenue"), Literal(int(row[9]))))

            # Rating
            if row[10]:
                graph.add((URIRef(ontURI + title), URIRef(ontURI + "#movie_rating"), Literal(float(row[10]))))

            # Collection
            if row[11]:
                graph.add((URIRef(ontURI + title), URIRef(ontURI + "#collection"), Literal(str(row[11]))))

            # Original Title
            if row[13]:
                graph.add((URIRef(ontURI + title), URIRef(ontURI + "#movie_original_title"), Literal(str(row[13]))))

            # Language
            if row[14]:
                graph.add((URIRef(ontURI + title), URIRef(ontURI + "#language"), Literal(str(row[14]))))

            # Prod Country
            if row[12]:
                for elem in literal_eval(row[12]):
                    graph.add((URIRef(ontURI + title), URIRef(ontURI + "#prod_country"), Literal(elem)))

            # Prod Company
            if row[6]:
                for elem in literal_eval(row[6]):
                    pc = formatURI(elem)
                    graph.add((URIRef(ontURI + pc), RDF.type, URIRef(ontURI + "#ProductionCompany")))

                    graph.add((URIRef(ontURI + pc), URIRef(ontURI + "#org_name"), Literal(elem)))

                    graph.add((URIRef(ontURI + title), URIRef(ontURI + "#productedBy"), URIRef(ontURI + pc)))

            # Cast
            if row[2]:
                for elem in literal_eval(row[2]):
                    ca = formatURI(elem[1])
                    mc = elem[0].split("(")[0].strip()

                    graph.add((URIRef(ontURI + ca), RDF.type, URIRef(ontURI + "#Actor")))

                    graph.add((URIRef(ontURI + ca), URIRef(ontURI + "#person_name"), Literal(elem[1])))

                    graph.add((URIRef(ontURI + title), URIRef(ontURI + "#starring"), URIRef(ontURI + ca)))

                    if mc:
                        if mc == "Himself" or mc == "Herself":
                            graph.add((URIRef(ontURI + title), URIRef(ontURI + "#main_character"), Literal(elem[1])))
                        else:
                            graph.add((URIRef(ontURI + title), URIRef(ontURI + "#main_character"), Literal(mc)))

            # Crew
            if row[3]:
                for elem in literal_eval(row[3]):
                    mm = formatURI(elem[1])

                    if elem[0] == "Director":
                        graph.add((URIRef(ontURI + mm), RDF.type, URIRef(ontURI + "#Director")))
                        graph.add((URIRef(ontURI + mm), URIRef(ontURI + "#person_name"), Literal(elem[1])))
                        graph.add((URIRef(ontURI + title), URIRef(ontURI + "#directedBy"), URIRef(ontURI + mm)))

                    elif elem[0] == "Editor":
                        graph.add((URIRef(ontURI + mm), RDF.type, URIRef(ontURI + "#Editor")))
                        graph.add((URIRef(ontURI + mm), URIRef(ontURI + "#person_name"), Literal(elem[1])))
                        graph.add((URIRef(ontURI + title), URIRef(ontURI + "#editedBy"), URIRef(ontURI + mm)))

                    elif elem[0] == "Screenplay" or elem[0] == "Writer":
                        graph.add((URIRef(ontURI + mm), RDF.type, URIRef(ontURI + "#Screenwriter")))
                        graph.add((URIRef(ontURI + mm), URIRef(ontURI + "#person_name"), Literal(elem[1])))
                        graph.add((URIRef(ontURI + title), URIRef(ontURI + "#screenplayBy"), URIRef(ontURI + mm)))

                    elif elem[0] == "Producer" or elem[0] == "Co-Producer" or elem[0] == "Executive Producer":
                        graph.add((URIRef(ontURI + mm), RDF.type, URIRef(ontURI + "#Producer")))
                        graph.add((URIRef(ontURI + mm), URIRef(ontURI + "#person_name"), Literal(elem[1])))
                        graph.add((URIRef(ontURI + title), URIRef(ontURI + "#producedBy"), URIRef(ontURI + mm)))

                    elif "Music Composer" in elem[0]:
                        graph.add((URIRef(ontURI + mm), RDF.type, URIRef(ontURI + "#MusicComposer")))
                        graph.add((URIRef(ontURI + mm), URIRef(ontURI + "#person_name"), Literal(elem[1])))
                        graph.add((URIRef(ontURI + title), URIRef(ontURI + "#musicBy"), URIRef(ontURI + mm)))
