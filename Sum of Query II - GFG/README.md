# Sum of Query II
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">You are given an array <strong>arr[]</strong> of <strong>n</strong> integers and <strong>q</strong> queries in an array <strong>queries[]</strong> of length <strong>2*q </strong>containing <strong>l</strong>, <strong>r</strong> pair for all q queries. You need to compute the following sum over q queries.</span></p>

<p><span style="font-size:18px">&nbsp;<img alt="" src="https://latex.codecogs.com/gif.latex?\sum_{i=l}^{r}arr[i]"></span></p>

<p><span style="font-size:18px">Array is 0-Indexed.</span></p>

<p><strong><span style="font-size:18px">Example 1:</span></strong></p>

<pre><span style="font-size:18px"><strong>Input:</strong> n = 4
arr = {1, 2, 3, 4}
q = 2
queries = {1, 4, 2, 3}
<strong>Output:</strong> 10 5
<strong>Explaination:</strong> In the first query we need sum 
from 1 to 4 which is 1+2+3+4 = 10. In the 
second query we need sum from 2 to 3 which is 
2 + 3 = 5.</span></pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You do not need to read input or print anything. Your task is to complete the function <strong>querySum()</strong> which takes n, arr, q and queries as input parameters and returns the answer for all the queries.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(n+q)<br>
<strong>Expected Auxiliary Space:</strong> O(n)</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ n, q ≤ 1000<br>
1 ≤ arr<sub>i</sub>&nbsp;≤ 10<sup>6</sup><br>
1 ≤ l ≤ r ≤ n</span></p>
</div>