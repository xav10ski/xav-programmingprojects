/*
 * Copyright 2017 Marc Liberatore.
 * Assignment given by Marc Liberatore as part of CS186: using data structures.
 * Completed by Xavier Wrenn.
 */

package crawler;

import java.net.URI;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

import org.jsoup.nodes.Document;

import document.RetrievedDocument;

/**
 * A simplified web crawler, specialized to crawl local URIs rather than to
 * retrieve remote documents.
 *
 */
public class UriCrawler {
	private Map<URI, RetrievedDocument> visited;
	private final int MAXIMUM_VISITS;
	private ArrayList<URI> unvisited;
	private int visitTrials;

	/**
	 * Instantiates a new UriCrawler. The maximum number of documents a crawler will
	 * attempt to visit, ever, is limited to visitQuota.
	 * 
	 * @param visitQuota the maximum number of documents a crawler will attempt to
	 *                   visit
	 * @throws IllegalArgumentException if maximumRetrievalAttempts is less than one
	 */
	public UriCrawler(int visitQuota) throws IllegalArgumentException {
		if (visitQuota < 1)
			throw new IllegalArgumentException();
		this.visited = new HashMap<URI, RetrievedDocument>();
		this.MAXIMUM_VISITS = visitQuota;
		this.unvisited = new ArrayList<URI>();
	}

	/**
	 * Returns the set of URIs that this crawler has attempted to visit
	 * (successfully or not).
	 * 
	 * @return the set of URIs that this crawler has attempted to visit
	 */
	public Set<URI> getVistedUris() {
		return visited.keySet();
	}

	/**
	 * Returns the set of RetrievedDocuments corresponding to the URIs this crawler
	 * has successfully visited.
	 * 
	 * @return the set of RetrievedDocuments corresponding to the URIs this crawler
	 *         has successfully visited
	 */
	public Set<RetrievedDocument> getVisitedDocuments() {
		return new HashSet<RetrievedDocument>(visited.values());
	}

	/**
	 * Adds a URI to the collections of URIs that this crawler should attempt to
	 * visit. Does not visit the URI.
	 * 
	 * @param uri the URI to be visited (later!)
	 */
	public void addUri(URI uri) {
		unvisited.add(uri);
	}

	/**
	 * Attempts to visit a single as-yet unattempted URI in this crawler's
	 * collection of to-be-visited URIs.
	 * 
	 * Visiting a document entails parsing the text and links from the URI.
	 * 
	 * If the parse succeeds:
	 * 
	 * - The "file:" links should be added to this crawler's collection of
	 * to-be-visited URIs.
	 * 
	 * - A new RetrievedDocument should be added to this crawler's collection of
	 * successfully visited documents.
	 * 
	 * If the parse fails, this method considers the visit attempted but
	 * unsuccessful.
	 * 
	 * @throws MaximumVisitsExceededException if this crawler has already attempted
	 *                                        to visit its quota of visits
	 * @throws NoUnvisitedUrisException       if no more unattempted URI remain in
	 *                                        this crawler's collection of URIs to
	 *                                        visit
	 */
	public void visitOne() throws MaximumVisitsExceededException, NoUnvisitedUrisException {
		if (unvisited.isEmpty()) throw new NoUnvisitedUrisException();
		if (MAXIMUM_VISITS == visitTrials) throw new MaximumVisitsExceededException();
		
		visitTrials++;
		URI top = unvisited.remove(0);
		Document uriDocument = CrawlerUtils.parse(top);
		
		if (uriDocument == null) return;
		
		String documentText = uriDocument.text();
		List<URI> listOfURIs = new ArrayList<URI>(CrawlerUtils.getFileUriLinks(uriDocument));
		RetrievedDocument retrievedDoc = new RetrievedDocument(top, documentText, listOfURIs);
		
		visited.put(top, retrievedDoc);
		
		for (URI entry : listOfURIs) addUri(entry);
	}

	/**
	 * Attempts to visit all URIs in this crawler (and any URIs they reference, and
	 * so on).
	 * 
	 * This method will not raise a MaximumVisitsExceededException if there are more
	 * URIs than can be visited. It will instead stop once the UriCrawler's quota
	 * has been reached.
	 */
	public void visitAll() {
		while ((visitTrials != MAXIMUM_VISITS) && !unvisited.isEmpty()) {
			visitTrials++;
			URI nextURI = unvisited.remove(0);
			Document nextDoc = CrawlerUtils.parse(nextURI);
			
			if (nextDoc == null) return;
			
			String t = nextDoc.text();
			List<URI> listOfURIs = new ArrayList<URI>(CrawlerUtils.getFileUriLinks(nextDoc));
			RetrievedDocument retrievedDocument = new RetrievedDocument(nextURI, t, listOfURIs);
			
			visited.put(nextURI, retrievedDocument);
			
			for (URI entry : listOfURIs) addUri(entry);
		}
	}
}
