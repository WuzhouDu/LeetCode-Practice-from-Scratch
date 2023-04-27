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
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        if (postorder.empty()) return nullptr;
        if (postorder.size() == 1) return new TreeNode(postorder[0]);
        int pivot = postorder.back();
        TreeNode* newNode = new TreeNode(pivot);
        int index_inOrder;
        for (int i = 0; i < inorder.size(); i++){
            if (inorder[i] == pivot) {
                index_inOrder = i;
                break;
            }
        }
        // postorder.pop_back();
        vector<int> left_In(inorder.begin(), inorder.begin() + index_inOrder);
        vector<int> left_Post(postorder.begin(), postorder.begin() + left_In.size());
        vector<int> right_In(inorder.begin() + index_inOrder + 1, inorder.end());
        vector<int> right_Post(postorder.begin() + left_In.size(), postorder.end()-1);
        newNode->left = buildTree(left_In, left_Post);
        newNode->right = buildTree(right_In, right_Post);
        return newNode;
    }
};