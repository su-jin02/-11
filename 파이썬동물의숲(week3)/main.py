import time
import random

print("""
  ___          _                    _   _____                         _               
 / _ \        (_)                  | | /  __ \                       (_)              
/ /_\ \ _ __   _  _ __ ___    __ _ | | | /  \/ _ __   ___   ___  ___  _  _ __    __ _ 
|  _  || '_ \ | || '_ ` _ \  / _` || | | |    | '__| / _ \ / __|/ __|| || '_ \  / _` |
| | | || | | || || | | | | || (_| || | | \__/\| |   | (_) |\__ \\__ \| || | | || (_| |
\_| |_/|_| |_||_||_| |_| |_| \__,_||_|  \____/|_|    \___/ |___/|___/|_||_| |_| \__, |
                                                                                 __/ |
                                                                                |___/ 
""")
print("~ 모여봐요 멋사의 숲 ~\n")

name = input("이름을 입력해달라구리 : ")
island = input("섬 이름을 입력해달라구리 : ")

print(name + "님 반가워요! " + island + "섬에 오신것을 환영합니다-!")
time.sleep(1)

animal = {'릴리안': 0, '탁호': 0, '미첼': 0, '리처드': 0}
animals = list(animal.items())
my_bell = 3000
my_pocket = []
store = {'가습기': 1400, '강아지 인형': 2400, '강의실 책상': 2500, '몬스테라': 1700}

action_boolean = 1

# 4가지 반복하기
while action_boolean:
    print("\n어떤 것을 해볼까요?")
    answer_action = input("0. 종료 1. 상점가기 2. 주민 찾아가기 3. 나무 흔들기 4. 정보 확인하기 ")
    time.sleep(1)

    # 0. 게임 종료
    if answer_action == "0":
        print("게임이 종료되었습니다")
        action_boolean=0
        time.sleep(1)


    # 1. 상점가기를 선택한경우
    elif answer_action == "1":
        print("상점에 온걸 환영해구리")
        print("현재 상점에는 이런 물건들이 있어구리 \n")
        item = list(store.items())
        for i in range(len(item)):
            print(i+1 , ".", item[i][0], ": " , item[i][1])
        a = input("\n어떤 물건을 구입하겠어구리? (숫자로 입력) : ")
        price = item[int(a)-1][1]
        if(price > my_bell):
            print("돈이 부족해서 못산다구리")
        else:
            print(item[int(a)-1][0]+"을(를) 구입하셨습니다!")
            my_pocket.append(item[int(a)-1][0])
            my_bell -= item[int(a)-1][1]
            print("남은 벨:", my_bell)
            del store[item[int(a)-1][0]]
        time.sleep(1)


    # 2. 주민 찾아가기를 선택한 경우
    elif answer_action == "2":
        print("우리 마을에 있는 주민이야")
        for i in range(4):
            print(i+1 , ".", animals[i][0])
        number = input("어떤 주민을 찾아갈까? ")
        number = int(number)
        print(animals[number-1][0], "에게 무엇을 할까?")
        answer_animal_action = input("1. 말걸기 2. 선물하기 3. 떄리기 ")
        time.sleep(1)


        # 2-1. 말걸기를 선택한경우
        if answer_animal_action == "1":
            if(number == 1):
                animal["릴리안"] += 1
                print("어머",name, "왔구나! 반가워!")
                print("어제는 어찌나 벚꽃이 이쁘던지 기분이 참 좋더라니까")
                print(name + "도 놀러다녀오는 건 어때?")
            elif(number == 2):
                animal["탁호"] += 1
                print("안녀엉" , name, " 나는 탁호약히 \n오늘 저녁은 뭘 먹을지 너무 고민이 돼~ 약히")
            elif(number == 3):
                animal["미첼"] += 1
                print(name + "아~! 반가워~! 오늘 날씨 되게 좋지않아?")
                print("마구마구 산책을 하고 싶어져 동글")
            elif (number == 4):
                animal["리처드"] += 1
                print(name + "야아~")
                print("나무를 흔들었더니 100벨이 나왔어어~")
                print(name + "도 한 번 흔들어봐아~ 그래유")
            print(animals[number-1][0], "와(과) 친밀도가 1 상승했다구리")
            time.sleep(1)


        # 2-1. 선물하기를 선택한 경우
        elif answer_animal_action == "2":
            if(len(my_pocket) > 0):
                print("내 주머니엔 이렇게 있어")
                for i in range(len(my_pocket)):
                    print(i + 1, ".", my_pocket[i])
                pocketnum = input("어떤 것을 선물할까? (숫자로 입력) ")
                pocketnum = int(pocketnum)
                print(animals[number-1][0], "에게", my_pocket[pocketnum-1],"을(를) 선물했다!")
                del my_pocket[pocketnum-1]
                print(animals[number - 1][0], "과 친밀도가 5 상승했다구리")
                animal[animals[number-1][0]] +=5
            else:
                print("선물이 불가능하다구리")
            time.sleep(1)


        # 2-3. 떄리기를 선택한 경우
        elif answer_animal_action == "3":
            print(animals[number - 1][0], "을(를) 때렸다!!")
            print("아야아아 왜 그러는거야 ㅡㅡ")
            print(animals[number - 1][0], "과 친밀도가 1 감소했다구리")
            animal[animals[number - 1][0]] -= 1
            time.sleep(1)




    # 3. 나무 흔들기를 선택한 경우
    elif answer_action == "3":
        shake = ["100벨", "사과", "벌"]
        result = random.choice(shake)

        print("나무를 흔듭니다\n응..?")

        # 100벨이 떨어질경우
        if result == "100벨":
            my_bell += 100
            print("100벨이 떨어졌다구리!!\n100벨을 획득했다구리!!")

        # 사과가 떨어질경우
        elif result == "사과":
            my_pocket.append("사과")
            print("사과가 떨어졌다구리!!\n사과를 획득했다구리!!")

        # 벌이 나타날경우
        elif result == "벌":
            print("벌이 나타났습니다\n아야.. 벌에게 물렸어..")
        time.sleep(1)




    # 4. 정보보기를 선택한 경우
    elif answer_action == "4":
        # 이름 출력
        print("이름: " + name)
        # 남은 벨 출력
        print("벨: " + str(my_bell) + "벨")
        # 주머니 출력
        print("주머니: ")
        if(len(my_pocket) > 0):
            for i in my_pocket:
                print(my_pocket)
        else:
            print("주머니가 비었다구리")
        # 주민 친밀도 출력
        print("주민 친밀도: ")
        for i,j in animal.items():
            print(i,":",j)
        time.sleep(1)

        # 잘못된 입력을 했을경우
    else:
        print("잘못된 입력입니다. 다시 입력해주세요.")

