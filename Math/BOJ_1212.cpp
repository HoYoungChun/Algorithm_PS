#include<iostream>
#include<algorithm>
#include<string>

using namespace std;

int main(void) {
	string str;
	cin >> str;
	int t = 1;

	for (int i = 0; i < str.length(); i++) {
		int num = str[i] - '0';

		if (num >= 4) { cout << '1'; num %= 4; t = 0; }
		else if (t == 0) cout << '0';

		if (num >= 2) { cout << '1'; num %= 2; t = 0;}
		else if (t == 0) cout << '0';

		if (num >= 1) { cout << '1'; t = 0;}
		else if (t == 0) cout << '0';
	}
}
