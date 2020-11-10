#include<iostream>
#include<algorithm>
#include<cstring>

using namespace std;

int dp[1002][1002];

int main(void) {
	char a[1002];
	char b[1002];
	cin >> a >> b;
	int a_l = strlen(a);
	int b_l = strlen(b);

	for (int i = 0; i <= a_l; i++)
		dp[i][0] = 0;
	for (int i = 0; i <= b_l; i++)
		dp[0][i] = 0;
	for (int i = 1; i <= a_l; i++) {
		for (int j = 1; j <= b_l; j++) {
			if (a[i-1] == b[j-1])
				dp[i][j] = dp[i - 1][j - 1] + 1;
			else
				dp[i][j] = max({ dp[i][j - 1],dp[i - 1][j] });
		}
	}

	cout << dp[a_l][b_l] << '\n';
	
}
