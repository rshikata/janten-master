import { assert } from "chai";
import JantenMasterController from "../src/janten-master-controller";
import QuestionInformation from "../src/question-information";
import AnswerInformation from "../src/answer-information";
import ResultInformation from "../src/result-information";
import MockHttpCommunicationController from "./mock/MockHttpCommunicationController";
const fs = require("fs");

/**
 * JantenMasterControllerクラスのテスト
 */
describe("JantenMasterController", () => {
	/**
	 * getQestionInformation()のテスト
	 */
	describe("getQestionInformation()", () => {
		/**
		 * 正常に問題情報を取得できた場合、問題情報が格納されたオブジェクト(QuestionInformation)が返される。
		 */
		it("正常に取得できた場合", async () => {
			const controller = createController();
			const questionTestData = JSON.parse(
				fs.readFileSync("./test/test-data/question-data.json", "utf8")
			);
      
			controller.testController.setRequestDataReturn(questionTestData);

			const result = await controller.getQestionInformation();
			assert.instanceOf(result, QuestionInformation);
		});

		/**
		 * 問題情報取得でエラーが発生した場合、例外（Error）が発生する。
		 */
		it("問題情報取得でエラーが発生した場合", async () => {
			const controller = createController();
			controller.testController.setRequestError(true);

			try {
				await controller.getQestionInformation();
				assert.fail("Exception not thrown");
			} catch (e) {
				assert.instanceOf(e, Error);
			}

		});

		/**
		 * 取得したレスポンスにエラーメッセージが含まれていた場合、例外（Error）が発生する。
		 */
		it("取得したレスポンスにエラーメッセージが含まれていた場合", async () => {
			const controller = createController();
			const errorTestData = JSON.parse(
				fs.readFileSync("./test/test-data/error-data.json", "utf8")
			);

			controller.testController.setRequestDataReturn(errorTestData);
			try {
				await controller.getQestionInformation();
				assert.fail("Exception not thrown");
			} catch (e) {
				assert.instanceOf(e, Error);
				assert.equal(e.message, "dummy-error");
			}
		});
	});

	/**
	 * registerAnswerInformation()のテスト
	 */
	describe("registerAnswerInformation()", () => {
		/**
		 * 回答情報を正常に登録できた場合
		 */

		it("正常に登録できた場合", async () => {
			const controller = createController();
			try {
				controller.testController.setRequestDataReturn({ data: {}, error: {} });
				await controller.registerAnswerInformation(createAnswerInformation());
			} catch (e) {
				assert.fail("Exception thrown");
			}
		});

		/**
		 * 引数が不正(AnswerInformation以外)の場合、例外（TypeError）が発生する。
		 */
		it("引数が不正の場合", async () => {
			const controller = createController();
			try {
				await controller.registerAnswerInformation("dummy");

				assert.fail("Exception not thrown");
			} catch (e) {
				assert.instanceOf(e, TypeError);
				assert.equal(e.message, "引数が不正です。");
			}
		});

		/**
		 * 回答情報の登録時にエラーが発生した場合、例外（Error）が発生する。
		 */
		it("登録時にエラーが発生した場合", async () => {
			const controller = createController();

			controller.testController.setRequestError(true);
			try {
				await controller.registerAnswerInformation("dummy");
				assert.fail("Exception not thrown");
			} catch (e) {
				assert.instanceOf(e, Error);
			}
		});

		/**
		 * 取得したレスポンスにエラーメッセージが含まれていた場合、例外（Error）が発生する。
		 */
		it("取得したレスポンスにエラーメッセージが含まれていた場合", async () => {
			const controller = createController();

			const errorTestData = JSON.parse(
				fs.readFileSync("./test/test-data/error-data.json", "utf8")
			);
			controller.testController.setRequestDataReturn(errorTestData);
			try {
				await controller.getQestionInformation();
				assert.fail("Exception not thrown");
			} catch (e) {
				assert.instanceOf(e, Error);
				assert.equal(e.message, "dummy-error");
			}		
		});
	});

	/**
	 * getAggregateResults()のテスト
	 */
	describe("getAggregateResults()", () => {
		/**
		 * 集計結果が正常に取得できた場合、集計情報が格納された配列が返される。
		 */
		it("正常に取得できた場合", async () => {
			const controller = createController();
			const answerTestData = JSON.parse(
				fs.readFileSync("./test/test-data/answer-data.json", "utf8")
			);

			controller.testController.setRequestDataReturn(answerTestData);
			const result = await controller.getAggregateResults(1);
			assert.instanceOf(result[0], ResultInformation);
			assert.equal(result.length, 2);
		});

		/**
		 * 引数が不正(int以外)の場合、例外（TypeError）が発生する。
		 */
		it("引数が不正の場合", async () => {
			const controller = createController();
			try {
				await controller.getAggregateResults("dummy");
				assert.fail("Exception not thrown");
			} catch (e) {
				assert.instanceOf(e, TypeError);
				assert.equal(e.message, "引数が不正です。");
			}
		});

		/**
		 * 集計情報の取得でエラーが発生した場合、例外（Error）が発生する。
		 */
		it("集計情報の取得時にエラーが発生した場合", async () => {
			const controller = createController();
			controller.testController.setRequestError(true);
			try {
				await controller.getAggregateResults(1);
				assert.fail("Exception not thrown");
			} catch (e) {
				assert.instanceOf(e, Error);
			}
		});

		/**
		 * 取得したレスポンスにエラーメッセージが含まれていた場合、例外（Error）が発生する。
		 */
		it("取得したレスポンスにエラーメッセージが含まれていた場合", async () => {
			const controller = createController();

			const errorTestData = JSON.parse(
				fs.readFileSync("./test/test-data/error-data.json", "utf8")
			);
			controller.testController.setRequestDataReturn(errorTestData);
			try {
				await controller.getAggregateResults(1);
				assert.fail("Exception not thrown");
			} catch (e) {
				assert.instanceOf(e, Error);
				assert.equal(e.message, "dummy-error");
			}
		});
	});
});

export default class JantenMasterControllerForTest extends JantenMasterController {
	constructor() {
		super();
		this.testController = new MockHttpCommunicationController();
	}
	_createHttpOperator() {
		return this.testController;
	}
}
const createController = () => {
	return new JantenMasterControllerForTest();
};

const createAnswerInformation = () => {
	return new AnswerInformation(1, "dummy", "dummy");
};
