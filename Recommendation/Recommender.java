package recommender;

import java.util.*;

import entities.Movie;
import similarity.*;

public class Recommender {
	private ArrayList<Movie> movies;
	private TFIDF tfidf;

	public Recommender(ArrayList<Movie> movies) {
		this.movies = movies;
		this.tfidf = new TFIDF(movies);
	}
	
	public double[] vectorize(Movie ref, Movie rnd) {
		double[] vec = new double[3];
		
		vec[0] = tfidf.yearTFIDF(ref, rnd);
		vec[1] = tfidf.artistTFIDF(ref, rnd);
		vec[2] = tfidf.genreTFIDF(ref, rnd);
		
		return vec;
	}

	public ArrayList<Movie> recommendation(Movie ref) {
		HashMap<Movie, Double> valued = new HashMap<Movie, Double>();
		
		double[] refVec = vectorize(ref, ref);
		
		for(int i = 0; i < movies.size(); i++) {
			double[] rndVec = vectorize(ref, movies.get(i));
			double val = Similarity.cosineSimilarity(refVec, rndVec);
			
			if(!(movies.get(i).equals(ref))) {
				valued.put(movies.get(i), val);
				
				double minVal = 1.0;
				Movie rem = ref;
				
				if(valued.keySet().size() > 5) {
					
					for(Map.Entry<Movie, Double> entry : valued.entrySet()) {
						if(entry.getValue() < minVal) {
							rem = entry.getKey();
							minVal = entry.getValue();
						}
					}
					
					valued.remove(rem);
				}
				
			}
		}
		
		ArrayList<Movie> res = new ArrayList<Movie>(valued.keySet());
		return res;
	}
}
