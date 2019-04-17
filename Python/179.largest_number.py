    """
    More explanation

    1-we define a function that compares two string (a,b) . we consider a bigger than b if a+b>b+a
    for example : (a="2",b="11") a is bigger than b because "211" >"112"

    2-convert all elements of the list from int to string

    3-sort the list descendingly using the comparing function we defined
    for example sorting this list ["2","11","13"] using the function defined in step 1 would produce ["2","13","11"]

    4-we concatatenate the list "21311"
    """
from functools import cmp_to_key
class Solution:
    """
    对于两个数字a和b来说，如果将其都转为字符串，如果ab > ba，则a排在前面，比如9和34，由于934>349，所以9排在前面，再比如说30和3，由于303<330，所以3排在30的前面。按照这种规则对原数组进行排序后，将每个数字转化为字符串再连接起来就是最终结果。
    """
    def largestNumber(self, nums: List[int]) -> str:
        comp = lambda a, b: 1 if a + b < b + a else -1 if a + b > b + a else 0
        largest_num = ''.join(sorted(map(str, nums), key=cmp_to_key(comp)))
        return '0' if largest_num[0] == '0' else largest_num
