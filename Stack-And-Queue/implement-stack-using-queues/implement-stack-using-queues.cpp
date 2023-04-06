class MyStack {
public:
    queue<int> one;
    queue<int> two;
    MyStack() {

    }
    
    void push(int x) {
        if (one.empty()){
            one.push(x);
            while (!two.empty()){
                int temp = two.front();
                two.pop();
                one.push(temp);
            }
        }
        else{
            two.push(x);
            while (!one.empty()){
                int temp = one.front();
                one.pop();
                two.push(temp);
            }
        }
    }
    
    int pop() {
        if (one.empty()){
            int temp = two.front();
            two.pop();
            return temp;
        }
        else {
            int temp = one.front();
            one.pop();
            return temp;
        }
    }
    
    int top() {
        return one.empty() ? two.front() : one.front();
    }
    
    bool empty() {
        return one.empty() && two.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */