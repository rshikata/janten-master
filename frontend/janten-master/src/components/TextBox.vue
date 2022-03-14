<template>
	<div class="text-box">
		<h2>名前:</h2>
		<input
			type="text"
			class="player-name"
			size="15"
			v-model="playerName"
			v-bind:disabled="disabledMode"
		/>
	</div>
</template>

<script>
export default {
	name: "text-box",

	props: {
		disabledMode: {
			type: Boolean,
			default: false,
		},
	},
	data() {
		return {
			playerName: "",
		};
	},
	methods: {
		clear() {
			this.playerName = "";
		},
	},
	watch: {
		playerName: function () {
			const pattern =
				/[!"#$%&'()*+\-.,/:;<=>?@[\\\]^_`{|}~！”＃＄％＆’（）＝～｜‘｛＋＊｝＜＞？＿－＾￥＠「；：」、。・ /\s]/g;
			this.playerName = this.playerName.replace(pattern, "");
			this.$emit("setInputText", this.playerName);
		},
	},
};
</script>

<style>
.text-box {
	display: flex;
	flex-direction: row;
}
.player-name {
	margin-top: 10px;
	margin-left: 20px;
	height: 50px;
	font-size: 150%;
}
</style>
