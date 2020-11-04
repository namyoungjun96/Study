
public class Recursion {
	public static void main(String[] args) {
		recursive(5);
	}
	
	static void recursion(int n){
		if(n==0)
			return;
		else {
			System.out.println("¹Ý°©½À´Ï´Ù");
			
			recursion(n-1);
		}
	}
	
	static int mul(int n) {
		if(n==1)
			return 1;
		else
			return n+mul(n-1);
	}
	
	public static int recursive(int n) {
        int i;
        System.out.println(n);
        if (n < 1)    return 2;
        else {
            i = (2 * recursive(n - 1)) + 1;
            System.out.printf("%d\n", i);
            return i;
        }
    }
}
