#include<iostream>
#include<algorithm>
#include<cstring>

#define NEITHER 0
#define UP 1
#define LEFT 2
#define UP_AND_LEFT 3

void trace(int i, int j);

using namespace std;

int dp[1002][1002];
int track[1002][1002];
char a[1002];
char b[1002];

int main(void) {
	
	cin >> a >> b;
	int a_l = strlen(a);
	int b_l = strlen(b);

	for (int i = 0; i <= a_l; i++) {
		dp[i][0] = 0;
	}
	for (int i = 0; i <= b_l; i++) {
		dp[0][i] = 0;
	}
	for (int i = 1; i <= a_l; i++) {
		for (int j = 1; j <= b_l; j++) {
			if (a[i - 1] == b[j - 1]) {
				dp[i][j] = dp[i - 1][j - 1] + 1;
				track[i][j] = UP_AND_LEFT;
			}
			else if (dp[i][j - 1] > dp[i - 1][j]) {
				dp[i][j] = dp[i][j - 1];
				track[i][j] = LEFT;
			}
			else {
				dp[i][j] = dp[i-1][j];
				track[i][j] = UP;
			}
		}
	}

	std::cout << dp[a_l][b_l] << '\n';
	trace(a_l, b_l);
	
}

void trace(int i, int j) {
	if (i < 0 || j < 0) {
		return;
	}
	if (track[i][j] == UP_AND_LEFT) {
		trace(i - 1, j - 1);
		cout << a[i-1];
	}
	else if (track[i][j] == UP) {
		trace(i - 1, j);
	}
	else {
		trace(i, j - 1);
	}
}
