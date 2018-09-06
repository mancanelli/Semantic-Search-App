
def formatURI(text):
    for ch in [".", "-", ")", "(", ":", "| ", '"', "[", "]", "> ", "{", "}", "#"]:
        if ch in text:
            text = text.replace(ch, "")

    for ch in ["/", "\\", "'", "`", "^", ">", "&", "   "]:
        if ch in text:
            text = text.replace(ch, " ")

    if "& " in text:
        text = text.replace("& ", "and ")

    if "%" in text:
        text = text.replace("%", "_percent")

    text = text.replace(" ", "_")
    return "#" + text


"""
g.add((rdflib.URIRef(link + "#ciao"), rdflib.RDF.type, rdflib.URIRef(link + "#Movie")))

bag = rdflib.BNode()
g.add((bag, rdflib.RDF.type, rdflib.RDF.Bag))

# The bag has 3 authors
g.add((bag, rdflib.URIRef(u'http://www.w3.org/1999/02/22-rdf-syntax-ns#_1'), rdflib.Literal("mio")))
g.add((bag, rdflib.URIRef(u'http://www.w3.org/1999/02/22-rdf-syntax-ns#_2'), rdflib.Literal("tuo")))

g.add((rdflib.URIRef(link + "#ciao"), rdflib.URIRef(link + "#main_character"), bag))

bag = rdflib.BNode()
g.add((bag, rdflib.RDF.type, rdflib.RDF.Bag))

# The bag has 3 authors
g.add((bag, rdflib.URIRef(u'http://www.w3.org/1999/02/22-rdf-syntax-ns#_1'), rdflib.Literal("nostro")))

g.add((rdflib.URIRef(link + "#ciao"), rdflib.URIRef(link + "#main_character"), bag))
"""
