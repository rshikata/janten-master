class AggregateResultsInformation:
    """牌IDと回答数の情報を保持する

    Attributes:
        answer_pai_id (Pai): 回答牌の牌情報
        answer_count (int): 回答数
    """

    def __init__(self, answer_pai_id, answer_count):
        self.__answer_pai_id = answer_pai_id
        self.__answer_count = answer_count

    @property
    def answer_pai_id(self):
        return self.__answer_pai_id

    @property
    def answer_count(self):
        return self.__answer_count
