/**
 * HttpCommunicationControllerクラスをmockするクラス
 */

export default class MockHttpCommunicationController {
	constructor() {
		this.returnValue;
		this.isErrorOnMethod = false;
	}

	async getQestionInformation() {
		if (this.isErrorOnMethod) {
			throw new Error();
		}
		return await this.returnValue;
	}

	async registerAnswerInformation(answer) {
		if (this.isErrorOnMethod) {
			throw new Error();
		}
	}

	async getAggregateResults(questionId) {
		if (this.isErrorOnMethod) {
			throw new Error();
		}
		return await this.returnValue;
	}

	setReturn(value) {
		this.returnValue = value;
	}

	setError(isError) {
		this.isErrorOnMethod = isError;
	}
}
