<script>
	import { onMount } from 'svelte';
	import { fetchPredictions } from '$lib/api';
	import { t } from '$lib/i18n.js';

	let items = [];
	let loading = true;
	let error = null;

	onMount(async () => {
		try {
			const res = await fetchPredictions();
			items = res.data;
		} catch (e) {
			error = e.message;
		} finally {
			loading = false;
		}
	});

	function imageUrl(path) {
		return `https://api.adam-gbyte.my.id/${path.replaceAll('\\', '/')}`;
	}

	function formatDate(date) {
		return new Date(date).toLocaleString('id-ID');
	}

	function badgeColor(label) {
		const map = {
			0: 'bg-yellow-500', // hampir_matang
			1: 'bg-green-500', // matang_sempurna
			2: 'bg-red-500', // mentah
			3: 'bg-emerald-500', // sangat_matang
			4: 'bg-orange-500' // setengah_matang
		};
		return map[label] ?? 'bg-gray-500';
	}
</script>

<svelte:head>
	<title>{$t('nav.history')} | Cavendish</title>
</svelte:head>

<div class="min-h-screen bg-linear-to-br from-gray-50 via-white to-gray-100 p-6 pt-6">
	<div class="mx-auto max-w-7xl space-y-8">
		<!-- Header -->
		<header class="space-y-2 text-center">
			<h1 class="text-3xl font-extrabold text-gray-800">
				{$t('history.title')}
			</h1>
			<p class="text-gray-500">
				{$t('history.subtitle')}
			</p>
		</header>

		<!-- Loading -->
		{#if loading}
			<div class="grid grid-cols-2 gap-6 sm:grid-cols-3 lg:grid-cols-4">
				{#each Array(8) as _}
					<div class="aspect-square animate-pulse rounded-2xl bg-gray-200"></div>
				{/each}
			</div>
		{/if}

		<!-- Error -->
		{#if error}
			<div class="mx-auto max-w-xl rounded-xl bg-red-100 p-4 text-center text-red-700">
				{error}
			</div>
		{/if}

		<!-- Empty -->
		{#if !loading && items.length === 0}
			<div class="py-20 text-center text-gray-500">
				{$t('history.empty')}
			</div>
		{/if}

		<!-- Gallery -->
		{#if !loading && items.length > 0}
			<section class="grid grid-cols-2 gap-6 sm:grid-cols-3 lg:grid-cols-4">
				{#each items as item}
					<article
						class="group relative aspect-square overflow-hidden rounded-2xl shadow transition hover:shadow-xl"
					>
						<!-- Image -->
						<img
							src={imageUrl(item.file_path)}
							alt="Prediction"
							class="h-full w-full object-cover transition duration-700 group-hover:scale-110"
						/>

						<!-- Gradient Overlay -->
						<div
							class="absolute inset-0 bg-linear-to-t from-black/80 via-black/30 to-transparent opacity-0 transition group-hover:opacity-100"
						></div>

						<!-- Badge -->
						<span
							class={`absolute top-3 left-3 rounded-full px-3 py-1 text-xs font-semibold text-white ${badgeColor(
								item.prediction
							)}`}
						>
							{$t('labels.' + item.prediction)}
						</span>

						<!-- Hover Content -->
						<div
							class="absolute inset-0 flex flex-col justify-end p-4 text-white opacity-0 transition group-hover:opacity-100"
						>
							<div class="space-y-2">
								<p class="text-sm font-semibold">
									{$t('classification.confidence')}
									{(item.confidence * 100).toFixed(1)}%
								</p>

								<!-- Confidence Bar -->
								<div class="h-2 overflow-hidden rounded-full bg-white/30">
									<div
										class="h-full bg-white"
										style={`width: ${(item.confidence * 100).toFixed(0)}%`}
									></div>
								</div>

								<p class="text-xs text-gray-200">
									{formatDate(item.created_at)}
								</p>
							</div>
						</div>
					</article>
				{/each}
			</section>
		{/if}
	</div>
</div>
