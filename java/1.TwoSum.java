#1.https://leetcode.com/problems/two-sum/
class Solution {
    public int[] twoSum(int[] nums, int target) {
      HashMap<Integer, Integer> Parul = new HashMap<>();
      for ( int i=0; i < nums.length; i++) {
	    if(Parul.containsKey(target - nums[i])) {
		    // int D = Parul.get(target - nums[i]);
		    return new int[] {Parul.get(target - nums[i]), i};
	    }
	    Parul.put(nums[i],i);

        }
    throw new IllegalArgumentException("No two sum solution");
    }
}