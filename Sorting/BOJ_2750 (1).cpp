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
 
    for (int i = 1; i < testnum; i++) {
        int temp = arr[i];
        int k = i;
        while (k != 0 && arr[k - 1] > temp) {
            arr[k] = arr[k - 1];
            k--;
        }
        arr[k] = temp;
    }//삽입정렬
 
    for (int i = 0; i < testnum; i++) {
        cout << arr[i]<<"\n";
    }//출력
 
}
