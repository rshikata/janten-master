/**
 * 機能に対応したデータの登録・取得を実行する。
 */

class JantenMasterController {
	/**
	 * 問題情報を取得する
	 *
	 * @return {QuestionInformation} 問題情報が格納されたentityを返す
	 * @throws {error} 問題情報の取得に失敗した場合に発生する例外
	 */
	getQestionInformation() {}

	/**
	 * 回答情報を登録する
	 *
	 * @param {number} questionId - 問題のID
	 * @param {string} playerName - プレーヤーの名前
	 * @param {number} answerPaiId - 回答牌のID
	 * @throws {error} 登録に失敗した場合に発生する例外
	 */
	registerAnswerInformation(questionId, playerName, answerPaiId) {}

	/**
	 * 集計結果を取得する
	 *
	 * @param {number} questionId - 問題のID
	 * @return {array<AnswerInformation>} 牌に対する集計情報を保持したentityを格納した配列を返す
	 * @throws {error} 集計結果の取得に失敗した場合に発生する例外
	 */
	getAggregateResults(questionId) {}
}
