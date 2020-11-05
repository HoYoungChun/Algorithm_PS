#include<iostream>
#include<algorithm>

using namespace std;
long long int dp[1000002];

int main(void) {
	dp[1] = 1;
	dp[2] = 2;
	dp[3] = 4;
	for (int i = 4; i <= 1000000; i++) {
		dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009;
	}

	int T = 0;
	int n = 0;
	cin >> T;
	while (T--) {
		cin >> n;
		cout << dp[n] << '\n';
	}
}
