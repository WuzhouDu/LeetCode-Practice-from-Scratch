class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> result(n, vector<int>(n, 0));
        int offset = 0;
        int loop = n / 2;
        int middle = n / 2;
        int count = 1;
        
        while (loop--){

            for (int i = offset; i < n - offset - 1; i++){
                result[offset][i] = count++;
            }
            for (int i = offset; i < n - offset - 1; i++){
                result[i][n - offset - 1] = count++;
            }
            for (int i = n - offset - 1; i > offset; i--){
                result[n - offset - 1][i] = count++;
            }
            for (int i = n - offset - 1; i > offset; i--){
                result[i][offset] = count++;
            }
            offset++;
        }

        if (n % 2){
            result[middle][middle] = n*n;
        }
        return result;
    }
};