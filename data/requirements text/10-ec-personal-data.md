# Kebutuhan Riset: Data Pribadi Pegawai (EC Personal Data)

## Sumber dan ruang lingkup

- Source: `data/raw/BRD - EC Personal Data.md`
- Aktor: pegawai sebagai pemohon, HR Compensation & Benefit sebagai pemeriksa dan pemberi persetujuan, serta administrator HR yang berwenang mengajukan perubahan.
- Cakupan: pengajuan, pemeriksaan, persetujuan, perbaikan, penarikan, riwayat, dan integrasi perubahan data pribadi.
- Unit riset: `REQ-PD` memuat skenario dalam bahasa alami; `KON-PD` memuat ketentuan pendukung. Bagian yang bertentangan dalam sumber tetap memerlukan konfirmasi.

## Skenario kebutuhan

### REQ-PD-001: Mengajukan perubahan data pribadi

**Rujukan:** Expected New System Business Flow > Update Personal Data; Functional Requirements > Personal Data Request > Update Personal Data Request dan Personal Data Form; Validation Rules > Mandatory Field Validation.

**Kebutuhan:** Pegawai membuka bagian Data Pribadi dan memilih jenis informasi yang akan diperbarui. Sistem harus menyediakan formulir sesuai bagian data yang dipilih. Pegawai mengisi perubahan dan mengunggah dokumen pendukung yang dipersyaratkan. Sistem harus memastikan seluruh kolom wajib terisi dan dokumen wajib tersedia sebelum pengajuan diproses. Setelah pegawai mengirimkan pengajuan yang lengkap, sistem harus meneruskannya kepada HR Compensation & Benefit dan mengirimkan notifikasi pengajuan baru. Data yang diajukan masih berupa permohonan sampai memperoleh persetujuan. Hak mengubah bagian yang bertentangan dengan tabel rincian kolom memerlukan konfirmasi pada ambiguitas 1.

### REQ-PD-002: Membatasi pengajuan aktif pada bagian yang sama

**Rujukan:** Functional Requirements > Execption Handling > Multiple Personal Data Section Update; Validation Rules > Personal Data Update Validation.

**Kebutuhan:** Ketika pegawai mengajukan perubahan suatu bagian Data Pribadi, sistem harus memeriksa pengajuan pegawai tersebut pada bagian yang sama. Jika masih terdapat pengajuan berstatus `In Progress`, sistem harus menolak pengajuan baru pada bagian tersebut. Sebagai contoh, pengajuan perubahan alamat yang masih berjalan harus menghalangi pengajuan perubahan alamat berikutnya. Pegawai tetap dapat mengajukan perubahan pada bagian lain yang diperbolehkan apabila bagian itu tidak memiliki pengajuan `In Progress`. Pengajuan pada bagian yang sama dapat dibuat kembali setelah pengajuan sebelumnya berstatus `Approved` atau `Withdrawn`.

### REQ-PD-003: Menyetujui perubahan dan menerapkannya pada tanggal efektif

**Rujukan:** Expected New System Business Flow > Update Personal Data; Business Rules > Approval; Functional Requirements > Personal Data Request > Approval > Approve; Notification/Notifikasi > Personal Data Update Completed.

**Kebutuhan:** HR Compensation & Benefit memeriksa perubahan dan dokumen pendukung serta memverifikasi kelengkapan dan kesesuaiannya. Jika persyaratan terpenuhi, HR Compensation & Benefit dapat menyetujui pengajuan dengan komentar opsional. Sistem harus menyelesaikan alur persetujuan, menyimpan riwayat perubahan, dan memberi tahu pegawai bahwa pengajuan telah disetujui. Sistem hanya boleh menerapkan perubahan sebagai data resmi setelah pengajuan berstatus `Approved` dan tanggal efektifnya berlaku. Ketidaksesuaian antara waktu penerapan ini dan redaksi notifikasi selesai dijelaskan pada ambiguitas 5.

### REQ-PD-004: Mengembalikan pengajuan untuk diperbaiki dan diajukan ulang

**Rujukan:** Business Rules > Send Back & Resubmission; Functional Requirements > Personal Data Request > Approval > Send Back dan Edit Personal Data Request; Validation Rules > Send Back Validation; Notification/Notifikasi > Personal Data Update Resubmitted.

**Kebutuhan:** Jika HR Compensation & Benefit memerlukan perbaikan data atau dokumen, HR Compensation & Benefit mengembalikan pengajuan melalui tindakan `Send Back`. Sistem harus mewajibkan komentar sebelum menerima tindakan tersebut dan menyampaikan pengembalian beserta komentar kepada pegawai. Pegawai dapat memperbaiki pengajuan sesuai catatan HR dan mengirimkannya kembali. Sistem harus mencatat perubahan dan pengajuan ulang dalam catatan aktivitas, memberi tahu HR Compensation & Benefit, serta memulai kembali proses persetujuan dari awal.

### REQ-PD-005: Menarik pengajuan yang dikembalikan

**Rujukan:** Business Rules > Withdrawal; Functional Requirements > Personal Data Request > Withdraw Personal Data Request dan Execption Handling > Withdraw; Validation Rules > Withdraw Validation.

**Kebutuhan:** Pegawai dapat menarik pengajuan yang berstatus `Sent Back`. Ketika pegawai melakukan tindakan `Withdraw` pada pengajuan tersebut, sistem harus mengubah statusnya menjadi `Withdrawn`, menghentikan proses persetujuan, mencatat tindakan dalam catatan aktivitas, dan memberi tahu HR Compensation & Benefit. Sistem tidak boleh memproses kembali pengajuan yang sudah ditarik. Pengajuan dengan status selain `Sent Back` tidak memenuhi ketentuan penarikan. Penyelarasan istilah tindakan dan status pada skenario ini dijelaskan dalam ambiguitas 6.

### REQ-PD-006: Menentukan kelayakan tanggungan saat pemeriksaan

**Rujukan:** Business Rules > Dependents; Functional Requirements > Personal Data Request > Personal Data Form > HR Compensation & Benefit; Personal Data Field Details > Dependants.

**Kebutuhan:** Pegawai mengajukan perubahan data tanggungan beserta dokumen yang dipersyaratkan. Saat memeriksa pengajuan, HR Compensation & Benefit dapat menetapkan kelayakan tanggungan sebagai `Eligible` atau `Not Eligible`. Sistem harus membatasi perubahan status kelayakan kepada HR pada tahap pemeriksaan atau persetujuan; pegawai tidak boleh menetapkannya sendiri. Sistem harus membatasi jumlah tanggungan pegawai paling banyak tiga orang. Lampiran tanggungan harus tetap dibedakan dari lampiran milik pegawai.

### REQ-PD-007: Mengajukan perubahan rekening bank

**Rujukan:** Business Rules > Payment Information; Validation Rules > Payment Information Change Validation; Personal Data Field Details > Payment Informations.

**Kebutuhan:** Pegawai dapat memiliki lebih dari satu rekening dan mengajukan perubahan rekening melalui informasi pembayaran. Sistem harus membatasi pengajuan perubahan rekening bank paling banyak satu kali dalam satu tahun untuk pegawai yang sama. Jika batas tersebut telah terpakai, sistem harus menolak pengajuan perubahan berikutnya. Pengajuan yang diperbolehkan tetap harus melalui pemeriksaan dan persetujuan HR Compensation & Benefit sebelum berlaku sebagai data resmi. Cakupan pembatasan terhadap rekening penggajian dan asuransi serta definisi periode tahun memerlukan konfirmasi pada ambiguitas 3.

### REQ-PD-008: Melampirkan dokumen pendukung pengajuan

**Rujukan:** Business Rules > Supporting Document; Functional Requirements > Attachment; Validation Rules > Personal Data Update Validation; Security Requirements > Attachment Security.

**Kebutuhan:** Pegawai mengunggah dokumen pendukung sesuai jenis perubahan, misalnya buku nikah atau kartu keluarga untuk perubahan status pernikahan dan kartu keluarga untuk perubahan data anak. Sistem harus menerapkan format berkas sesuai konfigurasi dan membatasi ukuran berkas sesuai batas yang ditentukan. Sistem tidak boleh memproses pengajuan tanpa dokumen wajib. Sistem harus menyimpan dokumen sebagai bagian dari pengajuan terkait. Setelah pengajuan memasuki proses persetujuan, pegawai tidak boleh mengubah atau menghapus dokumen yang tersimpan kecuali melalui mekanisme perubahan yang disediakan sistem. Format dan batas ukuran yang belum lengkap dicatat pada ambiguitas 2.

### REQ-PD-009: Melihat status dan riwayat perubahan

**Rujukan:** WHO > HR Admin dan Requestor; Functional Requirements > Personal Data History dan Monitoring; Security Requirements > Personal Data Access dan Data Change History.

**Kebutuhan:** Pegawai dapat melihat status, posisi proses, dan riwayat pengajuan miliknya. HR Compensation & Benefit dapat melihat pengajuan, dokumen, dan riwayat dalam kewenangannya. Sistem harus menyediakan riwayat yang memuat data setelah perubahan, pegawai, pemberi persetujuan, tanggal pengajuan, tanggal persetujuan, dan status pengajuan. Untuk perubahan yang disetujui, sistem harus menyimpan bagian data, kolom yang berubah, nilai sebelumnya, nilai baru, pelaku perubahan, waktu perubahan, dan ID pengajuan. Sistem harus membatasi akses riwayat sesuai kewenangan pengguna.

### REQ-PD-010: Meneruskan perubahan yang disetujui ke modul terkait

**Rujukan:** WHAT > In Scope > Integration; Functional Requirements > Integration Trigger; Business Rules > Approval.

**Kebutuhan:** Setelah seluruh proses persetujuan selesai, sistem harus memicu pembaruan pada modul terkait sesuai jenis perubahan yang disetujui. Perubahan dapat berkaitan dengan Organization Structure, Position Management, Payroll & Compensation, atau Benefit Reimbursement. Informasi pembayaran yang disetujui menjadi dasar pembaruan administrasi penggajian, sedangkan perubahan status pernikahan dan tanggungan yang disetujui menjadi dasar pembaruan administrasi manfaat. Sistem tidak boleh meneruskan perubahan yang belum memperoleh persetujuan akhir sebagai pembaruan resmi. Penerapan data pribadi tetap tunduk pada tanggal efektif dalam REQ-PD-003; jadwal teknis sinkronisasi belum dirinci sebagaimana ambiguitas 7.

### REQ-PD-011: Mengingatkan HR atas pengajuan yang belum diproses

**Rujukan:** WHAT > In Scope > Notification & Reminder; Notification/Notifikasi > Personal Data Update Approval Reminder dan Notification Matrix.

**Kebutuhan:** Jika pengajuan masih menunggu pemeriksaan dan pemberi persetujuan belum melakukan tindakan dalam periode pengingat yang dikonfigurasi, sistem harus mengirimkan pengingat kepada HR Compensation & Benefit. Notifikasi harus mengacu pada pengajuan yang masih memerlukan pemeriksaan. BRD tidak menentukan nilai tetap untuk periode pengingat, sehingga skenario ini mengikuti konfigurasi yang disepakati.

### REQ-PD-012: Membatasi akses data pribadi dan dokumen

**Rujukan:** Business Rules > Personal Data Change; Security Requirements > Personal Data Access, Document Access, dan Attachment Security.

**Kebutuhan:** Ketika pegawai mengakses data pribadi, pengajuan, riwayat, atau dokumen pendukung, sistem harus membatasi akses pegawai pada data dan pengajuannya sendiri. Ketika HR Compensation & Benefit melakukan pemeriksaan, sistem harus menyediakan data dan dokumen sesuai tanggung jawabnya. Sistem harus menolak pengguna tanpa kewenangan yang mencoba membaca atau mengubah data pribadi maupun mengakses dokumen pendukung. Administrator HR yang berwenang dapat mengajukan perubahan sesuai aturan bisnis sumber; kewenangan ini tidak memperluas hak layanan mandiri pegawai ke data orang lain.

## Ketentuan pendukung

### KON-PD-001: Daftar bagian data dalam cakupan BRD

**Rujukan:** WHAT > In Scope > Pengajuan Perubahan Data Personal; Functional Requirements > Personal Data Request > Update Personal Data Request.

**Ketentuan:** BRD mencantumkan informasi pribadi, biografi, alamat, kontak, identitas nasional, kontak darurat utama, tanggungan, pembayaran, posisi dan organisasi, rincian pekerjaan, hubungan pekerjaan, rincian kepegawaian, dokumen pribadi, kompensasi, komponen pembayaran tidak berulang, informasi waktu kerja, informasi dasar, informasi rinci, pendidikan, penghargaan, pengalaman kerja internal, pekerjaan sebelumnya, kursus, sertifikasi, keanggotaan profesional, dan kegiatan sukarela. Pencantuman suatu bagian belum memastikan seluruh kolomnya boleh diubah oleh pegawai karena tabel rincian memuat pembatasan yang bertentangan dengan daftar umum. Katalog kolom lengkap tetap dirujuk ke BRD; pertentangannya dicatat pada ambiguitas 1.

### KON-PD-002: Informasi pribadi dan biografi

**Rujukan:** Personal Data Field Details > Personal Information dan Biographical Information.

**Ketentuan:** Informasi pribadi memuat tanggal efektif, nama depan, tengah, dan belakang, sapaan, nama lengkap, agama, jenis kelamin, status pernikahan, tanggal mulai status pernikahan, kewarganegaraan, preferensi lokal, dan lampiran kartu keluarga. Sistem harus mengisi nama lengkap dari nama depan, tengah, dan belakang serta menjadikannya hanya dapat dibaca. Tanggal efektif, nama depan, sapaan, nama lengkap, agama, jenis kelamin, dan status pernikahan ditandai wajib. Lampiran kartu keluarga bersifat opsional pada tabel ini; kewajiban dokumen untuk jenis perubahan tertentu tetap mengikuti REQ-PD-008. Informasi biografi memuat tempat dan tanggal lahir yang wajib serta tanggal kematian yang opsional.

### KON-PD-003: Alamat dan informasi kontak

**Rujukan:** Personal Data Field Details > Addresses dan Contact Information.

**Ketentuan:** Alamat menggunakan jenis alamat rumah dan memuat alamat lengkap, RT/RW, negara, provinsi, kota, kecamatan, kelurahan atau desa, kode pos, dan penanda alamat utama. Nilai wilayah merujuk data geografis. Alamat, negara, provinsi, kota, kode pos, jenis alamat, dan penanda utama ditandai wajib. Informasi telepon memuat jenis pribadi atau kantor, nomor lengkap, dan penanda utama; jenis dan nomor wajib diisi. Informasi surel mencakup jenis pribadi atau kantor, alamat surel, dan penanda utama, tetapi tabel menandainya hanya dapat dibaca oleh pegawai. Hak edit yang berbeda dengan daftar umum tetap tercakup dalam ambiguitas 1.

### KON-PD-004: Identitas nasional

**Rujukan:** Business Rules > National ID; Personal Data Field Details > National ID Information.

**Ketentuan:** Pegawai dapat memiliki lebih dari satu identitas nasional. Jenis identitas harus mencakup KTP dan paspor. Setiap entri memuat jenis, negara, nomor identitas, penanda utama, dan lampiran opsional; seluruh kolom selain lampiran ditandai wajib. BRD mewajibkan KTP dan menyebutkan bahwa pegawai ekspatriat mengisi nomor paspor pada bagian KTP. Pemetaan ini tetap memerlukan konfirmasi pada ambiguitas 4 agar jenis identitas tidak disimpulkan secara sepihak.

### KON-PD-005: Kontak darurat dan tanggungan

**Rujukan:** Business Rules > Emergency Contact dan Dependents; Personal Data Field Details > Emergency Contact dan Dependants.

**Ketentuan:** Pegawai dapat memiliki paling banyak dua kontak darurat dan tiga tanggungan. Kontak darurat memuat nama, hubungan, dan nomor telepon yang wajib, serta nomor alternatif, jenis kelamin, tanggal lahir, surel, dan penanda utama yang opsional. Data utama tanggungan memuat tanggal efektif, nama depan dan belakang, hubungan, serta tanggal lahir yang wajib; nama tengah dan beberapa lampiran bersifat opsional. Rincian tanggungan meliputi hubungan keluarga, informasi pribadi dan biografi, identitas nasional, alamat, serta beberapa lampiran. Sistem harus mempertahankan kaitan lampiran dengan tanggungan terkait. Status kelayakan hanya boleh diubah oleh HR saat pemeriksaan atau persetujuan sebagaimana REQ-PD-006.

### KON-PD-006: Rincian informasi pembayaran

**Rujukan:** Business Rules > Payment Information; Personal Data Field Details > Payment Informations > Payroll dan Insurance.

**Ketentuan:** Informasi pembayaran memuat tanggal mulai efektif yang wajib dan tanggal akhir efektif yang dinonaktifkan untuk pengisian. Data penggajian memuat jenis pembayaran, metode pembayaran, mata uang, negara bank, pemilik rekening, dan nomor rekening; metode pembayaran ditandai wajib. Data asuransi juga memuat jenis serta klasifikasi atau kelompok asuransi di samping informasi bank dan pembayaran. Secara bawaan, rekening asuransi sama dengan rekening penggajian. Sistem mendukung lebih dari satu rekening; ketentuan frekuensi perubahan mengikuti REQ-PD-007.

### KON-PD-007: Kolom yang dibatasi untuk perubahan oleh pegawai

**Rujukan:** Personal Data Field Details > Contact Information > Email Information, Position Information, Organisational Information, Job Details, Time Information, Job Relationships, Compensations, dan Pay Targets; Business Rules > Time Management.

**Ketentuan:** Tabel rincian menandai surel, posisi, organisasi, rincian pekerjaan, informasi waktu kerja, hubungan pekerjaan, dan seluruh kolom Pay Targets sebagai hanya dapat dibaca. Pada kompensasi, Amount ditandai dapat diubah, sedangkan Pay Component, Frequency, dan Percentage hanya dapat dibaca. Informasi waktu kerja menampilkan jenis roster dan jadwal kerja yang mengikuti jam kerja dalam kontrak pegawai. Penggunaan tabel rinci sebagai batas hak edit merupakan interpretasi penjabaran sebelumnya; interpretasi ini belum menyelesaikan pertentangannya dengan daftar bagian yang dapat diajukan pada KON-PD-001 dan harus dikonfirmasi sebelum menjadi acuan evaluasi sebagaimana ambiguitas 1.

### KON-PD-008: Dokumen pribadi dan latar belakang pegawai

**Rujukan:** Personal Data Field Details > Personal Documents, Education, Honors / Awards, Work Exprience Within Company, Previous Employment, Courses, Certifications, Professional Memberships, dan Volunteer Involvement.

**Ketentuan:** Dokumen pribadi memuat negara atau wilayah, jenis, judul, nomor dokumen, tanggal dan tempat terbit, instansi penerbit, tanggal kedaluwarsa, serta lampiran; tanggal terbit ditandai wajib. Bagian latar belakang meliputi pendidikan, penghargaan, pengalaman kerja internal, pekerjaan sebelumnya, kursus, sertifikasi, keanggotaan profesional, dan kegiatan sukarela. Pendidikan mewajibkan sekolah, jurusan, gelar, dan bukti kelulusan; penghargaan mewajibkan nama penghargaan. Pengalaman kerja internal mewajibkan tanggal mulai dan jabatan; pekerjaan sebelumnya juga mewajibkan tanggal berakhir dan nama perusahaan. Kursus mewajibkan nama, durasi, dan tanggal selesai. Sertifikasi mewajibkan nama sertifikasi atau lisensi; keanggotaan profesional mewajibkan organisasi, dan kegiatan sukarela mewajibkan nama komunitas atau organisasi. Rincian kolom lainnya mengikuti katalog BRD.

### KON-PD-009: Kerahasiaan data

**Rujukan:** Security Requirements > Data Confidentiality, Document Access, dan Attachment Security.

**Ketentuan:** Sistem harus memperlakukan identitas nasional, tanggal lahir, alamat, kontak pribadi, kontak darurat, informasi pembayaran, data tanggungan, jenjang pegawai, dan gaji pokok sebagai data rahasia. Daftar BRD tidak membatasi kemungkinan adanya data rahasia lain. Akses harus mengikuti pengendalian berdasarkan peran atau RBAC. Dokumen pendukung juga bersifat rahasia dan tetap terkait dengan pengajuan. Pembatasan akses operasional mengikuti REQ-PD-012.

### KON-PD-010: Catatan aktivitas dan jejak audit

**Rujukan:** Business Rules > History & Audit Trail; Functional Requirements > Monitoring > Activity Log; Security Requirements > Audit Trail dan Data Change History.

**Ketentuan:** Sistem harus mencatat pengajuan, persetujuan, pengeditan, pengembalian, pengajuan ulang, penarikan, perubahan data, dan komentar pemeriksaan. Setiap aktivitas audit harus memuat pengguna, peran, kegiatan, tanggal dan waktu, serta ID pengajuan. Jejak audit hanya dapat dibaca dan tidak boleh diubah atau dihapus oleh pengguna. Riwayat perubahan memuat bagian data, kolom yang berubah, nilai lama dan baru, pelaku, waktu perubahan, dan ID pengajuan. Riwayat tidak boleh dihapus melalui proses pengajuan.

### KON-PD-011: Migrasi riwayat

**Rujukan:** WHAT > In Scope > Data Migration.

**Ketentuan:** Migrasi mencakup riwayat Data Pribadi dari tahun 2021 sampai catatan terbaru yang tersedia pada sumber. Ketentuan migrasi ini tidak dengan sendirinya menentukan urutan pesan untuk skenario perubahan data sehari-hari.

## Batas cakupan

Modul ini tidak menjalankan pengunduran diri, pemberhentian, pemutusan hubungan kerja, atau penyelesaian kewajiban keluar pegawai. Perhitungan gaji, bonus, tunjangan, dan pajak; perekrutan; evaluasi kinerja, sasaran, dan talenta; pembuatan struktur organisasi atau posisi; penghapusan posisi; serta transaksi Employee Status Change berada di luar cakupannya. Transaksi ESC mencakup promosi, mutasi, demosi, reklasifikasi, perpanjangan kontrak, serta perubahan jam atau jadwal kerja. Modul terkait dapat menggunakan data yang telah disetujui tanpa memindahkan proses bisnisnya ke modul Data Pribadi.

## Ambiguitas dan batas interpretasi

1. Daftar bagian yang dapat diajukan bertentangan dengan tabel rincian yang menandai sejumlah kolom hanya dapat dibaca. KON-PD-001 dan KON-PD-007 mempertahankan kedua bukti. Pihak bisnis perlu memastikan hak edit per kolom; penjabaran ini tidak menetapkan sendiri bagian mana yang akhirnya boleh diubah.
2. Format lampiran untuk setiap bagian dan batas ukuran yang dikonfigurasi belum dinyatakan lengkap. Tabel tertentu menyebut JPG/PDF atau PDF, sedangkan Attachment menyerahkannya kepada konfigurasi. REQ-PD-008 tidak menetapkan nilai atau daftar format tambahan.
3. BRD belum menjelaskan apakah batas satu perubahan rekening per tahun mencakup seluruh rekening, rekening penggajian, rekening asuransi, atau gabungannya; batas periode tahun juga belum dirinci. Parameter ini diperlukan sebelum menilai kasus batas REQ-PD-007.
4. Kewajiban KTP, dukungan paspor, dan arahan mengisi nomor paspor ekspatriat pada bagian KTP perlu dikonfirmasi sebagai aturan identitas yang konsisten. KON-PD-004 mempertahankan ketiganya.
5. Aturan persetujuan mewajibkan tercapainya tanggal efektif sebelum data berubah. Templat notifikasi selesai menyatakan data terbaru sudah tersedia setelah persetujuan selesai. Penerapan dan redaksi notifikasi untuk tanggal efektif di masa depan belum dijelaskan; REQ-PD-003 tidak menganggap keduanya selalu terjadi bersamaan.
6. Nama status penarikan ditulis `Withdraw` dalam satu bagian dan `Withdrawn` pada bagian penanganan pengecualian serta validasi. REQ-PD-005 memakai `Withdraw` untuk tindakan dan `Withdrawn` untuk status agar narasi konsisten; pemetaan nilai status implementasi tetap perlu diperiksa terhadap sumber yang disepakati.
7. BRD menyebut pembaruan modul terkait setelah persetujuan akhir, tetapi tidak merinci jadwal sinkronisasi, kegagalan integrasi, atau pengulangan pengiriman. REQ-PD-010 tidak menambahkan perilaku tersebut.

Skenario dan ketentuan di atas merupakan normalisasi bahasa dan struktur dokumen sumber. Satu ID skenario dapat memuat beberapa pernyataan perilaku; ID tersebut bukan label kebenaran atau satu kebutuhan atomik yang telah divalidasi. Gunakan dokumen sumber dan keputusan penelaah untuk menetapkan acuan penilaian konsistensi.

