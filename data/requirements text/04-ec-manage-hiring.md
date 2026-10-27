# Penjabaran Kebutuhan: EC Pengelolaan Perekrutan (Manage Hiring)

## Sumber dan cakupan

- Source: `data/raw/BRD - EC Manage Hiring.md`
- Proses: permohonan perekrutan (Request to Employ/RTE), penyusunan gaji (Salary Build Up/SBU), pengisian data karyawan baru, dan evaluasi masa percobaan.
- Peran: Department Head User, OD TM/OD Section, HR Recruitment, rangkaian pemberi persetujuan, LM Requester, Senior Manager HCM, HR-CompBen, IT & System, dan Finance.

## Kebutuhan Fungsional

### Permohonan perekrutan (Request to Employ)

1. Memungkinkan Department Head User mengajukan dokumen RTE dan Position Description dalam format PDF setelah memeriksa anggaran kebutuhan tenaga kerja yang telah disetujui.
2. Meneruskan RTE melalui validasi anggaran oleh OD TM/OD Section, tinjauan HR Recruitment, dan rangkaian persetujuan berurutan yang disebutkan: Senior Manager HCM, Senior Manager Business Unit, GMO/GM PD/Chief Geo, Director in Charge, dan Director of HC.
3. Menyediakan tampilan bagi pemberi persetujuan serta tindakan menyetujui/mengembalikan. Permohonan yang dikembalikan dapat diajukan ulang atau ditarik kembali.
4. Mendukung pencarian dan pemilihan jabatan oleh HR Recruitment. Jika tidak ada jabatan yang tersedia, memungkinkan OD meninjau permohonan jabatan baru berdasarkan anggaran kebutuhan tenaga kerja dan mengembalikan keputusan kepada HR Recruitment.

### Penyusunan gaji (Salary Build Up)

1. Memungkinkan HR Recruitment membuat usulan SBU dengan informasi demografis perekrutan, jenis kelamin staf/nonstaf, agama/jumlah tenaga kerja staf, golongan, beberapa pembanding internal, riwayat pekerjaan dalam bentuk tabel, gaji/komponen sebelumnya, komponen gaji yang diisi secara manual, serta pilihan status kepegawaian/roster kerja pada PTAR Offer.
2. Meneruskan SBU melalui Senior Manager HCM, Director of HC, Senior Manager Business Unit, GMO/GM PD/Chief Geo, dan Director in Charge. Setiap tahap menyetujui atau mengembalikan usulan; HR Recruitment dapat mengajukan ulang atau menarik kembali usulan.
3. Menyediakan pembuatan surat penawaran (Offering Letter) bagi HR Recruitment hanya setelah seluruh persetujuan SBU yang diwajibkan selesai.

### Data karyawan baru

1. Memungkinkan HR Recruitment membuat data karyawan baru setelah jabatan yang valid dipilih atau dibuat.
2. Mencatat status kepegawaian, data organisasi, data pribadi/keluarga/alamat/pendidikan/telepon/identitas nasional, ID pengguna HRIS, dan email.
3. Mendukung tanggung jawab pada tahap lanjutan: pengisian kompensasi dan tunjangan oleh HR-CompBen, aktivasi di Mata Air oleh IT & System, serta pengisian data penggajian oleh Finance.

### Evaluasi masa percobaan

1. Memicu pengingat 30 dan 14 hari sebelum masa percobaan berakhir.
2. Memungkinkan Department Head User melengkapi dan mengajukan evaluasi; HR Recruitment meninjau dan mengatur peninjau; LM Requester dan Senior Manager HCM memberikan tinjauan dan umpan balik.
3. Mengizinkan persetujuan, pengembalian, perbaikan, pengajuan ulang, pengumpulan umpan balik, dan pembuatan surat pemberitahuan oleh HR Recruitment. BRD menetapkan tanggung jawab distribusi akhir kepada Department Head User.

**Aturan perilaku dan prasyarat bersama**

- RTE harus menyertakan formulir RTE dan Position Description serta bergantung pada anggaran kebutuhan tenaga kerja yang telah disetujui.
- SBU tidak dapat berlanjut hingga pemberi persetujuan pada tahap saat ini menyetujuinya. Pengembalian mengembalikan usulan agar dapat diajukan atau ditarik kembali.
- Data karyawan baru harus menggunakan jabatan yang tersedia atau jabatan yang dibuat melalui tinjauan anggaran kebutuhan tenaga kerja yang telah disetujui.
- Lampiran wajib untuk RTE dan data karyawan baru divalidasi; BRD secara umum mengizinkan PDF atau JPG, sedangkan RTE dan PD secara khusus disebut menggunakan format PDF.
- Penarikan kembali menetapkan status `Withdrawn`, memberi tahu HR Recruitment, dan mencatat tindakan tersebut.
- Penerima, pemicu, dan perincian pesan notifikasi di luar pengingat masa percobaan yang disebutkan secara eksplisit ditandai dalam sumber sebagai hal yang memerlukan konfirmasi.

**Interaksi dan dependensi antarmodul**

- Position Management dan Organisation Structure menyediakan data jabatan yang tersedia dan data organisasi.
- Kompensasi/tunjangan, aktivasi IT, dan pemrosesan penggajian oleh Finance merupakan tanggung jawab tahap lanjutan; kontrak integrasinya belum didefinisikan secara lengkap dalam BRD ini.

**Akses, audit, dan perilaku fungsional tambahan**

- Urutan proses karyawan baru berlanjut setelah pengisian oleh HR Recruitment: HR Compensation & Benefit mengisi kompensasi/tunjangan; IT & System membuat akun HRIS/email dan mengaktifkan karyawan di Mata Air; Finance mengisi data penggajian; proses saat ini juga mencatat pendaftaran wajah dan sidik jari.
- Notifikasi RTE dan SBU merupakan kebutuhan yang dinyatakan secara konkret dalam sumber: pengajuan memberi tahu OD TM/OD Section atau Senior Manager HCM; pengembalian memberi tahu pemohon; persetujuan pada tahap sebelumnya memberi tahu pemberi persetujuan berikutnya. Pengingat masa percobaan pada 30 dan 14 hari dikirim kepada HR Recruitment; pengajuan evaluasi masa percobaan dan penyelesaian tinjauan akhir juga memberi tahu HR Recruitment.
- Data sensitif mencakup informasi pribadi dan kepegawaian, RTE/PD, informasi gaji/usulan SBU, anggaran kebutuhan tenaga kerja, evaluasi/umpan balik masa percobaan, serta komentar persetujuan. Menerapkan RBAC; pengguna yang tidak berwenang tidak dapat melihat, mengunduh, atau mengubah data maupun dokumen terkait.
- Mencatat dalam audit aktivitas pengajuan, persetujuan, pengembalian, pengajuan ulang, perubahan data, tindakan alur kerja, pengisian data karyawan baru, dan pembuatan jabatan, beserta ID pengguna, peran, aktivitas, waktu, ID permohonan/referensi, dan data terkait yang berubah. Jejak audit operasional bersifat hanya baca.
- Mempertahankan kebutuhan migrasi data historis dari 2021 hingga data terbaru. Pencarian kandidat, pemeliharaan organisasi, pemeliharaan anggaran kebutuhan tenaga kerja, pembayaran penggajian, perjanjian kerja, serta keputusan/kebijakan kepegawaian tetap berada di luar modul ini.

**Skenario kasus penggunaan**

1. RTE tanpa anggaran kebutuhan tenaga kerja yang telah disetujui tidak dapat berlanjut hingga proses terkait anggaran diselesaikan.
2. SBU yang dikembalikan pada tingkat persetujuan mana pun dapat diperbaiki dan diajukan ulang, lalu menghasilkan Offering Letter hanya setelah persetujuan akhir.
3. HR Recruitment tidak dapat membuat data karyawan baru untuk jabatan yang tidak tersedia tanpa persetujuan OD untuk membuat jabatan tersebut.
4. Pengingat masa percobaan dikirim pada kedua interval yang disebutkan dan tinjauan yang selesai mencapai tahap surat pemberitahuan.

## Ambiguitas sumber di luar himpunan kebutuhan yang dapat dieksekusi

- Menetapkan katalog kolom RTE/SBU yang lengkap dan konfigurasi alur kerja yang tepat.
- Sumber menentukan penerima dan pemicu notifikasi, tetapi tidak menentukan sarana pengiriman, tata kelola templat, perilaku saat pengiriman gagal, atau penanggung jawab akhir yang tidak ambigu untuk distribusi surat masa percobaan.
- Sumber memuat bagian yang tidak terkait bernama `Benefits Submission Field Details`; bagian tersebut sebaiknya tidak dianggap sebagai cakupan Manage Hiring tanpa konfirmasi dari pihak bisnis.
