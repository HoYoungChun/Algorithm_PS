#include <bits/stdc++.h>
using namespace std;

int main()
{
  ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
  queue <int> que;
  int N; cin >> N;
  while(N--){
    string s; cin >> s;
    if(s == "push"){
      int num; cin >> num;
      que.push(num);
    }
    else if(s == "front"){
      if(!que.empty())
        cout<<que.front()<<"\n";
      else
        cout<<-1<<"\n";
    }
    else if(s == "back"){
      if(!que.empty())
        cout<<que.back()<<"\n";
      else
        cout<<-1<<"\n";
    }
    else if(s == "size"){
      cout<<que.size()<<"\n";
    }
    else if(s == "empty"){
      if(que.empty()) cout<< 1 <<"\n";
      else cout<< 0 <<"\n";
    }
    else{
      if(que.empty()) cout<< -1 <<"\n";
      else{
        cout<< que.front() <<"\n";
        que.pop();
      }
    }
  }

  return 0;
}
