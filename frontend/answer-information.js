/**
 * 回答情報を保持する
 *
 * @member {number} questionId - 問題のID
 * @member {string} playerName - プレーヤーの名前
 * @member {string} answerPaiId - 回答牌のID
 *
 */

export default class AnswerInformation {
	constructor(questionId, playerName, answerPaiId) {
		this._questionId = questionId;
		this._playerName = playerName;
		this._answerPaiId = answerPaiId;
	}

	get questionId() {
		return this._questionId;
	}

	get playerName() {
		return this._playerName;
	}

	get answerPaiId() {
		return this._answerPaiId;
	}
}
