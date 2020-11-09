#include<iostream>
#include<algorithm>

using namespace std;

int dp[100002];
int p[100002];

int main(void) {
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> p[i];
	}

	dp[0] = p[0];
	for (int i = 1; i < n; i++) {
		if (dp[i - 1] > 0)
			dp[i] = dp[i - 1] + p[i];
		else
			dp[i] = p[i];
	}

	int max = dp[0];
	for (int i = 1; i < n; i++) {
		if (max < dp[i])
			max = dp[i];
	}
	cout << max << '\n';
}
