package similarity;

import java.util.*;

import entities.Movie;

public class TFIDF {
	private ArrayList<Movie> movies;
	
	public TFIDF(ArrayList<Movie> movies) {
		this.movies = movies;
	}
	
	public double yearTFIDF(Movie ref, Movie rnd) {
		double tf = 0;
		double idf = 0;
		int cnt = 0;
		
		if(rnd.getYear().equals(ref.getYear()))
			tf++;
		
		for(Movie movie : movies)
			if(movie.getYear().equals(ref.getYear()))
				cnt++;
		
		idf = Math.log10(((double) movies.size()) / ((double) cnt));
		
		return tf * idf;
	}
	
	public double artistTFIDF(Movie ref, Movie rnd) {
		double tf = 0;
		double idf = 0;
		int cnt = 0;
		
		for(int i = 0; i < rnd.getArtists().size(); i++)
			for(int j = 0; j < ref.getArtists().size(); j++)
				if(rnd.getArtists().get(i).equals(ref.getArtists().get(j)))
					tf++;
		
		if(rnd.getArtists().size() > 1)
			tf = tf / rnd.getArtists().size();
		else
			tf = tf / 2;
		
		for(Movie movie : movies)
			for(int i = 0; i < movie.getArtists().size(); i++)
				for(int j = 0; j < ref.getArtists().size(); j++)
					if(movie.getArtists().get(i).equals(ref.getArtists().get(j)))
						cnt++;
		
		idf = Math.log10(((double) movies.size()) / ((double) cnt));
		
		return tf * idf;
	}
	
	public double genreTFIDF(Movie ref, Movie rnd) {
		double tf = 0;
		double idf = 0;
		int cnt = 0;
		
		for(int i = 0; i < rnd.getGenres().size(); i++)
			for(int j = 0; j < ref.getGenres().size(); j++)
				if(rnd.getGenres().get(i).equals(ref.getGenres().get(j)))
					tf++;
		
		if(rnd.getGenres().size() > 1)
			tf = tf / rnd.getGenres().size();
		else
			tf = tf / 2;
		
		for(Movie movie : movies)
			for(int i = 0; i < movie.getGenres().size(); i++)
				for(int j = 0; j < ref.getGenres().size(); j++)
					if(movie.getGenres().get(i).equals(ref.getGenres().get(j)))
						cnt++;
		
		idf = Math.log10(((double) movies.size()) / ((double) cnt));
		
		return tf * idf;
	}
}
