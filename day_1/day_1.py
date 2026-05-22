score = 0
answer_1 = "3"
answer_2 = "2"
answer_3 = "1"

print("다음 단어의 뜻은 무엇일까요? -> 勉強")
print("(1) 말하다 (2) 차이 (3) 공부 (4) 역사 (5) 일")
answer = input("번호를 입력하세요 >> ")
if (answer == answer_1):
    print("정답!")
    score = score + 1
else:
    print("오답!")

print("다음 단어의 뜻은 무엇일까요? -> 基本")
print("(1) 과정 (2) 기본 (3) 일본 (4) 물건 (5) 학교")
answer = input("번호를 입력하세요 >> ")
if (answer == answer_2):
    print("정답!")
    score = score + 1
else:
    print("오답!")

print("다음 단어의 뜻은 무엇일까요? -> 頑張る")
print("(1) 노력하다 (2) 팔다 (3) 빌다 (4) 일어나다 (5) 자다")
answer = input("번호를 입력하세요 >> ")
if (answer == answer_3):
    print("정답!")
    score = score + 1
else:
    print("오답!")

print("최종 점수는 ", score, "입니다!")