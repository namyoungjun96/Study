import java.util.Scanner;

public class Match {
	int count;

	void match(int[][] ladder) {
		Scanner sc=new Scanner(System.in);
		
		for(int i=1; i<ladder.length-1; i++) {
			for(int j=0; j<ladder[i].length; j++) {
				System.out.print(ladder[i][j]+" ");
			}
			System.out.println();
		}

		/*while(true) {
			System.out.print("몇 번을 원하시나요 ? : ");

			count=sc.nextInt();

			for(int i=0; i<ladder.length; i++) {
				try {
					if(ladder[i][count]==0) {
						System.out.println("("+(i+1)+" ,"+(count+1)+")");
						continue;
					}

					else if((ladder[i][count]+ladder[i][count+1])==2) {
						System.out.println("("+(i+1)+" ,"+(count+1)+")");
						count++;
					}
					else {
						System.out.println("("+(i+1)+" ,"+(count+1)+")");
						count--;
					}
				} catch(Exception e){
					if(ladder[i][count]-ladder[i][count-1]==0) {
						System.out.println("("+(i+1)+" ,"+(count+1)+")");
						count--;
					}
					else {
						continue;
					}
				}
			}
		}*/

		sc.close();
	}
}
