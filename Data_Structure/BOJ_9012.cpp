#include <bits/stdc++.h>
using namespace std;

int main()
{
  ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
  int T; cin>>T; //테스트케이스

  while(T--){
    stack<char> stck;
    bool ans = true;
    string s; cin >> s;
    
    for(int i=0; i<s.length(); i++){ //문자열 전체탐색
      //'('일때
      if(s[i]=='('){
        stck.push('(');
      }
      //')'일때
      else{
        if(stck.empty()){ //스택이 비었으면
          ans = false;
          break;
        }
        else{
          stck.pop();
        }
      }
    }

    if(!stck.empty()) //문자열 다 탐색했는데, 스택이 비지 않았으면
      ans = false;
    
    if(ans) cout<<"YES"<<"\n";
    else cout<<"NO"<<"\n";

  }
  
  return 0;
}
