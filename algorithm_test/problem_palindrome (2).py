t = int(input())

# index를 사용해서 새로운 역방향 문자열을 생성
for tc in range(1, t+1):
    text = input()
    result = ''
    # 문자열을 뒤집어야 하기에 뒤에서 부터
    for i in range(len(text)-1, -1, -1):
        result += text[i]   # text의 마지막 글자부터 더함

    is_palindrome = 0
    # 생성된 결과가 원본과 같은지 비교
    if result == text:
        is_palindrome = 1
    else:
        is_palindrome = 0
    print(f'#{tc} {is_palindrome}')
########################################################################

    # 이진탐색을 이용해서 희문 검색
    for i in range(len(text)//2):   # 길이의 반
        if text[i] != text[len(text) -1 - i]:   # 일치하지 않는다면
            print(f'#{tc} 0')   # 0을 print하고 break
            break
    else:
        print(f'#{tc} 1')   # 모두 일치하다면 else 실행