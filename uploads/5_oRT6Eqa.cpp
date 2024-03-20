#include <bits/stdc++.h>
using namespace std;

string solve(int n, int k, int c, vector<int>& arr) {
    string ans = "";
    while (n > 0) {
        if (k == 0) {
            ans += to_string(arr[n - 1]);
            arr.pop_back();
            n -= 1;
        }
        else if (k < 0) {
            ans += to_string(arr[0]);
            arr.erase(arr.begin());
            n -= 1;
        } 
        else {
            int x = c / n;
            int y = ceil((float)k / x);
            ans += to_string(arr[y - 1]);
            arr.erase(arr.begin() + (y - 1));
            c /= n;
            n -= 1;
            k -= (y - 1) * x;
        }
    }
    return ans;
}

int main() {
    int t;
    cin >> t;
    while(t--) {
        int n, k;
        cin >> n;
        cin >> k;
    
        vector<int> arr;
        int total = 1;
        for (int i = 0; i < n; i++) {
            total *= (i + 1);
            arr.push_back(i + 1);
        }
        string result = solve(n, k, total, arr);
        cout << result << endl;
    }

    return 0;
}