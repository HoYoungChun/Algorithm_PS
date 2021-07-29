## 7/29(목) algorithm 스터디 - 문자열 조작
### 1. 유효한 팰린드롬
*  isalnum()은 영문자, 숫자 여부를 판별(isalpha(), isdigit()는 영문자만, 숫자만 판별)
```python
if one_s.isalnum(): #숫자거나 문자일때만
```

*  파이썬의 리스트는 pop() 함수에서 인덱스를 지정할 수 있고, 0을 지정하면 맨 앞의 값을 가져옴
*  list의 pop(0)은 O(n)이고, deque의 popleft()는 O(1)
*  [::-1]로 뒤집기. [:]를 통해 참조가 아닌 값을 복사
```python
str1 = "abcd"
str2 = str1[::-1] # "dcba" 참조
str3 = str1 #같은 객체 참조
str4 = str1[:] #새로운 객체 참조
```
*  슬라이싱은 매우 빠르게 동작
*  정규표현식으로 문자,숫자만 남기기
```python
s = re.sub('[^a-z0-9]','',s) 
```
*  [파이썬 메소드마다의 시간복잡도](https://wayhome25.github.io/python/2017/06/14/time-complexity)


### 2. 문자열 뒤집기
* s[:] = s[::-1]은 같은 객체에서 내용이 바뀌고, s=s[::-1]은 새로운 객체가 할당
```python
s=['h','e','l','l','o']
s = s[::-1] #새로운 객체 참조
s[:] = s[::-1] #같은 객체에서 내용변경
```
*  [reverse와 reversed의 차이](https://itholic.github.io/python-reverse-reversed/)


### 3. 로그 파일 재정렬
* lambda함수 구현
```python
letters.sort(key=lambda x: (x.split()[1:], x.split()[0])) # 첫번째 비교대상이 리스트
```
* map, reduce, filter 함수
```python
map(함수, 리스트) : 리스트로부터 원소를 하나씩 꺼내서 함수를 적용시킨 다음, 그 결과를 새로운 리스트에 담기
reduce(함수, 시퀀스) : 시퀀스(문자열, 리스트, 튜플)의 원소들을 누적적으로 함수에 적용
filter(함수, 리스트) : 리스트에 들어있는 원소들을 함수에 적용시켜서 결과가 참인 값들로 새로운 리스트 만들기

```


### 4. 가장 흔한 단어
* 정규식에서 \w는 단어 문자를 뜻하며, ^는 not을 의미한다.
```python
re.sub(r'[^\w]',' ',paragraph) #단어 문자를 제외하고 모두 공백으로 바꾸기
```
* 딕셔너리 변수에서 값이 가장 큰 키를 가져올때, max 함수에 key로 get함수를 넣어서 가져온다.
```python
max(counts,key=counts.get)
```
* defaultdict(int)는 기본값이 0이다. int가 아닌 list와 set은 기본값이 []와 ()이다.
* Counter객체를 통해 항목의 개수를 셀 수 있다.
* Counter객체에 most_common(1)로 가장 많이 등장하는 항목을 추출할 수 있다.
```python
words = [1,2,1,1,3,2]
counts = collections.Counter(words)
return counts.most_common(1)[0][0]
```


### 5. 그룹 애너그램
* dictionary의 key는 immutable 자료형만 가능하다.(string, int, tuple) cf. mutable: (list, dictionary)
* immutable 객체는 call by reference, mutable 객체는 call by value로 동작한다.
* sorted()에 문자열을 전달하면 결과를 리스트로 전달해서 join()으로 합쳐야 한다.
```python
str="hello"
''.join(sorted(str)) #ehllo
```
* 리스트 자료형에 제공되는 sort()는 제자리 정렬로 입력을 출력이 덮어 씌우고, sorted()는 정렬 결과를 별도로 리턴한다.
* sort()와 sorted() 모두 key 옵션을 통해 정렬을 위한 함수를 지정할 수 있다. 일반 함수 또는 lambda함수를 이용할 수 있다.
* 파이썬의 기본정렬은 팀소트(Timsort)를 이용한다.
* [정렬 종류별로 시간복잡도 + 각 특징 정리](https://velog.io/@wan088/%EC%A0%95%EB%A0%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%A0%95%EB%A6%AC)


### 6. 가장 긴 팰린드롬 부분 문자열
* 투 포인터를 이용하는 방식
* 최장 공통 부분 문자열(Longest Common Substring) with 다이나믹 프로그래밍
* 유니코드와 UTF-8 관련 내용

