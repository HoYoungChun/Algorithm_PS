#include<iostream>
 
using namespace std;
 
void pop();
void push(int num);
 
int arr[100005];//index 1부터 사용하니까
int n = 0;//힙에 들어있는 원소의 수
 
 
 
int main(void) {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
 
    int testnum = 0;
    int num = 0;
 
    cin >> testnum;
    for (int i = 0; i < testnum; i++) {
        cin >> num;
        if (num == 0) {
            pop();
        }
        else {
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
            while (t * 2 <= n) {
                if (t * 2 == n) {
                    if (abs(arr[t * 2]) < abs(arr[t])) {
                        swap(arr[t * 2], arr[t]);
                        t *= 2;
                    }
                    else if ((abs(arr[t * 2]) == abs(arr[t])) && arr[t * 2] < 0) {
                        swap(arr[t * 2], arr[t]);
                        t *= 2;
                    }
                    else {
                        break;
                    }
                }
                else {// 이 부분의 경우의 수를 나누는 것이 상당히 복잡
                    if ((abs(arr[t * 2]) < abs(arr[t * 2 + 1])) && (abs(arr[t * 2]) < abs(arr[t]))) {
                        swap(arr[t * 2], arr[t]);
                        t *= 2;
                    }
                    else if ((abs(arr[t * 2]) < abs(arr[t * 2 + 1])) && (abs(arr[t * 2]) == abs(arr[t])) && (arr[t * 2] < 0)) {
                        swap(arr[t * 2], arr[t]);
                        t *= 2;
                    }
                    else if ((abs(arr[t * 2]) > abs(arr[t * 2 + 1])) && (abs(arr[t * 2 + 1]) < abs(arr[t]))) {
                        swap(arr[t * 2 + 1], arr[t]);
                        t = t * 2 + 1;
                    }
                    else if ((abs(arr[t * 2]) > abs(arr[t * 2 + 1])) && (abs(arr[t * 2 + 1]) == abs(arr[t])) && (arr[t * 2 + 1] < 0)) {
                        swap(arr[t * 2 + 1], arr[t]);
                        t = t * 2 + 1;
                    }
                    else if ((abs(arr[t * 2]) == abs(arr[t * 2 + 1])) && (abs(arr[t * 2 + 1]) < abs(arr[t]))) {
                        if (arr[t * 2 + 1] <  arr[t * 2]) {
                            swap(arr[t * 2 + 1], arr[t]);
                            t = t * 2 + 1;
                        }
                        else{//arr[t*2+1] == arr[t*2]일 때는 어느쪽을 바꿔도 상관없으므로 이 경우에 포함
                            swap(arr[t * 2], arr[t]);
                            t = t * 2;
                        }
                    }
                    else if ((abs(arr[t * 2]) == abs(arr[t * 2 + 1])) && (abs(arr[t * 2 + 1]) == abs(arr[t])) && arr[t] > 0) {
                        //절댓값이 모두 같을 때 arr[t] > 0이어야만 swap해줘야하는 경우가 생긴다.
                        if (arr[t * 2 + 1] < arr[t * 2]) {
                            swap(arr[t * 2 + 1], arr[t]);
                            t = t * 2 + 1;
                        }
                        else {//arr[t*2] == arr[t*2+1]일 때는 어느쪽을 바꿔도 상관없으므로 이 경우에 포함
                            swap(arr[t * 2], arr[t]);
                            t = t * 2;
                        }
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
        if (abs(arr[t / 2]) > abs(arr[t])) {
            swap(arr[t / 2], arr[t]);
            t /= 2;
        }
        else if ((abs(arr[t / 2]) == abs(arr[t])) && arr[t] < 0) {
            swap(arr[t / 2], arr[t]);
            t /= 2;
        }
        else {
            break;
        }
    }
}
