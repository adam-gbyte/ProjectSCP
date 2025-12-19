<script>
  import { onMount, onDestroy } from 'svelte';
  import { browser } from '$app/environment';

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
      <h1 class="text-xl font-bold">Pisang Cavendish</h1>

      <!-- DESKTOP MENU -->
      <ul class="hidden md:flex items-center gap-6 font-medium">
        <li><a href="/" class="nav-link">Home</a></li>
        <li><a href="/about" class="nav-link">About</a></li>
        <li><a href="/classification" class="nav-link">Klasifikasi</a></li>
        <li><a href="/history" class="nav-link">Riwayat</a></li>
        <li><a href="/paper" class="nav-link">Paper</a></li>
      </ul>

      <!-- MOBILE BUTTON -->
      <button
        class="md:hidden flex items-center justify-center rounded-lg p-2 hover:bg-black/5"
        on:click={toggleMenu}
        aria-label="Toggle menu"
      >
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none"
          viewBox="0 0 24 24" stroke="currentColor">
          {#if menuOpen}
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M6 18L18 6M6 6l12 12" />
          {:else}
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M4 6h16M4 12h16M4 18h16" />
          {/if}
        </svg>
      </button>
    </div>

    <!-- MOBILE MENU -->
    {#if menuOpen}
      <div
        class="md:hidden mt-2 rounded-2xl bg-white/90 backdrop-blur-xl shadow-lg overflow-hidden"
      >
        <ul class="flex flex-col">
          <li><a href="/" class="mobile-link">Home</a></li>
          <li><a href="/about" class="mobile-link">About</a></li>
          <li><a href="/classification" class="mobile-link">Klasifikasi</a></li>
          <li><a href="/history" class="mobile-link">Riwayat</a></li>
          <li><a href="/paper" class="mobile-link">Paper</a></li>
        </ul>
      </div>
    {/if}
  </div>
</nav>
