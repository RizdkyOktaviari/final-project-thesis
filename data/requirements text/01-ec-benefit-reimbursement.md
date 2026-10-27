# Kebutuhan Riset: Penggantian Biaya Manfaat Karyawan (EC Benefit Reimbursement)

## Sumber dan ruang lingkup

- Source: `data/raw/BRD - EC Benefit Reimbursement.md`
- Cakupan: pengajuan bantuan manfaat karyawan, khususnya bantuan pendidikan (Education Assistance), beserta pemeriksaan kelayakan, persetujuan, riwayat, dan data untuk administrasi pembayaran.
- Aktor: pegawai, HR Compensation & Benefit, dan Super Admin sesuai kewenangannya. Employee Central menyediakan data pegawai dan tanggungan; pelaksanaan pembayaran berada pada proses terkait di luar modul ini.

## Skenario kebutuhan

### REQ-BR-001: Menyiapkan pengajuan bantuan pendidikan

**Rujukan:** Functional Requirements / Benefit Submission / Benefit Submission Form, Education Assistance Details, dan Dependent Data Auto-Fill.

**Kebutuhan:** Pegawai harus dapat menyiapkan pengajuan bantuan pendidikan melalui formulir Benefit Assistance. Sistem harus menampilkan tanggal klaim, jenis manfaat, mata uang, dan nilai hak manfaat. Sistem harus menampilkan tanggungan yang memenuhi syarat berdasarkan data Employee Central. Setelah pegawai memilih tanggungan, sistem harus mengisi data tanggungan yang tersedia dari Employee Central ke dalam formulir. Pegawai harus dapat melengkapi data tambahan pada kolom yang dapat diedit dan menambahkan rincian pendidikan untuk paling banyak tiga tanggungan yang memenuhi syarat.

### REQ-BR-002: Menghitung nilai bantuan pendidikan

**Rujukan:** Business Rules / Benefit Eligibility & Calculation; Functional Requirements / Benefit Eligibility & Calculation / Benefit Calculation; Integration / Employee Central Data Integration.

**Kebutuhan:** Sistem harus menggunakan kategori manfaat, tingkat pendidikan, jumlah tanggungan yang memenuhi syarat, dan plafon pada periode terkait untuk menghitung nilai bantuan pendidikan. Untuk pegawai baru dan pegawai kontrak, sistem harus menghitung nilai secara prorata berdasarkan tanggal mulai bekerja (Date of Hire) dari Employee Central dan tanggal batas akhir pengajuan. Sistem harus menampilkan hasil perhitungan sebagai nilai hak manfaat yang tidak dapat diubah oleh pegawai. Rumus dan nilai plafon harus mengikuti kebijakan yang berlaku; dokumen ini tidak menetapkan nilai pengganti untuk kebijakan tersebut.

### REQ-BR-003: Memeriksa kelayakan dan riwayat klaim

**Rujukan:** Business Rules / Dependent & Duplicate Claim, Education Assistance Claim Frequency, dan Duplicate Claim; Functional Requirements / Benefit Eligibility Validation, Duplicate Claim Validation, dan Education Assistance Claim Frequency; Validation Rules / Submission Validation.

**Kebutuhan:** Sebelum pengajuan, sistem harus memeriksa kelayakan pegawai, kelayakan serta usia tanggungan, kesesuaian hubungan satu banding satu antara data tanggungan dan rincian klaim, riwayat klaim, frekuensi pengajuan, dan sisa plafon. Sistem harus menolak penggunaan tanggungan yang berusia lebih dari 23 tahun, klaim untuk tanggungan yang sama oleh lebih dari satu pegawai dalam periode yang sama, serta klaim berulang pegawai tetap untuk tanggungan dan periode yang sama. Sistem harus membatasi klaim PAUD menjadi satu kali dan klaim TK menjadi dua kali per tanggungan, serta mengizinkan klaim SD sampai perguruan tinggi selama plafon masih tersedia. Apabila batas frekuensi atau plafon telah tercapai, sistem harus menolak pengajuan. BRD mengizinkan pengajuan berulang pegawai kontrak selama plafon tersisa; hubungan pengecualian ini dengan larangan pengajuan yang masih aktif belum ditetapkan dan dicatat pada bagian ambiguitas.

### REQ-BR-004: Memeriksa periode pengajuan

**Rujukan:** Business Rules / Benefit Period & Cut-off; Functional Requirements / Benefit Period & Cut-off; Execption Handling / Submission Period Validation.

**Kebutuhan:** Sistem harus menampilkan periode manfaat atau tahun ajaran yang berlaku dan memeriksa tanggal pengajuan terhadap periode tersebut. Pengajuan normal oleh pegawai harus tersedia mulai 1 Juli sampai 15 Juni tahun berikutnya. Jika pegawai mengajukan pada 16 sampai 30 Juni, sistem harus menolak pengajuan dan menampilkan informasi bahwa periode pengajuan ditutup. Sistem harus memvalidasi batas akhir setiap periode dan memberikan peringatan setelah batas tersebut. BRD menetapkan penguncian tahun ajaran pada 15 Juni dan juga menyebut peringatan mendekati batas akhir; jarak waktu untuk peringatan tersebut harus mengikuti ketentuan perusahaan yang belum dirinci dalam sumber.

### REQ-BR-005: Melampirkan dokumen pendukung

**Rujukan:** Requirement Identification / In Scope / Supporting Document; Functional Requirements / Supporting Document / Supporting Document Upload; Validation Rules / Benefits Reimbursement Validation dan Mandatory Field Validation.

**Kebutuhan:** Pegawai harus dapat melampirkan dokumen pendukung yang sesuai dengan bantuan yang diajukan. Sistem harus memeriksa kelengkapan dokumen wajib dan membatasi ukuran setiap dokumen paling banyak 10 MB. Sistem harus menyimpan dokumen sebagai bagian dari pengajuan dan tidak boleh memproses pengajuan apabila dokumen wajib belum tersedia. Aturan umum sumber menerima PDF atau JPG, sedangkan kolom Attachment pada Education Claim Form menyebut PDF; format yang digunakan sebagai kriteria penerimaan final harus menunggu penyelesaian konflik sumber tersebut.

### REQ-BR-006: Mengajukan dan menyetujui klaim

**Rujukan:** Business Rules / Benefit Submission, Approval, dan Integrity; Functional Requirements / Approval Workflow / Benefit Review dan Approve / Send Back; Notification / Submission Notification dan Status Notification.

**Kebutuhan:** Pada pengajuan normal, pegawai harus mengajukan klaim miliknya sendiri dengan data dan dokumen wajib yang lengkap. Sistem harus meneruskan pengajuan kepada HR Compensation & Benefit dan mengirimkan notifikasi pengajuan baru. HR Compensation & Benefit harus dapat melihat data serta dokumen pendukung dan memverifikasi kesesuaiannya sebelum memberikan keputusan. Jika HR Compensation & Benefit menyetujui klaim, sistem harus mencatat persetujuan, memberitahukan hasil kepada pegawai, dan menyediakan data yang disetujui sebagai dasar administrasi pembayaran.

### REQ-BR-007: Mengembalikan dan mengajukan ulang klaim

**Rujukan:** Business Rules / Approval; Functional Requirements / Approval Workflow / Approve / Send Back; Notification / Status Notification; Validation Rules / Send Back Validation.

**Kebutuhan:** Jika klaim memerlukan perbaikan, HR Compensation & Benefit harus dapat mengembalikan klaim kepada pegawai melalui Send Back dengan komentar wajib. Sistem harus mencegah Send Back tanpa komentar dan harus menyertakan komentar peninjau pada notifikasi kepada pegawai. Pegawai harus dapat memperbaiki pengajuan yang dikembalikan dan mengajukannya ulang untuk menjalani proses pemeriksaan dan persetujuan yang berlaku.

### REQ-BR-008: Mengajukan klaim dengan tanggal mundur

**Rujukan:** Expected New System Business Flow / Benefits Submission; Business Rules / Benefit Submission dan Approval; Functional Requirements / Super Admin Backdate Submission.

**Kebutuhan:** Dalam kasus pengajuan dengan tanggal mundur yang diizinkan, Super Admin harus dapat membuat pengajuan atas nama pegawai dan menentukan tanggal pengajuan sesuai kewenangannya. Sistem harus mencatat Super Admin sebagai pembuat, pegawai sebagai pemilik pengajuan, tanggal pembuatan aktual, dan tanggal pengajuan. Pengajuan tersebut harus tetap mengikuti pemeriksaan dan persetujuan yang berlaku, kecuali perusahaan telah menyetujui ketentuan khusus. Dokumen ini tidak menetapkan pengecualian persetujuan baru.

### REQ-BR-009: Menarik pengajuan

**Rujukan:** Business Rules / Withdrawal; Execption Handling / Withdraw; Validation Rules / Withdraw Validation.

**Kebutuhan:** Ketika pegawai melakukan penarikan pengajuan (Withdraw) yang diizinkan, sistem harus mengubah statusnya menjadi Withdrawn, mengirimkan notifikasi kepada HR Compensation & Benefit, dan mencatat tindakan tersebut pada log aktivitas. Sistem tidak boleh memproses kembali pengajuan yang telah berstatus Withdrawn. Aturan bisnis dan tabel validasi membatasi penarikan pada pengajuan yang dikembalikan (Sent Back), sedangkan uraian penanganan pengecualian menyebut penarikan secara umum. Skenario ini menetapkan akibat penarikan; cakupan status yang mengizinkan tindakan tersebut tetap memerlukan konfirmasi.

### REQ-BR-010: Membatalkan klaim yang telah disetujui

**Rujukan:** Functional Requirements / Approval Workflow / Approved Benefit Cancellation; Notification / Status Notification.

**Kebutuhan:** Super Admin harus dapat membatalkan klaim yang telah disetujui sesuai kewenangannya. Sistem harus mencatat status pembatalan dan identitas pengguna yang membatalkan. Sistem harus mengirimkan notifikasi pembatalan kepada pegawai serta menampilkan komentar pada notifikasi tersebut.

### REQ-BR-011: Menelusuri riwayat dan mengekspor data klaim

**Rujukan:** Functional Requirements / Submission History & Tracking; Reporting & Data Export / Benefit Data Export; Supporting Document / Education Assistance Form.

**Kebutuhan:** Pegawai harus dapat melihat status dan riwayat pengajuan miliknya. HR Compensation & Benefit harus dapat melihat riwayat pengajuan yang menjadi kewenangannya dan mengunduh formulir Education Assistance. Sistem harus menyediakan ekspor data klaim dalam format Excel yang memuat informasi klaim, pegawai, jenis manfaat, periode, nilai manfaat, dan status. Data klaim yang telah disetujui harus tersedia untuk kompilasi dan administrasi pembayaran oleh HR Compensation & Benefit sesuai proses yang berlaku.

### REQ-BR-012: Mengingatkan peninjau klaim yang tertunda

**Rujukan:** Notification/Notifikasi / 5. Benefit Submission Approval Reminder dan Notification Matrix.

**Kebutuhan:** Ketika pengajuan masih menunggu persetujuan dan peninjau belum bertindak dalam periode pengingat yang dikonfigurasikan, sistem harus mengirimkan pengingat kepada HR Compensation & Benefit sebagai pihak yang harus menindaklanjutinya. Sumber tidak menetapkan nilai interval pengingat; interval tidak boleh diasumsikan sama dengan interval pengingat modul lain.

## Ketentuan pendukung

### KON-BR-001: Kolom formulir bantuan pendidikan

**Rujukan:** Functional Requirements / Benefits Submission Field Details / Education Claim Form.

**Ketentuan:** Formulir harus memuat tanggal klaim, pilihan manfaat, mata uang, nilai hak manfaat, nama siswa, nomor identitas siswa, usia, tanggal lahir, tingkat sekolah, kelas, tahun pendidikan, jenis kelamin siswa, nama sekolah, alamat sekolah, lampiran, dan keterangan. Mata uang, nilai hak manfaat, nama siswa, usia, tanggal lahir, tahun pendidikan, serta jenis kelamin siswa ditandai tidak dapat diedit. Pegawai dapat mengisi tanggal klaim, pilihan manfaat, nomor identitas siswa, tingkat sekolah, kelas, alamat sekolah, lampiran, dan keterangan pada kolom yang dapat diedit. Tanggal lahir, jenis kelamin, kelas, alamat sekolah, dan keterangan bersifat opsional; kolom lainnya wajib menurut tabel. Nama sekolah wajib tetapi ditandai tidak dapat diedit pada tabel sumber; perbedaan dengan penjabaran terdahulu dicatat pada bagian ambiguitas.

### KON-BR-002: Kebijakan bantuan dan hubungan data

**Rujukan:** Requirement Identification / In Scope / Benefit Eligibility & Calculation dan Benefit Period & Cut-off; Business Rules / Benefit Eligibility & Calculation serta Dependent & Duplicate Claim.

**Ketentuan:** Data pegawai, tanggungan, dan tanggal mulai bekerja harus berasal dari Employee Central. Jika suami dan istri sama-sama pegawai, hanya salah satu pegawai yang dapat menggunakan tanggungan yang sama untuk klaim dalam periode yang sama sesuai status tanggungan. Periode manfaat dapat mencakup tahun berjalan atau tahun berikutnya sesuai ketentuan. Bantuan yang telah diterima tidak harus dikembalikan hanya karena pegawai kemudian mengundurkan diri. Sumber juga mencakup kebutuhan konfigurasi kategori bantuan berdasarkan tingkat jabatan untuk kebijakan mendatang, sedangkan penetapan dan pemeliharaan kebijakan manfaat berada di luar modul ini.

### KON-BR-003: Akses dan kerahasiaan

**Rujukan:** Security Requirements / Data Confidentiality, Benefit Submission Access, dan Document Access.

**Ketentuan:** Sistem harus menerapkan hak akses berdasarkan peran terhadap data pegawai, tanggungan, jenis dan periode manfaat, nilai klaim, dokumen pendukung, dan informasi persetujuan. Pegawai hanya boleh mengakses pengajuan, status, riwayat, dan dokumen miliknya sendiri. HR Compensation & Benefit hanya boleh mengakses pengajuan serta bukti yang diperlukan dalam tanggung jawabnya. Super Admin hanya boleh menjalankan akses dan tindakan khusus sesuai kewenangan yang diberikan. Pengguna tanpa kewenangan tidak boleh melihat atau mengunduh dokumen pendukung.

### KON-BR-004: Jejak audit dan riwayat status

**Rujukan:** Functional Requirements / Submission History & Tracking; Security Requirements / Audit Trail.

**Ketentuan:** Sistem harus mencatat status pengajuan, tanggal pengajuan, tanggal perubahan status, dan pihak yang melakukan tindakan. Jejak audit sekurang-kurangnya harus mencakup pengajuan, perubahan, persetujuan, pengembalian, pengajuan ulang, dan penarikan. Setiap aktivitas harus menyimpan pengguna, peran, jenis aktivitas, tanggal dan waktu, serta ID pengajuan. Pengajuan dengan tanggal mundur harus tetap membedakan identitas pembuat dan pemilik pengajuan serta tanggal pembuatan aktual dan tanggal pengajuan.

### KON-BR-005: Migrasi riwayat

**Rujukan:** Requirement Identification / In Scope / Data Migration.

**Ketentuan:** Sistem harus mendukung migrasi riwayat Benefit Reimbursement sejak 2021 sampai data sumber terbaru yang tersedia. Rentang tersebut merupakan cakupan riwayat sumber dan bukan tanggal buatan untuk setiap pengajuan.

## Batas cakupan

Modul ini tidak mencakup Condolence Assistance, perubahan data pegawai atau tanggungan, penetapan dan perubahan kebijakan maupun nilai manfaat, perhitungan atau pembayaran langsung melalui Payroll, pelaksanaan pembayaran oleh HR Compensation & Benefit, serta pengelolaan proses luring setelah batas akhir pengajuan. Proses pembayaran oleh Finance yang disebut pada alur bisnis merupakan proses terkait di luar fungsi pengajuan ini. Rujukan: Requirement Identification / Out Scope dan Expected New System Business Flow / Benefits Submission.

## Ambiguitas dan batas interpretasi

- **Format dokumen:** aturan umum Supporting Document menerima PDF atau JPG, tetapi tabel Education Claim Form menyebut PDF untuk Attachment. REQ-BR-005 belum menetapkan satu aturan format final.
- **Status penarikan:** Business Rules / Withdrawal dan Withdraw Validation membatasi penarikan pada Sent Back; Execption Handling / Withdraw menjelaskan tindakan tanpa batas status. REQ-BR-009 tidak memperluas hak penarikan ke semua tahap.
- **Duplikasi dan pegawai kontrak:** terdapat larangan pengajuan In Progress untuk pegawai dan tanggungan yang sama, sementara pegawai kontrak dengan sisa plafon dapat mengajukan ulang. Daftar status yang dianggap aktif serta hubungan pengecualian kontrak dengan larangan tersebut perlu ditetapkan sebelum dijadikan aturan acuan eksperimen.
- **Nama sekolah:** penjabaran terdahulu menyebut nama sekolah diisi pegawai, tetapi Education Claim Form menandai School's Name sebagai tidak dapat diedit. KON-BR-001 mempertahankan isi tabel sumber; asal pengisian nilainya belum dijelaskan.
- **Kebijakan yang belum dirinci:** sumber tidak menyediakan nilai plafon, rumus prorata lengkap, atau jarak waktu peringatan mendekati batas akhir. Kebutuhan konfigurasi kategori berdasarkan jabatan untuk masa mendatang harus dibedakan dari pemeliharaan kebijakan yang dinyatakan di luar cakupan.
