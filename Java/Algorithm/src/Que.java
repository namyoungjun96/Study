
public class Que {
	static int size=500;
	static int top=0;
	static int bottom=0;
	static int[] str=new int[size];
	
	public static void main(String[] args) {
		enqueue(1);
		enqueue(2);
		enqueue(3);
		
		System.out.println(dequeue());
		System.out.println(dequeue());
		System.out.println(dequeue());
		System.out.println(dequeue());
	}
	
	static int enqueue(int n) {
		if(top>=size) 
			return -1;
		str[top++]=n;
		
		return 0;
	}
	
	static int dequeue() {
		if(bottom>=top)
			return -1;
		
		return str[bottom++];
	}
}
