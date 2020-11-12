#include<iostream>
#include<algorithm>

using namespace std;

int p[10002];
int dp[10002][3];

int main(void) {
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++) {
		cin >> p[i];
	}

	dp[1][0] = 0; dp[1][1] = p[1]; dp[1][2] = 0;

	for (int i = 2; i <= n; i++) {
		dp[i][0] = max({ dp[i - 1][0],dp[i - 1][1],dp[i - 1][2] });
		dp[i][1] = dp[i - 1][0] + p[i];
		dp[i][2] = dp[i - 1][1] + p[i];
	}
	cout << max({ dp[n][0],dp[n][1],dp[n][2] }) << '\n';
	
}
