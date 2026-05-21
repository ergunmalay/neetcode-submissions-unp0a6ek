class Solution {
    public int[] getConcatenation(int[] nums) {
        int[] ars = new int[nums.length * 2];

        for (int i = 0; i < nums.length; i++) {
            ars[i] = nums[i];
            ars[i + nums.length] = nums[i];
        }

        return ars; 
    }
}