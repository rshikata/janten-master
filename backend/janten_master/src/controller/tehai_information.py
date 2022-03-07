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


class TehaiInformation:
    """問題に対応した手牌情報と作成・更新日時を保持する

    Attributes:
        tehai_id (int): 手牌のID
        tehai_01 (Pai): 牌情報
        tehai_02 (Pai): 牌情報
        tehai_03 (Pai): 牌情報
        tehai_04 (Pai): 牌情報
        tehai_05 (Pai): 牌情報
        tehai_06 (Pai): 牌情報
        tehai_07 (Pai): 牌情報
        tehai_08 (Pai): 牌情報
        tehai_09 (Pai): 牌情報
        tehai_10 (Pai): 牌情報
        tehai_11 (Pai): 牌情報
        tehai_12 (Pai): 牌情報
        tehai_13 (Pai): 牌情報
        create_datetime (str): 作成日時
        update_datetime (str): 更新日時

    """

    def __init__(
        self,
        tehai_id: Pai,
        tehai_01: Pai,
        tehai_02: Pai,
        tehai_03: Pai,
        tehai_04: Pai,
        tehai_05: Pai,
        tehai_06: Pai,
        tehai_07: Pai,
        tehai_08: Pai,
        tehai_09: Pai,
        tehai_10: Pai,
        tehai_11: Pai,
        tehai_12: Pai,
        tehai_13: Pai,
        create_datetime: str,
        update_datetime: str,
    ):
        self.__tehai_id = tehai_id
        self.__tehai_01 = tehai_01
        self.__tehai_02 = tehai_02
        self.__tehai_03 = tehai_03
        self.__tehai_04 = tehai_04
        self.__tehai_05 = tehai_05
        self.__tehai_06 = tehai_06
        self.__tehai_07 = tehai_07
        self.__tehai_08 = tehai_08
        self.__tehai_09 = tehai_09
        self.__tehai_10 = tehai_10
        self.__tehai_11 = tehai_11
        self.__tehai_12 = tehai_12
        self.__tehai_13 = tehai_13
        self.__create_datetime = create_datetime
        self.__update_datetime = update_datetime

    @property
    def tehai_id(self):
        return self.__tehai_id

    @property
    def tehai_01(self):
        return self.__tehai_01

    @property
    def tehai_02(self):
        return self.__tehai_02

    @property
    def tehai_03(self):
        return self.__tehai_03

    @property
    def tehai_04(self):
        return self.__tehai_04

    @property
    def tehai_05(self):
        return self.__tehai_05

    @property
    def tehai_06(self):
        return self.__tehai_06

    @property
    def tehai_07(self):
        return self.__tehai_07

    @property
    def tehai_08(self):
        return self.__tehai_08

    @property
    def tehai_09(self):
        return self.__tehai_09

    @property
    def tehai_10(self):
        return self.__tehai_10

    @property
    def tehai_11(self):
        return self.__tehai_11

    @property
    def tehai_12(self):
        return self.__tehai_12

    @property
    def tehai_13(self):
        return self.__tehai_13

    @property
    def create_datetime(self):
        return self.__create_datetime

    @property
    def update_datetime(self):
        return self.__update_datetime
