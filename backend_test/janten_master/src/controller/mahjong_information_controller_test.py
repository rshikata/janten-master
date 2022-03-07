try:
    import os
    import sys
    import unittest
    from unittest.mock import Mock

    sys.path.append(os.path.join(os.path.dirname(__file__), "../../../.."))
except ImportError as e:
    sys.exit(str(e))
else:
    from backend.janten_master.src.controller.mahjong_information_controller import (
        MahjongInformationController,
    )
    from backend.janten_master.src.controller.pai import (
        Pai,
    )
    from backend.janten_master.src.controller.aggregate_results_information import (
        AggregateResultsInformation,
    )
    from backend.janten_master.src.controller.not_found_exception import (
        NotFoundException,
    )
    from backend.janten_master.src.controller.sqlite_exception import (
        SqliteException,
    )
    from backend.janten_master.src.controller.question_information import (
        QuestionInformation,
    )
    from backend.janten_master.src.controller.tehai_information import (
        TehaiInformation,
    )


class TestMahjongInformationController(unittest.TestCase):
    """register_answer_information()のテスト"""

    def test_register_answer_information1(self):
        """register_answer_information()をテストするメソッド

        テスト項目:
            引数がすべて正しい場合、正常時の連想配列とステータスコードが返される。

        """

        controller = self.__create_mahjong_controller()
        controller.test_operator.insert_answer_information.return_value = None

        result = controller.register_answer_information(1, "test", "MAN_01")
        self.assertEqual(result[0], {"data": {}, "error": {}})
        self.assertEqual(result[1], 200)

    def test_register_answer_information2(self):
        """register_answer_information()をテストするメソッド

        テスト項目:
            引数は正しいが例外(SqliteException)が発生した場合、エラーメッセージを含む連想配列とステータスコードが返される。
        """

        controller = self.__create_mahjong_controller()
        controller.test_operator.insert_answer_information.side_effect = SqliteException

        result = controller.register_answer_information(1, "dummy", "MAN_01")
        self.assertEqual(
            result[0], {"data": {}, "error": {"message": "回答情報の登録に失敗しました。"}}
        )
        self.assertEqual(result[1], 404)

    def test_register_answer_information3(self):
        """register_answer_information()をテストするメソッド

        テスト項目:
            引数は正しいが例外(Exception)が発生した場合、エラーメッセージを含む連想配列とステータスコードが返される。
        """

        controller = self.__create_mahjong_controller()
        controller.test_operator.insert_answer_information.side_effect = Exception

        result = controller.register_answer_information(1, "dummy", "TEST_01")
        self.assertEqual(result[0], {"data": {}, "error": {"message": "例外が発生しました。"}})
        self.assertEqual(result[1], 404)

    """get_aggregate_results()のテスト"""

    def test_get_aggregate_results1(self):
        """get_aggregate_results()をテストするメソッド

        テスト項目:
            引数がすべて正しい場合、正常時の連想配列とステータスコードが返される。
        """

        controller = self.__create_mahjong_controller()
        test_data = [AggregateResultsInformation(Pai.MAN_01, 5)]
        controller.test_operator.select_aggregate_information.return_value = test_data

        result = controller.get_aggregate_results(1)

        self.assertIn("id", result[0]["data"]["answer_imformation"][0])
        self.assertIn("path", result[0]["data"]["answer_imformation"][0])
        self.assertIn("number", result[0]["data"]["answer_imformation"][0])
        self.assertIn("error", result[0])
        self.assertEqual(result[1], 200)

    def test_get_aggregate_results2(self):
        """get_aggregate_results()をテストするメソッド

        テスト項目:
            引数は正しいが例外(SqliteException)が発生した場合、エラーメッセージを含む連想配列とステータスコードが返される。
        """

        controller = self.__create_mahjong_controller()
        controller.test_operator.select_aggregate_information.side_effect = (
            SqliteException
        )

        result = controller.get_aggregate_results(1)

        self.assertEqual(
            result[0], {"data": {}, "error": {"message": "集計結果の取得に失敗しました。"}}
        )
        self.assertEqual(result[1], 404)

    def test_get_aggregate_results2(self):
        """get_aggregate_results()をテストするメソッド

        テスト項目:
            引数は正しいが例外(NotFoundException)が発生した場合、エラーメッセージを含む連想配列とステータスコードが返される。
        """

        controller = self.__create_mahjong_controller()
        controller.test_operator.select_aggregate_information.side_effect = (
            NotFoundException
        )

        result = controller.get_aggregate_results(1)

        self.assertEqual(result[0], {"data": {}, "error": {"message": "回答データが存在しません。"}})
        self.assertEqual(result[1], 404)

    def test_get_aggregate_results3(self):
        """get_aggregate_results()をテストするメソッド

        テスト項目:
            引数は正しいが例外(Exception)が発生した場合、エラーメッセージを含む連想配列とステータスコードが返される。
        """

        controller = self.__create_mahjong_controller()
        controller.test_operator.select_aggregate_information.side_effect = Exception

        result = controller.get_aggregate_results(1)

        self.assertEqual(result[0], {"data": {}, "error": {"message": "例外が発生しました。"}})
        self.assertEqual(result[1], 404)

    """get_question_information()のテスト"""

    def test_get_question_information1(self):
        """get_question_information()をテストするメソッド

        テスト項目:
            正常に問題情報が取得できた場合、正常時の連想配列とステータスコードが返される。
        """

        controller = self.__create_mahjong_controller()
        controller.test_operator.convert_to_path.return_value = "test"
        controller.test_operator.get_number_of_records.return_value = 1

        controller.test_operator.select_question_information.return_value = (
            self.__create_question_object()
        )

        controller.test_operator.select_tehai_information.return_value = (
            self.__create_tehai_object()
        )

        result = controller.get_question_information()

        self.assertIn("question-id", result[0]["data"])
        self.assertIn("id", result[0]["data"]["dora-pai"])
        self.assertIn("path", result[0]["data"]["dora-pai"])
        self.assertIn("id", result[0]["data"]["tsumo-pai"])
        self.assertIn("path", result[0]["data"]["tsumo-pai"])
        self.assertIn("id", result[0]["data"]["tehai"][0])
        self.assertIn("path", result[0]["data"]["tehai"][0])
        self.assertIn("error", result[0])
        self.assertEqual(result[1], 200)

    def test_get_question_information2(self):
        """get_question_information()をテストするメソッド

        テスト項目:
            レコード数取得時に例外(SqliteException)が発生した場合、エラーメッセージを含む連想配列とステータスコードが返される。
        """

        controller = self.__create_mahjong_controller()
        controller.test_operator.convert_to_path.return_value = "dummy"
        controller.test_operator.get_number_of_records.side_effect = SqliteException

        controller.test_operator.select_question_information.return_value = (
            self.__create_question_object()
        )

        controller.test_operator.select_tehai_information.return_value = (
            self.__create_tehai_object()
        )

        result = controller.get_question_information()

        self.assertEqual(result[0], {"data": {}, "error": {"message": "問題の取得に失敗しました。"}})
        self.assertEqual(result[1], 404)

    def test_get_question_information3(self):
        """get_question_information()をテストするメソッド

        テスト項目:
            問題情報取得時に例外(SqliteException)が発生した場合、エラーメッセージを含む連想配列とステータスコードが返される。
        """

        controller = self.__create_mahjong_controller()
        controller.test_operator.convert_to_path.return_value = "dummy"
        controller.test_operator.get_number_of_records.return_value = 1

        controller.test_operator.select_question_information.side_effect = (
            SqliteException
        )

        controller.test_operator.select_tehai_information.return_value = (
            self.__create_tehai_object()
        )

        result = controller.get_question_information()

        self.assertEqual(result[0], {"data": {}, "error": {"message": "問題の取得に失敗しました。"}})
        self.assertEqual(result[1], 404)

    def test_get_question_information4(self):
        """get_question_information()をテストするメソッド

        テスト項目:
            問題情報取得時に例外(NotFoundException)が発生した場合、エラーメッセージを含む連想配列とステータスコードが返される。
        """

        controller = self.__create_mahjong_controller()
        controller.test_operator.convert_to_path.return_value = "dummy"
        controller.test_operator.get_number_of_records.return_value = 1

        controller.test_operator.select_question_information.side_effect = (
            NotFoundException
        )

        controller.test_operator.select_tehai_information.return_value = (
            self.__create_tehai_object()
        )

        result = controller.get_question_information()

        self.assertEqual(result[0], {"data": {}, "error": {"message": "問題データが存在しません。"}})
        self.assertEqual(result[1], 404)

    def test_get_question_information5(self):
        """get_question_information()をテストするメソッド

        テスト項目:
            手牌情報取得時に例外(SqliteException)が発生した場合、エラーメッセージを含む連想配列とステータスコードが返される。
        """

        controller = self.__create_mahjong_controller()
        controller.test_operator.convert_to_path.return_value = "dummy"
        controller.test_operator.get_number_of_records.return_value = 1

        controller.test_operator.select_question_information.return_value = (
            self.__create_question_object()
        )

        controller.test_operator.select_tehai_information.side_effect = SqliteException

        result = controller.get_question_information()

        self.assertEqual(result[0], {"data": {}, "error": {"message": "問題の取得に失敗しました。"}})
        self.assertEqual(result[1], 404)

    def test_get_question_information6(self):
        """get_question_information()をテストするメソッド

        テスト項目:
            手牌情報取得時に例外(NotFoundException)が発生した場合、エラーメッセージを含む連想配列とステータスコードが返される。
        """

        controller = self.__create_mahjong_controller()
        controller.test_operator.convert_to_path.return_value = "dummy"
        controller.test_operator.get_number_of_records.return_value = 1

        controller.test_operator.select_question_information.return_value = (
            self.__create_question_object()
        )

        controller.test_operator.select_tehai_information.side_effect = (
            NotFoundException
        )

        result = controller.get_question_information()

        self.assertEqual(result[0], {"data": {}, "error": {"message": "問題データが存在しません。"}})
        self.assertEqual(result[1], 404)

    def test_get_question_information7(self):
        """get_question_information()をテストするメソッド

        テスト項目:
            例外(Exception)が発生した場合、エラーメッセージを含む連想配列とステータスコードが返される。
        """

        controller = self.__create_mahjong_controller()
        controller.test_operator.convert_to_path.return_value = "dummy"
        controller.test_operator.get_number_of_records.return_value = 0

        controller.test_operator.select_question_information.return_value = (
            self.__create_question_object()
        )

        controller.test_operator.select_tehai_information.return_value = (
            self.__create_tehai_object()
        )

        result = controller.get_question_information()

        self.assertEqual(result[0], {"data": {}, "error": {"message": "例外が発生しました。"}})
        self.assertEqual(result[1], 404)

    def __create_question_object(self):
        test_question = QuestionInformation(
            1,
            Pai.MAN_01,
            Pai.MAN_01,
            1,
            "2022-01-01 09:00:00",
            "2022-01-01 09:00:00",
        )
        return test_question

    def __create_tehai_object(self):
        test_tehai = TehaiInformation(
            1,
            Pai.MAN_01,
            Pai.MAN_01,
            Pai.MAN_01,
            Pai.MAN_01,
            Pai.MAN_01,
            Pai.MAN_01,
            Pai.MAN_01,
            Pai.MAN_01,
            Pai.MAN_01,
            Pai.MAN_01,
            Pai.MAN_01,
            Pai.MAN_01,
            Pai.MAN_01,
            "2022-01-01 09:00:00",
            "2022-01-01 09:00:00",
        )
        return test_tehai

    def __create_mahjong_controller(self):
        return self.MahjongInformationController_forTest()

    class MahjongInformationController_forTest(MahjongInformationController):
        def __init__(self):
            self.test_operator = Mock()

        def _create_db_accessor(self):
            # FactoryMethodをオーバーライド
            return self.test_operator

        def _create_resource_controller(self):
            return self.test_operator


if __name__ == "__main__":
    unittest.main()
