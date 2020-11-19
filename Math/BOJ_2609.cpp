#include<iostream>
#include<algorithm>

using namespace std;

int main(void) {
	int a, b;
	int GCD;//최대공약수: greatest common divisor
	int LCM;//최소공배수: largest common multiple

	cin >> a >> b;
	if (a > b) swap(a, b);//a<=b로 만들기

	for (int i = 1; i <= b; i++) {
		if (a%i == 0 && b%i == 0)
			GCD = i;
	}

	for (int i = b; i <= b * a; i++) {
		if (i%a == 0 && i%b == 0) {
			LCM = i;
			break;
		}
	}
	
	cout << GCD << '\n' << LCM << '\n';
}
