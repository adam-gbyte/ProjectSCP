<script>
  import { predictImage } from "$lib/api";

  let file;
  let previewUrl = null;
  let loading = false;
  let data = null;
  let error = null;

  function handleFile(e) {
    file = e.target.files[0];
    if (file) {
      previewUrl = URL.createObjectURL(file);
      data = null;
      error = null;
    }
  }

  async function submit() {
    if (!file) return;

    loading = true;
    error = null;

    try {
      data = await predictImage(file);
    } catch (e) {
      error = e.message ?? "Terjadi kesalahan";
    } finally {
      loading = false;
    }
  }

  function reset() {
    file = null;
    previewUrl = null;
    data = null;
    error = null;
  }

  function imageUrl(path) {
    return `http://localhost:8000/${path.replaceAll("\\", "/")}`;
  }
</script>

<div class="pt-6 min-h-screen bg-linear-to-br from-green-50 via-white to-yellow-50 p-6">
  <div class="mx-auto max-w-6xl">
    <!-- TITLE -->
    <h1 class="mb-8 text-center text-3xl font-extrabold text-green-800">
      Prediksi Kematangan Buah Pisang Cavendish
    </h1>

    <!-- GRID -->
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">

<!-- ================= LEFT : INPUT ================= -->
<section class="space-y-6">

  <!-- INPUT CARD -->
  <div class="rounded-3xl bg-white p-6 shadow-xl space-y-4">

    <!-- TITLE -->
    <div>
      <h3 class="text-lg font-bold text-gray-800">
        Input Gambar
      </h3>
      <p class="text-sm text-gray-500">
        Upload gambar buah pisang cavendish untuk diprediksi tingkat kematangannya
      </p>
    </div>

    <!-- DROPZONE / PREVIEW -->
    <div class="relative overflow-hidden rounded-2xl border border-dashed border-yellow-400 bg-yellow-50">

      {#if previewUrl}
        <!-- PREVIEW -->
        <img
          src={data ? imageUrl(data.image_path) : previewUrl}
          alt="Preview"
          class="h-72 w-full object-cover transition"
          class:blur-sm={loading}
        />

        <!-- CHANGE IMAGE -->
        <label
          class="absolute top-3 right-3 cursor-pointer rounded-full bg-white/90 px-4 py-1.5 text-xs font-semibold text-gray-700 shadow hover:bg-white"
        >
          Ganti
          <input
            type="file"
            accept="image/*"
            on:change={handleFile}
            class="hidden"
          />
        </label>
      {:else}
        <!-- EMPTY STATE -->
        <label
          class="flex h-72 cursor-pointer flex-col items-center justify-center gap-3 text-center transition hover:bg-yellow-100"
        >
          <input
            type="file"
            accept="image/*"
            on:change={handleFile}
            class="hidden"
          />

          <!-- ICON -->
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-12 w-12 text-yellow-500"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M3 16l4-4a3 3 0 014 0l1 1m4-5a3 3 0 013 3v7M7 16h10" />
          </svg>

          <span class="text-lg font-semibold text-yellow-700">
            Klik untuk upload gambar
          </span>
          <span class="text-sm text-gray-500">
            PNG, JPG, JPEG
          </span>
        </label>
      {/if}

      <!-- LOADING OVERLAY -->
      {#if loading}
        <div class="absolute inset-0 flex items-center justify-center bg-white/70 backdrop-blur-sm">
          <div class="h-10 w-10 animate-spin rounded-full border-4 border-green-600 border-t-transparent"></div>
        </div>
      {/if}
    </div>
  </div>

  <!-- ACTION BUTTONS -->
  <div class="flex flex-col sm:flex-row gap-3">
    <button
      on:click={submit}
      disabled={!file || loading}
      class="flex-1 rounded-xl bg-green-600 px-6 py-3 font-semibold text-white shadow-lg transition hover:bg-green-700 disabled:opacity-50"
    >
      {loading ? "Memproses..." : "Prediksi"}
    </button>

    <button
      on:click={reset}
      class="flex-1 rounded-xl border border-gray-300 px-6 py-3 font-semibold text-gray-600 transition hover:bg-gray-100"
    >
      Reset
    </button>
  </div>

  {#if error}
    <div class="rounded-lg bg-red-100 p-3 text-red-700">
      {error}
    </div>
  {/if}

</section>

      <!-- ================= RIGHT : RESULT ================= -->
      <section>
        {#if data}
          <div class="h-full rounded-2xl bg-white p-6 shadow-xl">
            <h2 class="mb-6 text-center text-xl font-bold text-gray-800">
              Hasil Prediksi
            </h2>

            <div class="space-y-5">
              <div class="flex items-center justify-between">
                <span class="text-sm text-gray-500">Status</span>
                <span class="rounded-full bg-green-100 px-3 py-1 text-sm font-semibold text-green-700">
                  {data.status}
                </span>
              </div>

              <div class="flex items-center justify-between">
                <span class="text-sm text-gray-500">Prediksi</span>
                <span class="text-lg font-bold capitalize text-gray-800">
                  {data.prediction.replace("_", " ")}
                </span>
              </div>

              <div>
                <div class="mb-1 flex items-center justify-between text-sm">
                  <span class="text-gray-500">Confidence</span>
                  <span class="font-semibold text-gray-700">
                    {(data.confidence * 100).toFixed(2)}%
                  </span>
                </div>

                <div class="h-2 w-full rounded-full bg-gray-200">
                  <div
                    class="h-2 rounded-full bg-green-600 transition-all"
                    style={`width: ${(data.confidence * 100).toFixed(2)}%`}
                  ></div>
                </div>
              </div>

              <div class="pt-4 text-center text-xs text-gray-400">
                ID Prediksi: {data.id}
              </div>
            </div>
          </div>
        {:else}
          <div class="flex h-full items-center justify-center rounded-2xl border-2 border-dashed border-gray-300 text-gray-400">
            Hasil prediksi akan muncul di sini
          </div>
        {/if}
      </section>

    </div>
  </div>
</div>
