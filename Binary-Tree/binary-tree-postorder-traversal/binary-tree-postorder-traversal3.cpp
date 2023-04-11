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
        vector<int> result;
        stack<TreeNode*> stk;
        TreeNode* cur = root;
        if (cur == nullptr) return result;
        stk.push(cur);
        while (!stk.empty()){
            cur = stk.top();
            stk.pop();
            if (cur == nullptr){
                cur = stk.top();
                stk.pop();
                result.push_back(cur->val);
            }
            else{
                stk.push(cur);
                stk.push(nullptr);
                if (cur->right != nullptr) stk.push(cur->right);
                if (cur->left != nullptr) stk.push(cur->left);
            }
        }
        return result;
    }
};