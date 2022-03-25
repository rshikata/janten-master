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

	setRequestDataReturn(value) {
		this.returnValue = value;
	}

	setRequestError(isError) {
		this.isErrorOnRequestData = isError;
	}
}
