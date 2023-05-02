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
    vector<int> answer;
    int pre = INT_MIN;
    int frequency = 0;
    int max = 0;

    void traverse(TreeNode* root) {
        if (!root) return;
        traverse(root->left);
        if (pre == INT_MIN) {
            pre = root->val;
            frequency = 1;
            max = 1;
            answer.push_back(root->val);
        }
        else if (root->val == pre) {
            frequency++;
            if (frequency == max) {
                answer.push_back(root->val);
            }
            else if (frequency > max) {
                answer.clear();
                answer.push_back(root->val);
                max = frequency;
            }
        }
        else {
            frequency = 1;
            pre = root->val;
            if (frequency == max) {
                answer.push_back(root->val);
            }
        }
        traverse(root->right);
    }

    vector<int> findMode(TreeNode* root) {
        traverse(root);
        return answer;
    }
};