/**
 * 麻雀牌のIDとパスを保持する
 *
 * @member {string} paiId - 牌のID
 * @member {string} imagePath - 画像へのパス
 *
 */
export default class Pai {
	constructor(paiId, imagePath) {
		this._paiId = paiId;
		this._imagePath = imagePath;
	}

	get paiId() {
		return this._paiId;
	}

	get imagePath() {
		return this._imagePath;
	}
}
