package codingtest.company;

public abstract class GetLogInfo {
	private String name;
	private int count;
	
	public GetLogInfo(String name, int count) {
		this.name = name;
		this.count = count;
	}
	
	String getName() {
		return name;
	}
	
	int getCount() {
		return count;
	}
	
	void plusCount() {
		this.count ++;
	}
}
