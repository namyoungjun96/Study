package codingtest.company;

public class API extends GetLogInfo {
	
	public API(String name, int count) {
		super(name, count);
	}
	
	@Override
	public String toString() {
		return super.getName() + " : " + super.getCount();
	}
}
