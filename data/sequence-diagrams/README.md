# Dataset Sequence Diagram Mermaid untuk Consistency Checking

Sumber requirements: https://github.com/RizdkyOktaviari/final-project-thesis/tree/main/data/requirements%20text

Dataset terdiri dari **30 sequence diagram** dalam format Mermaid (.mmd), masing-masing dipetakan ke kebutuhan fungsional yang relevan di 10 modul. Sebanyak **26 diagram tanpa injeksi kesalahan disengaja** dan **4 diagram dengan injeksi inkonsistensi semantik terkontrol**.

## Struktur
- `diagrams/*.mmd`: satu sequence diagram per berkas.
- `manifest.json`: pemetaan diagram dan requirement terkait.
- `ground_truth.csv`: label dan penjelasan injeksi kesalahan.

## Catatan penggunaan penelitian
- Angka label 0 berarti tidak ada kesalahan *yang sengaja diinjeksi*, **bukan** jaminan diagram sempurna.
- Label 1 menunjukkan diagram dengan kesalahan terkontrol, seperti omission, addition, dan temporal violation.
- Pemisahan evaluasi: berikan model hanya requirements dan berkas diagram, **jangan** berikan manifest atau ground truth saat inferensi.
- Tetapkan terlebih dahulu unit penilaian (diagram atau pasangan requirement–diagram), kemudian lakukan review dan anotasi pakar untuk membangun gold standard.
- Untuk hasil yang reprodusibel, kunci revisi commit dan validasi sintaks Mermaid sebelum eksperimen.
- Beberapa sumber requirements memiliki ambiguitas yang harus diselesaikan sebelum pengujian konsistensi berbasis aturan spesifik.
