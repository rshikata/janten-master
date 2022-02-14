/**
 * 機能に対応したデータの登録・取得を実行する。
 */
import HttpCommunicationController from "./http-communication-controller";
import Pai from "./pai";
import HTTPMthod from "./http-method";
import QuestionInformation from "./question_information";
import ResultInformation from "./result-information";
import AnswerInformation from "./answer-information";

export default class JantenMasterController {
	/**
	 * 問題情報を取得する
	 *
	 * @return {QuestionInformation} 問題情報
	 * @throws {Error} 問題情報の取得に失敗した場合に発生するエラー
	 */
	async getQestionInformation() {
		const operator = this._createHttpOperator();
		const url = "http://localhost:8000/webapi/v1/question-information/";
		const questionData = await operator.requestData(url, HTTPMthod.GET);

		if (Object.keys(questionData["error"]).length == 0) {
			return this._perseQestionInformation(questionData);
		} else {
			throw new Error(questionData["error"]["message"]);
		}
	}

	/**
	 * 回答情報を登録する
	 *
	 * @param {AnswerInformation} answer - 回答情報
	 * @throws {Error} 登録に失敗した場合に発生するエラー
	 * @throws {SyntaxError} 引数が不正の場合に発生するエラー
	 */
	async registerAnswerInformation(answer) {
		if (!(answer instanceof AnswerInformation)) {
			throw new SyntaxError("引数が不正です。");
		}
		const answerData = {
			question_id: answer.questionId,
			player_name: answer.playerName,
			answer_pai: answer.answerPaiId,
		};

		const operator = this._createHttpOperator();
		const url = "http://localhost:8000/webapi/v1/answer-information/";
		const registerResult = await operator.requestData(
			url,
			HTTPMthod.POST,
			answerData
		);

		if (Object.keys(registerResult["error"]).length != 0) {
			throw new Error(registerResult["error"]["message"]);
		}
	}

	/**
	 * 集計結果を取得する
	 *
	 * @param {number} questionId - 問題のID
	 * @return {array<ResultInformation>} 牌に対する集計情報
	 * @throws {Error} 集計結果の取得に失敗した場合に発生するエラー
	 * @throws {SyntaxError} 引数が不正の場合に発生するエラー
	 */
	async getAggregateResults(questionId) {
		if (isNaN(questionId)) {
			throw new SyntaxError("引数が不正です。");
		}
		const operator = this._createHttpOperator();
		const url = `http://localhost:8000/webapi/v1/aggregate-results/?id=${questionId}`;
		const AggregateResults = await operator.requestData(url, HTTPMthod.GET);
		if (Object.keys(AggregateResults["error"]).length == 0) {
			const result = this._perseAggregateResults(AggregateResults);

			result.sort((a, b) => b.answerCount - a.answerCount);

			return result;
		} else {
			throw AggregateResults["error"]["message"];
		}
	}

	// パースして集計情報を作成
	_perseAggregateResults(results) {
		const answerData = results["data"]["answer_imformation"];

		const totalAnswer = answerData.reduce((sum, answer) => {
			return sum + answer["number"];
		}, 0);

		const resultList = [];
		answerData.forEach((answer) => {
			const pai = new Pai(answer["id"], answer["path"]);
			const ratio = Math.round((answer["number"] / totalAnswer) * 1000) / 10;
			resultList.push(new ResultInformation(pai, ratio, answer["number"]));
		});

		return resultList;
	}

	// パースして問題情報を作成
	_perseQestionInformation(question) {
		const tehai = question["data"]["tehai"];
		const dora = new Pai(
			question["data"]["dora-pai"]["id"],
			question["data"]["dora-pai"]["path"]
		);
		const tsumo = new Pai(
			question["data"]["tsumo-pai"]["id"],
			question["data"]["tsumo-pai"]["path"]
		);
		let tehaiList = [];
		tehai.forEach((element) => {
			const pai = new Pai(element["id"], element["path"]);
			tehaiList.push(pai);
		});

		const questionInformation = new QuestionInformation(
			question["data"]["question-id"],
			dora,
			tsumo,
			tehaiList
		);
		return questionInformation;
	}

	_createHttpOperator() {
		return new HttpCommunicationController();
	}
}
