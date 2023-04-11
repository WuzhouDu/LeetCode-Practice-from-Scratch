/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        stack<TreeNode*> stk;
        vector<int> result;
        TreeNode* cur = root;
        if (cur == nullptr) return result;
        stk.push(cur);
        while (!stk.empty()){
            cur = stk.top();
            result.push_back(cur->val);
            stk.pop();
            if (cur->left != nullptr) stk.push(cur->left);
            if (cur->right != nullptr) stk.push(cur->right);
        }
        reverse(result.begin(), result.end());
        return result;
    }
};