# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    rootMap = {}
    def robChildren(self, root):
        if (root):
            return self.rob(root.left) + self.rob(root.right)
        else:
            return 0
    def rob(self, root: Optional[TreeNode]) -> int:
        if (Solution.rootMap.get(root)):
            return Solution.rootMap[root]
        if (root):
            result = max(self.robChildren(root.left) + self.robChildren(root.right) + root.val, self.rob(root.left) + self.rob(root.right))
            Solution.rootMap[root] = result
            return result
        else:
            Solution.rootMap[root] = 0
            return 0
        



# class Solution:
#     def rob(self, root: Optional[TreeNode]) -> int:
#         def dfs(node: Optional[TreeNode]) -> (int, int):
#             if node is None:  # 递归边界
#                 return 0, 0  # 没有节点，怎么选都是 0
#             l_rob, l_not_rob = dfs(node.left)  # 递归左子树
#             r_rob, r_not_rob = dfs(node.right)  # 递归右子树
#             rob = l_not_rob + r_not_rob + node.val  # 选
#             not_rob = max(l_rob, l_not_rob) + max(r_rob, r_not_rob)  # 不选
#             return rob, not_rob
#         return max(dfs(root))  # 根节点选或不选的最大值