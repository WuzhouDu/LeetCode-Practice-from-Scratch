class MyLinkedList {
public:
    struct ListNode{
        int val = 1001;
        ListNode* next = NULL;
    };

    public: ListNode* head;

    MyLinkedList() {
        head = new ListNode();
    }
    
    int get(int index) {
        int i = 0;
        ListNode* current = head;

        while (current != NULL && current->val != 1001){
            if (i == index) return current->val;
            i++;
            current = current->next;
        }
        return -1;
    }
    
    void addAtHead(int val) {
        if (head->val == 1001){
            head->val = val;
            return;
        }

        ListNode* newNode = new ListNode();
        newNode->val = val;
        newNode->next = head;
        head = newNode;
    }
    
    void addAtTail(int val) {
        if (head->val == 1001){
            head->val = val;
            return;
        }

        ListNode* newNode = new ListNode();
        newNode->val = val;
        ListNode* current = head;
        while (current->next != NULL){
            current = current->next;
        }
        current->next = newNode;
    }
    
    void addAtIndex(int index, int val) {
        if (head->val == 1001 && index == 0){
            head->val = val;
            return;
        }

        if (head->val == 1001 && index > 0) return;

        ListNode* newNode = new ListNode();
        newNode->val = val;
        int i = 1;

        if (index == 0){
            newNode->next = head;
            head = newNode;
            return;
        }

        ListNode* current = head;
        while (current != NULL){
            if (i == index){
                newNode->next = current->next;
                current->next = newNode;
                return;
            }
            i++;
            current = current->next;
        }
    }
    
    void deleteAtIndex(int index) {
        if (index == 0){
            ListNode* temp = head;
            head = head->next;
            delete temp;
            return;
        }

        ListNode* current = head;
        int i = 1;
        while (current->next != NULL){
            if (index == i){
                ListNode* temp = current->next;
                current->next = current->next->next;
                delete temp;
                return;
            }
            i++;
            current = current->next;
        }
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