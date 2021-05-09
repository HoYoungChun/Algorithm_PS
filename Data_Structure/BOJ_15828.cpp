#include <bits/stdc++.h>
using namespace std;

int main()
{
  ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
  int N; cin >> N; // 라우터 내부의 버퍼의 크기
  queue<int> que;
  
  while(true){
    int input; cin >> input;
    if(input == -1) break;
    else if(input == 0){
      que.pop();
    }
    else if(que.size()<N){
      que.push(input);
    }
  }

  if(que.empty()) cout<<"empty"<<"\n";

  while(!que.empty()){
    cout<< que.front()<< ' ';
    que.pop();
  }
  
  return 0;
}
