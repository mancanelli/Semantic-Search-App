package entities;

import java.util.ArrayList;

public class Game {
	private String uri;
	private Integer year;
	private String esrb;
    private String genre;
    private String platform;
	private ArrayList<String> publishers;

	public Game(String uri, Integer year, String esrb, String platform, String genre) {
		super();
		this.uri = uri;
		this.year = year;
        this.esrb = esrb;
        this.genre = genre;
        this.platform = platform;
		this.publishers = new ArrayList<>();
	}

	public Game(String uri, Integer year, String esrb, String platform, String genre, ArrayList<String> publishers) {
		super();
		this.uri = uri;
		this.year = year;
        this.esrb = esrb;
        this.genre = genre;
        this.platform = platform;
		this.publishers = publishers;
	}

	public String getUri() {
		return uri;
	}

	public void setUri(String uri) {
		this.uri = uri;
	}

    public String getEsrb() {
		return esrb;
	}

	public void setEsrb(String esrb) {
		this.esrb = esrb;
	}

    public String getGenre() {
		return genre;
	}

	public void setGenre(String genre) {
		this.genre = genre;
	}

    public String getPlatform() {
		return platform;
	}

	public void setPlatform(String platform) {
		this.platform = platform;
	}

	public Integer getYear() {
		return year;
	}

	public void setYear(Integer year) {
		this.year = year;
	}

	public ArrayList<String> getPublishers() {
		return publishers;
	}

	public void setPublishers(ArrayList<String> publishers) {
		this.publishers = publishers;
	}

	public void addPublisher(String publisher) {
		this.publishers.add(publisher);
	}

	@Override
	public String toString() {
		return this.uri;
	}

	@Override
	public boolean equals(Object obj) {
		if((obj == null) || !(obj instanceof Game))
			return false;

		return ((Game) obj).getUri().equals(this.getUri());
	}

	@Override
	public int hashCode() {
		return uri.hashCode();
	}
}
