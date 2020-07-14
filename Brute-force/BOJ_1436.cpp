#include<iostream>
using namespace std;

int main(void) 
{
	int N;
	cin >> N;//N은 몇번째 영화인지
	int total = 0;//몇번째인지 센다
	int cnt = 0;//6의 개수를 센다
	int i = 666;
	while (total <= 10000) {
		cnt = 0;
		int res = i;
		int temp = i;
		while (temp != 0) {
			if (temp % 10 == 6) {
				cnt++;//연속으로 나타나고 있는 6의개수 증가
			}
			else {
				cnt = 0;//연속으로 나타나는게 끊기면
			}
			if (cnt == 3)//연속으로 3개존재하는게 확인되면
				break;
			temp /= 10;
		}
		if (cnt == 3)
			total++;
		if (total == N) {
			cout << res;
			break;
		}
		i++;
	}
	return 0;
}
