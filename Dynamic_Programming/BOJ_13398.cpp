#include<iostream>
#include<algorithm>

using namespace std;

long long p[100002];
long long DL[100002];
long long DR[100002];

int main(void) {
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++) {
		cin >> p[i];
	}
	if (n == 1) { cout << p[1]; return 0; }

	DL[1] = p[1];
	for (int i = 2; i <= n; i++) {
		if (DL[i - 1] > 0)
			DL[i] = DL[i - 1] + p[i];
		else
			DL[i] = p[i];
	}//DL[i]는 i번째 수에서 끝나는 최대 연속합

	DR[n] = p[n];
	for (int i = n - 1; i >= 1; i--) {
		if (DR[i + 1] > 0)
			DR[i] = DR[i + 1] + p[i];
		else
			DR[i] = p[i];
	}//DR[i]는 i번째 수에서 시작하는 최대 연속합

	long long max = DR[1];
	for (int i = 2; i <= n; i++) {
		if (max < DR[i])
			max = DR[i];
	}//제거된 값이 없을때의 최대 연속합

	for (int i = 1; i <= n; i++) {
		if (max < DL[i - 1] + DR[i + 1])
			max = DL[i - 1] + DR[i + 1];
	}//제거된 값이 있을때의 최대 연속합들과 비교
	cout << max << '\n';

}
