/*
 * Copyright 2017 Marc Liberatore.
 */

package log;

public class SuspectEntry implements Comparable<SuspectEntry> {

	String name;
	String phoneNumber;
	String passportNumber;

	public SuspectEntry(String name, String phoneNumber, String passportNumber) {
		this.name = name.trim();
		this.phoneNumber = phoneNumber;
		this.passportNumber = passportNumber.trim();
	}

	public int compareTo(SuspectEntry other) {
		return this.getName().compareTo(other.getName());
				
	}
	
	public String toString() {
		return this.getName() + " " + this.getPhoneNumber() + " " + this.getPassportNumber();
		
	}

	public double hashDouble() {
		return Double.parseDouble(passportNumber);
	}

	public String getPassportNumber() {
		return passportNumber;
	}

	public void setPassportNumber(String passportNumber) {
		this.passportNumber = passportNumber;
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + ((passportNumber == null) ? 0 : passportNumber.hashCode());
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		SuspectEntry other = (SuspectEntry) obj;
		if (passportNumber == null) {
			if (other.passportNumber != null)
				return false;
		} else if (!passportNumber.equals(other.passportNumber))
			return false;
		return true;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getPhoneNumber() {
		return phoneNumber;
	}

	public void setPhoneNumber(String phoneNumber) {
		this.phoneNumber = phoneNumber;
	}

}
