#include<iostream>
#include<algorithm>

using namespace std;
int p[1002];
int dp[1002];


int main(void) {
	int N;
	cin >> N;
	for (int i = 1; i <= N; i++) {
		cin >> p[i];
	}

	for (int i = 1; i <= N; i++) {
		int max = dp[0] + p[i];
		for (int j = 1; j < i; j++) {
			if (max < dp[j] + p[i - j])
				max = dp[j] + p[i - j];
		}
		dp[i] = max;
	}
	cout << dp[N] << '\n';
}
