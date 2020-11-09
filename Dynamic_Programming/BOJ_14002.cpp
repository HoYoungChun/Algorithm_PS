#include<iostream>
#include<algorithm>

void printr(int find_i);

using namespace std;

int dp[1001][2];
int p[1001];

int main(void) {
	int N;
	cin >> N;
	for (int i = 1; i <= N; i++) {
		cin >> p[i];
	}

	for (int i = 1; i <= N; i++) {
		dp[i][0] = 1;
		dp[i][1] = i;
		for (int j = 1; j <= i; j++) {
			if (p[j]<p[i] && dp[j][0] + 1>dp[i][0]) {
				dp[i][0] = dp[j][0] + 1;
				dp[i][1] = j;
			}
		}
	}

	int max_ind = 1;
	for (int i = 2; i <= N; i++) {
		if (dp[max_ind][0] < dp[i][0])
			max_ind = i;
	}

	cout << dp[max_ind][0] << '\n';
	printr(max_ind);
}

void printr(int find_i) {
	if (dp[find_i][1] == find_i) {
		cout << p[find_i]<<" ";
		return;
	}
	printr(dp[find_i][1]);
	cout << p[find_i]<<" ";
}
