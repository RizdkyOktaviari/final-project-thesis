# Penjabaran Kebutuhan: PMGM Penilaian Kinerja (Performance Assessment)

## Sumber dan cakupan

- Source: `data/raw/BRD PMGM - Performance Assessment.md`
- Peran: OD Admin, karyawan (Employee), atasan langsung (Direct Supervisor), dan atasan satu tingkat di atas atasan langsung (One-Up Supervisor).
- Siklus proses: konfigurasi dan peluncuran templat, penilaian diri, peninjauan oleh atasan, normalisasi di luar sistem dengan impor ke sistem, finalisasi, pelaporan, dan audit.

## Kebutuhan Fungsional

1. Memungkinkan OD membuat, mengubah, menggandakan, melihat pratinjau, meluncurkan, menutup, dan mengonfigurasi templat Penilaian Kinerja (Performance Assessment) yang terpisah untuk Staff dan Non-Staff. Konfigurasi mencakup pengaturan umum, skala penilaian, peta rute/alur kerja, periode, notifikasi, peserta, bahasa, bagian, dan kolom.
2. Memungkinkan karyawan menggunakan formulir sesuai kategori/bahasanya, melihat tahap pada peta rute, memberi nilai dan komentar pada sasaran, mengunggah lampiran opsional, memasukkan aspirasi, menyimpan draf, dan mengajukan setelah lolos validasi wajib.
3. Mengunci pengeditan oleh karyawan setelah pengajuan, kecuali jika penilaian dikembalikan untuk diperbaiki.
4. Memungkinkan Direct Supervisor meninjau penilaian diri, menyesuaikan nilai, memberikan komentar, mencatat kelebihan dan aspek yang perlu ditingkatkan, serta mengajukan kepada One-Up Supervisor. Memungkinkan One-Up Supervisor melihat penilaian diri dan penilaian Direct Supervisor, menyesuaikan nilai/komentar, dan menyelesaikan tahapnya.
5. Mendukung satu atau dua tingkat peninjauan untuk Non-Staff. Menggunakan struktur organisasi untuk Staff; OD mengonfigurasi peta rute Non-Staff per departemen saat peluncuran.
6. Menyediakan notifikasi dan pengingat yang dapat dikonfigurasi berdasarkan tindakan, tugas yang belum selesai, tenggat, penerima, subjek, waktu, dan frekuensi.
7. Memungkinkan OD mengekspor data PA untuk departemen terpilih menjadi satu file XLSX atau CSV per departemen; membuat kelompok normalisasi; mengimpor/mengimpor ulang hasil departemen dengan catatan wajib dan lampiran opsional; mempertahankan riwayat impor sebelumnya; serta menyesuaikan nilai akhir secara individual dengan catatan wajib.
8. Memungkinkan OD melakukan finalisasi setelah normalisasi departemen. Sistem mengubah status PA menjadi `Completed`, mengunci nilai akhir, dan hanya menampilkan nilai akhir kepada karyawan.
9. Menyediakan laporan PA dengan filter periode, Staff/Non-Staff, jenjang jabatan, departemen, karyawan, dan status, serta ekspor XLSX atau CSV.
10. Mendukung penanganan mutasi/promosi karyawan, pengunduran diri/pemutusan hubungan kerja karyawan, dan pengunduran diri atasan, termasuk penggantian peninjau atau pelewatan tahap peninjauan oleh OD ketika atasan mengundurkan diri sebelum meninjau.

**Aturan perilaku, perhitungan, dan prasyarat**

- Skala penilaian adalah 1 hingga 6, dengan nama dan deskripsi yang dikonfigurasi. Komentar pada sasaran wajib diisi; lampiran bersifat opsional. Aspirasi diisi oleh karyawan, sedangkan kelebihan/aspek yang perlu ditingkatkan diisi oleh atasan.
- Menyimpan draf tidak memajukan tahap. Pengajuan mensyaratkan pengisian setiap kolom wajib. Templat tidak dapat diubah setelah diluncurkan.
- Direct Supervisor tidak dapat melihat nilai dari One-Up Supervisor; One-Up Supervisor dapat melihat nilai dari karyawan dan Direct Supervisor. Riwayat nilai hanya dapat diakses oleh OD.
- OD tidak memiliki tindakan persetujuan dalam alur kerja PA. OD dapat memindahkan penilaian secara massal ke tahap Normalization dan hanya menjalankan tindakan administratif normalisasi.
- Nilai Keseluruhan Formulir (Overall Form Rating) dihitung dengan rumus `sum(section rating x section weight) / sum(section weight)`. Sebelum proses selesai, karyawan melihat tanda hubung sebagai pengganti nilai keseluruhan.
- Pembahasan normalisasi berlangsung di luar sistem. Impor terakhir yang berhasil menjadi impor aktif; seluruh file sebelumnya tetap tersimpan dalam riwayat dan log audit.
- Aktivitas Goal Management tidak memengaruhi nilai/perhitungan PA. Penilaian otomatis untuk penilaian diri yang belum selesai, tampilan GAP, bagian tanda tangan, dan bagian konfirmasi penerimaan berada di luar cakupan.

**Perilaku akses dan audit**

- OD dapat melihat seluruh penilaian, status, riwayat nilai/komentar, dan jejak audit; OD dapat mengganti pemetaan peninjau dengan catatan wajib.
- Karyawan dapat melihat penilaiannya dan nilai akhir pada tahap yang diizinkan, tetapi tidak dapat melihat rincian penilaian One-Up Supervisor atau riwayat nilai.
- Seluruh kejadian pemberian nilai, komentar, persetujuan/pengembalian untuk perbaikan, perubahan peninjau, impor, impor ulang, dan finalisasi dapat diaudit.

**Perilaku fungsional tambahan**

- Direct Supervisor dan One-Up Supervisor dapat menyimpan draf dan mengembalikan penilaian untuk diperbaiki sebelum mengajukan hasil peninjauan masing-masing. Bagian Ringkasan (Summary Section) tersedia sesuai tahap; Direct Supervisor dapat menetapkan nilai bagian secara manual, sedangkan Nilai Keseluruhan Formulir tetap dihitung oleh sistem.
- Jalur administrator yang dikonfigurasi menggunakan satu tingkat peninjauan oleh Manager; Director dapat menjadi peninjau akhir apabila OD mengonfigurasinya. Ketentuan ini melengkapi aturan hierarki Staff dan peta rute Non-Staff tanpa menggantikannya.
- Kelompok normalisasi hanya memerlukan nama dan mengikuti periode PA yang aktif; kelompok ini tidak memiliki periode buka/tutup tersendiri. Dokumen sumber juga mensyaratkan peninjauan hasil validasi impor.
- Mutasi/promosi karyawan mempertahankan sasaran yang telah diajukan dan menambahkan penanda `Is Transferred`; pengunduran diri/pemutusan hubungan kerja menghapus karyawan dari daftar peserta aktif.

**Skenario kasus penggunaan**

1. Karyawan Staff mengajukan penilaian diri yang valid, sehingga memicu peninjauan oleh Direct Supervisor dan penguncian formulir.
2. Peserta Non-Staff memperoleh peta rute yang dikonfigurasi OD dengan paling banyak dua tingkat peninjauan.
3. OD mengekspor dua departemen dan memperoleh dua file terpisah, lalu mengimpor ulang hasil yang telah diperbaiki dengan tetap mempertahankan ketersediaan riwayat.
4. Finalisasi mengunci nilai akhir dan menampilkannya kepada karyawan, sedangkan rincian data peninjauan tidak ditampilkan.
