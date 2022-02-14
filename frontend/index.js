import Vue from "vue";
import VueSelectImage from "vue-select-image";
require("vue-select-image/dist/vue-select-image.css");
import QuestionViewController from "./question-view-controller";

Vue.use(VueSelectImage);

new Vue({
	el: "#display-area",
	data: {
		dora: { id: 5, src: "../pai-images/ji3-66-90-l.png" },
		stumo: {},
		tehai: [{}],
		resultImages: [{}],
		playerName: "",
		viewMode: false,
		SelectImage: "",
		id: "",
	},
	created() {
		// 最初の問題取得
		//this.dora.push({ id: 5, src: "pai-images/ji3-66-90-l.png" });
		this.changeImage();
	},
	methods: {
		onSelectImage: function (selected) {
			//this.SelectImage = "id:" + selected.id;

			if (this.id == selected.id) {
				this.$refs["single-select-image"].removeFromSingleSelected();
				this.id = "";
			} else {
				this.id = selected.id;
			}
		},
		async changeImage() {
			const operator = new QuestionViewController();
			const data = await operator.onClickNextQuestionButtonEvent();
			console.log(data.dora);
			this.dora = data.dora;
			this.tsumo = {};
			//this.tehai = data.tehai.slice();
			this.tehai = [{ id: 5, src: "../pai-images/ji3-66-90-l.png" }].slice();
			this.viewMode = false;
			this.playerName = "";
		},

		answerButton() {
			this.viewMode = true;
			this.resultImages.splice(0);
			let im = [
				{ src: "../pai-images/ji2-66-90-l.png", raito: "20", number: 2 },
			];
			im.forEach((element) => {
				this.resultImages.push(element);
			});

			//console.log(this.resultImages);
		},
	},
	watch: {
		playerName: function () {
			pattern = /[!"#$%&'()\*\+\-\.,\/:;<=>?@\[\\\]^_`{|}~]/g;
			this.playerName = this.playerName.replace(pattern, "");
		},
	},
});
//const app = Vue.createApp(View);
//app.use(VueSelectImage);

//Vue.createApp(View).mount("#display-area");
//app.mount("#display-area");
