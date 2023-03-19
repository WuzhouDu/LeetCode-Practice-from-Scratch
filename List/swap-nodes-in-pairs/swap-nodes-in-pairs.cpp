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
    ListNode* swapPairs(ListNode* head) {
        if (head == nullptr || head->next == nullptr) return head;
        ListNode* dummyHead = new ListNode(0, head);
        ListNode* current = head;
        ListNode* previous = dummyHead;
        ListNode* temp;
        ListNode* next;
        while (current != nullptr){
            next = current->next;
            if (next != nullptr) temp = next->next;
            else{
                return dummyHead->next;
            } 
            next->next = current;
            current->next = temp;
            previous->next = next;
            previous = current;
            current = temp;
        }
        return dummyHead->next;
    }
};