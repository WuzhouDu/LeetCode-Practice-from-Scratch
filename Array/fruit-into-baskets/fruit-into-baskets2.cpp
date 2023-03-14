class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        int result = 0;
        int count = 0;
        int start = 0;
        // should maintain a hash map to count the number of categories in the basket
        unordered_map<int, int> basket;

        for (int i = 0; i < fruits.size(); i++){
            if (basket[fruits[i]] == 0) count++;
            basket[fruits[i]]++;

            while (count > 2){
                basket[fruits[start]]--;
                if (basket[fruits[start]] == 0) count--;
                start++;
            }
            
            result = max(i - start + 1, result);
        }
        return result;
    }
};