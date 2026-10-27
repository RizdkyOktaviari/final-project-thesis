# Penjabaran Kebutuhan: PMGM Pengelolaan Sasaran (Goal Management)

## Sumber dan cakupan

- Source: `data/raw/BRD_PMGM_Goal_Management.md`
- Peran: OD Section, karyawan, Direct Supervisor, manajer di tingkat atas/One-Up Supervisor, dan Department Head/pimpinan untuk eskalasi pengingat.

## Kebutuhan Fungsional

1. Memungkinkan OD membuat periode KPI dengan tanggal mulai dan tenggat, memilih karyawan yang dikecualikan, membuka/membuka kembali periode, dan mengonfigurasi notifikasi.
2. Menyediakan dua formulir KPI yang dipilih secara otomatis, satu untuk Staff dan satu untuk Non-Staff. Selama periode terbuka, karyawan dapat membuat, mengubah, menghapus, menyimpan, dan mengajukan KPI mereka; setelah periode ditutup, mereka hanya dapat membuat atau mengubah aktivitas yang terkait.
3. Memvalidasi jumlah maksimal 10 butir KPI, total bobot 100%, bobot per butir sebesar 5-25% untuk Staff dan 5-30% untuk Non-Staff, serta total bobot Learning & Growth yang tidak melebihi 15%.
4. Mendukung penurunan KPI (cascade) oleh manajer yang memenuhi syarat kepada bawahan langsung. Memvalidasi bobot KPI turunan yang diwajibkan sebelum pengajuan, lalu mengirimkan KPI yang diajukan untuk ditinjau oleh Direct Supervisor.
5. Memungkinkan Direct Supervisor menyetujui atau meminta revisi dengan catatan wajib. Memungkinkan OD memberikan persetujuan akhir atau meminta revisi. Revisi mengembalikan KPI kepada karyawan, lalu melalui Direct Supervisor kembali sebelum sampai ke OD.
6. Mengunci KPI yang telah selesai meskipun periode masih terbuka. Menyediakan notifikasi dalam aplikasi dan email yang sesuai, eskalasi pengingat, serta format/durasi/penerima/isi yang dapat dikonfigurasi.
7. Menerapkan batasan visibilitas: karyawan mengelola KPI mereka sendiri; atasan/manajer melihat KPI bawahan yang diizinkan berdasarkan hierarki organisasi; OD melihat seluruh karyawan, status, riwayat peninjauan, dan riwayat revisi.
8. Menyimpan perubahan KPI, persetujuan, revisi, dan catatan peninjauan dalam jejak audit. Mengekspor KPI milik sendiri/bawahan ke PDF dan data KPI departemen ke Excel untuk OD.
9. Mendukung revisi pertengahan tahun (Mid-Year), termasuk penggantian status oleh OD dan pembukaan kembali. Jika terjadi perubahan posisi/departemen selama periode KPI, mengembalikan KPI ke draf agar dapat disusun ulang untuk peran baru.
10. Memungkinkan OD mengonfigurasi aturan bisnis KPI, penyertaan/pengecualian peserta, pengaturan notifikasi, dan apakah KPI turunan bersifat wajib. Bawahan tidak dapat mengubah atau menghapus KPI turunan yang wajib.

**Aturan perilaku dan prasyarat**

- Staff menggunakan perspektif Finance, Stakeholder, Internal Process, dan Learning & Growth. Tidak semua perspektif wajib digunakan apabila tidak sesuai dengan pekerjaan.
- Peran terendah yang diizinkan menurunkan KPI adalah Supervisor. Direct Supervisor untuk Staff tidak boleh melompati tingkat hierarki saat menurunkan KPI; untuk Non-Staff, penurunan KPI dilakukan oleh Supervisor.
- Manajer harus menyelesaikan dan mengajukan KPI miliknya sendiri sebelum menurunkan KPI kepada bawahan. Karyawan dapat membuat dan menyimpan draf tanpa menerima KPI turunan, tetapi tidak dapat mengajukan sebelum lolos validasi KPI turunan yang diwajibkan.
- Dokumen menyatakan bahwa bobot minimum bawaan KPI turunan yang diterima adalah 50% dan dapat dikonfigurasi oleh OD. Diagram yang disematkan dalam dokumen menyebutkan 40%. Hal ini merupakan konflik pada sumber; jangan memilih salah satu nilai tanpa keputusan bisnis.
- Ketika posisi manajer berubah, OD menyesuaikan alur kerja agar peran tersebut dapat melanjutkan peninjauan dan perubahan KPI yang diizinkan.
- Karyawan yang dikecualikan oleh OD tidak menerima notifikasi periode KPI dan tidak diwajibkan mengajukan KPI.
- Goal Management tidak mencakup penerusan otomatis ke OD pada tenggat, papan Aktivitas/Kanban dengan fitur seret dan lepas, pembuatan KPI di dalam sistem untuk anggota Dewan, maupun permintaan persetujuan peluncuran/pembukaan/penutupan.

**Perilaku notifikasi**

- Pengajuan mengirimkan notifikasi dalam aplikasi kepada pemohon dan Direct Supervisor, serta email kepada Direct Supervisor.
- Persetujuan mengirimkan notifikasi dalam aplikasi kepada pemohon dan pemberi persetujuan, serta email kepada pemohon.
- Revisi/pengembalian untuk perbaikan mengirimkan notifikasi dalam aplikasi kepada pemohon dan pemberi persetujuan, serta email kepada pemohon.
- Tahapan pengingat bawaan adalah tiga minggu kepada Department Head, dua minggu kepada Senior Manager/Director, dan satu minggu kepada GMO/Director, dengan mengikuti konfigurasi OD.

**Skenario kasus penggunaan**

1. Karyawan Staff dengan 11 KPI, total bobot yang salah, bobot per butir yang tidak valid, atau bobot Learning & Growth yang berlebihan tidak dapat menyimpan atau mengajukan KPI.
2. Karyawan dapat menyimpan draf tanpa menerima KPI turunan, tetapi tidak dapat mengajukan sampai ambang batas bobot KPI turunan yang telah dikonfirmasi terpenuhi.
3. Revisi oleh Supervisor yang disertai catatan menghasilkan status `Revise Required`, memungkinkan perbaikan, dan mengembalikan KPI ke jalur peninjauan yang benar.
4. KPI yang telah selesai tidak dapat diubah; periode Mid-Year memungkinkan proses revisi yang terdokumentasi.

## Ambiguitas sumber di luar himpunan kebutuhan yang dapat dieksekusi

Konfirmasikan apakah bobot minimum bawaan KPI turunan di lingkungan produksi adalah 40% atau 50%, serta apakah nilainya dapat dikonfigurasi per periode, formulir, atau organisasi.
