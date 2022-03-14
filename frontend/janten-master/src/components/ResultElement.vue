<template>
	<div class="result">
		<img :src="result.src" />
		<p class="stats">{{ result.answerRatio }}%({{ result.answerCount }}人)</p>
	</div>
</template>

<script>
export default {
	name: "result-element",
	props: {
		result: {
			type: Object,
		},
	},
};
</script>

<style>
.result {
	background: #23d3f1;
	display: flex;
	flex-direction: row;
}
.stats {
	font-size: 150%;
	padding: 10px 20px;
}
</style>
