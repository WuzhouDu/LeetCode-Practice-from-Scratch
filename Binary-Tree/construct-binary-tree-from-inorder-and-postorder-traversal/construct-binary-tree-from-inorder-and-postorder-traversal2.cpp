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
    unordered_map<int, int> map;

    TreeNode* establish(int in_begin, int in_end, int post_begin, int post_end, vector<int>& inorder, vector<int>& postorder) {
        if (in_begin > in_end) return nullptr;
        int pivot = postorder[post_end];
        int left_index = map[pivot];
        TreeNode* newNode = new TreeNode(pivot);
        int left_in_begin = in_begin;
        int left_in_end = left_index-1;
        int left_post_begin = post_begin;
        int left_post_end = post_begin + left_index-1 - in_begin;
        newNode->left = establish(left_in_begin, left_in_end, left_post_begin, left_post_end, inorder, postorder);

        int right_in_begin = left_index+1;
        int right_in_end = in_end;
        int right_post_begin = left_post_end + 1;
        int right_post_end = post_end-1;
        newNode->right = establish(right_in_begin, right_in_end, right_post_begin, right_post_end, inorder, postorder);
        return newNode;
    }

    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        for (int i = 0; i < inorder.size(); ++i){
            map[inorder[i]] = i;
        }
        return establish(0, inorder.size()-1, 0, postorder.size()-1, inorder, postorder);
    }
};