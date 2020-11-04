import java.util.Random;

public class Draw {
	int people=0;
	int[][] ladder;

	Random ra=new Random();

	public Draw() {}

	public Draw(int people) {
		this.people=people;
		this.ladder=new int[people+2][people];
	}

	void draw() {
		for(int i=1; i<ladder.length-1; i++) {
			for(int j=0; j<ladder[i].length; j++) {
				ladder[i][j]=ra.nextInt(2);
			}
		}
		
		for(int i=1; i<ladder.length-1; i++) {
			for(int j=0; j<ladder[i].length; j++) {
				System.out.print(ladder[i][j]+" ");
			}
			System.out.println();
		}
		System.out.println("-------------");

		for(int i=1; i<ladder.length; i++) {
			for(int j=0; j<ladder[i].length; j++) {
				try {
					if((ladder[i][j-1]+ladder[i][j-2]==0||ladder[i][j-1]+ladder[i][j-2]==1)&&ladder[i-1][j]==0) 
						ladder[i][j]=1;

					else if((ladder[i][j-1]+ladder[i][j-2]==2)&&ladder[i-1][j]==1)
						ladder[i][j]=0;

					else
						continue;
				} catch(Exception e) {
					if(ladder[i][j]==1) {
						continue;
					}
					else {
						continue;
					}
				}
			}
		}
		
		Match ma=new Match();
		ma.match(ladder);
	}
}
