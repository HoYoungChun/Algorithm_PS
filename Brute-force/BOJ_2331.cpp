#include<iostream>
using namespace std;

int main(void) 
{
	int N;
	cin >> N;
	
	int i = 0;
	int res = 0;

	for (i = 0; i < N; i++) {
		res = i;
		int div = res;
		while (div != 0) {
			res += div % 10;
			div /= 10;
		}

		if (res == N) {
			cout << i;
			break;
		}
	}

	if (i == N ) {
		cout << 0;
	}

	return 0;
}
