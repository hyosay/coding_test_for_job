def recursive_function(i):
    if i == 100:
        return
    print('재귀 함수를 {}호출합니다.'.format(i))
    recursive_function(i + 1)
recursive_function(0)