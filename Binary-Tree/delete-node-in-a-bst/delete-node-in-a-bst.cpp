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
    void help(TreeNode* left, TreeNode* right) {
        TreeNode* cur = right;
        while (cur) {
            if (left->val < cur->val) {
                if (cur->left) cur = cur->left;
                else break;
            }
            else {
                cout << "error" << endl;
            }
        }
        cur->left = left;
        return;
    }

    TreeNode* deleteNode(TreeNode* root, int key) {
        if (!root) return nullptr;
        if (root->val == key) {
            if (!root->left) return root->right;
            if (!root->right) return root->left;
            help(root->left, root->right);
            return root->right;
        }
        else {
            TreeNode* cur = root;
            TreeNode* pre = cur;
            int leftchild = true;
            while (cur) {
                if (cur->val < key) {
                    pre = cur;
                    cur = cur->right;
                    leftchild = false;
                }
                else if (cur->val > key) {
                    pre = cur;
                    cur = cur->left;
                    leftchild = true;
                }
                else {
                    if (!cur->left) {
                        if (leftchild) pre->left = cur->right;
                        else pre->right = cur->right;
                    }
                    else if (!cur->right) {
                        if (leftchild) pre->left = cur->left;
                        else pre->right = cur->left;
                    }
                    else {
                        help(cur->left, cur->right);
                        if (leftchild) pre->left = cur->right;
                        else pre->right = cur->right;                        
                    }
                    return root;
                }
            }
            return root;
        }
    }
};