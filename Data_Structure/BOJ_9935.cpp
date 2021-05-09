#include <bits/stdc++.h>
using namespace std;

int main()
{
  ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
  string str, bomb; cin >> str >> bomb;
  stack<char>stck;

  for(int i=0; i<str.length(); i++){ //문자열 전체 탐색
    stck.push(str[i]);
    if(str[i] == bomb.back()){
      int idx = bomb.length()-1;
      bool okay = true;

      for(; idx>=0 && !stck.empty(); idx--){
        if(stck.top() != bomb[idx]){
          okay=false; break;
        }
        else
          stck.pop();
      }

      if(idx>=0) okay = false;

      if(!okay){
        for(int i=idx+1;i<bomb.length(); i++)
          stck.push(bomb[i]);
      }
    }
  }

  string ans = "";
  while(!stck.empty()){
    ans += stck.top();
    stck.pop();
  }
  reverse(ans.begin(), ans.end());

  if(ans=="") ans="FRULA";
  cout<< ans <<"\n";

  return 0;
}
