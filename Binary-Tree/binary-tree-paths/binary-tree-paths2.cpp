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
    void traverse (TreeNode* cur, string path, vector<string>& result){
        if (cur == nullptr) return;
        path += to_string(cur->val);
        if (!cur->left && !cur->right) {
            result.push_back(path);
            return;
        }
        path += "->";
        if (cur->left) {
            traverse(cur->left, path, result);
        }
        if (cur->right){
            traverse(cur->right, path, result);
        }
    }


    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> result;
        string path = "";
        traverse(root, path, result);
        return result;
    }
};