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
    bool isSymmetric(TreeNode* root) {
        queue<TreeNode*> q;
        stack<TreeNode*> stk;
        q.push(root);
        if (root == nullptr) return true;
        if (root->left == nullptr && root->right == nullptr) return true;
        while (!q.empty()){
            int size = q.size();
            if (size%2 != 0 && size != 1) return false;
            for (int i = 0; i < size; i++){
                TreeNode* cur = q.front();
                q.pop();
                if (cur->left) q.push(cur->left);
                if (cur->right) q.push(cur->right);
                if (size == 1){
                    if (cur->left == nullptr) return false;
                    if (cur->right == nullptr) return false;
                    if (cur->left->val != cur->right->val) return false;
                    break;
                }
                if (i < size/2){
                    stk.push(cur->left);
                    stk.push(cur->right);                    
                }
                else{
                    if (cur->left == nullptr){
                        if (stk.top() == nullptr) stk.pop();
                        else return false;
                    }
                    else if (stk.top() != nullptr) {
                        if (cur->left->val == stk.top()->val) stk.pop();
                        else return false;
                    }
                    else return false;
                    if (cur->right == nullptr){
                        if (stk.top() == nullptr) stk.pop();
                        else return false;
                    }
                    else if (stk.top() != nullptr) {
                        if (cur->right->val == stk.top()->val) stk.pop();
                        else return false;
                    }
                    else return false;
                }
            }
            if (!stk.empty()) return false;
        }
        return true;
    }
};