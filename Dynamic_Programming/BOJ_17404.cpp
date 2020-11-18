#include<iostream>
#include<algorithm>

using namespace std;

int p[1002][3];
int dp[1002][3];

int main(void) {
	int N;
	cin >> N;
	for (int i = 1; i <= N; i++) {
		cin >> p[i][0];
		cin >> p[i][1];
		cin >> p[i][2];
	}

	int ans = 10000000;
	for (int k = 0; k <= 2; k++) {
		for (int j = 0; j <= 2; j++) {
			if (j == k)
				dp[1][j] = p[1][j];
			else
				dp[1][j] = 10000000;
		}

		for (int i = 2; i <= N; i++) {
			dp[i][0] = min({ dp[i - 1][1],dp[i - 1][2] }) + p[i][0];
			dp[i][1] = min({ dp[i - 1][0],dp[i - 1][2] }) + p[i][1];
			dp[i][2] = min({ dp[i - 1][0],dp[i - 1][1] }) + p[i][2];
		}

		
		for (int j = 0; j <= 2; j++) {
			if (j == k)
				continue;
			else
				ans = min({ ans,dp[N][j] });
		}
	}
	cout << ans << '\n';
}
