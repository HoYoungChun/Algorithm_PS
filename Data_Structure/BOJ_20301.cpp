#include <bits/stdc++.h>
using namespace std;

int main()
{
  ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
  int N,K,M; cin >> N >> K >> M;
  deque<int> deq;
  int direction = 1;  //1이면 정방향, -1이면 역방향
  int delete_num = 0; //제거한 사람의 수

  for(int i=1; i<=N; i++) //1부터 N까지 큐에 넣기
    deq.push_back(i);

  for(int i=0; i<K-1; i++){ //맨처음 출력할값을 front로 이동
    deq.push_back(deq.front()); //앞에껄 뒤로 옮겨서
    deq.pop_front();
  }

  while(1){ //deque이 빌때까지 반복
    cout<<deq.front()<<"\n";
    deq.pop_front();

    if(deq.empty()) break;

    delete_num +=1 ;
    if(delete_num>=M){ //제거한사람이 M이상이면 방향 바꾸기
      delete_num = 0;
      direction *= -1;
    }

    if(direction==1){ //순방향
      for(int i=0; i<K-1; i++){ //k-1번 동안 앞에걸 뒤로 옮기기
        deq.push_back(deq.front());
        deq.pop_front();
      }
    }
    else{ //역방향
      for(int i=0; i<K; i++){ //k번 동안 뒤에걸 앞으로 옮기기
        deq.push_front(deq.back());
        deq.pop_back();
      }
    }
    
  }


  return 0;
}
