#include<iostream>
#include<algorithm>

using namespace std;

long long count5(long long N) {
	long long ans = 0;
	for (long long i = 5; i <= N; i*=5) {
		ans += N / i;
	}
	return ans;
}

long long count2(long long N) {
	long long ans = 0;
	for (long long i = 2; i <= N; i *= 2) {
		ans += N / i;
	}
	return ans;
}

int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	long long N,M;
	long long n2 = 0;
	long long n5 = 0;
	cin >> N >> M;
	n2 += count2(N);
	n5 += count5(N);
	n2 -= count2(M);
	n5 -= count5(M);
	n2 -= count2(N-M);
	n5 -= count5(N-M);
	cout << min({ n2,n5 }) << '\n';
}
