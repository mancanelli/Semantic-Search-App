package recommender;

import java.util.*;

import entities.*;
import similarity.*;

public class Recommender {
	private ArrayList<Object> items;
	private TFIDF tfidf;

	public Recommender(ArrayList<Object> items) {
		this.items = items;
		this.tfidf = new TFIDF(items);
	}

	public double[] albumVector(Object ref, Object rnd) {
		double[] vec = new double[3];

		vec[0] = tfidf.albumYearTFIDF(ref, rnd);
		vec[1] = tfidf.albumArtistTFIDF(ref, rnd);
		vec[2] = tfidf.albumGenreTFIDF(ref, rnd);

		return vec;
	}

	public ArrayList<Object> recommendation(Object ref) {
		HashMap<Object, Double> valued = new HashMap<Object, Double>();

		double[] refVec = albumVector(ref, ref);

		for(Object item : items) {
			double[] rndVec = albumVector(ref, item);
			double val = Similarity.cosineSimilarity(refVec, rndVec);

			if(!(((Album) item).equals(((Album) ref)))) {
				valued.put(item, val);

				double minVal = 1.0;
				Object rem = ref;

				if(valued.keySet().size() > 5) {

					for(Map.Entry<Object, Double> entry : valued.entrySet()) {
						if(entry.getValue() < minVal) {
							rem = entry.getKey();
							minVal = entry.getValue();
						}
					}

					valued.remove(rem);
				}

			}
		}

		ArrayList<Object> res = new ArrayList<Object>(valued.keySet());
		return res;
	}
}
