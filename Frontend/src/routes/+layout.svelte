<script>
	import './layout.css';
	import favicon from '$lib/assets/favicon.svg';

	let { children } = $props();

  import Navbar from "$lib/components/Navbar.svelte";
  import Footer from "$lib/components/Footer.svelte";
</script>

<svelte:head>
  <link rel="icon" href={favicon} />
  <title>Pisang Cavendish</title>
</svelte:head>

<Navbar />

<main class="pt-16">
  {@render children()}
</main>

<Footer /> 