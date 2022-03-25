import { assert } from "chai";
import QuestionViewController from "../src/question-view-controller";
import ResultInformation from "../src/result-information";
import QuestionInformation from "../src/question-information";
import Pai from "../src/pai";
import MockJantenMasterController from "./mock/MockJantenMasterController";

/**
 * QuestionViewControllerクラスのテスト
 */
describe("QuestionViewController", () => {
	/**
	 * getRsultViewData()のテスト
	 */
	describe("getRsultViewData()", () => {
		/**
		 * 正常に集計結果が取得できた場合、集計結果のリストを返す。
		 */
		it("正常に取得できた場合", async () => {
			const controller = createController();

			controller.testController.setAggregateDataReturn([
				createResultInformation(),
			]);
      
			const result = await controller.getRsultViewData(1);
			assert.instanceOf(result, Array);
			assert.equal(result[0].paiId, "dummy");
			assert.equal(result[0].src, "dummy/dummy");
			assert.equal(result[0].answerRatio, 1);
			assert.equal(result[0].answerCount, 1);
		});

		/**
		 * 引数が不正(int以外)な場合、例外(TypeError)が発生する。
		 */
		it("引数が不正な場合", async () => {
			const controller = createController();
      
			controller.testController.setAggregateDataReturn([
				createResultInformation(),
			]);
			try {
				await controller.getRsultViewData("dummy");
				assert.fail("Exception not thrown");
			} catch (e) {
				assert.instanceOf(e, SyntaxError);
				assert.equal(e.message, "引数が不正です。");
			}
		});

		/**
		 * 集計結果の取得に失敗した場合、例外が発生する。
		 */
		it("集計結果の取得に失敗した場合", async () => {
			const controller = createController();

			controller.testController.setGetAggregateDataError(true);
			try {
				await controller.getRsultViewData("dummy");
				assert.fail("Exception not thrown");
			} catch (e) {
				assert.instanceOf(e, Error);
			}
		});
	});

	/**
	 * registerAnswerData()のテスト
	 */
	describe("registerAnswerData()", () => {
		/**
		 * 正常に回答情報が登録できた場合。
		 */
		it("正常に登録できた場合", async () => {
			const controller = createController();
			try {
				await controller.registerAnswerData(1, "dummy", "dummy");
			} catch (e) {
				assert.fail("Exception not thrown");
			}
		});

		/**
		 * 回答情報が不正な場合、例外(Error)が発生する。
		 */
		it("回答情報が不正な場合", async () => {
			const controller = createController();
			try {
				await controller.registerAnswerData(1, ":", "dummy");
				assert.fail("Exception not thrown");
			} catch (e) {
				assert.instanceOf(e, Error);
				assert.equal(e.message, "回答情報に未入力の項目があります。");
			}
		});

		/**
		 * 回答情報の登録に失敗した場合、例外(Error)が発生する。
		 */
		it("回答情報の登録に失敗した場合", async () => {
			const controller = createController();
			controller.testController.setRegisterAnswerDataError(true);
			try {
				await controller.registerAnswerData(1, "dummy", "dummy");
				assert.fail("Exception not thrown");
			} catch (e) {
				assert.instanceOf(e, Error);
			}
		});
	});

	/**
	 * getQestionViewData()のテスト
	 */
	describe("getQestionViewData()", () => {
		/**
		 * 正常に問題情報が取得できた場合、問題情報を含むオブジェクトが返される。
		 */
		it("正常に登録できた場合", async () => {
			const controller = createController();
			controller.testController.setQestionDataReturn(
				createQuestionInformation()
			);
			const result = await controller.getQestionViewData();

			assert.hasAllKeys(result, ["id", "dora", "tsumo", "tehai"]);
			assert.hasAllKeys(result["dora"], ["id", "paiId", "src"]);
			assert.hasAllKeys(result["tsumo"], ["id", "paiId", "src"]);
			assert.hasAllKeys(result["tehai"][0], ["id", "paiId", "src"]);
		});

		/**
		 * 問題情報の取得に失敗した場合、例外(Error)が発生する。
		 */
		it("問題情報の取得に失敗した場合", async () => {
			const controller = createController();
			controller.testController.setGetQestionDataError(true);
			try {
				await controller.getQestionViewData();
				assert.fail("Exception not thrown");
			} catch (e) {
				assert.instanceOf(e, Error);
			}
		});
	});
});

export default class QuestionViewControllerForTest extends QuestionViewController {
	constructor(url) {
		super(url);
		this.testController = new MockJantenMasterController();
	}
	_createJantenMasterOperator() {
		return this.testController;
	}
}
const createController = () => {
	return new QuestionViewControllerForTest("dummy");
};

// テスト用の問題情報を作成
const createQuestionInformation = () => {
	const testPai = new Pai("dummy", "dummy");
	const tehaiList = [];
	for (let i = 0; i < 13; i++) {
		tehaiList.push(testPai);
	}
	const questionInformation = new QuestionInformation(
		1,
		testPai,
		testPai,
		tehaiList
	);
	return questionInformation;
};

// テスト用の集計情報を作成
const createResultInformation = () => {
	const testData = new ResultInformation(new Pai("dummy", "dummy"), 1, 1);
	return testData;
};
