# Penjabaran Kebutuhan: EC Pengelolaan Posisi (Position Management)

## Sumber dan cakupan

- Source: `data/raw/BRD - EC Position Management.md`
- Tujuan: mengelola siklus hidup posisi, hierarki posisi, atribut unit organisasi, riwayat, penyajian bagan, migrasi, impor/ekspor, dan data referensi bersama.
- Peran: OD Admin memiliki hak akses untuk mengelola siklus hidup posisi serta bagan/impor/ekspor; Comben mengelola kode biaya; karyawan melihat data bagan posisinya sendiri.

## Kebutuhan Fungsional

1. Membuat, membaca, memperbarui, mengaktifkan, dan menonaktifkan posisi, baik melalui pembuatan umum maupun `Add Position Below` dari simpul Bagan Posisi yang dipilih.
2. Mengelola Kode Posisi (Position Code), Nama Posisi (Position Title), keterkaitan dengan unit organisasi, Posisi Atasan (Higher-Level Position), dan hubungan dengan posisi bawahan.
3. Menampilkan Bagan Posisi serta mendukung pencarian berdasarkan Kode Posisi, Nama Posisi, nama karyawan pemangku posisi, dan ID karyawan.
4. Menerapkan tanggal berlaku pada perubahan serta mempertahankan tampilan riwayat organisasi/posisi untuk tanggal berlaku yang dipilih.
5. Mengelola data Perusahaan, Direktorat, Divisi, Departemen, Seksi, dan kode biaya/pusat biaya sesuai batas kewenangan masing-masing peran.
6. Mengimpor data posisi SAP SuccessFactors secara massal, mengekspor Bagan Posisi dalam format PDF dan PNG, serta menyediakan posisi sebagai sumber referensi tunggal bagi modul EC terkait.
7. Mencatat seluruh perubahan dalam jejak audit, termasuk pelaku, waktu, dan data yang berubah.

**Aturan perilaku dan prasyarat**

- Kode Posisi bersifat unik. Nama Posisi harus sesuai dengan struktur organisasi aktif dan kebutuhan bisnis.
- Hanya OD yang mengelola siklus hidup dan hierarki posisi. Pengguna umum memiliki tampilan hanya baca sesuai hak aksesnya.
- Setiap posisi memiliki paling banyak satu Posisi Atasan yang aktif pada periode berlaku yang sama. Hierarki harus valid dan tidak boleh membentuk siklus.
- `Create Position` mengharuskan pengisian data secara manual. `Add Position Below` mewarisi/mengisi hierarki secara otomatis dari simpul induk yang dipilih pada bagan.
- Perubahan mempertahankan data sebelumnya melalui penerapan tanggal berlaku. Posisi yang memiliki riwayat karyawan, organisasi, atau transaksi tidak dapat dihapus.
- Penonaktifan hanya diperbolehkan jika tidak ada pemangku posisi aktif, kandidat aktif, maupun posisi bawahan aktif.
- Perubahan garis pelaporan memperbarui Bagan Posisi dan Bagan Organisasi sesuai tanggal berlaku.
- Posisi harus merujuk pada data Direktorat, Divisi, Departemen, dan Seksi yang valid.

**Perilaku fungsional tambahan**

- Validasi pembuatan dan pengeditan harus mencakup data wajib, format data, keunikan Kode Posisi, konsistensi organisasi, hubungan dengan posisi atasan yang valid, serta aturan bisnis Pengelolaan Posisi yang berlaku sebelum data disimpan.
- Pengeditan dapat mencakup Nama Posisi, Kode Pekerjaan (Job Code), Pusat Biaya (Cost Center), Lokasi, Tingkat Posisi (Position Level), atau Garis Pelaporan (Reporting Line) sesuai kewenangan pengguna. Pengeditan yang berhasil memperbarui informasi posisi dan struktur organisasi terkait serta mencatat riwayat audit dengan tanggal berlaku.
- `Add Position Below` setidaknya harus mengisi Posisi Atasan, Divisi, dan Departemen secara otomatis dari simpul bagan yang dipilih sebelum pengguna melengkapi data posisi baru.
- OD Admin dapat mengimpor/mengekspor data posisi dan bagan; Comben mengelola Kode Biaya/Pusat Biaya (Cost Code/Cost Center); karyawan memiliki akses hanya baca ke Bagan Posisi sesuai kewenangannya. Sumber migrasi adalah data posisi SAP SuccessFactors.

**Hal-hal di luar cakupan**

Pembuatan Job Code Framework secara otomatis, rekrutmen, RTE, transaksi ESC, data pribadi/kepegawaian, anggaran kebutuhan tenaga kerja, penggajian/kompensasi, pengelolaan alur kerja persetujuan, proses kontrak, kelompok talenta, dan perubahan garis pelaporan melalui seret dan lepas tidak termasuk dalam cakupan.

**Skenario kasus penggunaan**

1. OD membuat posisi melalui pembuatan umum dengan kode unik dan referensi organisasi yang valid.
2. OD menambahkan posisi bawahan dari bagan dan memperoleh hierarki yang diwarisi sesuai harapan.
3. Posisi dengan pemangku atau posisi bawahan aktif tidak dapat dinonaktifkan; posisi yang memiliki riwayat tidak dapat dihapus.
4. Pemilihan tanggal lampau menampilkan bagan dan kondisi posisi sebelumnya yang sesuai.

## Ambiguitas sumber di luar himpunan kebutuhan yang dapat dieksekusi

BRD tidak memiliki bab khusus yang merinci kebutuhan fungsional atau katalog kolom posisi. Penjabaran ini didasarkan pada hal-hal dalam cakupan, alur proses yang diharapkan, peran, dan aturan kebijakan.
