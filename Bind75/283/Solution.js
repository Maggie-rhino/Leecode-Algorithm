/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let zeroNums =0;
    let insertIdx =0;
    let l = nums.length;
    for(let i=0;i<l;i++){
        let current = nums[i];
        if(current ==0){zeroNums++;}
        else{
            nums[insertIdx] =current;
            insertIdx++;
        }
        if((insertIdx + zeroNums)>=l){break;}
    }
    if(zeroNums>0){
        for(let i =insertIdx;i<l;i++){
            nums[i] =0;
        }
    }
    

};