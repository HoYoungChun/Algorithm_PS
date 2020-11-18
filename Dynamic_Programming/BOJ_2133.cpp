#include<iostream>
#include<algorithm>

using namespace std;

int dp[32];

int main(void) {
	int N;
	cin >> N;
	dp[0] = 1;
	dp[2] = 3;
	for (int i = 3; i <= N; i++) {
		if (i % 2 != 0) {
			dp[i] = 0;
		}
		else {
			dp[i] += 3 * dp[i - 2];
			for (int j = 4; i-j>=0; j++) {
				dp[i] += 2 * dp[i - j];
			}
		}
	}
	cout << dp[N] << '\n';
}
