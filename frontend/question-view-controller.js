/**
 * 画面の入出力のための処理を実行する。
 */
import JantenMasterController from "./janten-master-controller";
import InputDataValidator from "./input-data-validator";
import AnswerInformation from "./answer-information";

export default class QuestionViewController {
	/**
	 * urlを初期化する
	 * @param {string} 表示する画像のURL
	 */
	constructor(url) {
		this._url = url;
	}

	/**
	 * 集計結果データを表示形式に変換する
	 * @param {number} questionId
	 * @return {array<Object>} 集計結果のリスト
	 * @throws {SyntaxError} 引数が不正の場合に発生するエラー
	 */
	async getRsultViewData(questionId) {
		if (isNaN(questionId)) {
			throw new SyntaxError("引数が不正です。");
		}
		const operator = this._createJantenMasterOperator();
		const aggregateResults = await operator.getAggregateResults(questionId);

		const resultList = [];
		aggregateResults.forEach((result, index) => {
			resultList.push(this._createResultElement(result, index));
		});

		return resultList;
	}

	/**
	 * 入力情報をチェックして、回答情報を登録する
	 * @param {number} questionId - 問題のID
	 * @param {string} playerName - プレーヤーの名前
	 * @param {number} answerPaiId - 回答牌のID
	 * @throws {Error} 登録情報に不正な値が存在する場合に発生するエラー
	 */
	async registerAnswerData(questionId, playerName, answerPaiId) {
		const operator = this._createJantenMasterOperator();
		const validator = new InputDataValidator();
		if (validator.validateAnswerInformation(playerName, answerPaiId)) {
			const answer = new AnswerInformation(questionId, playerName, answerPaiId);
			await operator.registerAnswerInformation(answer);
		} else {
			throw new Error("回答情報に未入力の項目があります。");
		}
	}

	/**
	 * 問題情報を表示形式に変換する
	 * @returns {Object} 問題情報リスト
	 */
	async getQestionViewData() {
		const operator = this._createJantenMasterOperator();
		const questionData = await operator.getQestionInformation();

		const tehai = questionData.tehai;
		const tehaiList = [];
		tehai.forEach((pai, index) => {
			tehaiList.push(this._createPaiElement(pai, index));
		});

		const qestionData = {
			id: questionData.questionId,
			dora: this._createPaiElement(questionData.doraId, 1),
			tsumo: this._createPaiElement(questionData.tsumoId, 14),
			tehai: tehaiList,
		};

		return qestionData;
	}

	// 集計結果要素の作成
	_createResultElement(result, index) {
		const resultElement = {
			id: index,
			paiId: result.answerPai.paiId,
			src: this._createURL(result.answerPai.imagePath),
			answerRatio: result.answerRatio,
			answerCount: result.answerCount,
		};
		return resultElement;
	}

	// 牌要素の作成
	_createPaiElement(pai, index) {
		const paiElement = {
			id: index,
			paiId: pai.paiId,
			src: this._createURL(pai.imagePath),
		};

		return paiElement;
	}

	// 画像URLの作成
	_createURL(path) {
		return `${this._url}/${path}`;
	}

	_createJantenMasterOperator() {
		return new JantenMasterController();
	}
}
