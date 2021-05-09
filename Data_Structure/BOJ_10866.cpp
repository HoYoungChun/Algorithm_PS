#include <bits/stdc++.h>
using namespace std;

int main()
{
  ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
  deque <int> deq;
  int N; cin >> N;
  while(N--){
    string s; cin >> s;
    if(s == "push_front"){
      int num; cin >> num;
      deq.push_front(num);
    }
    else if(s == "push_back"){
      int num; cin >> num;
      deq.push_back(num);
    }
    else if(s == "front"){
      if(!deq.empty())
        cout<<deq.front()<<"\n";
      else
        cout<<-1<<"\n";
    }
    else if(s == "back"){
      if(!deq.empty())
        cout<<deq.back()<<"\n";
      else
        cout<<-1<<"\n";
    }
    else if(s == "size"){
      cout<<deq.size()<<"\n";
    }
    else if(s == "empty"){
      if(deq.empty()) cout<< 1 <<"\n";
      else cout<< 0 <<"\n";
    }
    else if(s == "pop_front"){
      if(deq.empty()) cout<< -1 <<"\n";
      else{
        cout<< deq.front() <<"\n";
        deq.pop_front();
      }
    }
    else if(s == "pop_back"){
      if(deq.empty()) cout<< -1 <<"\n";
      else{
        cout<< deq.back() <<"\n";
        deq.pop_back();
      }
    }
  }

  return 0;
}
