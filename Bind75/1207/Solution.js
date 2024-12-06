/**
 * @param {number[]} arr
 * @return {boolean}
 */
var uniqueOccurrences = function(arr) {
    let flag =true;
    // step 1
    let cntMap = new Map();
    for(let i=0;i<arr.length;i++){
        k = arr[i];
        v=1;
        if(cntMap.has(k)){
            v= cntMap.get(k) +1;
        }
        cntMap.set(k,v);
    }

    // step 2 :
    let set = new Set(cntMap.values());
    if(set.size < cntMap.size){
        flag=false;
    }
    return flag;
};