#include<iostream>
#include<algorithm>
#include<string>

using namespace std;

int main(void) {
	string str;
	cin >> str;
	
	while (str.length() % 3 != 0)
		str = "0" + str;
	
	for (int i = 0; i < str.length(); i += 3) {
		cout << 4 * (str[i] - '0') + 2 * (str[i + 1] - '0') + 1 * (str[i + 2] - '0');
	}
}
