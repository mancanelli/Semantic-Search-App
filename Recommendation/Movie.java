package entities;

import java.util.ArrayList;

public class Movie {
	private String uri;
	private Integer year;
    private String collection;
    private ArrayList<String> actors;
    private ArrayList<String> directors;
    private ArrayList<String> writers;
    private ArrayList<String> companies;
	private ArrayList<String> countries;
	private ArrayList<String> genres;

	public Movie(String uri, Integer year, String collection) {
		super();
		this.uri = uri;
		this.year = year;
        this.collection = collection;
        this.actors = new ArrayList<>();
        this.directors = new ArrayList<>();
        this.writers = new ArrayList<>();
        this.companies = new ArrayList<>();
		this.countries = new ArrayList<>();
		this.genres = new ArrayList<>();
	}

	public Movie(String uri, Integer year, String collection, ArrayList<String> actors, ArrayList<String> directors, ArrayList<String> writers,
                ArrayList<String> companies, ArrayList<String> countries, ArrayList<String> genres) {
		super();
		this.uri = uri;
		this.year = year;
        this.collection = collection;
        this.actors = actors;
        this.directors = directors;
        this.writers = writers;
		this.companies = companies;
		this.countries = countries;
		this.genres = genres;
	}

	public String getUri() {
		return uri;
	}

	public void setUri(String uri) {
		this.uri = uri;
	}

    public String getCollection() {
		return collection;
	}

	public void setCollection(String collection) {
		this.collection = collection;
	}

	public Integer getYear() {
		return year;
	}

	public void setYear(Integer year) {
		this.year = year;
	}

	public ArrayList<String> getCountries() {
		return countries;
	}

	public void setCountries(ArrayList<String> countries) {
		this.countries = countries;
	}

	public void addCountry(String country) {
		this.countries.add(country);
	}

	public ArrayList<String> getGenres() {
		return genres;
	}

	public void setGenres(ArrayList<String> genres) {
		this.genres = genres;
	}

	public void addGenre(String genre) {
		this.genres.add(genre);
	}

    public ArrayList<String> getCompanies() {
		return companies;
	}

	public void setCompanies(ArrayList<String> companies) {
		this.companies = companies;
	}

	public void addCompany(String company) {
		this.companies.add(company);
	}

    public ArrayList<String> getActors() {
		return actors;
	}

	public void setActors(ArrayList<String> actors) {
		this.actors = actors;
	}

	public void addActor(String actor) {
		this.actors.add(actor);
	}

    public ArrayList<String> getDirectors() {
		return directors;
	}

	public void setDirectors(ArrayList<String> directors) {
		this.directors = directors;
	}

	public void addDirector(String director) {
		this.directors.add(director);
	}

    public ArrayList<String> getWriters() {
		return writers;
	}

	public void setWriters(ArrayList<String> writers) {
		this.writers = writers;
	}

	public void addWriter(String writer) {
		this.writers.add(writer);
	}

	@Override
	public String toString() {
		return this.uri;
	}

	@Override
	public boolean equals(Object obj) {
		if((obj == null) || !(obj instanceof Movie))
			return false;

		return ((Movie) obj).getUri().equals(this.getUri());
	}

	@Override
	public int hashCode() {
		return uri.hashCode();
	}
}
