#include<iostream>
#include<algorithm>

using namespace std;

int p[501][501];
int dp[501][501];

int main(void) {
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= i; j++)
			cin >> p[i][j];

	dp[1][1] = p[1][1];
	for (int i = 2; i <= n; i++) {
		dp[i][1] = dp[i - 1][1] + p[i][1];
		for (int j = 2; j < i; j++) {
			dp[i][j] = max({ dp[i - 1][j - 1], dp[i - 1][j] }) +p[i][j];
		}
		dp[i][i] = dp[i - 1][i - 1] + p[i][i];
	}

	int max = -1;
	for (int i = 1; i <= n; i++) {
		if (max < dp[n][i])
			max = dp[n][i];
	}
	cout << max << '\n';
}
