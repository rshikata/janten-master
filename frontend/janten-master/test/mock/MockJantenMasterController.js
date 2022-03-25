/**
 * JantenMasterControllerクラスをmockするクラス
 */

export default class MockJantenMasterController {
	constructor() {
		this.returnQestionData;
		this.returnAggregateData;
		this.isGetQestionDataError = false;
		this.isRegisterAnswerDataError = false;
		this.isGetAggregateDataError = false;
	}

	async getQestionInformation() {
		if (this.isGetQestionDataError) {
			throw new Error();
		}
		return await this.returnQestionData;
	}

	async registerAnswerInformation(answer) {
		if (this.isRegisterAnswerDataError) {
			throw new Error();
		}
	}

	async getAggregateResults(questionId) {
		if (this.isGetAggregateDataError) {
			throw new Error();
		}
		return await this.returnAggregateData;
	}

	setQestionDataReturn(value) {
		this.returnQestionData = value;
	}

	setAggregateDataReturn(value) {
		this.returnAggregateData = value;
	}

	setGetQestionDataError(isError) {
		this.isGetQestionDataError = isError;
	}

	setRegisterAnswerDataError(isError) {
		this.isRegisterAnswerDataError = isError;
	}

	setGetAggregateDataError(isError) {
		this.isGetAggregateDataError = isError;
	}
}
