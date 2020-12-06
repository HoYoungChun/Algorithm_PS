#include<iostream>
#include<algorithm>
 
using namespace std;
int arr[1000001];
 
int main(void) {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    
    int testnum = 0;
    cin >> testnum;
    for (int i = 0; i < testnum; i++) {
        cin >> arr[i];
    }
 
    sort(arr, arr + testnum);
 
    for (int i = 0; i < testnum; i++) {
        cout << arr[i]<<"\n";
    }
}

