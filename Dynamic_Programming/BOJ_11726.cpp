#include<iostream>
#include<algorithm>

using namespace std;

int dp[1002];

int main(void) {
	int N;
	cin >> N;
	dp[1] = 1; dp[2] = 2;
	for (int i = 3; i <= N; i++) {
		dp[i] = (dp[i - 1] + dp[i - 2]) % 10007;
	}
	cout << dp[N] << "\n";
}
