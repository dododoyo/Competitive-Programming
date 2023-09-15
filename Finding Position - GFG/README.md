# Finding Position
## Easy
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Some people(n) are standing in a queue. A selection process follows a rule where people standing on even positions&nbsp;are selected. Of the selected people a queue is formed and again out&nbsp;of these only&nbsp;people on even position&nbsp;are selected. This continues until we are left with one person.&nbsp;Find out the position of that person in the original queue.<br>
<br>
<strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input</strong>: n = 5
<strong>Output:</strong>&nbsp;4&nbsp;
<strong>Explanation</strong>: 1,2,3,4,5 -&gt; 2,4 -&gt; 4.</span>
</pre>

<p><br>
<span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>n = 9
<strong>Output:&nbsp;</strong>8
<strong>Explanation</strong>: 1,2,3,4,5,6,7,8,9
-&gt;2,4,6,8 -&gt; 4,8 -&gt; 8. </span>
</pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:&nbsp;&nbsp;</strong><br>
You dont need to read input or print anything. Complete the function <strong>nthPosition()&nbsp;</strong>which takes n&nbsp;as input parameter and returns the position(original queue) of that person who is left.</span><br>
<br>
<span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(logn)<br>
<strong>Expected Auxiliary Space:</strong> O(1)<br>
<br>
<strong>Constraints:</strong><br>
1&lt;= n&nbsp;&lt;=10<sup>8</sup></span></p>
</div>