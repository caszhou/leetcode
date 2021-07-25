# 假设Andy和Doris想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。 
# 
#  你需要帮助他们用最少的索引和找出他们共同喜爱的餐厅。 如果答案不止一个，则输出所有答案并且不考虑顺序。 你可以假设总是存在一个答案。 
# 
#  示例 1: 
# 
#  输入:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
# 输出: ["Shogun"]
# 解释: 他们唯一共同喜爱的餐厅是“Shogun”。
#  
# 
#  示例 2: 
# 
#  输入:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["KFC", "Shogun", "Burger King"]
# 输出: ["Shogun"]
# 解释: 他们共同喜爱且具有最小索引和的餐厅是“Shogun”，它有最小的索引和1(0+1)。
#  
# 
#  提示: 
# 
#  
#  两个列表的长度范围都在 [1, 1000]内。 
#  两个列表中的字符串的长度将在[1，30]的范围内。 
#  下标从0开始，到列表的长度减1。 
#  两个列表都没有重复的元素。 
#  
#  Related Topics 数组 哈希表 字符串 👍 112 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        list1_rest_index_dic = dict()
        for index1, item1 in enumerate(list1):
            list1_rest_index_dic[item1] = index1

        min_index_sum = None
        result = []
        for index2, item2 in enumerate(list2):
            if item2 in list1_rest_index_dic:
                index_sum = list1_rest_index_dic[item2] + index2

                if min_index_sum is None or index_sum < min_index_sum:
                    min_index_sum = index_sum
                    result = [item2]
                elif index_sum == min_index_sum:
                    result.append(item2)

        return result
# leetcode submit region end(Prohibit modification and deletion)
