export async function predictImage(file) {
  const formData = new FormData();
  formData.append("file", file);

  const res = await fetch("https://api.adam-gbyte.my.id/predict", {
    method: "POST",
    body: formData
  });

  if (!res.ok) {
    throw new Error("Gagal melakukan prediksi");
  }

  return await res.json();
}

export async function fetchPredictions() {
  const res = await fetch("https://api.adam-gbyte.my.id/predictions");

  if (!res.ok) {
    throw new Error("Gagal mengambil data riwayat");
  }

  return await res.json();
}
