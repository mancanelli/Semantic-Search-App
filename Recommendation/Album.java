package entities;

import java.util.ArrayList;

public class Album {
	private String uri;
	private Integer year;
	private ArrayList<String> artists;
	private ArrayList<String> genres;

	public Album(String uri, Integer year) {
		super();
		this.uri = uri;
		this.year = year;
		this.artists = new ArrayList<>();
		this.genres = new ArrayList<>();
	}

	public Album(String uri, Integer year, ArrayList<String> artists, ArrayList<String> genres) {
		super();
		this.uri = uri;
		this.year = year;
		this.artists = artists;
		this.genres = genres;
	}

	public String getUri() {
		return uri;
	}

	public void setUri(String uri) {
		this.uri = uri;
	}

	public Integer getYear() {
		return year;
	}

	public void setYear(Integer year) {
		this.year = year;
	}

	public ArrayList<String> getArtists() {
		return artists;
	}

	public void setArtists(ArrayList<String> artists) {
		this.artists = artists;
	}

	public void addArtist(String artist) {
		this.artists.add(artist);
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

	@Override
	public String toString() {
		return this.uri;
	}

	@Override
	public boolean equals(Object obj) {
		if((obj == null) || !(obj instanceof Album))
			return false;

		return ((Album) obj).getUri().equals(this.getUri());
	}

	@Override
	public int hashCode() {
		return uri.hashCode();
	}
}
