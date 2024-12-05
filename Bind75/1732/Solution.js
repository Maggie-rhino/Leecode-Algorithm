/**
 * @param {number[]} gain
 * @return {number}
 */
var largestAltitude = function(gain) {
    let highestAltitude =0;
    let current =0;
    for(let i =0;i< gain.length;i++){
        current +=gain[i];
        highestAltitude =Math.max(highestAltitude,current);
    }
    return highestAltitude;
};