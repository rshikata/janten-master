class MahjongInformationController:
    """機能に対応したデータ操作を行う"""

    def register_answer_information(self, question_id, player_name, answer_pai):
        """プレーヤーの回答情報をデータベースに登録する

        Args:
            question_id: 問題のID
            player_name: プレーヤーの名前
            answer_pai: 回答牌のID

        Returns:
            json: 登録結果を格納したjsonを返す
            
        """
        pass

    def get_aggregate_results(self, question_id):
        """データベースから集計情報を取得する

        Args:
            question_id (int): 問題のID
        
        Returns:
            json: 集計情報を取得した結果を格納したjsonを返す
        
        """
        pass

    def get_qestion_information():
        """データベースから問題情報を取得する
       
        Returns:
            json: 問題情報を取得した結果を格納したjsonを返す
        
        """
        pass

    