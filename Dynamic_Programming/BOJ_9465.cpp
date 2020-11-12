#include<iostream>
#include<algorithm>

using namespace std;

long long p[2][100002];
long long dp[3][100002];

int main(void) {
	int N;
	int T;
	cin >> T;
	while (T--) {
		cin >> N;
		for (int i = 0; i < N; i++) {
			cin >> p[0][i];
		}
		for (int i = 0; i < N; i++) {
			cin >> p[1][i];
		}

		dp[0][0] = 0; dp[1][0] = p[0][0]; dp[2][0] = p[1][0];

		for (int i = 1; i < N; i++) {
			dp[0][i] = max({dp[0][i - 1], dp[1][i - 1], dp[2][i - 1]});
			dp[1][i] = max({dp[0][i - 1] ,dp[2][i - 1] }) + p[0][i];
			dp[2][i] = max({dp[0][i - 1] ,dp[1][i - 1] }) + p[1][i];
		}
		cout << max({ dp[0][N - 1], dp[1][N - 1], dp[2][N - 1] }) << '\n';
	}
}
