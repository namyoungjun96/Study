import java.util.Scanner;

public class Check {
	int people;
	
	void numcheck(){
		Scanner sc=new Scanner(System.in);
		System.out.print("몇 명을 원하시나요 ? : ");
		people=sc.nextInt();
		
		Draw dr=new Draw(people);
		dr.draw();
		
		sc.close();
	}
}
