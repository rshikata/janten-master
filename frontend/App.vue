<template>
	<div class="display-area">
		<h1 class="sub-tittle">【問題】何切る?</h1>
		<div class="pai-area">
			<dora-image :doraImage="dora" />
			<tehai-image
				ref="tehaiImage"
				@changeSelectPai="setSelectPai"
				:tehaiImage="tehai"
				:disabled="viewMode"
			/>
		</div>
		<div class="button-area">
			<text-box
				ref="textBox"
				:disabledMode="viewMode"
				@setInputText="setPlayerName"
			/>
			<my-button :disabled="viewMode" @onClick="onClickAnswer">回答</my-button>
		</div>
		<h3 class="error-message">{{ errorMessage }}</h3>
		<div v-show="viewMode" class="results-area">
			<result-area :resultList="aggregateResults" />
			<my-button
				class="answer-button"
				:height="70"
				:width="120"
				:viewMode="viewMode"
				@onClick="onClickNextQuestion"
				>次の問題</my-button
			>
		</div>
	</div>
</template>

<script>
import DoraImage from "./components/DoraImage.vue";
import ResultArea from "./components/ResultArea.vue";
import TehaiImage from "./components/TehaiImage.vue";
import TextBox from "./components/TextBox.vue";
import MyButton from "./components/MyButton.vue";

import QuestionViewController from "./question-view-controller";

export default {
	name: "App",
	components: {
		DoraImage,
		TehaiImage,
		TextBox,
		ResultArea,
		MyButton,
	},
	data() {
		return {
			questionId: "",
			dora: {},
			tehai: [],
			paiId: null,
			playerName: null,
			viewMode: false,
			aggregateResults: [],
			errorMessage: "",
		};
	},
	async created() {
		try {
			await this.getQuestion();
		} catch (error) {
			this.errorMessage = error.message;
		}
	},
	methods: {
		async onClickAnswer() {
			try {
				await this.registerAnswer();
				this.setViewMode();
				await this.getAggregateResults();
				this.errorMessage = "";
			} catch (error) {
				this.errorMessage = error.message;
			}
		},

		async onClickNextQuestion() {
			try {
				await this.getQuestion();
				this.setViewMode();
				this.clear();
			} catch (error) {
				this.errorMessage = error.message;
			}
		},

		async getQuestion() {
			const operator = this._createQuestionViewController();
			const question = await operator.getQestionViewData();
			this.questionId = question.id;
			this.dora = question.dora;
			this.tehai = question.tehai.slice();
			this.tehai.push(question.tsumo);
		},

		async getAggregateResults() {
			const operator = this._createQuestionViewController();
			const aggregateResults = await operator.getRsultViewData(this.questionId);
			this.aggregateResults = aggregateResults.slice();
		},

		async registerAnswer() {
			const operator = this._createQuestionViewController();
			await operator.registerAnswerData(
				this.questionId,
				this.playerName,
				this.paiId
			);
		},

		clear() {
			this.$refs.tehaiImage.clear();
			this.$refs.textBox.clear();
			this.errorMessage = "";
			this.playerName = null;
			this.paiId = null;
		},

		setSelectPai(select) {
			this.paiId = select;
		},
		setPlayerName(name) {
			this.playerName = name;
		},
		setViewMode() {
			this.viewMode = !this.viewMode;
		},
		_createQuestionViewController() {
			return new QuestionViewController("http://localhost:8000");
		},
	},
};
</script>

<style>
body {
	background-color: #a1f8ed;
}

.sub-tittle {
	text-align: left;
	margin-left: 10%;
	margin-right: 10%;
}

.pai-area {
	padding: 30px;
	margin: 0 auto;
}

.display-area {
	display: flex;
	flex-direction: column;
	margin-top: 10%;
	margin-bottom: 10%;
}

.button-area {
	display: flex;
	flex-direction: row;
	margin-left: 60%;
	background: #a1f8ed;
}

.results-area {
	margin-left: 10%;
	margin-right: 10%;
}

.error-message {
	color: red;
	font-weight: bold;
	margin-left: 65%;
	margin-top: -5px;
}
.answer-button {
	margin-left: 90%;
}
</style>
