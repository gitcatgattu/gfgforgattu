<h2><a href="https://www.geeksforgeeks.org/problems/equilibrium-point-1587115620/1?page=1&company=Amazon&sprint=a663236c31453b969852f9ea22507634&sprint=a663236c31453b969852f9ea22507634&sortBy=submissions">Equilibrium Point</a></h2><h3>Difficulty Level : Easy</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given an array<strong> A </strong>of <strong>n</strong> non negative numbers. The task is to find the first <strong>equilibrium point</strong> in an array. Equilibrium point in an array is an index (or position) such that the <strong>sum</strong> of all elements <strong>before </strong>that index is <strong>same</strong> as <strong>sum </strong>of elements <strong>after </strong>it.</span></p>
<p><strong><span style="font-size: 18px;">Note:</span></strong><span style="font-size: 18px;"> Return e</span><span style="font-size: 18px;">quilibrium point in 1-based indexing.</span><span style="font-size: 18px;">&nbsp;Return -1 if no such point exists.&nbsp;</span></p>
<p><span style="font-size: 18px;"><strong>Example 1:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: 
</strong>n = 5 
A[] = {1,3,5,2,2} 
<strong>Output: <br></strong>3<strong> 
Explanation: </strong> 
equilibrium point is at position 3 as sum of elements before it (1+3) = sum of elements after it (2+2).<strong> </strong></span>
</pre>
<p><span style="font-size: 18px;"><strong>Example 2:</strong></span></p>
<pre><span style="font-size: 14pt;"><strong>Input:
</strong></span><span style="font-size: 18px;">n = 1
A[] = {1}
<strong>Output: <br></strong>1<strong>
Explanation:
</strong>Since there's only element hence its only the equilibrium point.</span></pre>
<p><span style="font-size: 18px;"><strong>Your&nbsp;Task:</strong><br>The task is to complete the function <strong>equilibriumPoint()</strong> which takes the array and n as input parameters and returns the point of equilibrium.&nbsp;</span></p>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity: </strong>O(n)<br><strong>Expected Auxiliary Space:</strong> O(1)</span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 &lt;= n&nbsp;&lt;= 10<sup>5</sup><br>0 &lt;= A[i] &lt;= 10<sup>9</sup></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Amazon</code>&nbsp;<code>Adobe</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>prefix-sum</code>&nbsp;<code>Arrays</code>&nbsp;<code>Data Structures</code>&nbsp;<code>Algorithms</code>&nbsp;