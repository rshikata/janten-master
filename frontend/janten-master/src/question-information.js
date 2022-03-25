/**
 * 問題情報を保持する
 *
 * @member {number} questionId - 問題のID
 * @member {Pai} doraId - ドラ牌のID
 * @member {Pai} tsumoId - ツモ牌のID
 * @member {array<Pai>} tehai - 手牌の配列
 *
 */

export default class QuestionInformation {
	constructor(questionId, doraId, tsumoId, tehai) {
		this._questionId = questionId;
		this._doraId = doraId;
		this._tsumoId = tsumoId;
		this._tehai = tehai;
	}

	get questionId() {
		return this._questionId;
	}

	get doraId() {
		return this._doraId;
	}

	get tsumoId() {
		return this._tsumoId;
	}

	get tehai() {
		return this._tehai;
	}
}
