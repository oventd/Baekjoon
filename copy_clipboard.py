import sys
import pyperclip

def copy_to_clipboard(text):
    """
    주어진 텍스트를 시스템 클립보드에 복사합니다.
    """
    pyperclip.copy(text)
    print(f"'{text}'가 클립보드에 복사되었습니다.")

def main():
    """
    스크립트 실행 시 명령행 인자를 받아 처리합니다.
    """
    # sys.argv는 명령행 인자들을 담고 있는 리스트입니다.
    # sys.argv[0]은 스크립트 파일 이름(clip.py)이고,
    # sys.argv[1]부터 실제 인자들이 시작됩니다.
    
    if len(sys.argv) < 2:
        print("사용법: python clip.py <복사할 텍스트>")
        return

    # 첫 번째 인자(sys.argv[1])를 가져옵니다.
    # 여러 인자를 합치고 싶다면 sys.argv[1:]를 사용하여 리스트로 가져와 join()으로 합치면 됩니다.
    input_text = sys.argv[1]
    
    # "hello "와 인자를 합쳐서 최종 텍스트를 만듭니다.
    final_text = rf"https://github.com/oventd/Baekjoon/tree/main/{input_text}"
    
    # 클립보드에 복사하는 함수 호출
    copy_to_clipboard(final_text)

if __name__ == "__main__":
    main()