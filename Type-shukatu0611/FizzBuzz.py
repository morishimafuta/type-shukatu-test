for num in range(1, 101):
    string = ''

    # ここから記述

    # if文は上から順に処理するので15の倍数を先頭に記述しないと'FizzBuzz'が表示されない
    if num % 15 == 0: 
        string ='FizzBuzz'
    
    elif num % 5 == 0:
        string = 'Buzz'
    
    elif num % 3 == 0:
        string = 'Fizz'

    else:
        string = str(num)

    # ここまで記述

    print(string)