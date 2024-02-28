#include <iostream>
#include <vector>
using namespace std;
int main() {
  int n, m;
  cin >> n >> m;
  vector<int> arr(n);
  for (int i = 0; i < n; i++) {
    cin >> arr[i];
  }
  int total_ones = 0, total_minus_ones = 0;
  for (int i = 0; i < n; i++) {
    total_minus_ones += (arr[i] == -1);
    total_ones += (arr[i] == 1);
  }
  vector<string> solution;
  for (int k = 0; k < m; k++) {
    int left, right;
    cin >> left >> right;
    if (left == right || (right - left + 1) % 2) {
      solution.push_back("0\n");
    } else {
      if ((right - left + 1) / 2 <= total_ones && (right - left + 1) / 2 <= total_minus_ones) {
        solution.push_back("1\n");
      } else {
        solution.push_back("0\n");
      }
    }
  }

  for (const string& s : solution) {
    cout << s;
  }
  return 0;
}
