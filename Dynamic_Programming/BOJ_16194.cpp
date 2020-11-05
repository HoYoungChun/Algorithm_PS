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
		int min = dp[0] + p[i];
		for (int j = 1; j < i; j++) {
			if (min > dp[j] + p[i - j])
				min = dp[j] + p[i - j];
		}
		dp[i] = min;
	}
	cout << dp[N] << '\n';
}
