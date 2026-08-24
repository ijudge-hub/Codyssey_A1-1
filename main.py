# 프로그램에서 사용할 카테고리 목록입니다.
# 여러 개의 카테고리를 순서대로 관리하기 위해 리스트를 사용합니다.
categories = [
    "텍스트 생성",
    "이미지 생성",
    "영상 생성",
    "페르소나",
    "자동화",
    "기타",
]


# 프로그램을 시작할 때 기본으로 등록되는 프롬프트 목록입니다.
# 여러 개의 프롬프트를 저장하기 위해 리스트를 사용합니다.
# 각각의 프롬프트는 제목, 내용, 카테고리, 즐겨찾기 상태를
# 하나로 묶어서 관리하기 위해 딕셔너리로 저장합니다.
prompts = [
    {
        # 프롬프트의 이름입니다.
        "title": "블로그 글 작성 도우미",

        # AI에게 전달할 실제 프롬프트 내용입니다.
        "content": (
            "당신은 10년 경력의 전문 블로거입니다. "
            "주어진 주제에 대해 서론, 본론, 결론 구조의 "
            "블로그 글을 작성해주세요."
        ),

        # 프롬프트가 속하는 분류입니다.
        "category": "텍스트 생성",

        # 즐겨찾기 여부입니다.
        # False는 아직 즐겨찾기에 등록되지 않았다는 뜻입니다.
        "favorite": False,
    },
    {
        "title": "제품 썸네일 생성",
        "content": (
            "제품의 특징이 잘 보이도록 밝고 선명한 "
            "온라인 쇼핑몰용 썸네일 이미지를 만들어주세요."
        ),
        "category": "이미지 생성",
        "favorite": False,
    },
    {
        "title": "IT 컨설턴트 페르소나",
        "content": (
            "당신은 15년 경력의 IT 컨설턴트입니다. "
            "사용자의 문제를 분석하고 이해하기 쉬운 해결책을 제안해주세요."
        ),
        "category": "페르소나",
        "favorite": False,
    },
]

# 사용자에게 값을 입력받고, 빈 값인지 확인하는 함수입니다.
# message에는 "제목: "처럼 사용자에게 보여줄 안내 문구가 들어옵니다.
def get_non_empty_input(message):
    # 올바른 값이 입력될 때까지 계속 반복합니다.
    while True:
        # input()으로 값을 입력받습니다.
        # strip()은 입력값 앞뒤의 불필요한 공백을 제거합니다.
        value = input(message).strip()

        # value에 글자가 하나라도 있으면 정상적인 입력입니다.
        if value:
            # 정상 입력값을 함수를 호출한 곳으로 돌려줍니다.
            return value

        # 아무것도 입력하지 않았거나 공백만 입력한 경우 안내합니다.
        print("입력값을 비워둘 수 없습니다. 다시 입력해주세요.")


# 사용자에게 카테고리 목록을 보여주고 선택받는 함수입니다.
def select_category():
    print("\n=== 카테고리 선택 ===")

    # enumerate()는 리스트의 순서와 값을 함께 가져옵니다.
    # start=1을 사용하여 화면 번호가 1부터 시작하게 합니다.
    for number, category in enumerate(categories, start=1):
        print(f"{number}. {category}")

    # 기본 목록에 없는 카테고리를 직접 입력할 수 있는 메뉴입니다.
    direct_input_number = len(categories) + 1
    print(f"{direct_input_number}. 직접 입력")

    # 정상적인 카테고리를 선택할 때까지 반복합니다.
    while True:
        choice = input("카테고리 번호 선택: ").strip()

        # isdigit()은 입력값이 숫자로만 구성되어 있는지 확인합니다.
        if choice.isdigit():
            # input()의 결과는 문자열이므로 int()로 정수로 바꿉니다.
            category_number = int(choice)

            # 1부터 기본 카테고리 개수까지 선택한 경우입니다.
            if 1 <= category_number <= len(categories):
                # 리스트 번호는 0부터 시작하므로 1을 빼서 접근합니다.
                return categories[category_number - 1]

            # 마지막 번호를 선택하면 카테고리를 직접 입력받습니다.
            if category_number == direct_input_number:
                return get_non_empty_input("새 카테고리 이름: ")

        # 숫자가 아니거나 메뉴 범위를 벗어난 경우 안내합니다.
        print("잘못된 선택입니다. 화면에 표시된 번호를 입력해주세요.")


# 새로운 프롬프트를 등록하는 함수입니다.
def add_prompt():
    print("\n=== 프롬프트 추가 ===")

    # 제목과 내용은 빈 값이 허용되지 않으므로 검증 함수를 사용합니다.
    title = get_non_empty_input("제목: ")
    content = get_non_empty_input("내용: ")

    # 카테고리는 카테고리 선택 함수를 통해 입력받습니다.
    category = select_category()

    # 새 프롬프트 한 개를 딕셔너리로 만듭니다.
    new_prompt = {
        "title": title,
        "content": content,
        "category": category,

        # 새로 추가한 프롬프트는 즐겨찾기가 아닌 상태로 시작합니다.
        "favorite": False,
    }

    # append()는 리스트의 마지막에 새로운 데이터를 추가합니다.
    prompts.append(new_prompt)

    print(f"\n'{title}' 프롬프트가 추가되었습니다.")
    print(f"현재 총 {len(prompts)}개의 프롬프트가 있습니다.")
# 사용자에게 프로그램의 메뉴를 보여주는 함수입니다.
# 함수는 특정 기능을 하나로 묶어 필요할 때 다시 사용할 수 있게 합니다.
# 현재 저장된 모든 프롬프트를 목록으로 출력하는 함수입니다.
def show_list():
    print("\n=== 프롬프트 목록 ===")

    # 리스트가 비어 있으면 False로 판단됩니다.
    # 저장된 프롬프트가 하나도 없을 때 안내하고 함수를 종료합니다.
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    # enumerate()를 사용하여 프롬프트 번호와 데이터를 함께 가져옵니다.
    # start=1을 사용하여 사용자가 보는 번호는 1부터 시작합니다.
    for number, prompt in enumerate(prompts, start=1):
        # favorite 값이 True이면 별표를 표시하고,
        # False이면 빈 문자열을 사용하여 아무것도 표시하지 않습니다.
        favorite_mark = "⭐" if prompt["favorite"] else ""

        # 딕셔너리에서 카테고리와 제목을 꺼내 목록 한 줄을 출력합니다.
        print(
            f"{number}. "
            f"[{prompt['category']}] "
            f"{prompt['title']} "
            f"{favorite_mark}"
        )

    # len()으로 전체 프롬프트 개수를 계산하여 출력합니다.
    print(f"총 {len(prompts)}개의 프롬프트가 있습니다.")
    # 사용자가 선택한 카테고리에 해당하는 프롬프트만 출력하는 함수입니다.
def show_by_category():
    print("\n=== 카테고리별 조회 ===")

    # 기존의 카테고리 선택 함수를 실행하여 사용자의 선택을 받습니다.
    selected_category = select_category()

    # 선택한 카테고리에 해당하는 프롬프트를 저장할 빈 리스트입니다.
    matched_prompts = []

    # 전체 프롬프트를 하나씩 확인합니다.
    for prompt in prompts:
        # 현재 프롬프트의 카테고리가 사용자가 선택한 카테고리와
        # 같은지 비교합니다.
        if prompt["category"] == selected_category:
            # 카테고리가 같으면 결과 리스트에 추가합니다.
            matched_prompts.append(prompt)

    # 해당 카테고리의 프롬프트가 하나도 없는 경우입니다.
    if not matched_prompts:
        print(f"'{selected_category}' 카테고리의 프롬프트가 없습니다.")
        return

    print(f"\n[{selected_category}] 카테고리 프롬프트:")

    # 검색된 프롬프트를 번호와 함께 출력합니다.
    for number, prompt in enumerate(matched_prompts, start=1):
        # favorite 값에 따라 즐겨찾기 별표를 표시합니다.
        favorite_mark = "⭐" if prompt["favorite"] else ""

        print(f"{number}. {prompt['title']} {favorite_mark}")

    # 선택한 카테고리에 포함된 프롬프트 개수를 출력합니다.
    print(f"총 {len(matched_prompts)}개의 프롬프트가 있습니다.")


# 제목 또는 내용에 검색어가 포함된 프롬프트를 찾는 함수입니다.
def search_prompt():
    print("\n=== 프롬프트 검색 ===")

    # 검색어를 입력받고 빈 값인지 검사합니다.
    keyword = get_non_empty_input("검색어: ")

    # 영어 검색 시 대소문자를 구분하지 않도록 소문자로 바꿉니다.
    lowered_keyword = keyword.lower()

    # 검색 결과를 저장할 빈 리스트입니다.
    search_results = []

    # 모든 프롬프트를 하나씩 확인합니다.
    for prompt in prompts:
        # 제목과 내용을 소문자로 바꿉니다.
        lowered_title = prompt["title"].lower()
        lowered_content = prompt["content"].lower()

        # 검색어가 제목 또는 내용에 포함되면 결과에 추가합니다.
        if (
            lowered_keyword in lowered_title
            or lowered_keyword in lowered_content
        ):
            search_results.append(prompt)

    # 검색 결과가 없으면 안내하고 함수를 종료합니다.
    if not search_results:
        print(f"'{keyword}'에 대한 검색 결과가 없습니다.")
        return

    print("\n검색 결과:")

    # 검색 결과를 번호와 함께 출력합니다.
    for number, prompt in enumerate(search_results, start=1):
        # 즐겨찾기 상태에 따라 별표를 표시합니다.
        favorite_mark = "⭐" if prompt["favorite"] else ""

        print(
            f"{number}. "
            f"[{prompt['category']}] "
            f"{prompt['title']} "
            f"{favorite_mark}"
        )

    # 검색 결과의 개수를 출력합니다.
    print(f"총 {len(search_results)}개의 프롬프트를 찾았습니다.")

# 사용자가 선택한 프롬프트의 전체 내용을 보여주는 함수입니다.
def show_detail():
    print("\n=== 프롬프트 상세 보기 ===")

    # 프롬프트가 하나도 없으면 선택할 수 없으므로 안내하고 종료합니다.
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    # 사용자가 번호를 확인할 수 있도록 전체 목록을 먼저 보여줍니다.
    show_list()

    # 상세하게 확인할 프롬프트 번호를 입력받습니다.
    choice = input("상세 보기 번호 입력: ").strip()

    # isdigit()으로 입력값이 숫자인지 확인합니다.
    if not choice.isdigit():
        print("프롬프트 번호는 숫자로 입력해주세요.")
        return

    # 입력받은 문자열을 정수로 변환합니다.
    prompt_number = int(choice)

    # 입력한 번호가 실제 프롬프트 범위에 포함되는지 확인합니다.
    if not 1 <= prompt_number <= len(prompts):
        print(f"1부터 {len(prompts)}까지의 번호를 입력해주세요.")
        return

    # 리스트의 순서는 0부터 시작하므로 입력 번호에서 1을 뺍니다.
    selected_prompt = prompts[prompt_number - 1]

    # 즐겨찾기 상태를 사용자가 이해하기 쉬운 문구로 바꿉니다.
    if selected_prompt["favorite"]:
        favorite_text = "등록됨 ⭐"
    else:
        favorite_text = "등록되지 않음"

    # 선택한 프롬프트의 전체 정보를 출력합니다.
    print("\n" + "─" * 40)
    print(f"제목: {selected_prompt['title']}")
    print(f"카테고리: {selected_prompt['category']}")
    print(f"즐겨찾기: {favorite_text}")
    print("─" * 40)
    print("내용:")
    print(selected_prompt["content"])
    print("─" * 40)

    # 선택한 프롬프트의 즐겨찾기 상태를 추가하거나 해제하는 함수입니다.
def toggle_favorite():
    print("\n=== 즐겨찾기 관리 ===")

    # 프롬프트가 하나도 없으면 선택할 수 없으므로 안내하고 종료합니다.
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    # 사용자가 번호를 확인할 수 있도록 전체 목록을 먼저 보여줍니다.
    show_list()

    # 즐겨찾기 상태를 변경할 프롬프트 번호를 입력받습니다.
    choice = input("프롬프트 번호 입력: ").strip()

    # 입력값이 숫자인지 확인합니다.
    if not choice.isdigit():
        print("프롬프트 번호는 숫자로 입력해주세요.")
        return

    # 문자열로 입력된 번호를 정수로 변환합니다.
    prompt_number = int(choice)

    # 번호가 실제 프롬프트 범위 안에 있는지 확인합니다.
    if not 1 <= prompt_number <= len(prompts):
        print(f"1부터 {len(prompts)}까지의 번호를 입력해주세요.")
        return

    # 리스트는 0부터 시작하므로 입력한 번호에서 1을 뺍니다.
    selected_prompt = prompts[prompt_number - 1]

    # not 연산자를 사용하여 현재 즐겨찾기 상태를 반대로 바꿉니다.
    # False는 True로, True는 False로 변경됩니다.
    selected_prompt["favorite"] = not selected_prompt["favorite"]

    # 변경된 즐겨찾기 상태에 따라 다른 안내 문구를 출력합니다.
    if selected_prompt["favorite"]:
        print(
            f"'{selected_prompt['title']}' 프롬프트를 "
            "즐겨찾기에 추가했습니다."
        )
    else:
        print(
            f"'{selected_prompt['title']}' 프롬프트의 "
            "즐겨찾기를 해제했습니다."
        )
    # print() 함수로 프로그램 이름과 각 메뉴 항목을 출력합니다.
    # 사용자에게 프로그램의 메뉴를 보여주는 함수입니다.
# 즐겨찾기로 등록된 프롬프트만 모아서 보여주는 함수입니다.
def show_favorites():
    print("\n=== 즐겨찾기 목록 ===")

    # 즐겨찾기로 등록된 프롬프트를 저장할 빈 리스트입니다.
    favorite_prompts = []

    # 전체 프롬프트를 하나씩 확인합니다.
    for prompt in prompts:
        # favorite 값이 True인 프롬프트만 결과 리스트에 추가합니다.
        if prompt["favorite"]:
            favorite_prompts.append(prompt)

    # 즐겨찾기된 프롬프트가 하나도 없으면 안내하고 종료합니다.
    if not favorite_prompts:
        print("즐겨찾기된 프롬프트가 없습니다.")
        return

    # 즐겨찾기된 프롬프트를 번호와 함께 출력합니다.
    for number, prompt in enumerate(favorite_prompts, start=1):
        print(
            f"{number}. "
            f"[{prompt['category']}] "
            f"{prompt['title']} ⭐"
        )

    # 즐겨찾기로 등록된 프롬프트의 개수를 출력합니다.
    print(f"총 {len(favorite_prompts)}개의 즐겨찾기가 있습니다.")


# 사용자에게 프로그램의 메뉴를 보여주는 함수입니다.
def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")

    # input() 함수는 사용자가 키보드로 입력한 값을 받습니다.
    # 입력받은 값은 문자열 형태로 choice 변수에 저장됩니다.
    choice = input("선택: ")

    # 사용자가 입력한 메뉴 번호를 함수 밖으로 전달합니다.
    return choice


# 프로그램의 전체 실행 흐름을 관리하는 함수입니다.
def main():
    # 프로그램 시작 시 등록된 기본 프롬프트 개수를 출력합니다.
    print(f"기본 프롬프트 {len(prompts)}개가 등록되었습니다.")

    # while True는 사용자가 종료를 선택할 때까지 계속 반복합니다.
    while True:
        # show_menu() 함수를 실행하고 사용자의 선택을 받습니다.
        choice = show_menu()

        # 사용자가 0을 입력하면 프로그램을 종료합니다.
        if choice == "0":
            print("프로그램을 종료합니다.")

            # break는 현재 실행 중인 while 반복문을 종료합니다.
            break

               # 사용자가 1번을 선택하면 프롬프트 추가 함수를 실행합니다.
        elif choice == "1":
            add_prompt()

           # 사용자가 2번을 선택하면 전체 프롬프트 목록을 출력합니다.
        elif choice == "2":
            show_list()
        # 사용자가 3번을 선택하면 카테고리별 조회를 실행합니다.
        elif choice == "3":
            show_by_category()

               # 사용자가 4번을 선택하면 프롬프트 검색을 실행합니다.
        elif choice == "4":
            search_prompt()

                # 사용자가 5번을 선택하면 프롬프트 상세 보기를 실행합니다.
        elif choice == "5":
            show_detail()

        # 사용자가 6번을 선택하면 즐겨찾기 상태를 변경합니다.
        elif choice == "6":
            toggle_favorite()

        # 사용자가 7번을 선택하면 즐겨찾기 목록을 출력합니다.
        elif choice == "7":
            show_favorites()

        # 0부터 7까지가 아닌 값을 입력하면 잘못된 입력으로 처리합니다.
        else:
            print("잘못된 번호입니다. 0부터 7까지 입력해주세요.")


# 이 파일을 직접 실행했을 때만 main() 함수를 호출합니다.
# 다른 파일에서 main.py를 불러올 때는 자동으로 실행되지 않습니다.
if __name__ == "__main__":
    main()
