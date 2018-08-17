class Calculator:
    """
    計算実行アドオン

    """

    def multiply(self, nums: list):
        result = 1

        for i in nums:
            result = result * nums[i]

        return result
            
