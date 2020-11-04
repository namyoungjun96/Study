
public class Stack {
	static int size=500;
	
	static int[] str=new int[size];
	static int top=0;
	
	public static void main(String[] args) {
		push(1);
		push(2);
		push(3);
		
		System.out.println(pop());
		System.out.println(pop());
		System.out.println(pop());
	}
	
	static int push(int n) {
		if(top>=size)
			return -1;
		str[top++]=n;
		
		return 0;
	}
	
	static int pop() {
		if(top<=0)
			return -1;
		
		return str[--top];
	}
}
