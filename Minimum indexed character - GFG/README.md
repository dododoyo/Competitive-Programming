# Minimum indexed character
## Easy
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a string&nbsp;<strong>str</strong>&nbsp;and another string&nbsp;<strong>patt</strong>. Find the minimum index of the character in <strong>str&nbsp;</strong>that is also present in&nbsp;<strong>patt</strong>.</span></p>

<p><br>
<span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>str = geeksforgeeks
patt = set
<strong>Output: </strong>1<strong>
Explanation: </strong>e is the character which is
present in given str "geeksforgeeks"
and is also presen in patt "set". Minimum
index of e is 1. </span>
</pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>str = adcffaet
patt = onkl
<strong>Output: </strong>-1<strong>
Explanation: </strong>There are none of the
characters which is common in patt
and str.</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:</strong><br>
You only need to complete the function <strong>minIndexChar()&nbsp;</strong>that returns&nbsp;the index of answer in str or returns -1&nbsp;in case no character of patt is present in str.</span></p>

<p><br>
<span style="font-size:18px"><strong>Expected Time Complexity:&nbsp;</strong>O(N).<br>
<strong>Expected Auxiliary Space:&nbsp;</strong>O(Number of distinct characters).</span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ |str|,|patt|&nbsp;≤ 10<sup>5&nbsp;</sup><br>
'a' &lt;= str<sub>i</sub>, patt<sub>i</sub>&nbsp;&lt;= 'z'</span></p>
</div>