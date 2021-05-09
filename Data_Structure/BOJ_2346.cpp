#include <bits/stdc++.h>
using namespace std;

int main()
{
  ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
  int N; cin >> N;
  vector<int>arr(N+1);
  for(int i=1; i<=N; i++){
    cin >> arr[i];
  } //각 풍선의 번호 입력받기

  deque<int>deq;
  for(int i=1; i<=N; i++){
    deq.push_back(i);
  } //1번 풍선 ~ N번 풍선까지 큐에 넣기

  while(N--){
    int move = arr[deq.front()];
    cout<< deq.front()<< " ";
    deq.pop_front();

    if(move > 0){ //풍선안에 적힌수가 양수일때
      move--;
      while(move--){
        deq.push_back(deq.front()); //앞에 있는거 뒤에 넣기
        deq.pop_front();
      }
    }
    else{ //풍선안에 적힌 수가 음수일때
      move = abs(move);
      while(move--){
        deq.push_front(deq.back()); //뒤에 있는거 앞에 넣기
        deq.pop_back();
      }
    }
    

  }

  return 0;
}
