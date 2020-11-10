#include<iostream>
#include<algorithm>

using namespace std;

long long dp[201][201];

int main(void) {
	int N, K;
	cin >> N >> K;

	for (int i = 0; i <= N; i++) {
		dp[i][1] = 1;
	}
	for (int j = 2; j <= K; j++) {
		for (int p = 0; p <= N; p++) {
			long long sum = 0;
			for (int i = 0; i <= p; i++) {
				sum += dp[i][j - 1] % 1000000000;
			}
			dp[p][j] = sum % 1000000000;
		}
	}
	cout << dp[N][K] << '\n';

}
