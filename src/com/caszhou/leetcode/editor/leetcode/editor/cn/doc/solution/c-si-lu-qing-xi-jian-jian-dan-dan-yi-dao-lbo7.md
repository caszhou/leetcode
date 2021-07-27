### 解题思路
理解一下题意，就是两个全排列的相乘，主要需要判断一下n里面到底包含多少质数。因为给定了范围，就直接百度100以内的质数有哪些硬编码进去了。

### 代码

```cpp
class Solution {
public:
    int numPrimeArrangements(int n) {
        vector<int> mark ={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97};
        int num = 0;//包含质数的个数 最终结果num！*(n-num)!
        for(int i:mark)
        {
            if(i<=n)    num++;
        }
        long long ret = 1;
        for(int i = 1;i<=num;i++)
        {
            if(ret>1000000007) ret%=1000000007;
            ret *=i;
        }
        for(int i = 1;i<=n-num;i++)
        {
            if(ret>1000000007) ret%=1000000007;
            ret *=i;
        }
        ret%=1000000007;
        return static_cast<int>(ret);
    }
};
```