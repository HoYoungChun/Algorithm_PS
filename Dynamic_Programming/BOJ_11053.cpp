#include<iostream>
#include<algorithm>

using namespace std;

int dp[1001];
int p[1001];

int main(void) {
	int N;
	cin >> N;
	for (int i = 1; i <= N; i++) {
		cin >> p[i];
	}

	for (int i = 1; i <= N; i++) {
		dp[i] = 1;
		for (int j = 1; j <= i; j++) {
			if (p[j]<p[i] && dp[j] + 1>dp[i]) {
				dp[i] = dp[j] + 1;
			}
		}
	}

	int max = dp[1];
	for (int i = 2; i <= N; i++) {
		if (max < dp[i])
			max = dp[i];
	}

	cout << max << '\n';
}
