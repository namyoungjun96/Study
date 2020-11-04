package sort;

import java.util.*;

public class sort1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] array= {1, 5, 2, 6, 3, 7, 4};
		int[][] commands= {{2, 5, 3}, {4, 4, 1}, {1, 7, 3}};
		
		Solution sol=new Solution();
		System.out.println(sol.solution(array, commands));
	}

}

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = {};
        int[] solution = {};
        int i, j, k, z;
        
        for(int x=0; x<commands.length; x++){
            i=commands[x][0];
            j=commands[x][1];
            k=commands[x][2];
            z=0;
            
            for(int y=i-1; y<j; y++){
                solution[z]=array[y];
                z++;
            }
            
            Arrays.sort(solution);
            answer[x]=solution[k-1];
        }
        
        return answer;
    }
}