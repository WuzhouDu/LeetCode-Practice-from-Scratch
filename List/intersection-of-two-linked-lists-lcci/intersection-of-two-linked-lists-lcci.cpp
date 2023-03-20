/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        int sizeA = 0;
        int sizeB = 0;
        ListNode* dummyHeadA = new ListNode(0);
        dummyHeadA->next = headA;
        ListNode* currentA = dummyHeadA;
        ListNode* dummyHeadB = new ListNode(0);
        dummyHeadB->next = headB;
        ListNode* currentB = dummyHeadB;
        while (currentA->next != NULL){
            currentA = currentA->next;
            sizeA++;
        }
        while (currentB->next != NULL){
            currentB = currentB->next;
            sizeB++;
        }
        currentA = dummyHeadA;
        currentB = dummyHeadB;
        if (sizeA > sizeB){
            for (int i = 1; i <= sizeA - sizeB; i++){
                currentA = currentA->next;
            }
        }
        else if (sizeA < sizeB){
            for (int i = 1; i <= sizeB - sizeA; i++){
                currentB = currentB->next;
            }
        }
        
        while (currentA->next != currentB->next && currentA->next != NULL && currentB->next != NULL){
            currentA = currentA->next;
            currentB = currentB->next;
        }
        return currentA->next;
    }
};