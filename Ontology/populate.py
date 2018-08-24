from ast import literal_eval
import rdflib
import csv


g = rdflib.Graph()
g.parse("ontology.owl", format="xml")

link = "http://www.semanticweb.org/matteo/ontologies/project"


def formatURI(text):
	for ch in [".", "-", ")", "(", ":", "| ", '"', "[", "]", "> ", "{", "}"]:
		if ch in text:
			text = text.replace(ch, "")
	
	for ch in ["/", "\\", "'", "`", "^", ">", "&", "   "]:
		if ch in text:
			text = text.replace(ch, " ")
	
	if "& " in text:
		text = text.replace("& ", "and ")
	
	text = text.replace(" ", "_")
	return "#" + text


with open('../Data/books_res.csv', 'r') as csvfile:
	csv_reader = csv.reader(csvfile, delimiter=',')
	
	i = 0
	
	for row in csv_reader:
		if i == 0:
			i = 1
			continue
		
		# Book
		title = formatURI(str(row[2]))
		g.add((rdflib.URIRef(link + title), rdflib.RDF.type, rdflib.URIRef(link + "#Book")))
		
		# Title
		g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#book_title"), rdflib.Literal(str(row[2]))))
		
		# Series
		if row[3]:
			g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#series"), rdflib.Literal(str(row[3]))))
		
		# Num Series
		if row[4]:
			g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#num_series"), rdflib.Literal(str(row[4]))))
		
		# Original Title
		if row[5]:
			g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#book_original_title"), rdflib.Literal(str(row[5]))))
		
		# Year
		if row[6]:
			g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#book_year"), rdflib.Literal(int(row[6]))))
		
		# Rating
		if row[7]:
			g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#book_rating"), rdflib.Literal(float(row[7]) * 2)))
		
		# Image
		if row[8]:
			g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#cover_image"), rdflib.URIRef(str(row[8]))))
		
		# Author
		if row[1]:
			author = formatURI(str(row[1]))
			g.add((rdflib.URIRef(link + author), rdflib.RDF.type, rdflib.URIRef(link + "#Author")))
			
			g.add((rdflib.URIRef(link + author), rdflib.URIRef(link + "#person_name"), rdflib.Literal(str(row[1]))))
			
			g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#writtenBy"), rdflib.URIRef(link + author)))


with open('../Data/games_res.csv', 'r') as csvfile:
	csv_reader = csv.reader(csvfile, delimiter=',')
	
	i = 0
	
	for row in csv_reader:
		if i == 0:
			i = 1
			continue
		
		# Game
		title = formatURI(str(row[0]))
		g.add((rdflib.URIRef(link + title), rdflib.RDF.type, rdflib.URIRef(link + "#Game")))
		
		# Title
		g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#game_name"), rdflib.Literal(str(row[0]))))
		
		# Platform
		if row[1]:
			g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#platform"), rdflib.Literal(str(row[1]))))
		
		# Year
		if row[3]:
			g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#game_year"), rdflib.Literal(row[3])))
			
		# Genre
		if row[4]:
			g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#game_genre"), rdflib.Literal(str(row[4]))))
		
		# ESRB
		if row[6]:
			g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#esrb"), rdflib.Literal(str(row[6]))))
		
		# Sales
		if row[7]:
			g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#na_sales"), rdflib.Literal(float(row[7]))))
		
		if row[8]:
			g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#eu_sales"), rdflib.Literal(float(row[8]))))
		
		if row[9]:
			g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#jp_sales"), rdflib.Literal(float(row[9]))))
		
		if row[10]:
			g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#glob_sales"), rdflib.Literal(float(row[10]))))
		
		# Rating
		if row[11]:
			g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#critic_score"), rdflib.Literal(float(row[11]) % 10)))
		
		if row[12]:
			g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#user_score"), rdflib.Literal(float(row[12]))))
		
		# Publisher
		if row[2]:
			pub = formatURI(str(row[2]))
			g.add((rdflib.URIRef(link + pub), rdflib.RDF.type, rdflib.URIRef(link + "#GamePublisher")))
			
			g.add((rdflib.URIRef(link + pub), rdflib.URIRef(link + "#org_name"), rdflib.Literal(str(row[2]))))
			
			g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#publishedBy"), rdflib.URIRef(link + pub)))
		
		# Developer
		if row[5]:
			for elem in row[5].split(", "):
				dev = formatURI(elem)
				g.add((rdflib.URIRef(link + dev), rdflib.RDF.type, rdflib.URIRef(link + "#GameDeveloper")))
				
				g.add((rdflib.URIRef(link + dev), rdflib.URIRef(link + "#org_name"), rdflib.Literal(elem)))
				
				g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#developedBy"), rdflib.URIRef(link + dev)))


with open('../Data/song_res.csv', 'r') as csvfile:
	csv_reader = csv.reader(csvfile, delimiter=',')
	
	i = 0
	
	for row in csv_reader:
		if i == 0:
			i = 1
			continue
		
		# Song
		title = formatURI(str(row[0]))
		g.add((rdflib.URIRef(link + title), rdflib.RDF.type, rdflib.URIRef(link + "#Song")))
		
		# Title
		g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#song_title"), rdflib.Literal(str(row[0]))))
		
		# Lyrics
		if row[2]:
			g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#lyrics"), rdflib.Literal(str(row[2]))))
		
		# Artist
		if row[1]:
			for elem in row[1].split(", "):
				art = formatURI(elem)
				g.add((rdflib.URIRef(link + art), rdflib.RDF.type, rdflib.URIRef(link + "#Artist")))
				
				g.add((rdflib.URIRef(link + art), rdflib.URIRef(link + "#person_name"), rdflib.Literal(elem)))
				
				g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#playedBy"), rdflib.URIRef(link + art)))
		

with open('../Data/album_res.csv', 'r') as csvfile:
	csv_reader = csv.reader(csvfile, delimiter=',')
	
	for row in csv_reader:
		
		# Album
		title = formatURI(str(row[0]))
		g.add((rdflib.URIRef(link + title), rdflib.RDF.type, rdflib.URIRef(link + "#Album")))
		
		# Title
		g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#album_title"), rdflib.Literal(str(row[0]))))
		
		# Review
		if row[2]:
			g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#review_url"), rdflib.Literal(str(row[2]))))
		
		# Rating
		if row[3]:
			g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#album_rating"), rdflib.Literal(float(row[3]))))
		
		# Review Date
		if row[5]:
			g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#review_date"), rdflib.Literal(row[5])))
		
		# Album Year
		if row[8]:
			g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#album_year"), rdflib.Literal(int(row[8]))))
		
		# Review
		if row[9]:
			g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#album_review"), rdflib.Literal(str(row[9]))))
		
		# Label
		if row[7]:
			for elem in literal_eval(row[7]):
				lab = formatURI(elem)
				g.add((rdflib.URIRef(link + lab), rdflib.RDF.type, rdflib.URIRef(link + "#Label")))
				
				g.add((rdflib.URIRef(link + lab), rdflib.URIRef(link + "#org_name"), rdflib.Literal(elem)))
				
				g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#labeledBy"), rdflib.URIRef(link + lab)))
		
		# Artist
		if row[1]:
			for elem in row[1].split(", "):
				art = formatURI(elem)
				g.add((rdflib.URIRef(link + art), rdflib.RDF.type, rdflib.URIRef(link + "#Artist")))
				
				g.add((rdflib.URIRef(link + art), rdflib.URIRef(link + "#person_name"), rdflib.Literal(elem)))
				
				g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#recordedBy"), rdflib.URIRef(link + art)))
		
		# Reviewer
		if row[4]:
			for elem in row[4].split(", "):
				rev = formatURI(elem)
				g.add((rdflib.URIRef(link + rev), rdflib.RDF.type, rdflib.URIRef(link + "#Reviewer")))
				
				g.add((rdflib.URIRef(link + rev), rdflib.URIRef(link + "#person_name"), rdflib.Literal(elem)))
				
				g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#reviewedBy"), rdflib.URIRef(link + rev)))
		
		# Genre
		if row[6]:
			for elem in literal_eval(row[6]):
				g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#album_genre"), rdflib.Literal(elem)))


with open('../Data/movies_res.csv', 'r') as csvfile:
	csv_reader = csv.reader(csvfile, delimiter=',')
	
	i = 0
	
	for row in csv_reader:
		if i == 0:
			i = 1
			continue
		
		# Movie
		title = formatURI(str(row[1]))
		g.add((rdflib.URIRef(link + title), rdflib.RDF.type, rdflib.URIRef(link + "#Movie")))
		
		# Title
		g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#movie_title"), rdflib.Literal(str(row[1]))))
		
		# Genre
		if row[4]:
			for elem in literal_eval(row[4]):
				g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#movie_genre"), rdflib.Literal(elem)))
		
		# Runtime
		if row[5]:
			g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#runtime"), rdflib.Literal(int(row[5]))))
		
		# Budget
		if row[7]:
			g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#budget"), rdflib.Literal(int(row[7]))))
		
		# Year
		if row[8]:
			g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#movie_date"), rdflib.Literal(row[8])))
		
		# Revenue
		if row[9]:
			g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#revenue"), rdflib.Literal(int(row[9]))))
		
		# Rating
		if row[10]:
			g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#movie_rating"), rdflib.Literal(float(row[10]))))
		
		# Collection
		if row[11]:
			g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#collection"), rdflib.Literal(str(row[11]))))
		
		# Original Title
		if row[13]:
			g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#movie_original_title"), rdflib.Literal(str(row[13]))))
		
		# Language
		if row[14]:
			g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#language"), rdflib.Literal(str(row[14]))))
		
		# Prod Country
		if row[12]:
			for elem in literal_eval(row[12]):
				g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#prod_country"), rdflib.Literal(elem)))
		
		# Tagline
		if row[15]:
			g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#tagline"), rdflib.Literal(str(row[15]))))
		
		# Overview
		if row[16]:
			g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#overview"), rdflib.Literal(str(row[16]))))
		
		# Prod Company
		if row[6]:
			for elem in literal_eval(row[6]):
				pc = formatURI(elem)
				g.add((rdflib.URIRef(link + pc), rdflib.RDF.type, rdflib.URIRef(link + "#ProductionCompany")))
				
				g.add((rdflib.URIRef(link + pc), rdflib.URIRef(link + "#org_name"), rdflib.Literal(elem)))
				
				g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#productedBy"), rdflib.URIRef(link + pc)))
		
		# Cast
		if row[2]:
			for elem in literal_eval(row[2]):
				ca = formatURI(elem[1])
				mc = elem[0].split("(")[0].strip()
				
				g.add((rdflib.URIRef(link + ca), rdflib.RDF.type, rdflib.URIRef(link + "#Actor")))
				
				g.add((rdflib.URIRef(link + ca), rdflib.URIRef(link + "#person_name"), rdflib.Literal(elem[1])))
				
				g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#starring"), rdflib.URIRef(link + ca)))
				
				if mc:
					if mc == "Himself" or mc == "Herself":
						g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#main_character"), rdflib.Literal(elem[1])))
					else:
						g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#main_character"), rdflib.Literal(mc)))

		# Crew
		if row[3]:
			for elem in literal_eval(row[3]):
				mm = formatURI(elem[1])
				
				if elem[0] == "Director":
					g.add((rdflib.URIRef(link + mm), rdflib.RDF.type, rdflib.URIRef(link + "#Director")))
					g.add((rdflib.URIRef(link + mm), rdflib.URIRef(link + "#person_name"), rdflib.Literal(elem[1])))
					g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#directedBy"), rdflib.URIRef(link + mm)))
				
				elif elem[0] == "Editor":
					g.add((rdflib.URIRef(link + mm), rdflib.RDF.type, rdflib.URIRef(link + "#Editor")))
					g.add((rdflib.URIRef(link + mm), rdflib.URIRef(link + "#person_name"), rdflib.Literal(elem[1])))
					g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#editedBy"), rdflib.URIRef(link + mm)))
				
				elif elem[0] == "Screenplay" or elem[0] == "Writer":
					g.add((rdflib.URIRef(link + mm), rdflib.RDF.type, rdflib.URIRef(link + "#Screenwriter")))
					g.add((rdflib.URIRef(link + mm), rdflib.URIRef(link + "#person_name"), rdflib.Literal(elem[1])))
					g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#screenplayBy"), rdflib.URIRef(link + mm)))
				
				elif elem[0] == "Producer" or elem[0] == "Co-Producer" or elem[0] == "Executive Producer":
					g.add((rdflib.URIRef(link + mm), rdflib.RDF.type, rdflib.URIRef(link + "#Producer")))
					g.add((rdflib.URIRef(link + mm), rdflib.URIRef(link + "#person_name"), rdflib.Literal(elem[1])))
					g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#producedBy"), rdflib.URIRef(link + mm)))
				
				elif "Music Composer" in elem[0]:
					g.add((rdflib.URIRef(link + mm), rdflib.RDF.type, rdflib.URIRef(link + "#MusicComposer")))
					g.add((rdflib.URIRef(link + mm), rdflib.URIRef(link + "#person_name"), rdflib.Literal(elem[1])))
					g.add((rdflib.URIRef(link + title), rdflib.URIRef(link + "#musicBy"), rdflib.URIRef(link + mm)))


f = open("populated.owl", "wb")
f.write(g.serialize(format='xml'))
f.close()

