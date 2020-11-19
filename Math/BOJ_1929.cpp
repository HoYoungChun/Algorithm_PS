#include<iostream>
#include<algorithm>

using namespace std;

bool prime[1000002];//지워졌으면 true(1), 소수인게 false(0)

int main(void) {
	prime[1] = true;
	for (int i = 2; i*i <= 1000000; i++) {
		if (prime[i] == false) {
			for (int j = i * 2; j <= 1000000; j+=i) {
				prime[j] = true;
			}
		}
	}

	int a, b;
	cin >> a >> b;
	for (int i = a; i <= b; i++) {
		if (prime[i] == false) {
			cout << i << '\n';
		}
	}


}
