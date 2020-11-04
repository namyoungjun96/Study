
public class MergeSort {
	static int[]str;
	static int[]cmp;

	public static void main(String[] args) {
		str=new int[]{3, 5, 7, 1, 3, 5, 9, 2};
		cmp=new int[str.length];
		
		printArray(str);
		merge(0, str.length-1);
		printArray(str);
	}

	static void merge(int start, int end) {
		if (start<end) {
			int mid = (start+end) / 2;
			merge(start, mid);
			merge(mid+1, end);

			int p = start;
			int q = mid + 1;
			int idx = p;

			while (p<=mid || q<=end) {
				if (q>end || (p<=mid && str[p]<str[q])) {
					cmp[idx++] = str[p++]; 
				} else {
					cmp[idx++] = str[q++]; 
				} 
			} 
			for (int i=start;i<=end;i++) {
				str[i]=cmp[i]; 
			} 
		}
	}
	
	public static void printArray(int[] a) {
		for (int i=0;i<a.length;i++) 
			System.out.print(a[i]+" "); 
		System.out.println(); 
		}
}
