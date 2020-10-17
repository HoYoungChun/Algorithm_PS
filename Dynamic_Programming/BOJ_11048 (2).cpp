#include <iostream>
#include <algorithm>

#define max(a,b) (((a) > (b)) ? (a) : (b))
using namespace std;
 
int DP[1002][1002];
int N, M;
 
int main() {
   ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    cin >> N >> M;
 
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= M; j++) {
            cin >> DP[i][j];
 
            DP[i][j] += max(DP[i - 1][j], max(DP[i - 1][j - 1], DP[i][j - 1]));
        }
    }
 
    cout << DP[N][M] << '\n';
 
    return 0;
}
