#include <bits/stdc++.h>
using namespace std;

int main()
{
  ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
  int N,K; cin >> N >> K;
  queue<int> que;

  for(int i=1; i<=N; i++) //1부터 N까지 큐에 넣기
    que.push(i);

  for(int i=0; i<K-1; i++){ //맨처음 출력할값을 front로 이동
    que.push(que.front()); //앞에껄 뒤로 옮겨서
    que.pop();
  }

  cout<<"<";

  while(que.size() > 1){
    cout<<que.front()<<", ";
    que.pop();
    for(int i=0; i<K-1; i++){ //k-1번동안 앞에걸 뒤로 옮기기
      que.push(que.front());
      que.pop();
    }
  }
  cout<< que.front()<<">\n";

  return 0;
}
