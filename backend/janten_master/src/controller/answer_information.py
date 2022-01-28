class AnswerInformation:
    """プレーヤーの回答情報を保持する

    Attributes:
        question_id (int): 問題のID
        player_name (str): プレーヤーの名前
        answer_pai_id (Pai): プレーヤーが回答した牌の牌情報

    """

    def __init__(self, question_id, player_name, answer_pai_id):
        self.__question_id = question_id
        self.__player_name = player_name
        self.__answer_pai_id = answer_pai_id

    @property
    def question_id(self):
        return self.__question_id

    @property
    def player_name(self):
        return self.__player_name

    @property
    def answer_pai_id(self):
        return self.__answer_pai_id
