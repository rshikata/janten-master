<template>
	<div class="tehai-area" :clickdisabled="disabled">
		<vue-select-image
			class="dora-image"
			:data-images="tehaiImage"
			@onselectimage="onSelectImage"
			ref="single-select-image"
		></vue-select-image>
	</div>
</template>

<script>
import VueSelectImage from "vue-select-image";
require("vue-select-image/dist/vue-select-image.css");

export default {
	name: "tehai-image",
	props: {
		tehaiImage: {
			type: Array,
			require: true,
		},
		disabled: {
			type: Boolean,
			default: false,
		},
	},
	components: {
		VueSelectImage,
	},

	data() {
		return {
			id: null,
			paiId: null,
		};
	},
	methods: {
		onSelectImage(selected) {
			if (this.id == selected.id) {
				this.$refs["single-select-image"].removeFromSingleSelected();
				this.paiId = null;
				this.id = null;
			} else {
				this.paiId = selected.paiId;
				this.id = selected.id;
			}
			this.$emit("changeSelectPai", this.paiId);
		},
		clear() {
			this.$refs["single-select-image"].removeFromSingleSelected();
		},
	},
};
</script>

<style>
.tehai-area {
	background: #0aa8c4;
}

.tehai-area[clickdisabled="true"] {
	background: #0aa8c4;
	pointer-events: none;
}
</style>
