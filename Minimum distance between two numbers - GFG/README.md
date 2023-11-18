# Minimum distance between two numbers
## Easy
<div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">You are given an&nbsp;array <strong>a</strong>, of <strong>n</strong> elements. Find the <strong>minimum </strong>index based distance between two distinct elements of the array, <strong>x</strong> and <strong>y</strong>. Return -1, if either <strong>x </strong>or <strong>y </strong>does not exist in the array.</span></p>
<p><span style="font-size: 18px;"><strong>Example 1:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:
</strong>N = 4
A[] = {1,2,3,2}
x = 1, y = 2
<strong>Output: </strong>1<strong>
Explanation: </strong>x = 1 and y = 2. There are
two distances between x&nbsp;and y, which are
1 and 3 out of which the least&nbsp;is 1.</span>
</pre>
<p><span style="font-size: 18px;"><strong>Example 2:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:
</strong>N = 7
A[] = {86,39,90,67,84,66,62}
x = 42, y = 12
<strong>Output: </strong>-1<strong>
Explanation: </strong>x = 42 and y = 12. We return
-1 as&nbsp;x and y don't exist in the array.</span></pre>
<p><strong><span style="font-size: 18px;">Your Task:</span></strong><br><span style="font-size: 18px;">Complete the function <strong>minDist()&nbsp;</strong>which takes the array <strong>a</strong>, and 3 integers <strong>n, x </strong>and <strong>y </strong>as input parameters and&nbsp;returns&nbsp;the <strong>minimum </strong>distance between&nbsp;<strong>x and y</strong> in the array.&nbsp;</span><span style="font-size: 18px;">Return -1, if either </span><strong style="font-size: 18px;">x&nbsp;</strong><span style="font-size: 18px;">or&nbsp;</span><strong style="font-size: 18px;">y&nbsp;</strong><span style="font-size: 18px;">does not exist in the array.</span></p>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity:</strong> O(N)<br><strong>Expected Auxiliary Space:</strong> O(1)</span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 &lt;= n &lt;= 10<sup>5</sup><br>0 &lt;= a[i], x, y &lt;= 10<sup>5<br></sup></span><span style="font-size: 18px;">x != y</span></p></div>