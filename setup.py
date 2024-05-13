import os
import subprocess
import webbrowser

# 메인 메뉴
def show_menu():
    print()
    print("*"*50)
    print()
    print("조선대학교 AISW 교육센터")
    print()
    print("1. 스파이크 프라임 2.0.10 설치")
    print()
    print("2. 레고 마인드 스톰 다운로드(Microsoft Store)")
    print()
    print("3. 파이썬 3.12 다운로드")
    print()
    print("4. matplotlib 라이브러리 설치")
    print()
    print("5. matplotlib 라이브러리 제거")
    print()
    print("6. (강사전용)디지털새싹 URL 모음")
    print()
    print("0. 종료")
    print()
    print()
    print("*"*50)

def menu1():
    webbrowser.open("https://bit.ly/spike2")

def menu2():
    webbrowser.open("https://bit.ly/get_mindstorms")

def menu3():
    clear_screen()
    webbrowser.open("https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe")
    print()
    print("파이썬 3.12를 다운로드하고 설치하는 방법을 안내합니다.")
    print()
    print("1. 다운로드 된 파일을 실행합니다.")
    print()
    print("2. 아래의 ""Add python.exe to PATH""를 선택 후 ""Customize installation""을 클릭합니다.")
    print()
    print("3. Optional Features는 수정하지 않고, Next를 클릭합니다.")
    print()
    print("4. ""Install Python 3.12 for all users""를 체크합니다.")
    print()
    print("5. ""Customize install location""을 ""C:\\Python312""로 변경 후 ""Install""을 클릭합니다.")
    print()
    print("6. ""Setup was successful""이 나오면 ""Close""를 눌러 종료합니다.")
    print()


def menu4():
    clear_screen()
    result = check_matplotlib_installed()
    if result == 0:
        print("matplotlib를 설치합니다.")
        subprocess.run(["pip", "install", "matplotlib"])
    elif result == 1:
        print("matplotlib가 이미 설치되어 있습니다.")

def menu5():
    clear_screen()
    result = check_matplotlib_installed()
    if result == 1:
        print("matplotlib를 제거합니다.")
        print("Proceed (Y/n)?이 나오면 Y를 입력 후 Enter키를 입력해주세요.")
        subprocess.run(["pip", "uninstall", "matplotlib"])
    elif result == 0:
        print("matplotlib가 설치되어 있지 않습니다.")

def menu7():
    while True:
        clear_screen()
        print("강사 코드를 입력해주세요.\n뒤로가기 : 0\n")
        paassword = input("강사인증코드 >> ")
        if paassword == 'chosunaisw':
            print()
            print("디지털새싹 URL 모음을 실행합니다.")
            print()
            clear_screen()
            webbrowser.open("https://bit.ly/chosun_aisw")
            break
        elif paassword == '0':
            break
        else:
            print("잘못된 강사 코드입니다.")
            clear_screen()
    

def check_matplotlib_installed():
    try:
        result = subprocess.run(['pip', 'freeze'], capture_output=True, text=True)
        installed_packages = result.stdout.split('\n')
        for package in installed_packages:
            if package.startswith('matplotlib'):
                return 1
        return 0  
    except Exception as e:
        print(f"오류 발생: {e}")
        return -1

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    while True:
        show_menu()
        select = input("원하는 작업의 메뉴를 입력해주세요: ")

        # 스파이크 프라임 설치
        if select == '1':
            menu1()
            input("엔터를 누르면 계속합니다.")
            clear_screen()
        # 레고 마인드 스톰 다운로드
        elif select == '2':
            menu2()
            input("엔터를 누르면 계속합니다.")
            clear_screen()
        # 파이썬 3.12 다운로드
        elif select == '3':
            menu3()
            input("엔터를 누르면 계속합니다.")
            clear_screen()
        # 파이썬 matplotlib 라이브러리 설치
        elif select == '4':
            menu4()
            input("엔터를 누르면 계속합니다.")
            clear_screen()
        # matplotlib 라이브러리 제거
        elif select == '5':
            menu5()
            input("엔터를 누르면 계속합니다.")
            clear_screen()
        # 강사 전용
        elif select == '6':
            menu7()
            input("엔터를 누르면 계속합니다.")
            clear_screen()
        # 종료
        elif select == '0':
            break
        # 다른 입력
        else:
            print("잘못된 입력입니다. 다시 시도해주세요.")
            input("엔터를 누르면 계속합니다.")
            clear_screen()
