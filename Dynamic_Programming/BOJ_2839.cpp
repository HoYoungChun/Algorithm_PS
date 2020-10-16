#include<iostream>
#include<algorithm>

using namespace std;
int arr[5005];//처음에 모두 0으로 초기화됨

int opti(int num) {
	if (arr[num] == -1)
		return -2;
	else if (arr[num] > 0)
		return arr[num];
	else {
		int n1 = opti(num - 3) + 1;
		int n2 = opti(num - 5) + 1;

		if (n1 == -1 && n2 == -1)
			return -2;
		else if (n1 == -1 || n2 == -1) {
			arr[num] = max(n1, n2);
			return arr[num];
		}
		else {
			arr[num] = min(n1, n2);
			return arr[num];
		}
	}
}

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	arr[0] = -1; arr[1] = -1; arr[2] = -1;
	arr[3] = 1; arr[4] = -1; arr[5] = 1;

	int N;
	cin >> N;
	int result = -1;

	if (N <= 5)
		result = arr[N];
	else {
		int n1 = opti(N - 3) + 1;
		int n2 = opti(N - 5) + 1;
		if (n1 == -1 || n2 == -1)
			result = max(n1, n2);
		else
			result = min(n1, n2);
	}
	cout << result << "\n";
}
