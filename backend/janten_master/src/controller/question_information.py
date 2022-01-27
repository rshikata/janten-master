class QuestionInformation:
    """表示する問題情報と作成・更新日時を保持する。

    Attributes:
        question_id (int): 問題のID
        dora_id (int): ドラ牌の牌ID
        tsumo_id (int): ツモ牌の牌ID
        tehai_id (int): 手牌のID
        create_datetime (str): 作成日時
        update_datetime (str): 更新日時

    """

    def __init__(
        self, question_id, dora_id, tsumo_id, tehai_id, create_datetime, update_datetime
    ):
        self.__question_id = question_id
        self.__dora_id = dora_id
        self.__tsumo_id = tsumo_id
        self.__tehai_id = tehai_id
        self.__create_datetime = create_datetime
        self.__update_datetime = update_datetime

    @property
    def question_id(self):
        return self.__question_id

    @property
    def dora_id(self):
        return self.__dora_id

    @property
    def tsumo_id(self):
        return self.__tsumo_id

    @property
    def tehai_id(self):
        return self.__tehai_id

    @property
    def create_datetim(self):
        return self.__create_datetime

    @property
    def update_datetime(self):
        return self.__update_datetime
