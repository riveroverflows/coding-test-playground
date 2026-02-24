#include <iostream>
#include <vector>
#include <sstream>
#include <string>

using namespace std;

void backtrack(vector<int>& curr, vector<int>& nums, vector<bool>& used, vector<vector<int>>& answer) {
    if (curr.size() == nums.size()) {
        answer.push_back(curr);
        return;
    }
    for (int i = 0; i < nums.size(); i++) {
        if (used[i]) continue;
        curr.push_back(nums[i]);
        used[i] = true;
        backtrack(curr, nums, used, answer);
        used[i] = false;
        curr.pop_back();
    }
}

vector<vector<int>> permute(vector<int>& nums) {
    vector<vector<int>> answer;
    vector<int> curr;
    vector<bool> used(nums.size(), false);
    backtrack(curr, nums, used, answer);
    return answer;
}

int main() {
    string line;
    getline(cin, line);

    vector<int> nums;
    stringstream ss(line);
    string token;
    while (getline(ss, token, ',')) {
        nums.push_back(stoi(token));
    }

    auto result = permute(nums);
    cout << "[";
    for (int i = 0; i < result.size(); i++) {
        cout << "[";
        for (int j = 0; j < result[i].size(); j++) {
            cout << result[i][j];
            if (j < result[i].size() - 1) cout << ", ";
        }
        cout << "]";
        if (i < result.size() - 1) cout << ", ";
    }
    cout << "]" << endl;
    return 0;
}