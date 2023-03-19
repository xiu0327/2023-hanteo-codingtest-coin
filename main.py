from coin import Coin

coin = Coin()


def coin_input_coins():
    print("동전의 종류를 입력해 주세요.")
    print("입력 예시 : 1,2,3,4")
    coins = input()
    return coins


def coin_input_expect():
    print("sum(합)을 입력해 주세요.")
    print("입력 예시 : 10")
    expect = input()
    return expect


def coin_service():
    input_coins = coin_input_coins()
    check(input_coins, coin.input_coins_pattern)
    input_expect = coin_input_expect()
    check(input_expect, coin.input_expect_pattern)
    coin.set_coins(input_coins)
    coin.set_expect(input_expect)
    return coin.solution()


def check(data, pattern):
    try:
        coin.input_check(pattern=pattern, data=data)
    except Exception as e:
        print(e.args[0])
        coin_service()


if __name__ == '__main__':
    answer = coin_service()
    print("answer = ", answer)
