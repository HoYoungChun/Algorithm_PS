#include<iostream>
#include<algorithm>

using namespace std;

int main(void) {
	int N;
	cin >> N;

	int sum = 0;
	int num;
	while (N--) {
		cin >> num;
		bool isit = true;
		for (int i = 2; i < num; i++) {
			if (num%i == 0) {
				isit = false;
				break;
			}
		}
		if (num == 1)
			isit = false;
		if (isit == true)
			sum++;
	}
	
	cout << sum << '\n';
}
