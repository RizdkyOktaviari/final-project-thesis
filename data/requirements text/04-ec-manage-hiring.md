# Kebutuhan Riset: Pengelolaan Penerimaan Karyawan (EC Manage Hiring)

## Sumber dan ruang lingkup

- Source: `data/raw/BRD - EC Manage Hiring.md`
- Proses: permintaan penerimaan karyawan melalui Request to Employ (RTE), usulan kompensasi melalui Salary Build Up (SBU), pencatatan data karyawan baru, dan evaluasi masa percobaan (probation).
- Aktor: Department Head User sebagai pengaju RTE dan evaluasi probation; OD TM/OD Section sebagai pemeriksa kebutuhan posisi dan anggaran tenaga kerja; HR Recruitment; pemberi persetujuan sesuai tahapan; LM Requester; Senior Manager HCM; HR Compensation & Benefit; IT & System; dan Finance.
- Kedudukan dokumen: narasi kebutuhan turunan untuk analisis riset. Uraian proses berjalan (As-Is), proses yang diharapkan (To-Be), dan keputusan yang belum lengkap tetap dibedakan.

## Skenario kebutuhan

### REQ-HIR-001: Mengajukan kebutuhan penerimaan karyawan

**Rujukan:** Expected New System Business Flow (To-Be), Request to Employ (RTE), langkah 1; Business Rules, Request to Employ (RTE); Functional Requirements, RTE Submission Form; Validation Rules, Request to Employ (RTE) Validation.

**Kebutuhan:** Department Head User harus memeriksa ketersediaan anggaran tenaga kerja yang telah disetujui (approved manning budget) sebelum mengajukan RTE. Jika anggaran belum tersedia, Department Head User mengusulkan anggaran baru kepada departemen terkait sebelum melanjutkan pengajuan. Department Head User kemudian mengirimkan dokumen RTE dan Position Description (PD) dalam format PDF. Sistem harus memeriksa kelengkapan kedua dokumen sebelum pengajuan dikirim dan meneruskan pengajuan yang memenuhi ketentuan kepada OD TM/OD Section untuk ditinjau. Sistem harus memberi notifikasi pengajuan RTE kepada OD TM/OD Section.

### REQ-HIR-002: Meninjau dan menyetujui RTE secara berjenjang

**Rujukan:** Expected New System Business Flow (To-Be), Request to Employ (RTE), langkah 2 sampai 6; Functional Requirements, RTE Review & Approval Workflow; Notification/Notifikasi, RTE Approval Required.

**Kebutuhan:** OD TM/OD Section harus meninjau RTE dan memvalidasi ketersediaan anggaran tenaga kerja. Jika OD menyetujui pengajuan, sistem harus meneruskannya kepada HR Recruitment untuk meninjau persyaratan rekrutmen. Jika HR Recruitment menyetujui pengajuan, sistem harus meneruskannya secara berurutan kepada Senior Manager HCM, Senior Manager Business Unit, Kepala Operasional/Kepala Divisi/Kepala Teknis, Director in Charge, dan Director of HC. Sistem harus menampilkan informasi pengajuan kepada pemberi persetujuan pada tahap yang menjadi kewenangannya. Setelah persetujuan pada suatu tahap diberikan, sistem harus meneruskan pengajuan dan memberi notifikasi kepada pemberi persetujuan berikutnya. Proses RTE selesai setelah Director of HC memberikan persetujuan akhir.

### REQ-HIR-003: Memperbaiki atau menarik RTE yang dikembalikan

**Rujukan:** Expected New System Business Flow (To-Be), Request to Employ (RTE), langkah 2 sampai 6; Validation Rules, Request to Employ (RTE) Validation; Functional Requirements, Execption Handling, Withdraw; Notification/Notifikasi, RTE Send Back.

**Kebutuhan:** Jika pemeriksa atau pemberi persetujuan tidak menyetujui RTE pada tahapnya, sistem harus mengembalikan pengajuan melalui tindakan Send Back dan memberi notifikasi kepada Department Head User. Pengaju harus memperbaiki pengajuan sebelum mengirimkannya kembali. Jika pengaju memilih Submit, pengajuan kembali ke tahap pengiriman dokumen RTE dan PD untuk diproses ulang. Jika pengaju memilih Withdraw, sistem harus mengubah status menjadi `Withdrawn`, memberi notifikasi kepada HR Recruitment, mencatat penarikan pada log aktivitas, dan mengakhiri proses pengajuan tersebut.

### REQ-HIR-004: Menyusun usulan kompensasi SBU

**Rujukan:** Expected New System Business Flow (To-Be), Salary Build Up (SBU), langkah 1; Functional Requirements, SBU Form; Business Rules, SBU Information; Validation Rules, Salary Build Up (SBU) Validation; Notification/Notifikasi, SBU Submission.

**Kebutuhan:** HR Recruitment harus dapat menyusun usulan kompensasi melalui formulir SBU dan menyiapkan alur persetujuannya. Sistem harus menyediakan informasi demografi penerimaan karyawan, grade, pembanding internal, riwayat pekerjaan, gaji sebelumnya, komponen gaji, dan penawaran Perusahaan A sebagaimana dijabarkan pada KON-HIR-001. HR Recruitment dapat menambahkan lebih dari satu pembanding internal dan memasukkan komponen gaji secara manual. Sebelum pengajuan dikirim untuk ditinjau, sistem harus memeriksa kelengkapan informasi usulan rekrutmen yang diwajibkan. Sistem harus meneruskan usulan SBU kepada Senior Manager HCM dan memberikan notifikasi pengajuan kepadanya.

### REQ-HIR-005: Menyetujui SBU dan membuat surat penawaran

**Rujukan:** Expected New System Business Flow (To-Be), Salary Build Up (SBU), langkah 2 sampai 8; Business Rules, Salary Build Up (SBU); Functional Requirements, SBU Review & Approval Workflow; Notification/Notifikasi, SBU Approval Required.

**Kebutuhan:** Sistem harus menampilkan usulan SBU kepada pemberi persetujuan sesuai urutan Senior Manager HCM, Director of HC, Senior Manager Business Unit, Kepala Operasional/Kepala Divisi/Kepala Teknis, dan Director in Charge. Setiap pemberi persetujuan meninjau usulan pada tahap kewenangannya. Sistem hanya boleh meneruskan SBU ke tahap berikutnya setelah tahap yang sedang berjalan memperoleh persetujuan, lalu harus memberi notifikasi kepada pemberi persetujuan berikutnya. Setelah seluruh persetujuan yang diwajibkan selesai, sistem harus memungkinkan HR Recruitment membuat surat penawaran (Offering Letter). Proses SBU selesai setelah surat penawaran dibuat.

### REQ-HIR-006: Memperbaiki atau menarik SBU yang dikembalikan

**Rujukan:** Expected New System Business Flow (To-Be), Salary Build Up (SBU), langkah 2 sampai 9; Validation Rules, Salary Build Up (SBU) Validation; Functional Requirements, Execption Handling, Withdraw; Notification/Notifikasi, SBU Send Back.

**Kebutuhan:** Jika pemberi persetujuan mengembalikan SBU melalui Send Back, sistem harus memberi notifikasi kepada HR Recruitment sebagai pengaju. HR Recruitment harus dapat memperbaiki usulan dan memilih Submit atau Withdraw. Jika HR Recruitment memilih Submit setelah memperbaiki usulan, sistem harus mengembalikannya ke tahap pengajuan SBU dan penyiapan alur persetujuan untuk diproses ulang. Jika HR Recruitment memilih Withdraw, sistem harus mengubah status menjadi `Withdrawn`, memberi notifikasi kepada HR Recruitment, mencatat tindakan tersebut pada log aktivitas, dan mengakhiri proses pengajuan.

### REQ-HIR-007: Menentukan posisi untuk karyawan baru

**Rujukan:** Expected New System Business Flow (To-Be), Input New Employee Data, langkah 1 sampai 6; Business Rules, Position Availability & Manning Budget; Functional Requirements, RTE Submission Form dan RTE Review & Approval Workflow; Validation Rules, Input New Employee Data Validation.

**Kebutuhan:** HR Recruitment harus mencari posisi untuk karyawan baru, dan sistem harus menampilkan informasi posisi yang tersedia agar HR Recruitment dapat memilihnya. Jika posisi tersedia, HR Recruitment memilih posisi tersebut dan dapat melanjutkan pencatatan data karyawan. Jika posisi belum tersedia, HR Recruitment mengajukan permintaan pembuatan posisi kepada OD TM/OD Section. OD harus meninjau permintaan terhadap anggaran tenaga kerja melalui proses manual. Jika permintaan memenuhi ketentuan anggaran, OD membuat posisi baru dan proses kembali kepada HR Recruitment untuk pencatatan data karyawan. Jika permintaan tidak memenuhi ketentuan anggaran, OD menyampaikan kepada HR Recruitment bahwa anggaran tidak tersedia dan proses permintaan posisi berakhir. Sistem harus mendukung penggunaan hasil peninjauan tersebut.

### REQ-HIR-008: Mencatat data awal karyawan baru

**Rujukan:** Expected New System Business Flow (To-Be), Input New Employee Data, langkah 5; Functional Requirements, Employee Data Entry Form dan Employee Data Processing; Supporting Document Upload; Validation Rules, Input New Employee Data Validation.

**Kebutuhan:** Setelah memilih posisi yang tersedia atau posisi baru yang telah dibuat melalui proses yang berlaku, HR Recruitment harus dapat memasukkan status hubungan kerja, data organisasi, informasi pribadi, keluarga, alamat, pendidikan, telepon, National ID, User ID HRIS, dan email karyawan baru. Sistem harus mengaitkan data karyawan dengan posisi yang dipilih dan menyimpan data yang dimasukkan HR Recruitment. Untuk dokumen pendukung pencatatan karyawan baru, sistem harus menerima format PDF atau JPG sesuai ketentuan dan memvalidasi kelengkapan dokumen wajib.

### REQ-HIR-009: Mendukung administrasi lanjutan karyawan baru

**Rujukan:** Functional Requirements, Employee Data Processing dan Data Integration & Dependency, Employee Data Dependency; Current System Business Flow (As-Is), Input New Employee data, langkah 7 sampai 9.

**Kebutuhan:** Sistem harus mendukung pemrosesan data karyawan baru oleh unit yang bertanggung jawab setelah pencatatan oleh HR Recruitment. HR Compensation & Benefit harus dapat memasukkan data kompensasi dan manfaat. IT & System harus dapat menjalankan aktivasi data karyawan baru di Sistem HRIS sesuai alur yang berlaku. Finance harus dapat memasukkan data payroll sesuai ruang lingkup yang ditetapkan.

### REQ-HIR-010: Mengingatkan evaluasi masa percobaan

**Rujukan:** Expected New System Business Flow (To-Be), Probation Evaluation, langkah 1; Business Rules, Probation Evaluation; Notification/Notifikasi, Probation Reminder 30 Days dan Probation Reminder 14 Days.

**Kebutuhan:** Sistem harus memicu notifikasi kepada HR Recruitment pada 30 hari dan 14 hari sebelum masa percobaan karyawan berakhir. HR Recruitment kemudian mengirimkan email kepada Department Head User agar evaluasi masa percobaan dilakukan.

### REQ-HIR-011: Mengajukan dan meninjau evaluasi masa percobaan

**Rujukan:** Expected New System Business Flow (To-Be), Probation Evaluation, langkah 2 sampai 5; Functional Requirements, Probation Evaluation Form dan Probation Evaluation Workflow; Validation Rules, Probation Evaluation Validation; Notification/Notifikasi, Probation Evaluation Submitted dan Probation Review Required.

**Kebutuhan:** Department Head User harus mengisi dan mengirimkan formulir evaluasi masa percobaan melalui aplikasi. Sistem harus meneruskan formulir dan memberi notifikasi kepada HR Recruitment. HR Recruitment harus meninjau formulir, memberikan persetujuan, dan mengatur alur pemeriksa sebelum evaluasi diteruskan. Sistem harus memberi notifikasi kepada pemeriksa berikutnya sesuai alur. LM Requester kemudian meninjau evaluasi dan mengirimkan hasil serta umpan balik sebelum proses diteruskan kepada Senior Manager HCM. Senior Manager HCM harus mengirimkan hasil tinjauan dan umpan balik sebelum HR Recruitment dapat mengompilasi hasil. Jika evaluasi dikembalikan melalui Send Back pada tahap yang berlaku, sistem harus memungkinkan Department Head User memperbaiki dan mengajukannya kembali.

### REQ-HIR-012: Menyelesaikan hasil evaluasi masa percobaan

**Rujukan:** Expected New System Business Flow (To-Be), Probation Evaluation, langkah 6 sampai 8; Business Rules, Probation Evaluation; Functional Requirements, Probation Evaluation Workflow; Notification/Notifikasi, Probation Review Completed.

**Kebutuhan:** Setelah pemeriksa terakhir mengirimkan hasil tinjauan dan umpan balik, sistem harus memberi notifikasi kepada HR Recruitment. HR Recruitment harus dapat menerima dan mengompilasi hasil tinjauan, mengunduh templat notifikasi, dan membuat surat pemberitahuan hasil masa percobaan berdasarkan persetujuan yang berlaku. HR Recruitment kemudian mengirimkan email kepada Department Head User. Department Head User bertanggung jawab mendistribusikan surat pemberitahuan kepada karyawan.

## Ketentuan pendukung

### KON-HIR-001: Isi dan perilaku data pada formulir SBU

**Rujukan:** In Scope, Salary Build Up (SBU); Business Rules, SBU Information; Functional Requirements, SBU Form.

**Ketentuan:** Informasi demografi penerimaan karyawan harus disajikan berdasarkan Division, Department, dan Section. Informasi jenis kelamin harus mencakup kategori Staff dan Non-Staff, sedangkan informasi agama dan jumlah tenaga kerja hanya mencakup Staff. Grade merupakan informasi referensi yang dapat dilihat, tetapi tidak dapat diubah oleh pemberi persetujuan. Internal Comparison harus mendukung lebih dari satu pembanding. Previous Employment harus berupa tabel yang menampung lebih dari satu riwayat perusahaan atau tempat kerja. Gaji dan komponen gaji sebelumnya harus ditampilkan sebelum bagian Penawaran Perusahaan. Penambahan komponen gaji dilakukan secara manual. Employment Status dan Work Roster Cycle pada Penawaran Perusahaan harus tersedia sebagai pilihan daftar.

### KON-HIR-002: Kewenangan persetujuan dan dokumen pendukung

**Rujukan:** In Scope, Approval Workflow; Functional Requirements, Supporting Document Upload; Validation Rules, Approval Workflow Validation.

**Ketentuan:** Pemberi persetujuan hanya boleh meninjau dan mengambil keputusan pada pengajuan yang menjadi tanggung jawabnya. Sistem harus membatasi hak pemberi persetujuan untuk mengubah formulir RTE dan SBU; perbaikan dilakukan melalui Send Back. Pengguna wajib memberikan komentar jika terdapat perubahan formulir selama proses persetujuan. Akses OD TM terhadap status persetujuan dibatasi sampai tingkat kewenangannya. Dokumen RTE dan PD secara khusus harus berformat PDF, sedangkan aturan umum dokumen pendukung RTE dan pencatatan karyawan baru menyebutkan PDF atau JPG. Kelengkapan dokumen wajib harus diperiksa sebelum proses yang membutuhkannya dilanjutkan.

### KON-HIR-003: Ketergantungan data antarmodul

**Rujukan:** In Scope, Integration; Functional Requirements, Data Integration & Dependency.

**Ketentuan:** Position Management harus menjadi sumber informasi posisi yang digunakan dalam proses penerimaan karyawan. Organization Structure menyediakan informasi struktur organisasi untuk tampilan demografi karyawan, sedangkan Employee Central menyediakan data karyawan sebagai pembanding. Pemrosesan kompensasi dan manfaat, aktivasi oleh IT & System, dan pencatatan payroll oleh Finance merupakan tanggung jawab lanjutan sesuai kewenangan masing-masing. BRD belum menetapkan kontrak integrasi teknis lengkap untuk tanggung jawab tersebut.

### KON-HIR-004: Kerahasiaan dan pembatasan akses

**Rujukan:** Security Requirements, Data Confidentiality, Sensitive Data Access, Authentication & Session Security, Document Access & Protection, dan Data Privacy & Retention.

**Ketentuan:** Sistem harus menerapkan akses berdasarkan peran dan kewenangan kerja terhadap informasi pribadi dan hubungan kerja, dokumen RTE dan PD, gaji serta usulan SBU, anggaran tenaga kerja, informasi ketersediaan posisi, hasil evaluasi masa percobaan, umpan balik, dan keputusan serta komentar persetujuan. Pengguna tanpa kewenangan tidak boleh melihat, mengunduh, atau mengubah data dan dokumen tersebut. Akses aplikasi harus menggunakan mekanisme autentikasi yang berlaku pada Employee Central atau platform perusahaan. Penggunaan, penyimpanan, dan penghapusan informasi pribadi dan hubungan kerja harus mengikuti kebijakan privasi dan retensi perusahaan serta mempertahankan catatan yang wajib tersedia untuk audit.

### KON-HIR-005: Jejak audit dan keterkaitan data

**Rujukan:** Security Requirements, Audit Trail dan Data Integrity; Functional Requirements, Execption Handling, Withdraw.

**Ketentuan:** Sistem harus mencatat pengiriman, persetujuan, pengembalian, pengiriman ulang, penarikan, perubahan data pengajuan, tindakan terhadap alur persetujuan, pencatatan dan perubahan data karyawan baru, serta pembuatan posisi baru apabila aktivitas tersebut dilakukan melalui aplikasi. Catatan harus memuat User ID, peran, jenis aktivitas, tanggal dan waktu, ID pengajuan atau referensi terkait, serta data yang berubah apabila relevan. Jejak audit harus hanya dapat dibaca oleh pengguna operasional. Sistem harus mempertahankan keterkaitan keputusan dengan pengajuan, karyawan baru dengan posisi, dan hasil tinjauan dengan evaluasi serta pemeriksanya. Perubahan data tidak boleh menghilangkan riwayat yang diperlukan untuk audit.

### KON-HIR-006: Migrasi riwayat dan konteks proses berjalan

**Rujukan:** In Scope, Data Migration; Current System Business Flow (As-Is), Input New Employee data, langkah 1 sampai 10; Functional Requirements, Employee Data Entry Form dan Employee Data Processing.

**Ketentuan:** Kebutuhan migrasi mencakup riwayat Manage Hiring sejak 2021 sampai data sumber terbaru yang tersedia. Alur As-Is juga mencatat permintaan dan persetujuan akun HRIS, pembuatan email dan pengguna HRIS oleh IT & System, pengisian User ID serta email oleh HR Recruitment, dan pencatatan wajah serta sidik jari oleh karyawan baru. Informasi tersebut harus dipertahankan sebagai konteks proses sumber. Pencatatan biometrik dan pembuatan akun tidak otomatis menjadi fungsi baru Manage Hiring hanya karena muncul pada alur As-Is; fungsi To-Be dan integrasinya harus mengikuti ruang lingkup yang dinyatakan dalam BRD.

## Batas cakupan

Publikasi lowongan, pencarian dan basis data kandidat, seleksi kandidat, psikotes, wawancara, pemeliharaan struktur organisasi atau posisi di luar permintaan posisi baru yang telah dijelaskan, serta penetapan atau pemeliharaan anggaran tenaga kerja berada di luar cakupan modul ini. Pemeliharaan data pribadi karyawan setelah pencatatan awal dilakukan melalui modul terkait.

Perhitungan payroll, pembayaran gaji atau kompensasi, administrasi payroll lanjutan, pengelolaan perjanjian kerja, dan administrasi pra-kerja di luar pencatatan awal tidak termasuk cakupan. Modul ini juga tidak menetapkan kebijakan masa percobaan, kriteria kelulusan, atau keputusan ketenagakerjaan lanjutan seperti perpanjangan masa percobaan, pemutusan hubungan kerja, dan perubahan status di luar alur yang disepakati. Dukungan pencatatan payroll pada REQ-HIR-009 tidak memperluas cakupan menjadi pelaksanaan pembayaran.

## Ambiguitas dan batas interpretasi

- Katalog lengkap data wajib RTE dan SBU serta konfigurasi rinci alur persetujuannya belum ditetapkan. Urutan peran yang tertulis dalam BRD tetap dipertahankan; parameter konfigurasi yang tidak dijelaskan tidak diisi dengan asumsi.
- Business Rules, Notification menyatakan rincian penerima, pemicu lain, dan isi pesan masih perlu dikonfirmasi, sedangkan Notification/Notifikasi menyediakan contoh serta matriks penerima dan pemicu yang konkret. Pemicu yang telah tertulis digunakan dalam skenario; kelengkapan matriks, mekanisme pengiriman teknis, tata kelola templat, dan penanganan kegagalan pengiriman masih perlu dipastikan. Sumber menyebut email, tetapi tidak merinci kontrak teknis pengirimannya.
- Business Rules dan alur As-Is menetapkan Department Head User sebagai distributor surat hasil masa percobaan kepada karyawan, sedangkan To-Be berhenti pada email HR Recruitment kepada Department Head User. Rincian langkah distribusi terakhir dan pembagian tanggung jawab dalam alur operasional akhir perlu ditegaskan sebelum dijadikan perilaku sistem otomatis.
- Peninjauan OD atas permintaan posisi baru ditandai sebagai proses manual pada To-Be, sementara Functional Requirements menyebut dukungan sistem untuk peninjauan. Dukungan sistem tersebut tidak membuktikan bahwa pemeriksaan atau keputusan anggaran dilakukan secara otomatis.
- Bagian Benefits Submission Field Details, Education Claim Form berisi data bantuan pendidikan yang tidak sesuai dengan lingkup Manage Hiring. Isinya tetap berada dalam BRD sumber dan tidak digunakan sebagai kebutuhan modul ini tanpa konfirmasi bisnis.

