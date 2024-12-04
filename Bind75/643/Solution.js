/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function(nums, k) {
    let sumMax = -Infinity;
    let l = nums.length;
    let current =0
    for(let i =0;i<l;i++){
        if(i<k){
            current +=nums[i];
        }else{
            current = current-nums[i-k] +nums[i];
        }
        if (i>=k-1){
            sumMax = Math.max(sumMax,current);
        }
    }
    return sumMax/k;
};