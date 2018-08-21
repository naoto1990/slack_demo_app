class Parser:
    """
    """
    # def __init__(self):
    #     super(Parser, self).__init__()
    #     self.arg = arg

    def parse_request(self, input_text: str):
        """
        Args:
            - input_text: 数値をスペース区切りで連結した文字列

        Returns:
            Intを含むリスト
        """
        num_str = input_text.split()
        result_list = []
        for num in num_str:
            result_list.append(int(num))

        return result_list
