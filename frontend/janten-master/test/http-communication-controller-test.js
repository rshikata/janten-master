import { assert } from "chai";
import HttpCommunicationController from "../src/http-communication-controller";
import fetchMock from "fetch-mock";

/**
 * HttpCommunicationControllerクラスのテスト
 */
describe("HttpCommunicationController", () => {
	/**
	 * requestData()のテスト
	 */
	describe("getQestionInformation()", () => {
		// fetchMockをリセット
		afterEach(() => {
			fetchMock.restore();
		});

		/**
		 * GETメソッドで正常にリクエストを送信した場合、正常なレスポンスが返される。
		 */
		it("GETメソッドで正常にリクエストを送信した場合", async () => {
			const controller = createController();
			const testResponse = {
				ResponseDummy: "Response dummy",
			};
			fetchMock.get("dummyURL", {
				status: 200,
				body: JSON.stringify(testResponse),
			});
			const result = await controller.requestData("dummyURL");
			assert.hasAllKeys(result, ["ResponseDummy"]);
		});

		/**
		 * POSTメソッドで正常にリクエストを送信した場合、正常なレスポンスが返される。
		 */
		it("POSTメソッドで正常にリクエストを送信した場合", async () => {
			const controller = createController();

			const testRequest = {
				RequestDummy: "Request dummy",
			};

			fetchMock.post(
				(url, opts) => {
					return (
						url === "/dummyURL" && opts.body === JSON.stringify(testRequest)
					);
				},
				{
					status: 200,
					body: JSON.stringify({ ResponseDummy: "POST successfully" }),
				}
			);

			const result = await controller.requestData(
				"dummyURL",
				"POST",
				testRequest
			);
			assert.hasAllKeys(result, ["ResponseDummy"]);
		});

		/**
		 * リクエストは正常だがレスポンスのステータスコードが200以外の場合、例外(Error)が発生する。
		 */
		it("レスポンスのステータスコードが200以外の場合", async () => {
			const controller = createController();
			const testResponse = {
				ResponseDummy: "Response dummy",
			};
			fetchMock.get("dummyURL", { status: 404 });
			try {
				const result = await controller.requestData("dummyURL");
			} catch (e) {
				assert.instanceOf(e, Error);
				assert.equal(e.message, "リクエストエラー");
				return;
			}
			assert.fail("Exception not thrown");
		});
	});
});

const createController = () => {
	return new HttpCommunicationController();
};
