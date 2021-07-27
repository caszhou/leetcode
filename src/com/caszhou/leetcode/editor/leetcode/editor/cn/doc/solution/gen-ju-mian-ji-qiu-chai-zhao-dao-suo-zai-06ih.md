矩形的圈数为 : (num+1)/2  向上取整
当前坐标所在圈数 : 行号 , 列号 ,num-行号 ,num-列号 中最小的 +1 即为所在圈数
假设矩形如下
假设坐标 **(1,3)**
**num=5;**
![image.png](https://pic.leetcode-cn.com/1617632558-ZbmKQV-image.png)
**圈数 :**  (5+1)/2=3   
**坐标所在圈数 :** 1+1=2  在第二圈

**边长为5的正方形面积 :** 5 * 5=25
**边长为(5-2*(2(所在圈数)-1))的正方形面积** = 3 * 3 = 9;
# 红圈的面积 - 绿圈的面积
![image.png](https://pic.leetcode-cn.com/1617633704-wjdLjC-image.png)


**面积的差为 25-9=16
即当前圈之前有16个元素**

所以当前圈左上角编号为 16%9 +1 = 8

![image.png](https://pic.leetcode-cn.com/1617633171-EPFzbN-image.png)
然后就根据坐标在正方形的四个边的哪个边,来判断他的编号
**代码如下:**
```
   public int orchestraLayout(int n, int xPos, int yPos) {
        //一共几圈
        int quan=(n+1)/2;
        long num=n;
        //第几圈
        int layer = Math.min(Math.min(yPos,xPos),Math.min( n - xPos - 1, n - yPos - 1))+1;
        //总面积
        long area=num*num;
        //当前所在圈面积
        long zhong=(num-2*(layer-1));
        zhong*=zhong;
        //求差 +1 得到当前圈左上角编号
        long index=(area-zhong)%9+1;
        //右边界
        int right=n-layer;
        //左边界
        int left=layer-1;
        if(xPos==left){
            //在 --- 上
            index+=yPos-left;
        }else if(yPos==right){
            //在   |上
            index+=right-left;
            index+=xPos-left;
        }else if(xPos==right){
            //在 __ 上
            index+=2*(right-left);
            index+=right-yPos;
        }else{
            //在 |  上
            index+=3*(right-left);
            index+=right-xPos;
        }
        return (int)(index%9==0?9:index%9);
    }
```
![image.png](https://pic.leetcode-cn.com/1617633406-EHeYLC-image.png)
