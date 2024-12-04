class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double sumMax =Float.NEGATIVE_INFINITY;
        int l = nums.length;

        // init window
        double current= 0;
        for (int i =0;i<l;i++){
            if (i<k){
                current =current+nums[i];
            }else{
                current = current - nums[i-k]+nums[i];
            }
            if ( i>=k-1){
                sumMax = Math.max(current,sumMax);
            }
        }
        return sumMax/k;
    }
}