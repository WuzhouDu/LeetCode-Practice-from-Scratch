/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode* current = new ListNode(0);
        current->next = head;
        
        if (head == NULL) return NULL;

        while (current->next != NULL){
            if (current->next->val == val){
                if (current->next == head){
                    head = head->next;
                }
                current->next = current->next->next;
            }
            current = current->next;
        }
        return head;
    }
};