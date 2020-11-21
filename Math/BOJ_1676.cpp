#include<iostream>
#include<algorithm>

using namespace std;

int main(void) {
	int N;
	cin >> N;
	int ans = 0;
	for (int i = 1; i <= N; i++) {
		int t = i;
		if (t % 5 == 0) {
			while (t % 5 == 0) {
				ans++;
				t /= 5;
			}
		}
	}
	cout << ans << '\n';
}
