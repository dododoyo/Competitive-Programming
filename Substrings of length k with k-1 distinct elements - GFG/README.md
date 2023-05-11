# Substrings of length k with k-1 distinct elements
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a String<strong> S </strong>consisting only lowercase alphabets&nbsp;and an integer <strong>K</strong>. </span><span style="font-size:18px">Find the count of all substrings of length <strong>K</strong> which have exactly K-1 distinct characters. </span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>S = "abcc"
K = 2
<strong>Output:
</strong>1
<strong>Explanation:</strong>
Possible substrings of length K = 2 are
ab : 2 distinct characters
bc : 2 distinct characters
cc : 1 distinct character
Only one valid substring exists {"cc"}. </span>
</pre>

<div><span style="font-size:18px"><strong>Example 2:</strong></span></div>

<pre><span style="font-size:18px"><strong>Input:
</strong>S = "aabab"
K = 3
<strong>Output :</strong>
3</span>
<span style="font-size:18px"><strong>Explanation:</strong>
Possible substrings of length K = 3 are
aab : 2 distinct characters
aba : 2 distinct characters
bab : 2 distinct characters.
All of these Substrings are a possible answer,
so the count is 3.</span>

</pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:&nbsp;&nbsp;</strong><br>
You don't need to read input or print anything. Your task is to complete the function <strong>countOfSubstrings()</strong>&nbsp;which takes a String S and an integer K as input and returns the count of substrings of length K having K-1 distinct characters.</span></p>

<p><br>
<span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(|S|)<br>
<strong>Expected Auxiliary Space:</strong> O(constant)</span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ K&nbsp;≤ |S| ≤ 10<sup>5</sup></span></p>
</div>