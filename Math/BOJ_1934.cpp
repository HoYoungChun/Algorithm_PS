#include<iostream>
#include<algorithm>

using namespace std;

int main(void) {
	int a, b;
	int GCD;//최대공약수: greatest common divisor
	int LCM;//최소공배수: largest common multiple

	int T;
	cin >> T;

	while (T--) {
		cin >> a >> b;
		if (a < b) swap(a, b);//a>=b로 만들기

		int ta=a;
		int tb=b;
		int r=1;
		while (r != 0) {
			r = ta % tb;
			ta = tb;
			tb = r;
		}
		GCD = ta;

		LCM = (a*b) / GCD;

		cout << LCM << '\n';
	}
}
