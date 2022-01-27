class AggregateResultsInformation:
    """牌IDと回答数の情報と作成・更新日時を保持する

    Attributes:
        answer_pai_id (int): 回答牌のID
        answer_count (int): 回答数
        create_datetime (str): 作成日時
        update_datetime (str): 更新日時

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
