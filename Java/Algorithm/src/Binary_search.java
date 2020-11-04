import java.util.Scanner;

public class Binary_search {
	public static void main(String[] args) {
		int[] a= {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
		int n=0;
		
		Scanner sc=new Scanner(System.in);
		
		System.out.print("찾으실 수를 입력하세요 : ");
		n=sc.nextInt();
		
		System.out.println(solve(a, n)+"번째 수 입니다.");
		sc.close();
	}

	static int solve(int []a, int n) {
		int range;
		range=a.length/2-1;

		while(range>=1) {
			if(n==a[range]) {
				return range+1;
			}
			else if(n<a[range])
				range=range/2;
			else if(n>a[range])
				range=(a.length+range)/2;
		}

		return -1;
	}
}