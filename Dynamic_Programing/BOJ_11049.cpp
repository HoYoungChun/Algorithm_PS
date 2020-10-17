#include<iostream>
 
#define INT_MAX 2147483647
 
using namespace std;
int d[502];
int M[502][502];
 
int find_matrix(int i, int j);//Ai부터 Aj까지의 곱에서 최소 곱셈수를 반환
 
int main(void) {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int N;
    int trash;
    cin >> N;
    cin >> d[0];
    for (int i = 1; i <= N; i++) {
        cin >> d[i];
        if (i < N)
            cin >> trash;
    }
 
    for (int i = 1; i <= N ; i++) {
        M[i][i] = 0;
    }
    //table에 basis넣기(setup)
 
    for (int j = 2; j <= N; j++) {
        for (int i = j-1; i >= 1; i--) {
            M[i][j] = find_matrix(i, j);
        }
    }
    //적절한 순서에 따라 table채우기(fill)
 
    cout << M[1][N] <<"\n";
}
 
int find_matrix(int i, int j) {
    if (i == j)
        return 0;//행렬이 하나일땐 필요한 곱셈수 0
    else {
        int min = INT_MAX;
        int temp;
        for (int k = i; k <= j - 1; k++) {
            if ((temp = M[i][k] + M[k+1][j] + d[i - 1] * d[k] * d[j]) < min) {
                min = temp;
            }
        }
        M[i][j] = min;
        return M[i][j];
    }
}
