<template>
	<div>
		<h1>【回答の集計結果】</h1>
		<div class="aggregate-results">
			<div v-for="resultData in resultList" :key="resultData.id">
				<result-element :result="resultData" />
			</div>
		</div>
	</div>
</template>

<script>
import ResultElement from "./ResultElement.vue";
export default {
	name: "result-area",
	components: {
		ResultElement,
	},
	props: {
		resultList: {
			type: Array,
			required: true,
		},
	},
};
</script>

<style>
.aggregate-results {
	display: flex;
	flex-wrap: wrap;
	flex-direction: row;
}
</style>
