/**
 * 情報を保持する
 *
 * @member {Pai} answerPai - 回答牌情報
 * @member {number} answerRatio - 回答割合
 * @member {number} answerCount - 回答数
 *
 */

export default class ResultInformation {
	constructor(answerPai, answerRatio, answerCount) {
		this._answerPai = answerPai;
		this._answerRatio = answerRatio;
		this._answerCount = answerCount;
	}

	get answerPai() {
		return this._answerPai;
	}

	get answerRatio() {
		return this._answerRatio;
	}

	get answerCount() {
		return this._answerCount;
	}
}
