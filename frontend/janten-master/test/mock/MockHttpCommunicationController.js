/**
 * HttpCommunicationControllerクラスをmockするクラス
 */

export default class MockHttpCommunicationController {
	constructor() {
		this.returnValue;
		this.isErrorOnRequestData = false;
	}
	async requestData(url, methodName = "GET", parameter = {}) {
		if (this.isErrorOnRequestData) {
			throw new Error();
		}
		return await this.returnValue;
	}

	setReturn(value) {
		this.returnValue = value;
	}

	setError(isError) {
		this.isErrorOnRequestData = isError;
	}
}
