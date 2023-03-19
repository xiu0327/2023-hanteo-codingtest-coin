import re


class Coin:
    def __init__(self):
        self.expect = None
        self.coins = None
        self.input_coins_pattern = r"\d+,\d+,\d+"
        self.input_expect_pattern = r"\d+"

    def input_check(self, data: str, pattern: str):
        match = re.match(pattern=pattern, string=data)
        if not match:
            raise Exception("입력 형식이 어긋 납니다.")

    def set_coins(self, input_coins: str):
        self.coins = list(map(int, input_coins.split(",")))

    def set_expect(self, input_expect: str):
        self.expect = int(input_expect)

    def setting_dp(self):
        dp = [0] * (self.expect + 1)
        return dp

    def solution(self):
        dp = self.setting_dp()
        dp[0] = 1
        for i in range(len(self.coins)):
            for j in range(self.coins[i], self.expect + 1):
                dp[j] = dp[j] + dp[j - self.coins[i]]

        return dp[self.expect]
