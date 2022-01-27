class TehaiInformation:
    """問題に対応した手牌情報と作成・更新日時を保持する

    Attributes:
        tehai_id (int): 手牌のID
        tehai_01 (int): 牌ID
        tehai_02 (int): 牌ID
        tehai_03 (int): 牌ID
        tehai_04 (int): 牌ID
        tehai_05 (int): 牌ID
        tehai_06 (int): 牌ID
        tehai_07 (int): 牌ID
        tehai_08 (int): 牌ID
        tehai_09 (int): 牌ID
        tehai_10 (int): 牌ID
        tehai_11 (int): 牌ID
        tehai_12 (int): 牌ID
        tehai_13 (int): 牌ID
        create_datetime (str): 作成日時
        update_datetime (str): 更新日時

    """

    def __init__(
        self,
        tehai_id,
        tehai_01,
        tehai_02,
        tehai_03,
        tehai_04,
        tehai_05,
        tehai_06,
        tehai_07,
        tehai_08,
        tehai_09,
        tehai_10,
        tehai_11,
        tehai_12,
        tehai_13,
        create_datetime,
        update_datetime,
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
