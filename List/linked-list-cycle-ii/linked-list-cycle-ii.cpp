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
    ListNode *detectCycle(ListNode *head) {
        ListNode* dummyHead = new ListNode(0);
        dummyHead->next = head;
        ListNode* slow = dummyHead;
        ListNode* fast = slow;
        int i = 1;

        // firstly, fast and slow will meet in the loop.
        while (fast != NULL){
            if (fast->next != NULL && fast->next->next != NULL){
                fast = fast->next->next;
                slow = slow->next;
            }
            else return NULL;
            if (fast == slow){
                break;
            }
        }
        // then, calculate the loop length
        while (fast->next != slow){
            fast = fast->next;
            i++;
        }

        slow = dummyHead;
        fast = dummyHead;
        while (i--){
            fast = fast->next;
        }
        while (slow->next != fast->next){
            slow = slow->next;
            fast = fast->next;
        }
        return slow->next;
        
    }
};