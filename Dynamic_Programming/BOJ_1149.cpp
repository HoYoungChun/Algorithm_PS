#include<iostream>
#include<algorithm>

using namespace std;

int p[1002][3];
int dp[1002][3];

int main(void) {
	int N;
	cin >> N;
	for (int i = 1; i <= N; i++) {
		cin >> p[i][0] >> p[i][1] >> p[i][2];
	}

	dp[1][0] = p[1][0]; dp[1][1] = p[1][1]; dp[1][2] = p[1][2];
	for (int i = 2; i <= N; i++) {
		dp[i][0] = min({ dp[i - 1][1] , dp[i - 1][2] }) + p[i][0];
		dp[i][1] = min({ dp[i - 1][0] , dp[i - 1][2] }) + p[i][1];
		dp[i][2] = min({ dp[i - 1][0] , dp[i - 1][1] }) + p[i][2];
	}

	cout << min({dp[N][0], dp[N][1], dp[N][2]}) << '\n';
}

