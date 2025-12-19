<script>
  import { onMount } from "svelte";
  import { fetchPredictions } from "$lib/api";

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
    return `http://localhost:8000/${path.replaceAll("\\", "/")}`;
  }

  function formatDate(date) {
    return new Date(date).toLocaleString("id-ID");
  }

  function badgeColor(label) {
    const map = {
      mentah: "bg-red-500",
      hampir_matang: "bg-yellow-500",
      setengah_matang: "bg-orange-500",
      matang_sempurna: "bg-green-500",
      sangat_matang: "bg-emerald-500"
    };
    return map[label] ?? "bg-gray-500";
  }
</script>

<div class="pt-6 min-h-screen bg-linear-to-br from-gray-50 via-white to-gray-100 p-6">
  <div class="max-w-7xl mx-auto space-y-8">

    <!-- Header -->
    <header class="text-center space-y-2">
      <h1 class="text-3xl font-extrabold text-gray-800">
        History Prediksi
      </h1>
      <p class="text-gray-500">
        Galeri hasil klasifikasi tingkat kematangan
      </p>
    </header>

    <!-- Loading -->
    {#if loading}
      <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-6">
        {#each Array(8) as _}
          <div class="aspect-square rounded-2xl bg-gray-200 animate-pulse"></div>
        {/each}
      </div>
    {/if}

    <!-- Error -->
    {#if error}
      <div class="max-w-xl mx-auto bg-red-100 text-red-700 p-4 rounded-xl text-center">
        {error}
      </div>
    {/if}

    <!-- Empty -->
    {#if !loading && items.length === 0}
      <div class="text-center text-gray-500 py-20">
        Belum ada data prediksi
      </div>
    {/if}

    <!-- Gallery -->
    {#if !loading && items.length > 0}
      <section class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-6">
        {#each items as item}
          <article
            class="group relative aspect-square rounded-2xl overflow-hidden shadow hover:shadow-xl transition"
          >
            <!-- Image -->
            <img
              src={imageUrl(item.file_path)}
              alt="Prediction"
              class="h-full w-full object-cover group-hover:scale-110 transition duration-700"
            />

            <!-- Gradient Overlay -->
            <div
              class="absolute inset-0 bg-linear-to-t from-black/80 via-black/30 to-transparent opacity-0 group-hover:opacity-100 transition"
            ></div>

            <!-- Badge -->
            <span
              class={`absolute top-3 left-3 px-3 py-1 text-xs font-semibold text-white rounded-full ${badgeColor(
                item.prediction
              )}`}
            >
              {item.prediction.replace("_", " ")}
            </span>

            <!-- Hover Content -->
            <div
              class="absolute inset-0 flex flex-col justify-end p-4 text-white opacity-0 group-hover:opacity-100 transition"
            >
              <div class="space-y-2">
                <p class="text-sm font-semibold">
                  Confidence {(item.confidence * 100).toFixed(1)}%
                </p>

                <!-- Confidence Bar -->
                <div class="h-2 bg-white/30 rounded-full overflow-hidden">
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
