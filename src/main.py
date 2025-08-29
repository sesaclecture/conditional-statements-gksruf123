# 염한결 과제 제출합니다!
# 시간과 능력 부족으로 인해 로그인 기능까지만 구현하였습니다..

# (1) 초기 사용자 목록 생성

users = {
    # "ID" : {
    #     "name": "",
    #     "birth": "",
    #     "password": "",
    #     "role": ""
    #     },
}

print(users)

# (2) 회원 가입

while True:
    status = int(input("회원 가입은 1번, 로그인은 2번을 눌러주세요."))
    match status:
        case 1:     #회원 가입 선택 시
            while True:     #출생연도
                year = int(input("출생연도 4자리를 입력해 주세요."))
                if 999 < year <= 2026:
                    break
                else:
                    print("잘못 입력하셨습니다. 다시 입력해 주세요.")
            while True:
                month = int(input("생월을 입력해 주세요."))
                if 9 < month <= 12:
                    break
                elif 0 < month <= 9:
                    month = str(0) + str(month)
                    break
                else:
                    print("잘못 입력하셨습니다. 다시 입력해 주세요.")
            while True:
                day = int(input("생일을 입력해 주세요."))
                if 9 < day <= 31:
                    break
                elif 0 < day <= 9:
                    day = str(0) + str(day)
                    break
                else:
                    print("잘못 입력하셨습니다. 다시 입력해 주세요.")
            birth = str(year) + str(month) + str(day)

            while True:     #아이디
                new_id = str(input("아이디를 입력하십시오."))
                if new_id in users:
                    print("사용할 수 없는 아이디입니다.")
                else:
                    break

            name = input("이름을 입력하세요.")     #이름

            while True:     #엄격한 비밀번호
                password = int(input("네 자리 이하의 숫자로만 된 비밀번호를 입력하세요."))
                if 0 > password and password > 10000:
                    print("조건에 맞는 비밀번호를 다시 입력하십시오.")
                else:
                    break

            if password == 0:       #role
                role = "admin"
            elif password%2 == 0:
                role = "editor"
            else:
                role = "viewer"

            users[new_id] = {
                "birth": birth,
                "name": name,
                "password": password,
                "role": role
            }
            print(users)

        case 2:     #로그인 기능
            while True:     # 아이디 확인 절차
                login_id = input("아이디를 입력하세요.")
                if login_id in users:
                    while True:     # 비밀번호 확인 절차
                        login_pd = int(input("비밀번호를 입력하세요."))
                        if login_pd == users[login_id]["password"]:
                            print("로그인되었습니다.")
                            break
                        else:
                            print("잘못되었습니다.")
                    break
                else:
                    print("잘못되었습니다.")

            #여기서부터 로그인 성공 시 추가 기능 넣어야 함.
        case _:
            break