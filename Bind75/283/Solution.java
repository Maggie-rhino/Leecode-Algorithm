class Solution {
    public void moveZeroes(int[] nums) {
        // one var to record the number of zero
        // the other var to record the current insert idx
        int numsZero =0;
        int idxInsert =0;
        int l = nums.length;
        for(int i=0;i<l;i++){
            int current = nums[i];
            System.out.println(current);
            if (current==0){
                numsZero++;
            }else{
                nums[idxInsert] =current;
                idxInsert++;
            }  
            if ((numsZero + idxInsert)>=l){
                break;
            }
        }
        if(numsZero>0){
            for(int j =idxInsert;j<l;j++){
                nums[j]=0;
            }
        }
    }
}