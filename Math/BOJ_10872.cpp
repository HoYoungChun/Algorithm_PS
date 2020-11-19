#include<iostream>
#include<algorithm>

using namespace std;

int main(void) {
	int N;
	cin >> N;

	int res = 1;
	for (int i = 1; i <= N; i++) {
		res *= i;
	}
	cout << res << '\n';

}
