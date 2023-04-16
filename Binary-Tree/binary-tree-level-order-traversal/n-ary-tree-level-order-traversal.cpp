/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<vector<int>> levelOrder(Node* root) {
        queue<Node*> q;
        vector<vector<int>> result;
        if (root == nullptr) {
            return result;
        }
        q.push(root);
        result.push_back(vector<int>{root->val});
        while (!q.empty()){
            q.push(nullptr);
            Node* cur = q.front();
            vector<int> temp;
            while (cur != nullptr){
                for (int i = 0; i < cur->children.size(); i++){
                    q.push(cur->children[i]);
                    temp.push_back(cur->children[i]->val);
                }
                q.pop();
                cur = q.front();
            }
            if (!temp.empty()) result.push_back(temp);
            q.pop();
        }
        return result;
    }
};