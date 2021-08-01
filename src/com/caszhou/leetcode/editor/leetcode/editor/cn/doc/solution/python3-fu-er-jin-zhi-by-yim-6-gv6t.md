### 解题思路
1. 思路
    - Python3中的除法是`向下取整`。示例：`3/-2=-1.5` 向下取整为`-2`，所以`3//-2=-2`
    - 转换公式：`N,mod=-(N>>1),N%2`

### 代码

```python3
class Solution:
    def baseNeg2(self, N: int) -> str:
        res=""
        while N:
            N,mod=-(N>>1),N%2
            res=str(mod)+res
        return res if res else "0"
```