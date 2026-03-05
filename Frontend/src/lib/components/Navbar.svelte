<script>
	import { onMount, onDestroy } from 'svelte';
	import { browser } from '$app/environment';
	import { t, locale, toggleLocale } from '$lib/i18n.js';

	let scrolled = false;
	let menuOpen = false;

	const handleScroll = () => {
		scrolled = window.scrollY > 50;
	};

	const toggleMenu = () => {
		menuOpen = !menuOpen;
	};

	onMount(() => {
		if (!browser) return;
		window.addEventListener('scroll', handleScroll);
	});

	onDestroy(() => {
		if (!browser) return;
		window.removeEventListener('scroll', handleScroll);
	});
</script>

<nav class="nav-base {scrolled ? 'nav-scrolled' : 'nav-transparent'}">
	<div class="mx-auto max-w-7xl px-6">
		<div class="flex h-16 items-center justify-between">
			<!-- LOGO -->
			<h1 class="text-xl font-bold">Cavendish</h1>

			<!-- DESKTOP MENU -->
			<ul class="hidden items-center gap-6 font-medium md:flex">
				<li><a href="/" class="nav-link">{$t('nav.home')}</a></li>
				<li><a href="/about" class="nav-link">{$t('nav.about')}</a></li>
				<li><a href="/classification" class="nav-link">{$t('nav.classification')}</a></li>
				<li><a href="/history" class="nav-link">{$t('nav.history')}</a></li>
				<li><a href="/paper" class="nav-link">{$t('nav.paper')}</a></li>
				<!-- LANGUAGE TOGGLE -->
				<li>
					<div
						class="flex items-center rounded-full border border-gray-300 p-1 text-sm font-semibold"
					>
						<button
							on:click={() => locale.set('id')}
							class="rounded-full px-3 py-1 transition
      {$locale === 'id' ? 'bg-black text-white' : 'text-gray-600 hover:bg-gray-100'}"
						>
							ID
						</button>

						<button
							on:click={() => locale.set('en')}
							class="rounded-full px-3 py-1 transition
      {$locale === 'en' ? 'bg-black text-white' : 'text-gray-600 hover:bg-gray-100'}"
						>
							EN
						</button>
					</div>
				</li>
			</ul>

			<!-- MOBILE BUTTON -->
			<div class="flex items-center gap-2 md:hidden">
				<!-- LANGUAGE TOGGLE (mobile) -->
				<div
					class="flex items-center rounded-full border border-gray-300 p-0.5 text-xs font-semibold"
				>
					<button
						on:click={() => locale.set('id')}
						class="rounded-full px-2 py-1 transition
    {$locale === 'id' ? 'bg-black text-white' : 'text-gray-600'}"
					>
						ID
					</button>

					<button
						on:click={() => locale.set('en')}
						class="rounded-full px-2 py-1 transition
    {$locale === 'en' ? 'bg-black text-white' : 'text-gray-600'}"
					>
						EN
					</button>
				</div>

				<button
					class="flex items-center justify-center rounded-lg p-2 hover:bg-black/5"
					on:click={toggleMenu}
					aria-label="Toggle menu"
				>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-6 w-6"
						fill="none"
						viewBox="0 0 24 24"
						stroke="currentColor"
					>
						{#if menuOpen}
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M6 18L18 6M6 6l12 12"
							/>
						{:else}
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M4 6h16M4 12h16M4 18h16"
							/>
						{/if}
					</svg>
				</button>
			</div>
		</div>

		<!-- MOBILE MENU -->
		{#if menuOpen}
			<div
				class="mt-2 overflow-hidden rounded-2xl bg-white/90 shadow-lg backdrop-blur-xl md:hidden"
			>
				<ul class="flex flex-col">
					<li><a href="/" class="mobile-link">{$t('nav.home')}</a></li>
					<li><a href="/about" class="mobile-link">{$t('nav.about')}</a></li>
					<li><a href="/classification" class="mobile-link">{$t('nav.classification')}</a></li>
					<li><a href="/history" class="mobile-link">{$t('nav.history')}</a></li>
					<li><a href="/paper" class="mobile-link">{$t('nav.paper')}</a></li>
				</ul>
			</div>
		{/if}
	</div>
</nav>
