# Korpus Kebutuhan (Requirements Corpus)

Direktori ini berisi korpus kebutuhan (*requirements corpus*) yang digunakan sebagai sumber bukti dalam penelitian tesis. Korpus ini secara sengaja dipisahkan menjadi material sumber dan hasil analisis turunan agar setiap hasil analisis dapat ditelusuri kembali ke dokumen *Business Requirements Document* (BRD) yang menjadi sumbernya.

## Peran Direktori

| Path | Peran | Aturan Pengeditan |
| --- | --- | --- |
| `raw/` | Berisi salinan BRD yang telah dianonimkan ke format Markdown; aset visual sumber tidak disertakan dalam versi publik. | Pertahankan fungsi bisnis dan ketertelusuran, tetapi jangan mempublikasikan nama asli, informasi pribadi, aset identitas, atau dokumen mentah. |
| `requirements text/` | Berisi sepuluh dokumen hasil penjabaran kebutuhan per modul yang telah dinormalisasi, serta satu dokumen audit cakupan korpus yang digunakan untuk analisis. | Catat hasil interpretasi, aturan bisnis yang dinyatakan secara eksplisit, skenario penerimaan (*acceptance scenarios*), dan konflik antarsumber yang belum terselesaikan. |
| `architecture/` | Rancangan arsitektur sistem pemeriksaan konsistensi berdasarkan draf tesis dan diagram paper rujukan. | Pertahankan keterkaitan dengan sumber dan bedakan metode usulan dari hasil eksperimen. |

## Arsitektur sistem penelitian

[Arsitektur Structure-Aware Hybrid Consistency Checking](architecture/README.md) memuat diagram Mermaid utama, rincian validasi dua arah, alur evaluasi, dan pemetaan komponen ke draf tesis serta paper rujukan. Diagram sumber tersedia sebagai berkas `.mmd` dan ditampilkan pada README agar dapat dibaca langsung di GitHub.

## Manifest Ketertelusuran (Traceability Manifest)

| ID | File Kebutuhan Turunan | BRD Sumber | Status Aset Visual |
| --- | --- | --- | --- |
| 01 | `requirements text/01-ec-benefit-reimbursement.md` | `raw/BRD - EC Benefit Reimbursement.md` | Dihapus |
| 02 | `requirements text/02-ec-employee-status-change.md` | `raw/BRD - EC Employee Status Change.md` | Dihapus |
| 03 | `requirements text/03-ec-foundation.md` | `raw/BRD - EC Foundation.md` | Dihapus |
| 04 | `requirements text/04-ec-manage-hiring.md` | `raw/BRD - EC Manage Hiring.md` | Dihapus |
| 05 | `requirements text/05-ec-organization-structure.md` | `raw/BRD - EC Organization Structure.md` | Dihapus |
| 06 | `requirements text/06-ec-position-management.md` | `raw/BRD - EC Position Management.md` | Dihapus |
| 07 | `requirements text/07-pmgm-performance-assessment.md` | `raw/BRD PMGM - Performance Assessment.md` | Dihapus |
| 08 | `requirements text/08-pmgm-goal-management.md` | `raw/BRD_PMGM_Goal_Management.md` | Dihapus |
| 09 | `requirements text/09-pmgm-goal-management-addendum.md` | `raw/BRD20Goal20-%20Adendum.md` | Dihapus |
| 10 | `requirements text/10-ec-personal-data.md` | `raw/BRD - EC Personal Data.md` | Dihapus |

Jumlah referensi aset visual menunjukkan banyaknya kemunculan gambar dalam Markdown, bukan selalu jumlah file gambar yang berbeda. Sebuah gambar sumber dapat secara sengaja ditampilkan lebih dari satu kali dalam dokumen BRD.

Saat ini, korpus terdiri atas:

- **10 dokumen BRD sumber**.
- **10 dokumen penjabaran kebutuhan turunan** berdasarkan modul.
- **1 dokumen audit cakupan korpus**.
- **0 aset gambar sumber dalam versi publik** (63 aset dikeluarkan sebagai pencegahan paparan identitas).

Rujukan gambar sumber diganti dengan penanda bahwa ilustrasi dikeluarkan dari korpus publik.

## Batasan Interpretasi (Interpretation Boundary)

File dalam direktori `requirements text/` bukan merupakan pengganti dokumen BRD asli.

File-file tersebut merupakan artefak analisis yang berisi hasil interpretasi kebutuhan, termasuk implikasi terhadap implementasi sistem dan ambiguitas yang ditemukan. Setiap interpretasi dan ambiguitas tetap diberi penanda secara jelas agar dapat dibedakan dari pernyataan yang secara eksplisit tercantum dalam dokumen sumber.

Dalam pelaksanaan eksperimen:

- Apabila eksperimen membutuhkan kebutuhan yang dijadikan sebagai **acuan kebenaran (*ground truth*)**, gunakan salinan BRD anonim yang terdapat pada direktori `raw/` sebagai referensi.
- Apabila eksperimen membutuhkan masukan analisis yang lebih ringkas dan terstruktur, gunakan dokumen penjabaran kebutuhan beserta dokumen BRD sumber yang bersesuaian berdasarkan tabel ketertelusuran di atas.

## Pemeriksaan Reprodusibilitas (Reproducibility Checks)

Sebelum menggunakan korpus dalam eksperimen atau melakukan *commit* terhadap material sumber baru, lakukan pemeriksaan berikut:

1. **Validasi referensi sumber.** Pastikan setiap file dalam direktori `requirements text/` memiliki satu entri `Source:` yang mengarah ke file yang benar-benar tersedia dalam direktori `raw/`.

2. **Validasi privasi visual.** Pastikan tidak ada aset logo, tanda tangan, tangkapan layar, atau diagram sumber nonanonim yang terbawa dalam publikasi.

3. **Pertahankan konflik kebutuhan yang belum terselesaikan.** Konflik aturan bisnis yang masih ditemukan pada dokumen sumber harus tetap dicatat dalam dokumen penjabaran kebutuhan, bukan diselesaikan secara sepihak dengan memilih suatu nilai tanpa dasar yang jelas. Contoh konflik yang saat ini ditemukan meliputi:
   - Nilai ambang batas (*threshold*) pada mekanisme *cascade* dalam modul Goal Management.
   - Beberapa aturan spesifik modul yang ditandai sebagai kesenjangan informasi pada dokumen sumber (*source gaps*).

4. **Batasi penggunaan aset visual sebagai ground truth.** Jangan menggunakan tanda tangan, logo, atau diagram sebagai data acuan berlabel (*labelled ground truth*), kecuali apabila eksperimen yang dilakukan secara eksplisit bertujuan mengevaluasi konten visual.
## Ketentuan anonimisasi

Salinan publik mengubah identitas organisasi, nama proyek, merek sistem yang dapat mengungkap sumber, dan nama orang menjadi label netral. Label pengganti tidak membuktikan bahwa materi bebas dari informasi sensitif secara kontekstual. Aset visual asli dikeluarkan dari pohon berkas terbaru; rujukan gambar diberi penanda. Untuk eksperimen berbasis diagram, buat ilustrasi sintetis atau diagram yang telah ditinjau anonimisasi secara terpisah. Riwayat Git sebelumnya masih dapat memuat identitas dan aset asli; mengubah berkas pada `main` tidak menghapus riwayat tersebut. Periksa juga hak penggunaan BRD dan catatan persetujuan pemilik data.

