<section
  id="home"
  class="pt-6 relative flex min-h-screen items-center bg-linear-to-br from-green-50 via-white to-yellow-50 px-6 py-16"
>
  <div
    class="mx-auto grid max-w-7xl grid-cols-1 items-center gap-10 md:grid-cols-2"
  >
    <!-- TEXT -->
    <div class="space-y-6">
      <h1
        class="text-4xl font-extrabold leading-tight text-green-800 md:text-5xl lg:text-6xl"
      >
        Klasifikasi Kematangan
        <span class="block text-yellow-600">
          Pisang Cavendish
        </span>
      </h1>

      <p class="max-w-xl text-base leading-relaxed text-gray-700 md:text-lg">
        Sistem cerdas berbasis <span class="font-semibold">Deep Learning</span>
        yang mampu mendeteksi tingkat kematangan buah pisang Cavendish secara
        otomatis menggunakan kombinasi
        <span class="font-semibold">MobileNetV2</span> dan
        <span class="font-semibold">Support Vector Machine (SVM)</span>.
      </p>

      <!-- CTA -->
      <div class="flex flex-col gap-4 sm:flex-row">
        <a
          href="/classification"
          class="inline-flex items-center justify-center rounded-xl bg-green-600 px-8 py-3 text-base font-semibold text-white shadow-lg transition hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-green-500"
        >
          Mulai Klasifikasi
        </a>

        <a
          href="/riwayat"
          class="inline-flex items-center justify-center rounded-xl border border-green-600 px-8 py-3 text-base font-semibold text-green-700 transition hover:bg-green-50"
        >
          History
        </a>

        <a
          href="/paper"
          class="inline-flex items-center justify-center rounded-xl border border-yellow-500 px-8 py-3 text-base font-semibold text-yellow-600 transition hover:bg-yellow-50"
        >
          Jurnal Penelitian
        </a>
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
