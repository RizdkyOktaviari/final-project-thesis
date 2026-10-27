# Penjabaran Kebutuhan: EC Struktur Organisasi (Organization Structure)

## Sumber dan cakupan

- Source: `data/raw/BRD - EC Organization Structure.md`
- Tujuan: pengelolaan unit organisasi secara terpusat dan visualisasi riwayat organisasi.
- Peran: Organization Development (membuat/membaca/memperbarui) dan Karyawan (Employee, hanya baca).

## Kebutuhan Fungsional

1. Mengelola data induk unit organisasi dan Struktur Organisasi dengan hierarki yang valid.
2. Menampilkan bagan organisasi, detail profil karyawan, dan kondisi organisasi pada tanggal atau periode yang dipilih.
3. Mengekspor Struktur Organisasi dalam format PDF dan PNG.
4. Menyediakan pencarian berdasarkan nama departemen, nama posisi, nama karyawan, atau ID NH melalui integrasi dengan modul terkait.
5. Menyimpan riwayat data dengan penerapan tanggal berlaku dan jejak audit untuk perubahan struktur.
6. Menjadi referensi organisasi bagi modul Employee Central serta mengintegrasikan perubahan ESC yang memengaruhi penempatan karyawan atau visualisasi.

**Aturan perilaku dan pengendalian akses**

- Setiap unit organisasi memerlukan identitas unik dan harus menjadi bagian dari hierarki yang valid.
- OD dapat mengakses seluruh struktur organisasi. Pengguna lain hanya dapat melihat struktur sesuai hak aksesnya dalam mode hanya baca.
- Standar kode Direktorat, Divisi, Departemen, dan Seksi mengikuti kebijakan HR Organization Development.
- OD dapat menyesuaikan garis pelaporan yang tidak mengubah Struktur Organisasi kapan saja berdasarkan permintaan Unit Bisnis dari pihak yang sekurang-kurangnya berada pada tingkat Department Head/Manager.
- Pengelolaan posisi, pengelolaan kode IPS, hierarki posisi, rekrutmen, perencanaan tenaga kerja, kompensasi, administrasi otorisasi, restrukturisasi melalui seret dan lepas, serta pelaksanaan transaksi ESC berada di luar cakupan.

**Batas proses fungsional**

Persetujuan usulan perubahan organisasi di luar sistem tetap dilakukan secara manual. OD meninjau usulan, dokumentasi, hierarki, dan justifikasi bisnis sebelum peninjauan berurutan oleh Training and Development, Senior Manager HCM, GMO/Director in Charge, dan Board of Director. Cakupan proses di dalam sistem dimulai dari pembaruan struktur organisasi yang telah disetujui dan penyimpanan riwayatnya.

**Perilaku fungsional tambahan**

- Setelah persetujuan manual, OD harus dapat menambah/mengubah data organisasi secara langsung atau mengimpor Struktur Organisasi dalam format CSV/XLSX. Struktur yang telah disetujui tersebut menjadi referensi aktif bagi modul terkait.
- Untuk perubahan tahunan atau triwulanan di bawah tingkat Departemen, alur persetujuan manual dapat berakhir pada GMO/Director in Charge. Perubahan pada tingkat Departemen dan di atasnya harus sampai kepada Director. Usulan yang ditolak dikembalikan kepada pemohon dan OD untuk direvisi.
- Struktur Organisasi tidak mencakup pembuatan atau pengelolaan Posisi, kode IPS, hierarki posisi, data pribadi/kepegawaian karyawan, penugasan manajer, rekrutmen, perencanaan tenaga kerja, penggajian/tunjangan, kinerja, talenta, integrasi sistem keuangan di luar referensi Pusat Biaya (Cost Center), peran keamanan, atau restrukturisasi melalui seret dan lepas.

**Skenario kasus penggunaan**

1. OD membuat atau mengubah unit organisasi hanya jika induk dan hierarkinya valid, lalu perubahan tersebut dapat ditelusuri dalam riwayat.
2. Pengguna membuka bagan organisasi pada tanggal berlaku sebelumnya dan melihat struktur yang berlaku saat itu.
3. Mutasi melalui ESC yang telah disetujui tercermin pada tampilan organisasi terkait, tanpa menyediakan pembuatan ESC di modul ini.
4. Karyawan hanya dapat melihat informasi organisasi sesuai hak aksesnya dan tidak dapat mengubahnya.

## Ambiguitas sumber di luar himpunan kebutuhan yang dapat dieksekusi

BRD tidak memiliki bab kebutuhan fungsional tersendiri. Kebutuhan di atas dirumuskan dari bagian cakupan, alur yang diharapkan, dan kebijakan modul. Definisi terperinci kolom untuk pembuatan/pembaruan serta pesan validasi tidak ditentukan.
