new submission with xor operation
```python
class Solution:
def singleNumber(self, nums: List[int]) -> int:
res = 0
for i in nums:res = res ^ i
return res
```