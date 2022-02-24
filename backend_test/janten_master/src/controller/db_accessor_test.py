try:
    import os
    import sys
    import unittest

    sys.path.append(os.path.join(os.path.dirname(__file__), "../../../.."))
except ImportError as e:
    sys.exit(str(e))
else:
    from backend.janten_master.src.controller.db_accessor import DBAccessor
    from backend.janten_master.src.controller.not_found_exception import (
        NotFoundException,
    )
    from backend.janten_master.src.controller.aggregate_results_information import (
        AggregateResultsInformation,
    )
    from backend.janten_master.src.controller.question_information import (
        QuestionInformation,
    )
    from backend.janten_master.src.controller.tehai_information import (
        TehaiInformation,
    )
    from backend.janten_master.src.controller.pai import (
        Pai,
    )
    from backend.janten_master.src.controller.answer_information import (
        AnswerInformation,
    )
    from backend.janten_master.src.controller.sqlite_exception import (
        SqliteException,
    )


class TestDBAccessor(unittest.TestCase):

    """get_number_of_records()のテスト"""

    def test_get_number_of_records1(self):
        """get_number_of_records()をテストするメソッド

        テスト項目:
            引数がすべて正しく、データベースアクセスに成功した場合、テーブルのレコード数が返される。
        """

        accessor = self._create_db_accessor()
        record_count = accessor.get_number_of_records(
            "janten_master.db", "question_information"
        )
        self.assertEqual(record_count, 2)

    def test_get_number_of_records2(self):
        """get_number_of_records()をテストするメソッド

        テスト項目:
            指定されたデータベースが存在しない場合、例外(SqliteException)が発生する。
        """

        accessor = self._create_db_accessor()
        with self.assertRaises(SqliteException):
            accessor.get_number_of_records("存在しないデータベース名", "question_information")

    def test_get_number_of_records3(self):
        """get_number_of_records()をテストするメソッド

        テスト項目:
            指定されたテーブルが存在しない場合、例外(SqliteException)が発生する。
        """

        accessor = self._create_db_accessor()
        with self.assertRaises(SqliteException):
            accessor.get_number_of_records("janten_master.db", "存在しないテーブル名")

    """select_aggregate_information()のテスト"""

    def test_select_aggregate_information1(self):
        """select_aggregate_information()をテストするメソッド

        テスト項目:
            引数がすべて正しく、データベースアクセスに成功した場合、集計結果が格納された配列が返される。
        """

        accessor = self._create_db_accessor()
        results = accessor.select_aggregate_information("janten_master.db", 1)

        self.assertNotEqual(len(results), 0)
        self.assertIsInstance(results[0], AggregateResultsInformation)

    def test_select_aggregate_information2(self):
        """select_aggregate_information()をテストするメソッド

        テスト項目:
            指定されたデータベースが存在しない場合、例外(SqliteException)が発生する。
        """

        accessor = self._create_db_accessor()
        with self.assertRaises(SqliteException):
            accessor.select_aggregate_information("存在しないデータベース名", 1)

    def test_select_aggregate_information3(self):
        """select_aggregate_information()をテストするメソッド

        テスト項目:
            指定された問題IDに対応するデータが存在しない場合、例外(NotFoundException)が発生する。
        """

        accessor = self._create_db_accessor()
        with self.assertRaises(NotFoundException):
            accessor.select_aggregate_information("janten_master.db", 5)

    """select_question_information()のテスト"""

    def test_select_question_information1(self):
        """select_question_information()をテストするメソッド

        テスト項目:
            引数がすべて正しく、データベースアクセスに成功した場合、問題情報が格納されたオブジェクトが返される。
        """

        accessor = self._create_db_accessor()
        result = accessor.select_question_information("janten_master.db", 1)
        self.assertIsInstance(result, QuestionInformation)

    def test_select_question_information2(self):
        """select_question_information()をテストするメソッド

        テスト項目:
            指定されたデータベースが存在しない場合、例外(SqliteException)が発生する。
        """

        accessor = self._create_db_accessor()
        with self.assertRaises(SqliteException):
            accessor.select_question_information("存在しないデータベース名", 1)

    def test_select_question_information3(self):
        """select_question_information()をテストするメソッド

        テスト項目:
            指定された問題IDに対応するデータが存在しない場合、例外(NotFoundException)が発生する。
        """

        accessor = self._create_db_accessor()
        with self.assertRaises(NotFoundException):
            accessor.select_question_information("janten_master.db", 5)

    """select_tehai_information()のテスト"""

    def test_select_tehai_information1(self):
        """select_tehai_information()をテストするメソッド

        テスト項目:
            引数がすべて正しく、データベースアクセスに成功した場合、手牌情報が格納されたオブジェクトが返される。
        """

        accessor = self._create_db_accessor()
        result = accessor.select_tehai_information("janten_master.db", 1)
        self.assertIsInstance(result, TehaiInformation)

    def test_select_tehai_information2(self):
        """select_select_tehai_information()をテストするメソッド

        テスト項目:
            指定されたデータベースが存在しない場合、例外(SqliteException)が発生する。
        """

        accessor = self._create_db_accessor()
        with self.assertRaises(SqliteException):
            accessor.select_tehai_information("存在しないデータベース名", 1)

    def test_select_tehai_information3(self):
        """select_tehai_information()をテストするメソッド

        テスト項目:
            指定された手牌IDに対応するデータが存在しない場合、例外(NotFoundException)が発生する。
        """

        accessor = self._create_db_accessor()
        with self.assertRaises(NotFoundException):
            accessor.select_tehai_information("janten_master.db", 5)

    """insert_answer_information()のテスト"""

    def test_insert_answer_information1(self):
        """insert_answer_information()をテストするメソッド

        テスト項目:
            引数がすべて正しく、データベースアクセスに成功した場合、回答情報がデータベースに登録される。
        """

        accessor = self._create_db_accessor()
        accessor.insert_answer_information(
            "janten_master.db", AnswerInformation(1, "dummy", Pai.MAN_01)
        )

    def test_insert_answer_information2(self):
        """insert_answer_information()をテストするメソッド

        テスト項目:
            指定されたデータベースが存在しない場合、例外(SqliteException)が発生する。
        """

        accessor = self._create_db_accessor()
        with self.assertRaises(SqliteException):
            accessor.insert_answer_information(
                "存在しないデータベース名", AnswerInformation(1, "dummy", Pai.MAN_01)
            )

    def _create_db_accessor(self):
        return DBAccessor()


if __name__ == "__main__":
    unittest.main()
