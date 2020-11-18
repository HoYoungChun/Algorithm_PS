#include<iostream>
#include<algorithm>

using namespace std;

int p[1002];
int idp[1002];
int ddp[1002];

int main(void) {
	int N;
	cin >> N;
	for (int i = 1; i <= N; i++) {
		cin >> p[i];
	}
	
	int max = -1;

	//i = Middle Choice
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= i; j++) {
			idp[j] = 1;
			for (int k = 1; k <= j; k++) {
				if (p[k]<p[j] && idp[k] + 1 > idp[j])
					idp[j] = idp[k] + 1;
			}
		}//idp[j]는 j를 부분수열의 마지막으로 가질때의 최대길이

		for (int j = N; j >= i; j--) {
			ddp[j] = 1;
			for (int k = N; k >= j; k--) {
				if (p[k] < p[j] && ddp[k] + 1 > ddp[j])
					ddp[j] = ddp[k] + 1;
			}
		}//ddp[j]는 j를 부분수열의 처음으로 가질때의 최대길이

		if (max < idp[i] + ddp[i] - 1)
			max = idp[i] + ddp[i] - 1;
	}

	cout << max << '\n';
}
