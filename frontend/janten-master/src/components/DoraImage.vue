<template>
	<div class="dora-area">
		<h2 class="dora">ドラ</h2>
		<img class="dora-image" :src="doraImage.src" />
	</div>
</template>

<script>
export default {
	name: "dora-image",
	props: {
		doraImage: {
			type: Object,
			required: true,
		},
	},
};
</script>

<style>
.dora-area {
	display: flex;
	flex-direction: row;
	margin-left: 70%;
}

.dora {
	margin-left: 35%;
	margin-top: 15%;
}

.dora-image {
	margin: 20px;
}
</style>
