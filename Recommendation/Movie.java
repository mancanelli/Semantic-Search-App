package entities;

import java.util.ArrayList;

public class Movie {
	private String uri;
	private Integer year;
	private ArrayList<String> artists;
	private ArrayList<String> genres;

	public Movie(String uri, Integer year) {
		super();
		this.uri = uri;
		this.year = year;
		this.artists = new ArrayList<>();
		this.genres = new ArrayList<>();
	}
	
	public Movie(String uri, Integer year, ArrayList<String> artists, ArrayList<String> genres) {
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
		String str = "Album: " + this.uri + " - Artists: ";
		
		String art = "";
		for(int i = 0; i < this.artists.size(); i++) {
			art += this.artists.get(i);
			if(i != this.artists.size()-1)
				art += ", ";
		}
		
		str += art + " - Genres: ";
		
		String gen = "";
		for(int i = 0; i < this.genres.size(); i++) {
			gen += this.genres.get(i);
			if(i != this.genres.size()-1)
				gen += ", ";
		}
		
		str += gen;
		return str;
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

