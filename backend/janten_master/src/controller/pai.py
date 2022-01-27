from enum import Enum


class Pai(Enum):
    """麻雀牌の情報を保持する"""

    # 萬子
    MAN_01 = {"id": "MAN_01", "index": "00-01-00", "order": 1}
    MAN_02 = {"id": "MAN_02", "index": "00-02-00", "order": 2}
    MAN_03 = {"id": "MAN_03", "index": "00-03-00", "order": 3}
    MAN_04 = {"id": "MAN_04", "index": "00-04-00", "order": 4}
    MAN_05 = {"id": "MAN_05", "index": "00-05-00", "order": 5}
    MAN_05R = {"id": "MAN_05R", "index": "00-05-01", "order": 6}  # 赤牌
    MAN_06 = {"id": "MAN_06", "index": "00-06-00", "order": 7}
    MAN_07 = {"id": "MAN_07", "index": "00-07-00", "order": 8}
    MAN_08 = {"id": "MAN_08", "index": "00-08-00", "order": 9}
    MAN_09 = {"id": "MAN_09", "index": "00-09-00", "order": 10}

    # 筒子
    PIN_01 = {"id": "PIN_01", "index": "01-01-00", "order": 11}
    PIN_02 = {"id": "PIN_02", "index": "01-02-00", "order": 12}
    PIN_03 = {"id": "PIN_03", "index": "01-03-00", "order": 13}
    PIN_04 = {"id": "PIN_04", "index": "01-04-00", "order": 14}
    PIN_05 = {"id": "PIN_05", "index": "01-05-00", "order": 15}
    PIN_05R = {"id": "PIN_05R", "index": "01-01-01", "order": 16}  # 赤牌
    PIN_06 = {"id": "PIN_06", "index": "01-06-00", "order": 17}
    PIN_07 = {"id": "PIN_07", "index": "01-07-00", "order": 18}
    PIN_08 = {"id": "PIN_08", "index": "01-08-00", "order": 19}
    PIN_09 = {"id": "PIN_09", "index": "01-09-00", "order": 20}

    # 索子
    SOU_01 = {"id": "SOU_01", "index": "02-01-00", "order": 21}
    SOU_02 = {"id": "SOU_02", "index": "02-02-00", "order": 22}
    SOU_03 = {"id": "SOU_03", "index": "02-03-00", "order": 23}
    SOU_04 = {"id": "SOU_04", "index": "02-04-00", "order": 24}
    SOU_05 = {"id": "SOU_05", "index": "02-05-00", "order": 25}
    SOU_05R = {"id": "SOU_05R", "index": "02-05-01", "order": 26}  # 赤牌
    SOU_06 = {"id": "SOU_06", "index": "02-06-00", "order": 27}
    SOU_07 = {"id": "SOU_07", "index": "02-07-00", "order": 28}
    SOU_08 = {"id": "SOU_08", "index": "02-08-00", "order": 29}
    SOU_09 = {"id": "SOU_09", "index": "02-09-00", "order": 30}

    # 字牌
    TON = {"id": "TON", "index": "03-01-00", "order": 31}
    NAN = {"id": "NAN", "index": "03-02-00", "order": 32}
    SYA = {"id": "SYA", "index": "03-03-00", "order": 33}
    PEI = {"id": "PEI", "index": "03-04-00", "order": 34}
    HAKU = {"id": "HAKU ", "index": "03-05-00", "order": 35}
    HATSU = {"id": "HATSU", "index": "03-06-00", "order": 36}
    TYUN = {"id": "TYUN", "index": "03-07-00", "order": 37}

    def get_values(pai_id):
        """牌IDからvalue値を返す
        Args:
          pai_id (str): 牌のID

        Returns:
            Pai: enumのvalue値を返す

        Raises:
            ValueError: 該当するデータが存在しない場合発生する例外
        """

        pai_value = None
        for pai in Pai:
            if pai.value.get("id") == pai_id:
                pai_value = pai

        if pai_value == None:
            raise ValueError

        return pai_value
