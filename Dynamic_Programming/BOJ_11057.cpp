#include<iostream>
#include<algorithm>

using namespace std;

long long dp[1002][10];

int main(void) {
	int N;
	cin >> N;

	for (int i = 0; i <= 9; i++) {
		dp[1][i] = 1;
	}

	for (int i = 2; i <= N; i++) {
		for (int j = 0; j <= 9; j++) {
			dp[i][j] = 0;
			for (int k = 0; k <= j; k++)
				dp[i][j] += dp[i-1][k] % 10007;
		}
	}
	
	long long sum = 0;
	for (int i = 0; i <= 9; i++) {
		sum += dp[N][i];
	}
	cout << sum % 10007 << '\n';
}
