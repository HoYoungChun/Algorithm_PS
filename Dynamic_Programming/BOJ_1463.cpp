#include<iostream>
#include<algorithm>

using namespace std;

int dp[1000002];

int main(void) {
	int N;
	cin >> N;
	dp[2] = 1; dp[3] = 1;
	for (int i = 4; i <= N; i++) {
		if (i % 6 == 0) {
			dp[i] = min({ dp[i / 3],dp[i / 2], dp[i - 1] }) + 1;
		}
		else if (i % 2 == 0 && i % 3 != 0) {
			dp[i] = min({ dp[i / 2], dp[i - 1] }) + 1;
		}
		else if (i % 2 != 0 && i % 3 == 0) {
			dp[i] = min({ dp[i / 3], dp[i - 1] }) + 1;
		}
		else {
			dp[i] = dp[i - 1] + 1;
		}
	}
	cout << dp[N] << "\n";
}
