/**
 * HTTPリクエストを送り、結果をHTTPレスポンスとして受け取る。
 */
export default class HttpCommunicationController {
	/**
	 * @param {string} url - リクエストURL
	 * @param {string} [methodName = "GET"] - リクエストメソッド名
	 * @param {string} [parameter] - リクエストパラメータ
	 * @return {json} 取得したjsonを返す
	 * @throws {Error} ネットワークやリクエストで失敗した場合発生するエラー
	 * @throws {SyntaxError} 引数が不正の場合発生するエラー
	 */

	async requestData(url, methodName = "GET", parameter) {
		const options = {
			method: methodName,
			headers: {
				"Content-Type": "application/json",
			},
		};
		if (methodName != "GET") {
			if (parameter == undefined) {
				throw new SyntaxError("parameter is undefined");
			}
			options.body = JSON.stringify(parameter);
		}

		const response = await fetch(url, options)
			.catch(() => {
				throw new Error("ネットワークエラーが発生しました。");
			})
			.then(async (response) => {
				return await response.json();
			})
			.catch(() => {
				throw new Error("リクエストエラー");
			});

		return await response;
	}
}
