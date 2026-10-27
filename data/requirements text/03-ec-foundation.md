# Penjabaran Kebutuhan: EC Layanan Dasar (Foundation)

## Sumber dan cakupan

- Source: `data/raw/BRD - EC Foundation.md`
- Foundation merupakan modul layanan bersama. Modul ini tidak secara langsung mengelola transaksi Human Capital; BRD modul yang menggunakan layanan Foundation menetapkan kolom dan rincian prosesnya masing-masing.

## Kebutuhan Fungsional

1. Mendukung beberapa perusahaan dalam satu platform. Administrator HR membuat, memperbarui, mengaktifkan, dan menonaktifkan perusahaan tanpa menghapus riwayat, menugaskan pengguna ke satu atau beberapa perusahaan, serta menyediakan konfigurasi perusahaan bagi modul EC.
2. Menyediakan akses perwakilan (Proxy Access). Pemohon memilih pengguna yang akan diwakili, masa berlaku dalam hari, dan alasan; meninjau rincian permohonan; lalu mengajukannya sehingga berstatus `Pending Approval`.
3. Mengirim notifikasi kepada pengguna yang akan diwakili dan memungkinkan pengguna tersebut menyetujui atau menolak permohonan. Mengaktifkan akses perwakilan yang telah disetujui hanya ketika periode berlakunya dimulai.
4. Menampilkan daftar akses perwakilan yang aktif, termasuk pemohon, pengguna yang diwakili, tanggal mulai, dan tanggal berakhir. Memungkinkan pemohon beralih pengguna hanya selama akses perwakilan aktif.
5. Memungkinkan pemohon mengembalikan akses dan pengguna yang diwakili mencabut akses. Mengakhiri akses secara otomatis ketika masa berlakunya habis dan mencegah perpindahan pengguna selanjutnya.
6. Membedakan aktivitas yang dilakukan melalui akses perwakilan dari aktivitas langsung, dengan mempertahankan identitas pemohon dan pengguna yang diwakili dalam data audit.
7. Menyediakan alur kerja persetujuan yang dapat digunakan kembali dan dikonfigurasi, dengan satu atau beberapa tingkat berurutan. Jenis pemberi persetujuan dapat ditentukan berdasarkan pengguna tertentu, posisi, atasan langsung, tingkat manajer, peran, dan secara opsional unit organisasi. Mendukung pengajuan, persetujuan, delegasi, pengembalian untuk perbaikan, dan penarikan kembali permohonan.
8. Menyediakan layanan bersama berupa pengendalian akses berbasis peran (RBAC), autentikasi, jejak audit, dukungan integrasi, serta log impor/validasi/rekonsiliasi migrasi bagi modul EC.

**Aturan perilaku dan pengendalian akses**

- Akses perwakilan memerlukan pengguna yang akan diwakili, alasan, masa berlaku dalam hari, status pengguna yang memenuhi syarat, dan persetujuan dari pengguna yang akan diwakili.
- Aktivitas melalui akses perwakilan hanya menggunakan cakupan data yang diizinkan bagi pengguna yang diwakili. Akses tersebut tidak memberikan izin tambahan kepada pemohon.
- Akses perwakilan yang ditolak, dikembalikan, dicabut, atau kedaluwarsa tidak dapat digunakan untuk beralih pengguna.
- Aktivitas alur kerja yang didelegasikan harus mencatat identitas penerima delegasi dalam log audit. Konfigurasi alur kerja dapat digunakan kembali di berbagai modul.
- Akses dibatasi berdasarkan peran, kewenangan, perusahaan, dan cakupan organisasi. Data pribadi sensitif memerlukan enkripsi pada lapisan aplikasi sebelum disimpan ke basis data.
- Jejak audit untuk data induk mencakup pelaku, cap waktu, tindakan, serta nilai sebelum/sesudah perubahan, dan tidak dapat diubah oleh pengguna aplikasi.
- Kegagalan integrasi harus dicatat dalam log. Data migrasi dari SAP SuccessFactors harus divalidasi dan direkonsiliasi sebelum sistem mulai beroperasi, sementara PTAR bertanggung jawab menyediakan data sumber hasil ekspor.

**Perilaku perlindungan data sensitif**

BRD menandai informasi identitas nasional, keuangan, kesehatan, biometrik, genetik, hukum, anak, dan riwayat lokasi sebagai informasi yang memerlukan enkripsi. Aturan pemrosesan pada tingkat kolom, penyamaran, pencarian, migrasi, dan integrasi tetap menjadi tanggung jawab BRD masing-masing modul yang menggunakan layanan Foundation.

**Perilaku fungsional tambahan**

- Administrator harus dapat membuat, mengubah, mengaktifkan, dan menonaktifkan konfigurasi alur kerja. Delegasi dibatasi waktunya dan hanya tersedia bagi pengguna aktif dengan kewenangan yang diperlukan.
- Notifikasi akses perwakilan diperlukan saat pengajuan permohonan (kepada pengguna yang akan diwakili), persetujuan dan penolakan (kepada pemohon), aktivasi (kepada pemohon dan pengguna yang diwakili), pengembalian lebih awal (kepada pengguna yang diwakili), pencabutan (kepada pemohon), dan berakhirnya masa berlaku (kepada kedua pihak).
- Jejak audit harus mencakup pembuatan, pembaruan, dan penghapusan, beserta pengguna, waktu, aktivitas, serta nilai sebelum/sesudah perubahan jika berlaku; pengguna aplikasi tidak dapat mengubah jejak audit tersebut.
- Dukungan migrasi mencakup impor, validasi sebelum impor, hasil validasi/rekonsiliasi, dan log migrasi. SAP SuccessFactors ditetapkan sebagai sistem sumber dan PTAR menyediakan data hasil ekspor.
- Foundation bertanggung jawab atas kemampuan bersama untuk perusahaan, alur kerja, akses perwakilan, keamanan, audit, integrasi, migrasi, dan perlindungan data. Modul yang menggunakan layanan Foundation tetap bertanggung jawab atas kolom bisnis dan transaksinya masing-masing.

**Skenario kasus penggunaan**

1. Pengguna yang akan diwakili menyetujui permohonan akses perwakilan yang valid, pemohon beralih pengguna selama periode yang disetujui, dan log menyimpan kedua identitas tersebut.
2. Pengembalian, pencabutan, dan berakhirnya masa berlaku secara otomatis langsung mencegah perpindahan pengguna serta menghasilkan catatan audit.
3. Alur kerja bertingkat yang telah dikonfigurasi mengarahkan proses secara berurutan, hanya mendelegasikan kepada pengguna aktif yang memenuhi syarat, dan mencatat pelaku delegasi.
4. Perusahaan dinonaktifkan tanpa kehilangan catatan sebelumnya dan tidak dapat digunakan sebagai cakupan operasi yang aktif.

**Batas interaksi antarmodul**

Kemampuan Foundation digunakan oleh Organization Structure, Position Management, Hiring, ESC, Benefit, Termination, dan seluruh modul EC lainnya untuk perilaku keamanan, audit, integrasi, dan akses perwakilan.
