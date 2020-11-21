#include<iostream>
#include<algorithm>

using namespace std;
int arr[102];

int gcd(int a, int b) {
	if (b == 0)
		return a;
	else
		return gcd(b, a%b);
}

int main(void) {
	int T, N;
	long long ans = 0;
	cin >> T;

	while (T--) {
		ans = 0;
		cin >> N;
		for (int i = 1; i <= N; i++) {
			cin >> arr[i];
		}
		for (int i = 1; i <= N-1; i++) {
			for (int j = i+1; j <= N; j++) {
					ans += gcd(arr[i], arr[j]);
			}
		}
		cout << ans << '\n';
	}

}
