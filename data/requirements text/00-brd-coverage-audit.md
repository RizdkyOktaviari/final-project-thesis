# Panduan Korpus dan Audit Cakupan Kebutuhan Riset

## Tujuan dan dasar penyusunan

Folder ini memuat sepuluh dokumen kebutuhan turunan dari BRD Employee Central dan PMGM. Dokumen disusun ulang dalam bahasa Indonesia untuk membantu penyiapan masukan penelitian pemeriksaan konsistensi antara spesifikasi kebutuhan dan sequence diagram.

Bentuk narasi mengikuti bagian Requirements pada gambar acuan: aktor disebutkan secara eksplisit, tindakan dan respons sistem dinyatakan dalam kalimat, serta urutan, kondisi, dan hasil dituliskan apabila didukung sumber. Narasi menggunakan kata **harus** untuk kewajiban sistem dan **dapat** untuk kemampuan atau pilihan yang diizinkan. Nama peran, kolom, fitur, format berkas, status, serta judul bagian sumber dipertahankan apabila diperlukan untuk ketertelusuran.

Penyusunan menggunakan penjabaran kebutuhan pada [snapshot 0f0cd909](https://github.com/RizdkyOktaviari/final-project-thesis/commit/0f0cd9099d1d2f2486605ac04e2f52de2af4c559) dan pemeriksaan bagian BRD terkait dalam `data/raw/`. Pembaruan terjemahan pada [snapshot 94bf431e](https://github.com/RizdkyOktaviari/final-project-thesis/commit/94bf431ed3a0438bf26631192ac0e65d3632a6c8) juga diperiksa sebelum format riset diterapkan di atasnya; tidak ditemukan penambahan aturan bisnis pada pembaruan terjemahan tersebut. Tanggal pembaruan format adalah 27 Oktober 2026. Dokumen sumber tetap menjadi rujukan untuk menilai kesetiaan narasi; perubahan bahasa dan struktur tidak dengan sendirinya menjadi validasi oleh pemilik proses bisnis.

## Struktur setiap dokumen

| Bagian | Isi dan peran dalam riset |
| --- | --- |
| Sumber dan ruang lingkup | Path BRD, aktor, tujuan, dan batas konteks. Kunci teknis `Source:` dipertahankan agar sesuai pemeriksaan ketertelusuran pada `data/README.md`. |
| Skenario kebutuhan | ID `REQ-<modul>-<nomor>`, judul, rujukan bagian BRD, dan paragraf `Kebutuhan` yang menjelaskan interaksi atau perilaku. |
| Ketentuan pendukung | ID `KON-<modul>-<nomor>`, rujukan, dan paragraf `Ketentuan` untuk rincian data, aturan lintas skenario, keamanan, audit, atau migrasi. |
| Batas cakupan | Fungsi yang dikecualikan dan batas antara proses aplikasi, proses manual, serta modul lain. |
| Ambiguitas dan batas interpretasi | Pernyataan sumber yang bertentangan, parameter yang belum ditentukan, dan interpretasi turunan yang memerlukan konfirmasi. |

Satu ID `REQ` adalah unit skenario, bukan jaminan bahwa paragraf tersebut hanya mengandung satu kebutuhan atomik. Sebuah paragraf dapat mengandung beberapa tindakan, kondisi, dan respons yang selanjutnya diuraikan dalam tahap analisis penelitian. `KON` juga tidak otomatis berarti kebutuhan nonfungsional: beberapa entri memuat aturan data atau bisnis yang membatasi perilaku fungsional. Klasifikasi akhir mengikuti definisi operasional penelitian.

Judul dan metadata merupakan penanda dokumen. Jika eksperimen memakai teks kebutuhan saja, ambil paragraf setelah label `Kebutuhan` beserta ketentuan yang relevan, kemudian simpan ID dan rujukannya sebagai metadata. Jangan memasukkan catatan konflik sebagai perilaku final tanpa penandaan yang sesuai.

## Pemetaan cakupan

| ID | Modul dan dokumen | Skenario | Ketentuan | Area sumber yang dipetakan |
| --- | --- | ---: | ---: | --- |
| 01 | [EC Benefit Reimbursement](01-ec-benefit-reimbursement.md) | 12 | 5 | Formulir, tanggungan, kelayakan dan perhitungan, frekuensi, periode, persetujuan, tanggal mundur, penarikan, pembatalan, notifikasi, ekspor, akses, audit, migrasi, dan integrasi. |
| 02 | [EC Employee Status Change](02-ec-employee-status-change.md) | 13 | 7 | Jenis perubahan, formulir berbasis peran, pemeriksaan OD, alur persetujuan, delegasi, penggantian pemberi persetujuan, lampiran, laporan, pemantauan, validasi, keamanan, tanggal efektif, migrasi, dan integrasi. |
| 03 | [EC Foundation](03-ec-foundation.md) | 13 | 5 | Banyak perusahaan, siklus proxy dan notifikasinya, konfigurasi alur persetujuan, delegasi, autentikasi dan RBAC, enkripsi, audit, integrasi, migrasi, serta tanggung jawab antarmodul. |
| 04 | [EC Manage Hiring](04-ec-manage-hiring.md) | 12 | 6 | RTE, SBU, posisi dan pegawai baru, evaluasi masa percobaan, urutan persetujuan, notifikasi, validasi, dokumen, keamanan, audit, migrasi, dan ketergantungan data. |
| 05 | [EC Organization Structure](05-ec-organization-structure.md) | 5 | 3 | Batas persetujuan manual, pembaruan dan impor internal, hierarki, kebijakan kode, pencarian, visualisasi, ekspor, kewenangan, tanggal berlaku, riwayat, dan hasil ESC. |
| 06 | [EC Position Management](06-ec-position-management.md) | 7 | 3 | Pembuatan umum dan posisi bawahan, perubahan posisi, aktivasi dan penonaktifan, hierarki, tanggal berlaku, akses, data biaya, impor, ekspor, migrasi, audit, dan referensi antarmodul. |
| 07 | [PMGM Performance Assessment](07-pmgm-performance-assessment.md) | 13 | 4 | Templat dan peluncuran, penilaian diri dan atasan, alur peninjauan, normalisasi, impor, finalisasi, laporan, perubahan peserta dan peninjau, perhitungan, akses, dan audit. |
| 08 | [PMGM Goal Management](08-pmgm-goal-management.md) | 12 | 3 | Periode, peserta, formulir, validasi KPI, cascade, persetujuan, revisi, aktivitas, notifikasi, pengingat, visibilitas, ekspor, revisi tengah tahun, perubahan jabatan, dan audit. |
| 09 | [Adendum PMGM Goal Management](09-pmgm-goal-management-addendum.md) | 3 | 1 | Tiga aturan adendum: pengajuan KPI atasan sebelum cascade, kewenangan Supervisor untuk Non-Staff, dan draf tanpa cascade; hubungan dengan validasi BRD utama. |
| 10 | [EC Personal Data](10-ec-personal-data.md) | 12 | 11 | Pengajuan dan pemeriksaan, persetujuan serta tanggal efektif, pengembalian, penarikan, batas data, kelayakan tanggungan, rekening, dokumen, status, riwayat, akses, audit, migrasi, dan integrasi. |
| | Jumlah | 102 | 48 | Sepuluh dokumen kebutuhan dan satu dokumen panduan serta audit ini. |

Jumlah tersebut menunjukkan unit penulisan dalam versi ini. Jumlah itu bukan jumlah pasangan kebutuhan dan diagram, kebutuhan atomik, kasus uji independen, atau label benar/salah yang telah divalidasi. Skenario pada adendum dapat menegaskan skenario dalam BRD utama; hubungan sumbernya harus dipertahankan saat membagi atau menghitung sampel riset.

## Penggunaan untuk pemeriksaan konsistensi

1. Pilih ID skenario dan ketentuan pendukung yang relevan. Pastikan aktor, objek data, kondisi, batas peran, serta hasil yang digunakan memang tercantum pada rujukan sumber.
2. Tentukan cakupan diagram yang dipasangkan dengan skenario. Beberapa ID dapat dipakai bersama jika diagram mencakup proses yang lebih luas; simpan pemetaannya agar penilai mengetahui konteks yang sama.
3. Gunakan urutan proses yang dinyatakan sumber. Jika sumber hanya menyatakan kemampuan atau aturan data, jangan menganggap urutan panggilan antarkomponen, layanan, atau basis data sebagai fakta yang sudah ditetapkan.
4. Periksa bagian ambiguitas. Kasus yang hasil penilaiannya bergantung pada aturan bertentangan perlu ditunda, ditandai belum terkonfirmasi, atau diselesaikan melalui keputusan penelaah yang terdokumentasi. Konflik internal BRD harus dibedakan dari ketidaksesuaian antara BRD dan diagram.
5. Tetapkan acuan penilaian bersama penelaah yang memahami domain sebelum menghitung akurasi atau kesalahan metode. Simpan keputusan, versi sumber, ID skenario, diagram, dan alasan label agar hasil dapat ditelusuri.

Korpus ini menyediakan teks kebutuhan terstruktur. Pasangan sequence diagram, hasil pemeriksaan otomatis, dan label acuan kebenaran tidak dibentuk hanya melalui penerjemahan ini. Gambar pada BRD, termasuk diagram proses, logo, dan tanda tangan, tetap merupakan bukti sumber sesuai konteksnya, bukan otomatis data berlabel untuk evaluasi.

## Konflik dan kesenjangan sumber yang dipertahankan

| Modul | Persoalan yang perlu diputuskan atau diperjelas |
| --- | --- |
| Benefit Reimbursement | PDF atau JPG dibanding PDF khusus formulir pendidikan; status yang mengizinkan penarikan; pengajuan aktif dan pengecualian kontrak; asal pengisian nama sekolah; rincian plafon, prorata, dan peringatan batas akhir. |
| Employee Status Change | Status penarikan; konfigurasi alur; hak laporan dan notifikasi pegawai; daftar penerima notifikasi selesai; kolom wajib dan hak edit; persentase kenaikan; tanggal mundur yang sekaligus diizinkan dan dikecualikan; DOC atau DOCX. |
| Foundation | Penerima notifikasi aktivasi proxy; interpretasi batas izin proxy; akibat perusahaan dinonaktifkan; konfigurasi delegasi, izin, integrasi, dan migrasi per modul. |
| Manage Hiring | Katalog dan konfigurasi rinci; kelengkapan notifikasi; distribusi surat masa percobaan; dukungan aplikasi terhadap pemeriksaan posisi manual; bagian formulir bantuan pendidikan yang tidak sesuai lingkup. |
| Organization Structure | Katalog data dan validasi rinci; hubungan tingkat persetujuan manual; batas penyesuaian jalur pelaporan; pemetaan dan waktu pembaruan dari ESC. |
| Position Management | Katalog posisi, format dan penanganan impor, rincian aktivasi, serta batas pengelolaan master kode biaya dan pemilihannya pada posisi. |
| Performance Assessment | Nilai keseluruhan manual atau otomatis; hak melihat riwayat nilai; istilah Approve atau Submit pada tahap terakhir; kriteria melewati peninjau atau menunjuk pengganti. |
| Goal Management dan adendum | Ambang cascade 40% atau 50% dan cakupan konfigurasi; makna arah penilaian; kewenangan penanda Mandatory; adendum tidak menyelesaikan konflik ambang. |
| Personal Data | Daftar bagian yang dapat diubah dibanding kolom hanya baca; format dan ukuran lampiran; cakupan batas perubahan rekening per tahun; identitas ekspatriat; tanggal efektif dan notifikasi; penamaan status penarikan; jadwal integrasi. |

Daftar rinci, bukti yang berlawanan, dan unit terdampak berada pada masing-masing dokumen. Penulisan ulang juga menandai interpretasi penjabaran terdahulu yang tidak didukung secara tegas oleh BRD, sehingga interpretasi tersebut tidak berubah menjadi fakta sumber secara diam-diam.

## Batas audit dan pemeriksaan struktur

Audit mencakup pemetaan ruang lingkup, aktor dan hak akses, aturan bisnis, kebutuhan fungsional, validasi, keamanan, audit, integrasi, migrasi, pelaporan, serta pemicu notifikasi. Metadata administrasi dokumen, piksel gambar, tanda tangan, redaksi lengkap surel, dan contoh pesan kesalahan tidak disalin kata demi kata; seluruhnya tetap dirujuk melalui `data/raw/`. Uraian As-Is dipertahankan sebagai konteks apabila diperlukan, dengan penanda agar tidak otomatis menjadi kewajiban To-Be.

Pemeriksaan struktur memverifikasi bahwa setiap dokumen modul memiliki satu `Source:` yang merujuk BRD yang tersedia, ID `REQ` dan `KON` unik serta berurutan dalam modulnya, setiap unit memiliki rujukan dan paragraf yang sesuai, dan referensi ID antarskenario dapat ditemukan. Pemetaan jumlah unit diperiksa terhadap isi berkas. Dokumen sumber dan berkas di luar folder sasaran tidak diubah oleh pembaruan ini. Pemeriksaan tersebut menguji struktur dan ketertelusuran dokumen; konfirmasi semantik serta label eksperimen tetap memerlukan penelaahan domain.

