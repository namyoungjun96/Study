package net.youngjun.spring4.chap05;

public class DataCollector implements ThresholdRequired {
	
	private int threshold;
	
	@Override
	public void setThreshold(int threshold) {
		// TODO Auto-generated method stub
		this.threshold = threshold;
	}
	
	public int getThreshold() {
		return threshold;
	}

}
