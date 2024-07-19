<script lang="ts">
	import Slider from '$lib/components/ui/slider/slider.svelte';
	let sliderValue = [0];
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<section class="flex flex-col justify-center items-center h-screen w-full gap-10">
	<h1 class="text-3xl">{sliderValue}</h1>
	<Slider bind:value={sliderValue} max={100} step={1} class="w-[240px]"  />
</section>

