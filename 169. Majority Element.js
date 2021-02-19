/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    nums.sort();
    var mod = nums[0];
    var maxCount = 1;
    var currCount = 1;
    var i;
    for (i = 0; i < nums.length + 1; i++) {
        if (i < nums.length && nums[i] === nums[i-1]) {
            currCount += 1;
        }
        else {
            if (currCount > maxCount) {
                maxCount = currCount;
                mod = nums[i-1];
            }
            currCount = 1;
        }
    }
    
    return mod;
};
