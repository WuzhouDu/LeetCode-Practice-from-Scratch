class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        int result = 0;

        for (int i = 0; i < fruits.size(); i++){
            int temp = 0;
            int second_cate = fruits.size();
            int first_cate = fruits[i];
            int j = i;
            while (j < fruits.size()){
                if (fruits[j] != first_cate && second_cate == fruits.size()){
                    second_cate = fruits[j];
                    j++;
                    temp++;
                }
                else if (fruits[j] != first_cate && fruits[j] != second_cate){
                    break;
                }
                else{
                    temp++;
                    j++;
                }
            }
            if (temp > result) result = temp;
        }
        return result;

    }
};