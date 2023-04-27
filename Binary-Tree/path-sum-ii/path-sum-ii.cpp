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
    void traverse(vector<int> &path, TreeNode* cur, int targetSum, vector<vector<int>> &result){
        if (!cur) return;
        path.push_back(cur->val);
        if (!cur->left && !cur->right){
            if (targetSum == cur->val) result.push_back(path);
        }
        else{
            if (cur->left){
                traverse(path, cur->left, targetSum - cur->val, result);
                path.pop_back();
            }
            if (cur->right){
                traverse(path, cur->right, targetSum - cur->val, result);
                path.pop_back();      
            }
      
        }

    }

    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<vector<int>> result;
        vector<int> path;
        if (!root) return result;
        traverse(path, root, targetSum, result);
        return result;
    }
};