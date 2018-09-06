package similarity;

import java.util.*;

import entities.*;

public class TFIDF {
	private ArrayList<Object> items;

	public TFIDF(ArrayList<Object> items) {
		this.items = items;
	}

	public double albumYearTFIDF(Object ref, Object rnd) {
		double tf = 0;
		double idf = 0;
		int cnt = 0;

		if(((Album) rnd).getYear().equals(((Album) ref).getYear()))
			tf++;

		for(Object item : items)
			if(((Album) item).getYear().equals(((Album) ref).getYear()))
				cnt++;

		idf = Math.log10(((double) items.size()) / ((double) cnt));

		return tf * idf;
	}

	public double albumArtistTFIDF(Object ref, Object rnd) {
		double tf = 0;
		double idf = 0;
		int cnt = 0;

		for(int i = 0; i < ((Album) rnd).getArtists().size(); i++)
			for(int j = 0; j < ((Album) ref).getArtists().size(); j++)
				if(((Album) rnd).getArtists().get(i).equals(((Album) ref).getArtists().get(j)))
					tf++;

		if(((Album) rnd).getArtists().size() > 1)
			tf = tf / ((Album) rnd).getArtists().size();
		else
			tf = tf / 2;

		for(Object item : items)
			for(int i = 0; i < ((Album) item).getArtists().size(); i++)
				for(int j = 0; j < ((Album) ref).getArtists().size(); j++)
					if(((Album) item).getArtists().get(i).equals(((Album) ref).getArtists().get(j)))
						cnt++;

		idf = Math.log10(((double) items.size()) / ((double) cnt));

		return tf * idf;
	}

	public double albumGenreTFIDF(Object ref, Object rnd) {
		double tf = 0;
		double idf = 0;
		int cnt = 0;

		for(int i = 0; i < ((Album) rnd).getGenres().size(); i++)
			for(int j = 0; j < ((Album) ref).getGenres().size(); j++)
				if(((Album) rnd).getGenres().get(i).equals(((Album) ref).getGenres().get(j)))
					tf++;

		if(((Album) rnd).getGenres().size() > 1)
			tf = tf / ((Album) rnd).getGenres().size();
		else
			tf = tf / 2;

		for(Object item : items)
			for(int i = 0; i < ((Album) item).getGenres().size(); i++)
				for(int j = 0; j < ((Album) ref).getGenres().size(); j++)
					if(((Album) item).getGenres().get(i).equals(((Album) ref).getGenres().get(j)))
						cnt++;

		idf = Math.log10(((double) items.size()) / ((double) cnt));

		return tf * idf;
	}
}
