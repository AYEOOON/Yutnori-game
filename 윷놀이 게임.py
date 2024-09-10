import random

# 현재 user의 정보를 저장할 dictionary
# 0: 상대방, 1: 당신
# 각각 user, score을 저장
current = {
  0: {"user": "상대방", "score": 0},
  1: {"user": "당신", "score": 0}
}

# 1 ~ 5점에 따른 윷 결과
yut = {1: "도", 2: "개", 3: "걸", 4: "윷", 5: "모"}

# 상대방과 당신의 순서를 확인할 변수
count = 0

while True:
  # 0, 1 번갈아서 윷을 던지므로 % 2 연산을 하여 순서를 구함
  order = count % 2
  
  # 윷을 던짐
  # random.randint(1, 5)를 사용하여 1부터 5사이의 랜덤한 값을 구함 
  throw = random.randint(1, 5)
  # 엔터키를 눌렀을 때, 조건에 맞게 출력
  input('')
  print("\">>> {}이 윷을 던졌습니다\"".format(current[order]["user"]))
  print(" ")

  # 현재 순서의 점수의 누적합을 구함
  current[order]["score"] += throw
  # 엔터키를 눌렀을 때, 조건에 맞게 출력
  input('')
  print("\"{}! {}점을 획득하여 {}의 점수는 현재 {}점 입니다\"".format(yut[throw], throw, current[order]["user"], current[order]["score"]))
  print(" ")

  # 현재 순서의 점수가 30점 이상이면 우승자와 상대방의 점수를 출력하고 while문 탈출
  if current[order]["score"] >= 30:
    # 윷놀이 게임에서 진 사람을 담은 변수
    lose = (count + 1) % 2
    input('')
    print("\">>> {}이 이겼습니다! {}의 점수는 {}점입니다.\"".format(current[order]['user'], current[lose]['user'], current[lose]["score"]))  
    break

  # 윷, 모가 나올 경우 순서를 바꾸지 않고 한번 더 출력할 수 있다는 문장을 출력하고 while문 다시 진행
  if throw == 4 or throw == 5:
    print("\"한번 더 던질 기회가 주어집니다.\"")
    print(" ")
  # 윷, 모가 아닌 경우 순서를 바꿈
  else:    
    count += 1
