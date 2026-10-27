# Audit Cakupan BRD terhadap Kebutuhan Fungsional dan Perilaku

## Tujuan dan metode

Audit ini memeriksa apakah setiap BRD yang diberikan memiliki penjabaran
kebutuhan fungsional dan perilaku yang sesuai dan memadai. Audit ini
memperlakukan hal-hal berikut sebagai **bukti kebutuhan**: cakupan, peran/akses,
aturan bisnis, kebutuhan fungsional, validasi, keamanan, audit, integrasi,
migrasi, pelaporan, dan pemicu notifikasi.
Audit ini tidak menyalin metadata pengendalian dokumen, piksel gambar sumber,
tanda tangan, redaksi email, contoh redaksi pesan kesalahan, atau narasi kondisi
saat ini secara kata demi kata; semuanya tetap tersimpan dan dapat dirujuk di `data/raw/`.

## Hasil

| ID | BRD | Penjabaran kebutuhan | Cakupan setelah audit ini | Bagian substantif sumber yang tercakup |
| --- | --- | --- | --- | --- |
| 01 | EC Benefit Reimbursement | `01-ec-benefit-reimbursement.md` | Lengkap | Cakupan/pengecualian, formulir, kelayakan/perhitungan, persetujuan, periode/batas waktu, notifikasi, riwayat/ekspor, akses, audit, migrasi, integrasi |
| 02 | EC Employee Status Change | `02-ec-employee-status-change.md` | Lengkap, dengan konflik pada sumber tetap dicatat | Cakupan/pengecualian, formulir berdasarkan peran, alur kerja/delegasi, lampiran, laporan, pemantauan, validasi, keamanan, migrasi, integrasi |
| 03 | EC Foundation | `03-ec-foundation.md` | Lengkap | Dukungan untuk beberapa perusahaan, siklus hidup/notifikasi akses perwakilan, alur kerja, RBAC, enkripsi, audit, integrasi, migrasi, dependensi |
| 04 | EC Manage Hiring | `04-ec-manage-hiring.md` | Lengkap | RTE, SBU, karyawan baru, masa percobaan, alur kerja, pemicu notifikasi, validasi, keamanan, audit, migrasi, dependensi |
| 05 | EC Organization Structure | `05-ec-organization-structure.md` | Lengkap | Cakupan/pengecualian, batas proses persetujuan manual, pembaruan/impor internal, kebijakan, akses berdasarkan peran, tanggal berlaku, dependensi ESC |
| 06 | EC Position Management | `06-ec-position-management.md` | Lengkap | Cakupan/pengecualian, alur pembuatan/penambahan posisi di bawah/pengubahan, hierarki/tanggal berlaku, akses berdasarkan peran, impor/ekspor, audit, kebijakan |
| 07 | PMGM Performance Assessment | `07-pmgm-performance-assessment.md` | Lengkap | Templat/peluncuran, alur kerja penilaian, normalisasi, finalisasi/pelaporan, penugasan ulang, perhitungan, visibilitas, audit |
| 08 | PMGM Goal Management | `08-pmgm-goal-management.md` | Lengkap, dengan konflik pada sumber tetap dicatat | Periode/templat, validasi KPI, penurunan KPI secara berjenjang, alur kerja, notifikasi, visibilitas, ekspor, revisi tengah tahun, audit, pengecualian |
| 09 | PMGM Goal Management Addendum | `09-pmgm-goal-management-addendum.md` | Lengkap | Tiga aturan bisnis dalam adendum dan hubungannya dengan BRD utama Goal Management |
| 10 | EC Personal Data | `10-ec-personal-data.md` | Lengkap, dengan konflik pada sumber tetap dicatat | Siklus permohonan/peninjauan, batasan bagian dan kolom, bukti pendukung, riwayat, keamanan, audit, migrasi, integrasi, pengecualian |

## Konflik dan kekosongan informasi pada sumber yang tetap dicatat secara eksplisit

- Benefit Reimbursement: format lampiran, status penarikan kembali permohonan, serta interpretasi atas permohonan aktif yang duplikat dan karyawan kontrak.
- Employee Status Change: ketentuan penarikan kembali permohonan tidak konsisten antara bagian fungsional dan bagian validasi; konfigurasi alur kerja yang tepat tidak dijelaskan.
- Goal Management: nilai bawaan bobot penurunan KPI secara berjenjang adalah 40% pada diagram dan 50% pada teks.
- Personal Data: daftar bagian yang dapat diajukan perubahannya bertentangan dengan entri hanya baca dalam katalog kolom terperinci; format/ukuran lampiran yang diizinkan dan subjenis perubahan pembayaran belum dijelaskan.

Hal-hal tersebut dicatat sebagai kekosongan informasi pada sumber dalam masing-masing penjabaran kebutuhan, dan tidak diselesaikan melalui audit ini.
