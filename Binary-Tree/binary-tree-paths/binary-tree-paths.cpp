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
    void traverse (TreeNode* cur, vector<int>& path, vector<string>& result){
        if (cur == nullptr) return;
        path.push_back(cur->val);
        if (!cur->left && !cur->right) {
            string temp;
            for (int i = 0; i < path.size()-1; i++){
                temp += to_string(path[i]);
                temp += "->";
            }
            temp += to_string(cur->val);
            result.push_back(temp);
            return;
        }
        if (cur->left) {
            traverse(cur->left, path, result);
            path.pop_back();
        }
        if (cur->right){
            traverse(cur->right, path, result);
            path.pop_back();
        }
    }


    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> result;
        vector<int> path;
        traverse(root, path, result);
        return result;
    }
};