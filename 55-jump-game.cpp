class Solution {
public:
    bool canJump(vector<int>& nums) {
        int fartest = 0;
        for (int i = 0; i < nums.size() - 1; i++){
            if (i > fartest){
                break;
            }
            if (fartest < (i + nums[i])){
                fartest = i + nums[i];
            }
        }

        if (fartest >= nums.size() - 1){
            return true;
        }
        else {
            return false;
        }

    }
};