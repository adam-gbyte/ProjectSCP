<script>
	import { t } from '$lib/i18n.js';
</script>

<svelte:head>
	<title>{$t('paper.title')} | Cavendish</title>
</svelte:head>

<div class="flex min-h-screen flex-col bg-gray-50">
	<!-- PDF Viewer -->
	<main class="flex-1 p-6">
		<div class="mx-auto max-w-6xl overflow-hidden rounded-2xl bg-white shadow-lg">
			<!-- svelte-ignore a11y_missing_attribute -->
			<iframe src="/sample.pdf" class="h-[85vh] w-full"></iframe>
		</div>
	</main>
</div>
