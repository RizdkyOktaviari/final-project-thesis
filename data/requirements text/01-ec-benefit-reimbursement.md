# Penjabaran Kebutuhan: EC Penggantian Biaya Tunjangan (Benefit Reimbursement)

## Sumber dan cakupan

- Source: `data/raw/BRD - EC Benefit Reimbursement.md`
- Fokus: bantuan tunjangan (Benefit Assistance), khususnya Bantuan Pendidikan (Education Assistance).
- Peran utama: Karyawan (Employee), HR Compensation & Benefit, serta Super Admin untuk pengajuan bertanggal mundur yang diizinkan atau pembatalan klaim yang telah disetujui.

## Kebutuhan Fungsional

1. Menyediakan formulir pengajuan Benefit Assistance bagi karyawan yang memuat tanggal klaim, pilihan tunjangan, mata uang, dan jumlah hak tunjangan yang dihitung oleh sistem.
2. Menyediakan baris perincian Bantuan Pendidikan untuk tanggungan yang memenuhi syarat. Karyawan dapat menambahkan hingga tiga tanggungan dan melengkapi identitas siswa, sekolah, kelas, tahun pendidikan, serta informasi pendukung.
3. Mengambil data tanggungan yang memenuhi syarat, tanggal mulai bekerja, dan data validasi terkait dari Employee Central. Mengisi otomatis data tanggungan yang tersedia setelah tanggungan dipilih.
4. Menghitung hak tunjangan berdasarkan kategori tunjangan, jenjang sekolah, jumlah tanggungan yang memenuhi syarat, plafon yang berlaku, dan aturan prorata untuk karyawan baru atau karyawan kontrak. Karyawan tidak dapat mengubah jumlah hasil perhitungan.
5. Memvalidasi kelayakan, usia tanggungan, hubungan tanggungan dengan klaim, frekuensi klaim, klaim duplikat, periode pengajuan, dan sisa plafon sebelum pengajuan.
6. Mendukung pengajuan oleh Super Admin atas nama karyawan dengan tanggal pengajuan tersendiri untuk kasus bertanggal mundur yang diizinkan. Menyimpan identitas pembuat dan pemilik permohonan untuk keperluan audit.
7. Menerima dokumen pendukung wajib hanya dalam format PDF atau JPG dan menyimpannya bersama klaim. Menyediakan formulir Bantuan Pendidikan yang dapat diunduh oleh HR Compensation & Benefit.
8. Meneruskan klaim yang diajukan kepada HR Compensation & Benefit untuk ditinjau. Peninjau dapat menyetujui atau mengembalikan klaim; pengembalian wajib disertai komentar dan memungkinkan karyawan memperbaiki serta mengajukan ulang klaim.
9. Mengizinkan Super Admin membatalkan klaim yang telah disetujui serta mencatat pelaku pembatalan dan statusnya.
10. Menyediakan riwayat klaim bagi karyawan dan HR, status terkini, tanggal status, pelaku aktivitas, ekspor laporan dalam format Excel, serta kumpulan data klaim yang telah disetujui untuk administrasi pembayaran.
11. Memberi tahu HR saat pengajuan; memberi tahu karyawan saat klaim disetujui, dikembalikan, atau dibatalkan; serta mengirim pengingat kepada peninjau untuk persetujuan yang masih tertunda.

**Aturan perilaku dan prasyarat**

- Dalam proses normal, hanya karyawan yang dapat mengajukan klaim. Super Admin menjadi pengecualian untuk pemrosesan bertanggal mundur yang diizinkan.
- Jenis tunjangan harus sesuai dengan kelayakan karyawan dan seluruh informasi wajib harus lengkap sebelum proses dapat dilanjutkan.
- Bantuan Pendidikan hanya menggunakan data tanggungan dari Employee Central, mengizinkan paling banyak tiga tanggungan, dan tidak mencakup tanggungan yang berusia lebih dari 23 tahun.
- Tanggungan yang sama tidak dapat diklaim oleh lebih dari satu karyawan pada periode yang sama. Karyawan tetap tidak dapat membuat klaim duplikat untuk tanggungan dan periode yang sama; karyawan kontrak dapat mengajukan klaim kembali hanya jika masih memiliki sisa plafon.
- Batas frekuensi adalah satu klaim PAUD dan dua klaim TK per tanggungan. Klaim untuk jenjang SD hingga perguruan tinggi dapat diajukan selama masih ada hak tunjangan.
- Periode tunjangan berlangsung dari 1 Juli hingga 15 Juni tahun berikutnya. Pengajuan normal oleh karyawan ditolak dari 16 hingga 30 Juni. Sistem memberi peringatan pada atau setelah batas akhir; sumber menyebut 15 Juni sebagai tanggal penguncian tahun akademik setiap tahun.
- Ketiadaan dokumen wajib menghalangi pemrosesan. BRD secara umum menyebut PDF atau JPG, sedangkan tabel Education Claim Form secara khusus mencantumkan PDF untuk kolom lampirannya.
- Permohonan yang sedang diproses untuk karyawan dan tanggungan yang sama menghalangi permohonan baru yang setara, tetapi dokumen juga menjelaskan ketentuan bagi karyawan kontrak yang memiliki sisa plafon. Implementasi memerlukan aturan status dan kelayakan yang tepat untuk menyelaraskan pernyataan tersebut.
- Penarikan kembali mengubah status permohonan menjadi `Withdrawn`, memberi tahu HR Compensation & Benefit, dan mencatat tindakan tersebut. Salah satu aturan sebelumnya membatasi penarikan kembali pada status `Sent Back`, sedangkan bagian pengecualian menjelaskan penarikan kembali secara lebih umum; hal ini perlu dikonfirmasi sebelum implementasi.

**Interaksi fungsional, akses, dan integrasi**

- Employee Central menjadi sumber informasi karyawan, tanggungan, dan tanggal mulai bekerja yang digunakan dalam perhitungan kelayakan dan prorata.
- Klaim yang telah disetujui menjadi masukan untuk administrasi pembayaran oleh HR Compensation & Benefit. BRD tidak mewajibkan pelaksanaan pembayaran penggajian secara langsung.
- Karyawan melihat klaim miliknya sendiri; HR Compensation & Benefit melihat klaim dalam lingkup kewenangannya; Super Admin hanya memiliki kemampuan khusus yang disebutkan.
- Riwayat harus mencatat status permohonan, tanggal, pelaku, dan aktivitas perubahan. Data pengajuan harus sesuai dengan bukti terlampir dan diverifikasi oleh HR.

**Perilaku fungsional tambahan**

- Membatasi ukuran setiap dokumen pendukung hingga 10 MB. Sumber menerima PDF atau JPG dalam aturan umum unggahan, tetapi Education Claim Form secara khusus menyebut lampiran wajibnya sebagai PDF; hal ini tetap dicatat sebagai konflik format yang belum terselesaikan.
- Mempertahankan perilaku kolom pada Education Claim Form: mata uang, hak tunjangan, data tanggungan yang dipilih, nama siswa, usia, tanggal lahir, jenis kelamin, dan tahun pendidikan berasal dari sistem atau bersifat hanya baca sesuai penandaan; karyawan mengisi nomor identitas siswa, sekolah, kelas opsional, nama/alamat sekolah, lampiran, dan catatan opsional.
- Mempertahankan aturan bahwa tunjangan yang telah diterima tidak dikembalikan hanya karena karyawan kemudian mengundurkan diri.
- Mempertahankan kebutuhan konfigurasi kebijakan mendatang untuk kategori Bantuan Pendidikan berdasarkan jenjang jabatan, sementara pemeliharaan kebijakan tunjangan itu sendiri tetap berada di luar modul ini.
- Memigrasikan riwayat Benefit Reimbursement dari 2021 hingga data sumber terbaru yang tersedia. Bantuan Kedukaan (Condolence Assistance), pemeliharaan data karyawan/tanggungan, pemeliharaan kebijakan, pembayaran penggajian secara langsung, dan pemrosesan luring setelah batas akhir tidak termasuk dalam modul ini.
- Notifikasi pengembalian dan pembatalan menyertakan komentar peninjau. Pengingat persetujuan yang tertunda dikirim kepada HR Compensation & Benefit.
- Jejak audit harus mencatat setidaknya pengajuan, pengeditan, persetujuan, pengembalian, pengajuan ulang, dan penarikan kembali, beserta pengguna, peran, waktu aktivitas, dan ID permohonan.

**Skenario kasus penggunaan**

1. Karyawan yang memenuhi syarat mengajukan Bantuan Pendidikan untuk tanggungan yang memenuhi syarat dengan bukti wajib dan memperoleh riwayat status.
2. Tanggungan berusia di atas 23 tahun, klaim PAUD/TK yang melebihi batas, klaim duplikat karyawan tetap, atau pengajuan pada periode penutupan 16-30 Juni ditolak sebelum pengajuan diteruskan.
3. HR mengembalikan klaim dengan komentar wajib; karyawan memperbaiki dan mengajukan ulang klaim.
4. Karyawan kontrak yang memiliki sisa plafon mengikuti aturan pengajuan klaim berulang yang dimaksud setelah ambiguitas di atas diselesaikan.
5. Super Admin membuat klaim bertanggal mundur dan jejak audit membedakan admin yang membuat klaim dari karyawan pemilik klaim.

## Ambiguitas sumber di luar himpunan kebutuhan yang dapat dieksekusi

- Mengonfirmasi seluruh format lampiran yang diizinkan untuk Education Claim Form.
- Mengonfirmasi apakah penarikan kembali hanya sah setelah `Sent Back` atau pada seluruh tahap yang belum selesai.
- Menetapkan status yang secara tepat menandakan klaim duplikat aktif dan pengecualian bagi karyawan kontrak.
