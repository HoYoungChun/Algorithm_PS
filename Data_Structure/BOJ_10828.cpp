#include <bits/stdc++.h>
using namespace std;

int main()
{
  ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
  stack<int> stck;
  int N; cin >> N;
  while(N--){
    string s; cin >> s;
    if(s == "push"){
      int num; cin >> num;
      stck.push(num);
    }
    else if(s == "top"){
      if(!stck.empty())
        cout<<stck.top()<<"\n";
      else
        cout<<-1<<"\n";
    }
    else if(s == "size"){
      cout<<stck.size()<<"\n";
    }
    else if(s == "empty"){
      if(stck.empty()) cout<< 1 <<"\n";
      else cout<< 0 <<"\n";
    }
    else{
      if(stck.empty()) cout<< -1 <<"\n";
      else{
        cout<< stck.top() <<"\n";
        stck.pop();
      }
    }
  }

  return 0;
}
