#include<iostream>
using namespace std;


int main(void) 
{
	char arr[51][51];
	int cnt = 0;
	int res = 3000;
	int N,M;
	cin >> N >> M;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> arr[i][j];
		}
	}
	//입력받기 완료
	
	for (int i = 0; i <= N - 8; i++) {
		for (int j = 0; j <= M - 8; j++) {
			//8x8의 맨왼쪽위는 arr[i][j]
			cnt = 0;//다시칠해야할 개수
			for (int k = i; k < i + 8; k++) {
				for (int p = j; p < j + 8; p++) {
					//맨왼쪽위가 W일 때 기준으로
					if (((k - i) + (p - j)) % 2 == 0) {
						//W이어야하는 위치
						if (arr[k][p] != 'W')
							cnt++;
					}
					else {
						//B이어야하는 위치
						if (arr[k][p] != 'B')
							cnt++;
					}
				}
			}
			if (cnt > 64 - cnt)
				cnt = 64 - cnt;
			if (cnt < res)
				res = cnt;
		}
	}

	cout << res;

	return 0;
}
