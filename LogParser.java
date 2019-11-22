/*
 * Submission by Xavier Wrenn (Student).
 * Copyright 2017 Marc Liberatore (Instructor).
 */

package log;

import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.Reader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Hashtable;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;

import com.opencsv.CSVReader;

public class LogParser {
	/**
	 * Returns a list of SuspectEntries corresponding to the CSV data supplied by
	 * the given Reader.
	 * 
	 * The data contains one or more lines of the format:
	 * 
	 * Marc,413-545-3061,1234567890
	 * 
	 * representing a name, phone number, and passport number.
	 * 
	 * @param r
	 *            an open Reader object
	 * @return a list of SuspectEntries
	 * @throws IOException
	 */
	public static List<SuspectEntry> parseLog(Reader r) throws IOException {
		List<SuspectEntry> suspects = new ArrayList<>();
		CSVReader reader = new CSVReader(r);
		String[] ln;
		while ((ln = reader.readNext()) != null) {
			SuspectEntry next = new SuspectEntry(ln[0], ln[1], ln[2]);
			suspects.add(next);
		}
		reader.close();
		return suspects;
	}

	/**
	 * Returns a sorted list of SuspectEntries whose passport numbers are common to
	 * all of the supplied entryLists.
	 * 
	 * The list is sorted lexicographically by passport number, breaking ties by
	 * name and then by phone number.
	 * 
	 * @param entryLists
	 *            a list of lists of SuspectEntries
	 * @return a sorted list of SuspectEntries whose passport numbers are common to
	 *         all of the supplied entryLists
	 */
	public static List<SuspectEntry> findCommonEntries(List<List<SuspectEntry>> entryLists) throws IllegalArgumentException {		
		if (entryLists.size() < 2) return new ArrayList<>();
		List<SuspectEntry> list = new ArrayList<SuspectEntry>();
		Set<SuspectEntry> set = new HashSet();

		HashMap<Integer, LinkedList<SuspectEntry>> map = new HashMap<Integer, LinkedList<SuspectEntry>>();
		set.addAll(entryLists.get(0));


		for (List<SuspectEntry> aList : entryLists) {
			set.retainAll(aList);
		}

		//		for (int i = 1; i < entryLists.size(); i++) {
		//			set.retainAll(entryLists.get(i));
		//		}





		list.addAll(set);

		for (List<SuspectEntry> aList : entryLists) {
			for (SuspectEntry person : aList) {
				if (!list.isEmpty())
					if (list.get(0).getPassportNumber().equals(person.getPassportNumber())) {
						list.add(person);
					}
			}
		}

		for (int i = 0; i < list.size()-1; i++) {
			if(list.get(i).getName().equals(list.get(i+1).getName())){
				list.remove(i+1);
			}
			if (list.get(i).getName().equals(list.get(i+1).getName())) {
				list.remove(i+1);
			}
		}


		list.sort(null);
		return list;

		//Set<SuspectEntry> duplicateIndividuals = new HashSet<SuspectEntry>();

		//		duplicateIndividuals.addAll(entryLists.get(0));
		//		duplicateIndividuals.retainAll(entryLists.get(1));
		//		
		//		double large = 0000000000000.0;
		//		double small = 9999999999999.0;
		//
		//		
		//		for (SuspectEntry personFrom0 : duplicateIndividuals) {
		//			if (personFrom0.hashDouble() > large)
		//				small = personFrom0.hashDouble();
		//			if (personFrom0.hashDouble() < small)				
		//				large = personFrom0.hashDouble();
		//			table.put(personFrom0.hashDouble(), new ArrayList<SuspectEntry>());
		//			table.get(personFrom0.hashDouble()).add(personFrom0);
		//		}
		//
		//		for (List<SuspectEntry> aList : entryLists) {
		//			for (SuspectEntry person : aList) {
		//				if (person.hashDouble() < small || person.hashDouble() > large)
		//					continue;
		//				if (table.containsKey(person.hashDouble()))
		//					table.get(person.hashDouble()).add(person);
		//			}
		//		}
		//		
		//		


	}

	public static void main(String[] args) {
		try {
			List<List<SuspectEntry>> listOfListsOfPeople = Arrays.asList(
					LogParser.parseLog(new FileReader("test" + File.separator + "log" + File.separator + "data0.csv")),
					LogParser.parseLog(new FileReader("test" + File.separator + "log" + File.separator + "data1.csv")),
					LogParser.parseLog(new FileReader("test" + File.separator + "log" + File.separator + "data2.csv")),
					LogParser.parseLog(new FileReader("test" + File.separator + "log" + File.separator + "data3.csv")),
					LogParser.parseLog(new FileReader("test" + File.separator + "log" + File.separator + "data4.csv")));

			List<SuspectEntry> sketchyPeople = findCommonEntries(listOfListsOfPeople);

			for (SuspectEntry sketchyPerson : sketchyPeople) {
				System.out.format("%-20s%-20s%-20s\n", sketchyPerson.getName(), sketchyPerson.getPhoneNumber(), sketchyPerson.getPassportNumber());
			}
			//System.out.println("...done");

		} catch (IOException e) {
			System.out.println("well dayum dawg");
			e.printStackTrace();
		}
	}

}
