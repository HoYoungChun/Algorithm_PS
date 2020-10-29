#include<iostream>
 
using namespace std;
 
void pop();
void push(int num);
 
int arr[100005];//index 1부터 사용하니까
int n = 0;//힙에 들어있는 원소의 수
 
 
 
int main(void) {
    ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
 
    int testnum = 0;
    int num = 0;
 
    cin >> testnum;
    for (int i = 0; i < testnum; i++) {
        cin >> num;
        if (num == 0) {
            pop();
        }
        if(num > 0){
            push(num);
        }
    }
 
}
 
void pop() {
    if (n == 0) {
        cout << 0 << "\n";
        return;
    }
    else {
        cout << arr[1] << "\n";
        arr[1] = arr[n];
        n--;
 
        //재정렬(index 1의 값이 변경됨)
        if (n != 0) {
            int t = 1;
            while (t*2 <= n) {
                if (t * 2 == n) {
                    if (arr[t * 2] < arr[t]) {
                        swap(arr[t * 2], arr[t]);
                        t *= 2;
                    }
                    else {
                        break;
                    }
                }
                else {
                    if (arr[t * 2] < arr[t * 2 + 1] && arr[t * 2] < arr[t]) {
                        swap(arr[t * 2], arr[t]);
                        t *= 2;
                    }
                    else if (arr[t * 2] >= arr[t * 2 + 1] && arr[t * 2 + 1] < arr[t]) {
                        swap(arr[t * 2 + 1], arr[t]);
                        t = t*2 +1;
                    }
                    else {
                        break;
                    }
                }
            }
        }
    }
}
 
void push(int num) {
    n++;
    arr[n] = num;
 
    //재정렬(index n의 값이 변경됨)
    int t = n;
    while (t != 1) {
        if (arr[t / 2] > arr[t]) {
            swap(arr[t / 2], arr[t]);
            t /= 2;
        }
        else {
            break;
        }
    }
}
