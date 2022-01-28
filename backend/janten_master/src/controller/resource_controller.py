class ResourceCntroller:
    """牌IDとパスとの間の変換を行う"""

    def __init__(self, root_path):
        self.__root_path = root_path

    def convert_to_path(self, pai_id):
        """牌情報からパスに変換

        Args:
            pai_id (Pai): 牌情報

        Returns:
            str: 牌IDに対応した画像ファイルパス
        """
        pai_index = pai_id.value.get("index")
        kind_list = ["man", "sou", "pin", "ji"]
        pai_value = pai_index.split("-")
        pai_kind = kind_list[int(pai_value[0])]
        pai_number = int(pai_value[1])
        akapai_flag = int(pai_value[2])

        if akapai_flag == 1:
            path = f"{self.__root_path}/aka{int(pai_value[0]) + 1}-66-90-l.png"
        else:
            path = f"{self.__root_path}/{pai_kind}{pai_number}-66-90-l.png"

        return path
