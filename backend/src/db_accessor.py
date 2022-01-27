class DBAccessor:
    """データベースに対するデータの取得・登録を行う"""

    def get_number_of_records():
        """テーブルのレコード数を取得する

        Args:
            table_name (str): データベースのテーブル名
        
        Returns:
            int: テーブルのレコード数

        Raises:
            SqliteException: データベースアクセスに失敗した場合に発生する例外

        """
        pass

    
    def select_aggregate_information(self,table_name,question_id):
        """集計結果を取得する

        Args:
            table_name (str): データベースのテーブル名
            question_id (int): 問題のID
        
        Returns:
            array<AggregateResultsInformation>: 回答情報を保持するentityの配列を返す

        Raises:
            SqliteException: データベースアクセスに失敗した場合に発生する例外

        """
        pass

    def select_question_information(self,tabele_name,question_id):
        """問題情報を取得する

        Args:
            table_name (str): データベースのテーブル名
            question_id (int): 問題のID
        
        Returns:
            QuestionInformation: 問題情報が格納されたentityを返す

        Raises:
            SqliteException: データベースアクセスに失敗した場合に発生する例外

        """
        pass

    def select_tehai_information(self,tabele_name,tehai_id):
        """手牌情報を取得する

        Args:
            table_name (str): データベースのテーブル名
            tehai_id (int): 手牌のID
        
        Returns:
            TehaiInformation: 手牌情報が格納されたentityを返す

        Raises:
            SqliteException: データベースアクセスに失敗した場合に発生する例外

        """
        pass

    def insert_answer_information(self,answer):
        """回答情報を登録する

        Args:
            answer (AnswerInformation): 回答情報が格納されたentity

        Raises:
            SqliteException: データベースアクセスに失敗した場合に発生する例外

        """