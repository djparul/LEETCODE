#https://leetcode.com/problems/last-stone-weight/
class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> pQueue = new PriorityQueue<Integer>(Collections.reverseOrder());
        for(int i = 0; i < stones.length; i++) {
            pQueue.add( stones[i] );
        }
        while(pQueue.size() >= 2) {
            Integer y = pQueue.poll();
            Integer x = pQueue.poll();
            if(x < y) {
                 pQueue.add(y-x);
            }
        }
        if(pQueue.isEmpty() == true) {
            return 0;    
        }
        else {
            return pQueue.peek();    
        }
    }
}