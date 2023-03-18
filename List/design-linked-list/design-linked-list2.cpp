class MyLinkedList {
public:
    struct ListNode{
        int val;
        ListNode* next = NULL;
    };

    ListNode* dummyHead;
    int size;

    
    MyLinkedList() {
        dummyHead = new ListNode();
        size = 0;
    }
    
    int get(int index) {
        if (index >= size) return -1;
        ListNode* current = dummyHead;
        while (index--){
            current = current->next;
        }
        return current->next->val;
    }
    
    void addAtHead(int val) {
        ListNode* newNode = new ListNode();
        newNode->val = val;
        newNode->next = dummyHead->next;
        dummyHead->next = newNode;
        size++;
        return;
    }
    
    void addAtTail(int val) {
        ListNode* newNode = new ListNode();
        newNode->val = val;
        newNode->next = NULL;
        ListNode* current = dummyHead;
        while (current->next != NULL){
            current = current->next;
        }
        current->next = newNode;
        size++;
        return;
    }
    
    void addAtIndex(int index, int val) {
        if (index > size) return;
        else if (index == size) addAtTail(val);
        else{
            ListNode* newNode = new ListNode();
            newNode->val = val;
            ListNode* current = dummyHead;
            while (index--){
                current = current->next;
            }
            newNode->next = current->next;
            current->next = newNode;
            size++;
            return;
        }
    }
    
    void deleteAtIndex(int index) {
        if (index >= size) return;
        if (size == 0) return;
        if (index == 0){
            dummyHead->next = dummyHead->next->next;
            size--;
            return;
        }
        ListNode* current = dummyHead;
        while (index--){
            current = current->next;
        }
        current->next = current->next->next;
        size--;
    }
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */