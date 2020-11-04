package exam;

public class Array {
	public static void main(String[] args) {
		int board[][]= {
				{0, 0, 0, 0, 0}, 
				{0, 0, 1, 0, 3}, 
				{0, 2, 5, 0, 1}, 
				{4, 2, 4, 4, 2},
				{3, 5, 1, 3, 1}
		};
		int moves[]= {1, 5, 3, 5, 1, 2, 1, 4};

		Solution sol=new Solution();
		System.out.println(sol.solution(board, moves));
	}
}

class Solution {
	public int solution(int[][] board, int[] moves) {
		int answer = 0;
		int s=0;
		int a[]=new int[moves.length];

		for(int i=0; i<moves.length; i++){
			for(int j=0; j<board.length; j++){
				if(board[j][moves[i]-1]!=0){
					a[s]=board[j][moves[i]-1];
					s++;
					board[j][moves[i]-1]=0;
					break;
				}
			}
            
            if(a[0]==0)
                continue;
            
			else if(a[s-1]!=0) {
				for(int k=1; k<a.length; k++) {
					if(a[k]==0)
						break;
					else if(a[k]==a[k-1]) {
						a[k]=0;
						a[k-1]=0;
                        
						s=k-1;
						answer+=2;
					}
				}
			}
		}

		return answer;
	}
}