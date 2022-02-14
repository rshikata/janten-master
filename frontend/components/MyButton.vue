<template>
	<button
		class="my-button"
		:disabled="disabled"
		:style="buttonStyle"
		@click="onClickAnswer"
	>
		<slot></slot>
	</button>
</template>

<script>
export default {
	name: "my-button",
	props: {
		disabled: {
			type: Boolean,
			default: false,
		},
		height: {
			type: Number,
			default: 50,
		},
		width: {
			type: Number,
			default: 80,
		},
	},
	methods: {
		onClickAnswer() {
			this.$emit("onClick");
		},
	},
	computed: {
		buttonStyle: function () {
			return `height: ${this.height}px;width: ${this.width}px;`;
		},
	},
};
</script>

<style>
.my-button {
	color: #000000;
	background: #66c5d6;
	font-size: 100%;
	padding: 5px 10px;
	margin-left: 20px;
	margin-top: 10px;
	border: solid;
	border-color: #000000;
}

.my-button:disabled {
	background: #525050;
}
</style>
