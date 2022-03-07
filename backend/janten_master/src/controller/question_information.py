try:
    import os
    import sys

    sys.path.append(os.path.join(os.path.dirname(__file__), "../../../.."))
except ImportError as e:
    sys.exit(str(e))
else:
    from backend.janten_master.src.controller.pai import (
        Pai,
    )


class QuestionInformation:
    """表示する問題情報と作成・更新日時を保持する。

    Attributes:
        question_id (int): 問題のID
        dora_id (Pai): ドラ牌の牌情報
        tsumo_id (Pai): ツモ牌の牌情報
        tehai_id (int): 手牌のID
        create_datetime (str): 作成日時
        update_datetime (str): 更新日時

    """

    def __init__(
        self,
        question_id: int,
        dora_id: Pai,
        tsumo_id: Pai,
        tehai_id: int,
        create_datetime: str,
        update_datetime: str,
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
