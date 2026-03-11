<script>
  import { t } from '$lib/i18n.js';
</script>

<footer class="bg-yellow-100 border-t border-yellow-200">
  <div class="mx-auto max-w-7xl px-6 py-12">

    <!-- TOP -->
    <div class="grid gap-10 md:grid-cols-3 items-start">

      <!-- BRAND -->
      <div class="space-y-3">
        <h2 class="text-xl font-extrabold text-green-900">
          Pisang Cavendish
        </h2>
        <p class="text-sm text-gray-600 leading-relaxed">
          {$t('footer.brand_desc')}
        </p>
      </div>

      <!-- NAVIGATION -->
      <div>
        <h3 class="mb-4 text-sm font-semibold uppercase tracking-wide text-green-800">
          {$t('footer.navigation')}
        </h3>
        <ul class="space-y-2 text-sm text-gray-700">
          <li>
            <a href="/" class="hover:text-green-700 transition">
              {$t('footer.home')}
            </a>
          </li>
          <li>
            <a href="/about" class="hover:text-green-700 transition">
              {$t('footer.about')}
            </a>
          </li>
          <li>
            <a href="/classification" class="hover:text-green-700 transition">
              {$t('footer.classification')}
            </a>
          </li>
          <li>
            <a href="/history" class="hover:text-green-700 transition">
              {$t('footer.history')}
            </a>
          </li>
        </ul>
      </div>

      <!-- INFO -->
      <div>
        <h3 class="mb-4 text-sm font-semibold uppercase tracking-wide text-green-800">
          {$t('footer.information')}
        </h3>
        <ul class="space-y-2 text-sm text-gray-700">
          <li>Universitas Nusa Putra</li>
          <li>Teknik Informatika</li>
          <!-- <li>Tugas Metodologi Penelitian</li> -->
        </ul>
      </div>
    </div>

    <!-- DIVIDER -->
    <div class="my-8 h-px bg-yellow-200"></div>

    <!-- BOTTOM -->
    <div class="flex flex-col items-center justify-between gap-4 text-sm text-gray-600 md:flex-row">
      <p>
        &copy; {new Date().getFullYear()} {$t('footer.copyright')}
      </p>
      <p class="text-gray-500">
        {$t('footer.made_by')} <span class="font-medium text-gray-700">{$t('footer.group')}</span>
      </p>
    </div>
  </div>
</footer>
