package similarity;

public final class Similarity {
	public static double cosineSimilarity(double[] vec1, double[] vec2) {
		double dotProduct = 0;
		double normVec1 = 0;
		double normVec2 = 0;
		
		for(int i = 0; i < vec1.length; i++) {
			dotProduct += vec1[i] * vec2[i];
			normVec1   += vec1[i] * vec1[i];
			normVec2   += vec2[i] * vec2[i];
		}
		
		double denom = Math.sqrt(normVec1) * Math.sqrt(normVec2);
		
		if(denom == 0 || Double.isNaN(denom))
			return 0;
		
		return dotProduct / denom;
	}
}
