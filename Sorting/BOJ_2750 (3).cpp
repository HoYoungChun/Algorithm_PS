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
 
    for (int i = 0; i < testnum - 1; i++) {
        for (int j = 0; j < testnum - 1 - i; j++) {
            if (arr[j] > arr[j + 1])
                swap(arr[j], arr[j + 1]);
        }
    }
    //거품정렬
 
    for (int i = 0; i < testnum; i++) {
        cout << arr[i]<<"\n";
    }//출력
 
}
