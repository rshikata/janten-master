try:
    import os
    import sys
    import sqlite3

    sys.path.append(os.path.join(os.path.dirname(__file__), "../../../.."))
except ImportError as e:
    sys.exit(str(e))
else:
    from backend.janten_master.src.controller.question_information import (
        QuestionInformation,
    )
    from backend.janten_master.src.controller.tehai_information import (
        TehaiInformation,
    )
    from backend.janten_master.src.controller.aggregate_results_information import (
        AggregateResultsInformation,
    )
    from backend.janten_master.src.controller.pai import (
        Pai,
    )
    from backend.janten_master.src.controller.not_found_exception import (
        NotFoundException,
    )
    from backend.janten_master.src.controller.answer_information import (
        AnswerInformation,
    )
    from backend.janten_master.src.controller.sqlite_exception import (
        SqliteException,
    )


class DBAccessor:
    """データベースに対するデータの取得・登録を行う"""

    def get_number_of_records(self, database_name: str, table_name: str):
        """テーブルのレコード数を取得する

        Args:
            database_name (str): データベース名
            table_name (str): データベースのテーブル名

        Returns:
            int: テーブルのレコード数

        Raises:
            SqliteException: データベースアクセスに失敗した場合に発生する例外

        """
        if not os.path.isfile(database_name):
            raise SqliteException

        try:
            with sqlite3.connect(database_name) as connection:
                cursor = connection.cursor()
                cursor.execute(f"SELECT COUNT(*) from {table_name}")
                record_count = cursor.fetchall()

            return record_count[0][0]
        except sqlite3.Error:
            raise SqliteException

    def select_aggregate_information(self, database_name: str, question_id: int):
        """集計結果を取得する

        Args:
            database_name (str): データベース名
            question_id (int): 問題のID

        Returns:
            array<AggregateResultsInformation>: 回答情報

        Raises:
            SqliteException: データベースアクセスに失敗した場合に発生する例外
            NotFoundException: idに対応するデータが存在しない場合に発生する例外

        """
        if not os.path.isfile(database_name):
            raise SqliteException

        try:
            with sqlite3.connect(database_name) as connection:
                cursor = connection.cursor()

                cursor.execute(
                    "SELECT answer_pai_id,count(answer_pai_id) from answer_information where question_id = ? group by answer_pai_id",
                    [question_id],
                )

                aggregate_results = cursor.fetchall()

                if len(aggregate_results) == 0:
                    raise NotFoundException

                aggregate_results_list = []

                for i in range(len(aggregate_results)):
                    aggregate_results_list.append(
                        AggregateResultsInformation(
                            Pai.get_values(aggregate_results[i][0]),
                            aggregate_results[i][1],
                        )
                    )

                return aggregate_results_list
        except sqlite3.Error:
            raise SqliteException

    def select_question_information(self, database_name: str, question_id: int):
        """問題情報を取得する

        Args:
            database_name (str): データベース名
            question_id (int): 問題のID

        Returns:
            QuestionInformation: 問題情報

        Raises:
            SqliteException: データベースアクセスに失敗した場合に発生する例外
            NotFoundException: idに対応するデータが存在しない場合に発生する例外

        """

        if not os.path.isfile(database_name):
            raise SqliteException

        try:
            with sqlite3.connect(database_name) as connection:
                cursor = connection.cursor()
                cursor.execute(
                    "SELECT * from question_information WHERE question_id = ?",
                    [question_id],
                )
                question_data = cursor.fetchall()

                if len(question_data) == 0:
                    raise NotFoundException

                question_entity = QuestionInformation(
                    question_data[0][0],
                    Pai.get_values(question_data[0][1]),
                    Pai.get_values(question_data[0][2]),
                    question_data[0][3],
                    question_data[0][4],
                    question_data[0][5],
                )

                return question_entity
        except sqlite3.Error:
            raise SqliteException

    def select_tehai_information(self, database_name: str, tehai_id: int):
        """手牌情報を取得する

        Args:
            database_name (str): データベース名
            tehai_id (int): 手牌のID

        Returns:
            TehaiInformation: 手牌情報

        Raises:
            SqliteException: データベースアクセスに失敗した場合に発生する例外
            NotFoundException: idに対応するデータが存在しない場合に発生する例外

        """

        if not os.path.isfile(database_name):
            raise SqliteException

        try:
            with sqlite3.connect(database_name) as connection:
                cursor = connection.cursor()
                cursor.execute(
                    "SELECT * from tehai_information WHERE tehai_id = ?", [tehai_id]
                )
                tehai_data = cursor.fetchall()

                if len(tehai_data) == 0:
                    raise NotFoundException

                tehai_entity = TehaiInformation(
                    tehai_data[0][0],
                    Pai.get_values(tehai_data[0][1]),
                    Pai.get_values(tehai_data[0][2]),
                    Pai.get_values(tehai_data[0][3]),
                    Pai.get_values(tehai_data[0][4]),
                    Pai.get_values(tehai_data[0][5]),
                    Pai.get_values(tehai_data[0][6]),
                    Pai.get_values(tehai_data[0][7]),
                    Pai.get_values(tehai_data[0][8]),
                    Pai.get_values(tehai_data[0][9]),
                    Pai.get_values(tehai_data[0][10]),
                    Pai.get_values(tehai_data[0][11]),
                    Pai.get_values(tehai_data[0][12]),
                    Pai.get_values(tehai_data[0][13]),
                    tehai_data[0][14],
                    tehai_data[0][15],
                )

            return tehai_entity
        except sqlite3.Error:
            raise SqliteException

    def insert_answer_information(self, database_name: str, answer: AnswerInformation):
        """回答情報を登録する

        Args:
            database_name (str): データベース名
            answer (AnswerInformation): 回答情報が格納されたentity

        Raises:
            SqliteException: データベースアクセスに失敗した場合に発生する例外
        """

        if not os.path.isfile(database_name):
            raise SqliteException

        try:
            with sqlite3.connect(database_name) as connection:
                cursor = connection.cursor()
                # 外部キーを有効化
                cursor.execute("PRAGMA foreign_keys = true")
                cursor.execute(
                    "INSERT INTO player_information(player_name) VALUES(?)",
                    [answer.player_name],
                )
                player_id = cursor.lastrowid  # 登録されたプレーヤーid
                cursor.execute(
                    "INSERT INTO answer_information(question_id,player_id,answer_pai_id) VALUES(?,?,?)",
                    [
                        answer.question_id,
                        player_id,
                        answer.answer_pai_id.value.get("id"),
                    ],
                )

                connection.commit()
        except sqlite3.Error:
            raise SqliteException
