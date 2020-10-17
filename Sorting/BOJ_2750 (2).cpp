#include<iostream>
#include<algorithm>
 
using namespace std;
int arr[1001];
 
int main(void) {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    
    int testnum = 0;
    cin >> testnum;
    for (int i = 0; i < testnum; i++) {
        cin >> arr[i];
    }//입력받기
 
    for (int i = 0; i < testnum-1; i++) {
        int min = arr[i];
        int tempindex = i;
        for (int j = i+1; j < testnum; j++) {
            if (arr[j] < min) {
                min = arr[j];
                tempindex = j;
            }
        }
        swap(arr[i], arr[tempindex]);
    }//선택정렬
 
 
    for (int i = 0; i < testnum; i++) {
        cout << arr[i]<<"\n";
    }//출력
 
}
