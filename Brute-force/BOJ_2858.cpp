#include<iostream>
using namespace std;

int main(void) 
{
	int L, W;
	int R, B;
	cin >> R >> B;

	int sum = B + R;//sum은 총 타일의 수
	int i, j;

	/*방정식을 풀면i+j가 2+R/2이고 R이 최대 5000이기 때문에
	i+j는 최대 2502이다. 그리고 i,j가 3보다 작으면 갈색타일이 0이되므로
	i,j는 반드시 3이상의 정수이다.
	*/
	for (i = 3; i < 2500; i++) {
		//i는 W 또는 L
		j = (2 + R / 2) - i;
		//j는 L 또는 W
		if (i*j == sum)//정답일때
			break;
	}

	if (i > j) {
		L = i, W = j;
	}
	else {
		L = j, W = i;
	}

	cout << L << ' ' << W;

	return 0;
}
