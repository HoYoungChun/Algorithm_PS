#include<iostream>
#include<algorithm>

using namespace std;

bool prime[1000002];//지워졌으면 true(1), 소수인게 false(0)

int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	prime[1] = true;
	for (int i = 2; i*i <= 1000000; i++) {
		if (prime[i] == false) {
			for (int j = i * 2; j <= 1000000; j+=i) {
				prime[j] = true;
			}
		}
	}

	int num;
	while (1) {
		cin >> num;
		if (num == 0)
			break;
		for (int i = 3; i <= num / 2; i += 2) {
			if (prime[i] == false && prime[num - i] == false) {
				cout << num << " = " << i << " + " << num - i << '\n';
				break;
			}
		}
	}

}
