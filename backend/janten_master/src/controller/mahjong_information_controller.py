try:
    import os
    import sys
    import random
    from dotenv import load_dotenv

    sys.path.append(os.path.join(os.path.dirname(__file__), "../../../.."))
except ImportError as e:
    sys.exit(str(e))
else:
    from backend.janten_master.src.controller.db_accessor import DBAccessor
    from backend.janten_master.src.controller.resource_controller import (
        ResourceCntroller,
    )
    from backend.janten_master.src.controller.answer_information import (
        AnswerInformation,
    )
    from backend.janten_master.src.controller.pai import (
        Pai,
    )


class MahjongInformationController:
    """機能に対応したデータ操作を行う"""

    def register_answer_information(self, question_id, player_name, answer_pai):
        """プレーヤーの回答情報をデータベースに登録する

        Args:
            question_id (int): 問題のID
            player_name (str): プレーヤーの名前
            answer_pai (str): 回答牌のID

        Returns:
            json: 登録結果を格納したjson
                正常時:
                {
                    "data": {},
                    "error": {},
                }
                例外発生時:
                {
                    "data": {},
                    "error": {"message": str},
                }
            int: ステータスコード
        """
        try:
            # .envを読み込む
            load_dotenv()
            DATABASE_NAME = os.getenv("DATABASE_NAME")

            accessor = self._create_db_accessor()
            answer = AnswerInformation(
                int(question_id), player_name, Pai.get_values(answer_pai)
            )
            accessor.insert_answer_information(DATABASE_NAME, answer)

            return {"data": {}, "error": {}}, 200

        except Exception:
            return self.__create_error_dict("回答情報の登録に失敗しました。"), 404

    def get_aggregate_results(self, question_id):
        """データベースから集計情報を取得する

        Args:
            question_id (int): 問題のID

        Returns:
            json: 集計情報を格納したjson
                正常時:
                {
                    "data": {
                        "answer_imformation":[
                            {"id":str, "path":str, "number":int},
                            ...
                        ]},
                    "error": {},
                }
                例外発生時:
                {
                    "data": {},
                    "error": {"message": str},
                }

            int: ステータスコード

        """
        try:
            # .envを読み込む
            load_dotenv()
            DATABASE_NAME = os.getenv("DATABASE_NAME")

            accessor = self._create_db_accessor()
            aggregate_results = accessor.select_aggregate_information(
                DATABASE_NAME, int(question_id)
            )

            results_list = []
            for data in aggregate_results:
                results_list.append(
                    [
                        data.answer_pai_id,
                        data.answer_count,
                    ]
                )

            aggregate_results_list = self.__create_aggregated_data_dict(results_list)

            result_dict = {
                "data": {"answer_imformation": aggregate_results_list},
                "error": {},
            }

            return result_dict, 200

        except Exception:
            return self.__create_error_dict("集計結果の取得に失敗しました。"), 404

    def get_question_information(self):
        """データベースから問題情報を取得する

        Returns:
            json: 問題情報を格納したjson

            正常時:
            {
                "data": {
                    "question-id ": int,
                    "dora-pai": {"id":str, "path":str},
                    "tsumo-pai": {"id":str, "path":str},
                    "tehai": [
                        {"id":str, "path":str},
                        ...
                    ]},
                "error": {}
            }
            例外発生時:
            {
                "data": {},
                "error": {"message": str},
            }

            int: ステータスコード
        """

        try:
            # .envを読み込む
            load_dotenv()
            DATABASE_NAME = os.getenv("DATABASE_NAME")

            accessor = self._create_db_accessor()
            record_count = accessor.get_number_of_records(
                DATABASE_NAME, "question_information"
            )

            question_id = random.randint(1, record_count)

            question = accessor.select_question_information(DATABASE_NAME, question_id)
            tehai = accessor.select_tehai_information(DATABASE_NAME, question.tehai_id)

            tehai_list = [
                tehai.tehai_01,
                tehai.tehai_02,
                tehai.tehai_03,
                tehai.tehai_04,
                tehai.tehai_05,
                tehai.tehai_06,
                tehai.tehai_07,
                tehai.tehai_08,
                tehai.tehai_09,
                tehai.tehai_10,
                tehai.tehai_11,
                tehai.tehai_12,
                tehai.tehai_13,
            ]

            dora_dict = self.__create_pai_data_dict([question.dora_id])
            tsumo_dict = self.__create_pai_data_dict([question.tsumo_id])
            tehai_dict = self.__create_pai_data_dict(tehai_list)

            result_dict = {
                "data": {
                    "question-id": question.question_id,
                    "dora-pai": dora_dict[0],
                    "tsumo-pai": tsumo_dict[0],
                    "tehai": tehai_dict,
                },
                "error": {},
            }

            return result_dict, 200

        except Exception:
            return self.__create_error_dict("問題の取得に失敗しました。"), 404

    # 牌情報のdictを作成する。
    def __create_pai_data_dict(self, pai_list):
        operator = ResourceCntroller("../pai-images")
        pai_data_list = []

        for pai in pai_list:
            pai_data_list.append(
                {"id": pai.value.get("id"), "path": operator.convert_to_path(pai)}
            )

        return pai_data_list

    # 集計情報のdictを作成する。
    def __create_aggregated_data_dict(self, pai_list):
        operator = ResourceCntroller("../pai-images")
        pai_data_list = []

        for pai in pai_list:
            pai_data_list.append(
                {
                    "id": pai[0].value.get("id"),
                    "path": operator.convert_to_path(pai[0]),
                    "number": pai[1],
                }
            )

        return pai_data_list

    # 例外発生時のdictを作成
    def __create_error_dict(self, message):

        return {"data": {}, "error": {"message": message}}

    def _create_db_accessor(self):
        return DBAccessor()
