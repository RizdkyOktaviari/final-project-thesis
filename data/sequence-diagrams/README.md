# Dataset Sequence Diagram Mermaid untuk Consistency Checking

Sumber kebutuhan: https://github.com/RizdkyOktaviari/final-project-thesis/tree/main/data/requirements%20text

Dataset berisi 20 sequence diagram dalam format Mermaid untuk 10 modul. Sebanyak 17 diagram tidak memiliki kesalahan yang disengaja, sedangkan tiga diagram memiliki injeksi inkonsistensi semantik untuk keperluan eksperimen.

## Struktur
- diagrams/*.mmd: setiap diagram pada file terpisah.
- manifest.json: pemetaan diagram ke requirement.
- ground_truth.csv: label dan penjelasan kesalahan.

## Metodologi
- Label 0 bukan jaminan bebas dari semua kesalahan; hanya tidak ada kesalahan yang sengaja disisipkan.
- Label 1 adalah injeksi kesalahan terkontrol.
- Jangan gunakan manifest atau ground_truth sebagai input model ketika mengevaluasi deteksi inkonsistensi.
- Validasi sintaks dan penilaian pakar tetap diperlukan sebelum digunakan sebagai gold standard.
