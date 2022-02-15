/**
 * プレーヤーから入力された情報のチェックを行う。
 */

export default class InputDataValidator {
	/**
	 * 入力された回答情報が正しいかチェックする
	 *
	 * @param {string} playerName - プレーヤーの名前
	 * @param {number} answerPaiId - 回答牌のID
	 * @return {boolean} 結果を真偽値で返す
	 */
	validateAnswerInformation(playerName, answerPaiId) {
		let validateFlag = false;
		if (answerPaiId && playerName) {
			const pattern =
				/[!"#$%&'()*+\-.,/:;<=>?@[\\\]^_`{|}~！”＃＄％＆’（）＝～｜‘｛＋＊｝＜＞？＿－＾￥＠「；：」、。・ /\s]/g;
			playerName = playerName.replace(pattern, "");
			if (playerName.length !== 0) {
				validateFlag = true;
			}
		}
		return validateFlag;
	}
}
