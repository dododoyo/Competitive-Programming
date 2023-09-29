# Maximum Width of Tree
## Easy
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a Binary Tree, find the maximum width of it.&nbsp;<strong>Maximum width </strong>is defined as the maximum number of nodes at any level.<br>
For example, the maximum width of the following tree is 4 as there are 4 nodes at the 3<sup>rd</sup> level.</span></p>

<p><span style="font-size:18px">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; /&nbsp;&nbsp;&nbsp;&nbsp; \<br>
&nbsp;&nbsp;&nbsp;&nbsp; 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3<br>
&nbsp;&nbsp; /&nbsp;&nbsp;&nbsp; \ &nbsp;&nbsp; /&nbsp;&nbsp;&nbsp; \<br>
&nbsp; 4&nbsp;&nbsp;&nbsp; 5&nbsp;&nbsp; 6&nbsp;&nbsp;&nbsp; 7<br>
&nbsp;&nbsp;&nbsp; \<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 8</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1
 &nbsp;&nbsp;&nbsp; /&nbsp;&nbsp;&nbsp;&nbsp;\
 &nbsp; &nbsp;2&nbsp; &nbsp; &nbsp;&nbsp;3
<strong>Output: </strong>2
On the first level there is only
one node 1
On the second level there are
two nodes 2, 3 clearly it is the 
maximum number of nodes at any level</span>

</pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 10
 &nbsp;&nbsp;&nbsp;&nbsp; /&nbsp;&nbsp;&nbsp;&nbsp; \
&nbsp;&nbsp;&nbsp;&nbsp;20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 30
 &nbsp; /&nbsp;&nbsp;&nbsp;&nbsp;\
 &nbsp;40&nbsp;&nbsp;&nbsp; 60
<strong>Output: </strong>2
There is one node on level 1(10)
There is two node on level 2(20, 30)
There is two node on level 3(40, 60)
Hence the answer is 2
</span>
</pre>

<p><strong><span style="font-size:18px">Your Task:</span></strong><br>
<span style="font-size:18px">You don't have to read any input. Complete the <strong>function getMaxWidth()&nbsp;</strong>that takes the&nbsp;<strong>node </strong>as a&nbsp;<strong>parameter </strong>and <strong>returns </strong>the<strong> maximum width</strong>. The driver code does the printing.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:&nbsp;</strong>O(N).<br>
<strong>Expected Auxiliary Space:&nbsp;</strong>O(Width of the tree).</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= Number of Nodes&lt;= 10<sup>5</sup><br>
0 &lt;= nodes values &lt;= 10<sup>5</sup></span><br>
&nbsp;</p>
</div>