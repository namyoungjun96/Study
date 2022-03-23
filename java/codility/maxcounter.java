/* 
코딜리티 레벨4
7분
77퍼
*/

class Solution {
    public int[] solution(int N, int[] A) {
        int[] answer = new int[N];
        int max = 0;

        for(int i=0; i<A.length; i++){
            if(A[i] <= N){
                answer[A[i]-1] += 1;

                if(max < answer[A[i]-1])
                    max = answer[A[i]-1];
            }
            else{
                for(int j=0; j<N; j++){
                    answer[j] = max;
                }
            }
        }

        return answer;
    }
}