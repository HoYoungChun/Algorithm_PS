#include<iostream>
#include<algorithm>
#include<cmath>

using namespace std;

int main(void) {
	long long N;
	int B;
	cin >> N >> B;

	long long i;
	for (i = 0; N >= pow(B, i); i++);
	i--;
	//B의 몇승부터 시작하는지 구하기

	while (i>=0) {
		if (N >= pow(B, i)) {
			int p = N / (int)pow(B, i);
			if (p <= 9) cout << p;			//p<9로 실수하지 말자
			else cout << char(p - 10 + 'A');
			N = N - (int)pow(B, i)*p;
		}
		else {
			cout << '0';
		}
		i--;
	}
}
