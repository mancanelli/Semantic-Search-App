package entities;

import java.util.ArrayList;

public class Book {
	private String uri;
	private Integer year;
	private String series;
	private ArrayList<String> authors;

	public Book(String uri, Integer year, String series) {
		super();
		this.uri = uri;
		this.year = year;
        this.series = series;
		this.authors = new ArrayList<>();
	}

	public Book(String uri, Integer year, String series, ArrayList<String> authors) {
		super();
		this.uri = uri;
		this.year = year;
        this.series = series;
		this.authors = authors;
	}

	public String getUri() {
		return uri;
	}

	public void setUri(String uri) {
		this.uri = uri;
	}

    public String getSeries() {
		return series;
	}

	public void setSeries(String series) {
		this.series = series;
	}

	public Integer getYear() {
		return year;
	}

	public void setYear(Integer year) {
		this.year = year;
	}

	public ArrayList<String> getAuthors() {
		return authors;
	}

	public void setAuthors(ArrayList<String> authors) {
		this.authors = authors;
	}

	public void addAuthor(String author) {
		this.authors.add(author);
	}

	@Override
	public String toString() {
		return this.uri;
	}

	@Override
	public boolean equals(Object obj) {
		if((obj == null) || !(obj instanceof Book))
			return false;

		return ((Book) obj).getUri().equals(this.getUri());
	}

	@Override
	public int hashCode() {
		return uri.hashCode();
	}
}
