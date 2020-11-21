#include<iostream>
#include<algorithm>

using namespace std;

long long gcd(long long a, long long b) {
	if (b == 0)
		return a;
	else
		return gcd(b, a%b);
}

int main(void) {
	long long N, S;
	cin >> N >> S;

	long long p,k;
	cin >> p;
	p = abs(p - S);
	N--;

	while (N--) {
		cin >> k;
		p = gcd(p, abs(k-S));
	}
	cout << p << '\n';
}
