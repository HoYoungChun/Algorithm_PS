#include<iostream>
#include<algorithm>
#include<cmath>

using namespace std;

int dp[100002];

int main(void) {
	int N;
	cin >> N;
	for (int i = 1; i <= N; i++) {
		dp[i] = i;//모두 1로만 구성된 최악의 경우
		for (int j = 1; j <= sqrt(i); j++) {
			dp[i] = min(dp[i], dp[i - j * j] + 1);
		}
	}
	
	cout << dp[N] << '\n';
}
