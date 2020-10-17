#include<iostream>
 
#define max(a,b) (((a) > (b)) ? (a) : (b))
using namespace std;
 
int candy[1002][1002];//input으로 들어오는 candy수를 저장할 배열
int opti[1002][1002];//opti[i][j]는 i,j까지 얻을 수 있는 최대 캔디수
 
int main(void) {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int N, M;
    cin >> N >> M;
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= M; j++) {
            cin >> candy[i][j];
        }
    }
 
    opti[1][1] = candy[1][1];
    
    for (int i = 1; i <= N; i++) {
        opti[i][1] = opti[i - 1][1] + candy[i][1];
    }//table에서 아래로만 가는 경우인 basis 넣기
    
    for (int j = 1; j <= M; j++) {
        opti[1][j] = opti[1][j-1] + candy[1][j];
    }//table에서 오른쪽으로만 가는 경우인 basis 넣기
 
    for (int i = 2; i <= N; i++) {
        for (int j = 2; j <= M; j++) {
            opti[i][j] = max(opti[i - 1][j], opti[i][j - 1]) + candy[i][j];
        }
    }//opti[i][j]는 i,j까지 얻을 수 있는 최대 캔디수
 
    cout << opti[N][M] << "\n";
}
