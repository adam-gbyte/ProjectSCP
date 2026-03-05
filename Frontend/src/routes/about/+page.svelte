<script>
	import { t } from '$lib/i18n.js';
</script>

<svelte:head>
	<title>{$t('nav.about')} | Cavendish</title>
</svelte:head>

<div class="min-h-screen bg-linear-to-br from-yellow-50 via-white to-green-50 pt-6">
	<!-- HERO SECTION -->
	<section class="mx-auto max-w-7xl px-6 pt-8 pb-28">
		<div class="grid items-center gap-16 md:grid-cols-2">
			<!-- TEXT -->
			<div class="space-y-10">
				<span
					class="inline-block rounded-full bg-yellow-100 px-5 py-2 text-sm font-semibold text-yellow-700"
				>
					{$t('about.badge')}
				</span>

				<h1 class="text-4xl leading-tight font-extrabold text-green-900 md:text-5xl">
					{$t('about.title')} <br />
					<span class="text-yellow-600">{$t('about.subtitle')}</span>
				</h1>

				<div class="space-y-6 text-lg leading-relaxed text-gray-700">
					<p>
						{$t('about.p1')} <span class="font-semibold">Computer Vision</span>.
					</p>

					<p>
						<span class="font-semibold">MobileNetV2</span>
						{$t('about.p2')}
						<span class="font-semibold">Support Vector Machine (SVM)</span>
						{$t('about.p2_into')}
						<strong> {$t('about.classes')}</strong>
					</p>
				</div>
			</div>

			<!-- IMAGE -->
			<div class="flex justify-center md:justify-end">
				<img
					src="/logo.png"
					alt="Pisang Cavendish"
					class="w-full max-w-md rounded-2xl shadow-xl transition hover:scale-105"
				/>
			</div>
		</div>
	</section>

	<!-- TECHNOLOGY STACK -->
	<section class="mx-auto max-w-7xl px-6 pt-8 pb-32">
		<div class="mb-16 text-center">
			<h2 class="text-3xl font-bold text-green-900">
				{$t('about.tech_title')}
			</h2>
			<p class="mt-4 text-lg text-gray-600">
				{$t('about.tech_desc')}
			</p>
		</div>

		<div class="grid gap-10 sm:grid-cols-2 lg:grid-cols-4">
			<div class="rounded-2xl bg-white p-8 shadow-md transition hover:shadow-lg">
				<h3 class="mb-3 text-lg font-bold text-green-800">Frontend</h3>
				<p class="text-gray-600">SvelteKit, HTML, CSS, JavaScript</p>
			</div>

			<div class="rounded-2xl bg-white p-8 shadow-md transition hover:shadow-lg">
				<h3 class="mb-3 text-lg font-bold text-green-800">Backend</h3>
				<p class="text-gray-600">Python (FastAPI)</p>
			</div>

			<div class="rounded-2xl bg-white p-8 shadow-md transition hover:shadow-lg">
				<h3 class="mb-3 text-lg font-bold text-green-800">Database</h3>
				<p class="text-gray-600">MongoDB</p>
			</div>

			<div class="rounded-2xl bg-white p-8 shadow-md transition hover:shadow-lg">
				<h3 class="mb-3 text-lg font-bold text-green-800">Model AI</h3>
				<p class="text-gray-600">MobileNetV2 + SVM</p>
			</div>
		</div>
	</section>
</div>
