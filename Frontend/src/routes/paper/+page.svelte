<svelte:head>
	<title>Preview Dokumen</title>
</svelte:head>

<div class="flex min-h-screen flex-col bg-gray-50">
	<!-- Toolbar -->
	<!-- <header class="flex items-center justify-between bg-white px-6 py-4 shadow-sm">
		<h1 class="text-xl font-semibold text-gray-700">📄 Preview Dokumen</h1>
		<a
			href="/sample.pdf"
			download
			class="rounded-lg bg-blue-600 px-4 py-2 text-white transition hover:bg-blue-700"
		>
			Unduh PDF
		</a>
	</header> -->

	<!-- PDF Viewer -->
	<main class="flex-1 p-6">
		<div class="mx-auto max-w-6xl overflow-hidden rounded-2xl bg-white shadow-lg">
			<!-- svelte-ignore a11y_missing_attribute -->
			<iframe src="/sample.pdf" class="h-[85vh] w-full"></iframe>
		</div>
	</main>
</div>
