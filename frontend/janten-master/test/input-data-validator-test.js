import { assert } from "chai";
import InputDataValidator from "../src/input-data-validator";

/**
 * InputDataValidatorクラスのテスト
 */
describe("InputDataValidator", () => {
	describe("validateAnswerInformation()のテスト", () => {
		/**
		 * 引数が全て正しい場合、trueが返される。
		 */
		it("引数が全て正しい場合", () => {
			const controller = createController();
			assert.isTrue(controller.validateAnswerInformation("dummy", "dummy"));
		});

		/**
		 * playerNameにstring型以外が指定された場合、、falseが返される。
		 */
		it("playerNameがstring型以外の場合", () => {
			const controller = createController();
			assert.isFalse(controller.validateAnswerInformation(1, "MAN_01"));
		});

		/**
		 * playerNameに半角記号が含まれる場合、falseが返される。
		 */
		it("playerNameに半角記号が含まれる場合", () => {
			const controller = createController();
			assert.isFalse(controller.validateAnswerInformation("!/:", "dummy"));
		});

		/**
		 * playerNameに半角スペースが含まれる場合、falseが返される。
		 */
		it("playerNameに半角スペースが含まれる場合", () => {
			const controller = createController();
			assert.isFalse(controller.validateAnswerInformation(" ", "dummy"));
		});

		/**
		 * playerNameに全角記号が含まれる場合、falseが返される。
		 */
		it("playerNameに全角記号が含まれる場合", () => {
			const controller = createController();
			assert.isFalse(controller.validateAnswerInformation("！・％", "dummy"));
		});

		/**
		 * playerNameに全角スペースが含まれる場合、falseが返される。
		 */
		it("playerNameに全角スペースが含まれる場合", () => {
			const controller = createController();
			assert.isFalse(controller.validateAnswerInformation("　", "dummy"));
		});

		/**
		 * playerNameに空文字が含まれる場合、falseが返される。
		 */
		it("playerNameに空文字が含まれる場合", () => {
			const controller = createController();
			assert.isFalse(controller.validateAnswerInformation("", "dummy"));
		});

		/**
		 * playerNameに不正文字と正しい文字が混在する場合、falseが返される。
		 */
		it("playerNameに不正文字と正しい文字が混在する場合", () => {
			const controller = createController();
			assert.isFalse(controller.validateAnswerInformation(":s・i", "dummy"));
		});

		/**
		 * answerPaiIdにstring型以外が指定された場合、falseが返される。
		 */
		it("answerPaiIdがstring型以外の場合", () => {
			const controller = createController();
			assert.isFalse(controller.validateAnswerInformation("dummy", 1));
		});
	});
});

const createController = () => {
	return new InputDataValidator();
};
