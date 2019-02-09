class Solution:
    def findTarget(self, root, target):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        dictionary = set()
        return self.helper(root, target, dictionary)
        
    def helper(self, root, target, dictionary):
        if not root:
            return False
        if target - root.val in dictionary:
            return True
        dictionary.add(root.val)
        return self.helper(root.left, target, dictionary) or self.helper(root.right, target, dictionary)
