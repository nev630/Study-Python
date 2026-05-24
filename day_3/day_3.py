word_dict = {}

while True:
    print("\n--- 영어 사전에 온 것을 환영합니다. ---")
    menu = input("1. 추가 2. 검색 3. 삭제 4. 종료 >> ")

    if (menu == "1"):
        data = input("추가할 단어와 뜻을 입력하세요 (예: apple 사과) >> ").split()
        if len(data) == 2:
            word_dict[data[0]] = data[1]
            print(f"'{data[0]}' 단어가 추가되었습니다.")
        else:
            print("형식이 올바르지 않습니다.")

    elif (menu == "2"):
        word = input("검색할 단어를 입력하세요: ")
        print(f"뜻: {word_dict.get(word, '찾을 수 없는 단어입니다.')}")

    elif (menu == "3"):
        word = input("삭제할 단어를 입력하세요: ")
        if word in word_dict:
            del word_dict[word]
            print("삭제되었습니다.")
        else:
            print("사전에 없는 단어입니다.")

    else:
        choice = input("프로그램을 종료하시겠습니까? (y / n) >>")
        if (choice == "y"):
            break
        elif (choice == "n"):
            continue