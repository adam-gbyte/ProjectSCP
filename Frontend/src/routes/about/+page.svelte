<div class="min-h-screen pt-6 bg-linear-to-br from-yellow-50 via-white to-green-50">

  <!-- HERO SECTION -->
  <section class="mx-auto max-w-7xl px-6 pt-8 pb-28">
    <div class="grid gap-16 md:grid-cols-2 items-center">

      <!-- TEXT -->
      <div class="space-y-10">
        <span class="inline-block rounded-full bg-yellow-100 px-5 py-2 text-sm font-semibold text-yellow-700">
          Tentang Sistem
        </span>

        <h1 class="text-4xl md:text-5xl font-extrabold leading-tight text-green-900">
          Klasifikasi <br />
          <span class="text-yellow-600">Kematangan Pisang Cavendish</span>
        </h1>

        <div class="space-y-6 text-lg text-gray-700 leading-relaxed">
          <p>
            Sistem ini dirancang untuk membantu petani dan pelaku agribisnis dalam
            menentukan tingkat kematangan buah pisang Cavendish secara cepat dan akurat
            menggunakan pendekatan <span class="font-semibold">Computer Vision</span>.
          </p>

          <p>
            Model <span class="font-semibold">MobileNetV2</span> digunakan untuk mengekstraksi
            fitur citra buah, kemudian diklasifikasikan menggunakan algoritma
            <span class="font-semibold">Support Vector Machine (SVM)</span> ke dalam
            lima kelas kematangan:
            <strong> mentah</strong>,
            <strong> setengah matang</strong>,
            <strong> hampir matang</strong>,
            <strong> matang</strong>, dan
            <strong> sangat matang</strong>.
          </p>
        </div>
      </div>

      <!-- IMAGE -->
    <div class="flex justify-center md:justify-end">
      <img
        src="/logo.jpg"
        alt="Pisang Cavendish"
        class="w-full max-w-md rounded-2xl shadow-xl transition hover:scale-105"
      />
    </div>
    </div>
  </section>

  <!-- TECHNOLOGY STACK -->
  <section class="mx-auto pt-8 max-w-7xl px-6 pb-32">
    <div class="mb-16 text-center">
      <h2 class="text-3xl font-bold text-green-900">
        Teknologi yang Digunakan
      </h2>
      <p class="mt-4 text-gray-600 text-lg">
        Arsitektur sistem dan teknologi pendukung
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
