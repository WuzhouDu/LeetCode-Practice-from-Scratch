class Solution {
public:
    int get_sum(int n){
        int result = 0;
        while (n/10 != 0){
            result += (n%10)*(n%10);
            n -= n%10;
            n /= 10;
        }
        result += n*n;
        return result;
    }

    bool isHappy(int n) {
        unordered_set<int> set;
        int sum;
        while (n != 1){
            sum = get_sum(n);
            if (set.find(sum) != set.end()) return false;
            else set.insert(sum);
            n = sum;
        }
        return true;
    }
};