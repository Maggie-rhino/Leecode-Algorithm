/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[][]}
 */
var findDifference = function(nums1, nums2) {
    let set1 = new Set(nums1);
    let set2 = new Set(nums2);
    let setLeft = new Set([...set1].filter( item => !set2.has(item)));
    let setRight = new Set([...set2].filter(item => !set1.has(item)));
    return [[...setLeft],[...setRight]]
};