/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * function NestedInteger() {
 *
 *     Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     @return {boolean}
 *     this.isInteger = function() {
 *         ...
 *     };
 *
 *     Return the single integer that this NestedInteger holds, if it holds a single integer
 *     Return null if this NestedInteger holds a nested list
 *     @return {integer}
 *     this.getInteger = function() {
 *         ...
 *     };
 *
 *     Set this NestedInteger to hold a single integer equal to value.
 *     @return {void}
 *     this.setInteger = function(value) {
 *         ...
 *     };
 *
 *     Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
 *     @return {void}
 *     this.add = function(elem) {
 *         ...
 *     };
 *
 *     Return the nested list that this NestedInteger holds, if it holds a nested list
 *     Return null if this NestedInteger holds a single integer
 *     @return {NestedInteger[]}
 *     this.getList = function() {
 *         ...
 *     };
 * };
 */
/**
 * @param {NestedInteger[]} nestedList
 * @return {number}
 *
 * if 1*1+2*1+3*1+4*1+4*3+6*2 = 10 + 12 + 12 = 34
 
 [ 7,5,2,
   [6,
     [4,2,
         [5],
         [[4,
            [98]],
          10]]]
   ,[],
    [[]]
 ]
 
 */

var getDepth = function(nestedList) {
    var currList = nestedList.getList();
    var maxDepth = 1;
    for (const elem of currList) {
        if (elem.isInteger()) continue;        
        var currDepth = getDepth(elem) + 1;
        maxDepth = Math.max(maxDepth, currDepth);
    }
    
    return maxDepth;
};

var getSum = function(nestedInt, depth) {
    var sum = 0;
    for (const elem of nestedInt.getList()) {
        if (elem.isInteger()) {
            sum += depth*elem.getInteger();
        }
        else {
            sum += getSum(elem, depth - 1);
        }
    }
    return sum;
}

var depthSumInverse = function(nestedList) {
    var maxDepth = 1;
    var currDepth = 1;
    
    for (const elem of nestedList) {
        if (elem.isInteger()) continue;
        currDepth = getDepth(elem)+1;
        maxDepth = Math.max(currDepth, maxDepth);
    }
    
    var sum = 0;
    for (const elem of nestedList) {
        if (elem.isInteger()) {
            sum += maxDepth*elem.getInteger();
        }
        else {
            sum += getSum(elem, maxDepth - 1);
        }        
    }
    return sum;
};
