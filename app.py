import os
import time

# 디렉터리 위치 변수 설정
위치 = os.path.expanduser('~') + "\\Desktop"
선택된_파일 = None

def show_menu():
    print("================지리는 텍스트 편집기================")
    print("========================메뉴=======================")
    print(f"1. 디렉토리 선택 (현재 위치: {위치})")
    print("2. 파일 선택")
    print("3. 파일 편집")
    print("4. 파일 보기")
    print("5. 파일 생성")
    print("6. 도움말")
    print("7. 종료")
    print("선택하려는 메뉴번호를 입력")
    print("======================================BETA VERSION")

def wait_for_enter():
    print("메뉴 화면으로 가려면 ENTER를 입력")
    while True:
        enser = input(">_")
        if enser == "":
            break

while True:
    show_menu()
    enser = input(">_")

    if enser == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("================지리는 텍스트 편집기================")
        print("========================메뉴=======================")
        print(f"현재 위치: {위치}")
        print("상위 폴더로 가기: back")
        print("현재 폴더에 있는 파일 보기: list")
        print("경로 입력: route")
        print("폴더 이름 입력: openin")
        print("======================================BETA VERSION")
        enser = input(">_")
        
        if enser == "back":
            위치 = os.path.dirname(위치)
            print(f"현재 위치를 {위치}로 변경했습니다")
            wait_for_enter()
        elif enser == "list":
            try:
                files = os.listdir(위치)
                for file in files:
                    print(file)
            except FileNotFoundError:
                print("디렉토리를 찾을 수 없습니다.")
            wait_for_enter()
        elif enser == "route":
            try:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("================지리는 텍스트 편집기================")
                print("========================메뉴=======================")
                print(f"현재 위치: {위치}")
                print("경로 위치 방법: C:\\Users\\a0109\\Desktop\\aaaa")
                print("======================================BETA VERSION")
                enser = input(">_")
                if not os.path.isdir(enser):
                    print("디렉토리를 찾을 수 없습니다.")
                else:
                    위치 = enser
            except Exception as e:
                print(f"알 수 없는 오류: {e}")
            wait_for_enter()
        elif enser == "openin":
            try:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("================지리는 텍스트 편집기================")
                print("========================메뉴=======================")
                print(f"현재 위치: {위치}")
                print("폴더 이름을 입력해주세요")
                print("======================================BETA VERSION")
                folder_name = input(">_")
                new_path = os.path.join(위치, folder_name)
                if os.path.isdir(new_path):
                    위치 = new_path
                else:
                    print("디렉토리를 찾을 수 없습니다.")
            except Exception as e:
                print(f"알 수 없는 오류: {e}")
            wait_for_enter()
        else:
            print("잘못된 입력입니다.")
            wait_for_enter()

    elif enser == "2":
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("================지리는 텍스트 편집기================")
            print("========================파일 선택====================")
            files = [f for f in os.listdir(위치) if os.path.isfile(os.path.join(위치, f))]
            for idx, file in enumerate(files):
                print(f"{idx + 1}. {file}")
            print("열려는 파일 번호를 입력해주세요.")
            file_number = int(input(">_"))
            선택된_파일 = files[file_number - 1]
            print(f"{선택된_파일} 파일이 선택되었습니다.")
        except (IndexError, ValueError):
            print("잘못된 입력입니다.")
        except Exception as e:
            print(f"알 수 없는 오류: {e}")
        wait_for_enter()

    elif enser == "3":
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("================지리는 텍스트 편집기================")
            print("========================파일 편집====================")
            if 선택된_파일 is None:
                print("편집할 파일이 선택되지 않았습니다. 먼저 파일을 선택해주세요.")
            else:
                file_path = os.path.join(위치, 선택된_파일)
                if os.path.isfile(file_path):
                    with open(file_path, 'r', encoding='utf-8') as file:
                        print(file.read())
                    print("텍스트를 입력해주세요. (기존 텍스트는 덮어쓰기됩니다) (변경을 취소하려면 비워두고 ENTER를 누르십시오)")
                    new_content = input()
                    if new_content == "":
                        print("변경을 취소했습니다.")
                    else:
                        with open(file_path, 'w', encoding='utf-8') as file:
                            file.write(new_content)
                        print("파일이 성공적으로 저장되었습니다.")
                else:
                    print("파일을 찾을 수 없습니다.")
        except Exception as e:
            print(f"알 수 없는 오류: {e}")
        wait_for_enter()

    elif enser == "4":
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("================지리는 텍스트 편집기================")
            print("========================파일 보기====================")
            if 선택된_파일 is None:
                print("파일 보기 위해 선택된 파일이 없습니다. 먼저 파일을 선택해주세요.")
            else:
                file_path = os.path.join(위치, 선택된_파일)
                if os.path.isfile(file_path):
                    with open(file_path, 'r', encoding='utf-8') as file:
                        print(file.read())
                else:
                    print("파일을 찾을 수 없습니다.")
        except Exception as e:
            print(f"알 수 없는 오류: {e}")
        wait_for_enter()


    elif enser == "5":
        print("================지리는 텍스트 편집기================")
        print("===================파일 생성=======================")
        print(f"현제 디렉토리에 파일을 생성합니다 현 위치: {위치}")
        print("파일의 이름을 작성해주세요(확장자명 포함)")
        print("======================================BETA VERSION")
        name = input(">_")
        full_path = os.path.join(위치, name)
        try:
            if not os.path.exists(위치):
                os.makedirs(위치)
            with open(full_path, 'w') as file:
                file.write("이 파일은 https://github.com/iwantmunsang/textpy 로 생성 돼었습니다")

            print(f"{full_path} 파일이 성공적으로 생성되었습니다.")
            wait_for_enter()
        except Exception as e:
            print(f"알 수 없는 오류: {e}")
            wait_for_enter()

    elif enser == "6":
        print("================지리는 텍스트 편집기================")
        print("===================파일 생성=======================")
        print("1.디랙토리 선택")
        print("    디랙토리를 선택합니다")
        print("    back을 사용하여 현재 위치의 상위 폴더로 갈수 \n    있습니다")
        print("    list를 사용하여 현재 디랙토리에 있는 파일, 폴더의\n    목록을 봅니다")
        print("    route를 사용하여 자세한 경로를 입력합니다\n    예시 : C:\Program Files\Java\jdk-18")
        print("    openin을 사용하여 현재 디랙토리에 있는 폴더중\n    이름을 입력하여 그 폴더를 위치로 지정합니다")
        print("\n\
    2.파일 선택\n\
        수정할 파일을 선택합니다\n\
    3.파일 편집\n\
        파일의 내용을 편집합니다\n\
    4.파일 보기\n\
        파일을 수정하지 않고 봅니다\n\
    5.파일 생성\n\
        파일을 현재 디랙 토리에 생성합니다\n\
        생성시 기본 글로\n\
        \"이 파일은 https://github.com/iwantmunsang/textpy\n\
        로 생성 돼었습니다\"가 자동으로 적힙니다\n\
    6.도움말\n\
        명령어의 사용법을 알려줍니다\n\
    7.종료\n\
        프로그램을 종료합니다")
        print("======================================BETA VERSION")
        wait_for_enter()

# print("2. 파일 선택")
# print("3. 파일 편집")
# print("4. 파일 보기")
# print("5. 파일 생성")
# print("6. 도움말")
# print("7. 종료

# print("================지리는 텍스트 편집기================")
# print("========================메뉴=======================")
# print(f"현재 위치: {위치}")
# print("상위 폴더로 가기: back")
# print("현재 폴더에 있는 파일 보기: list")
# print("경로 입력: route")
# print("폴더 이름 입력: openin")
# print("======================================BETA VERSION")
        
        

    elif enser == "7":
        print("프로그램을 종료합니다.")
        time.sleep(1)
        break

        
