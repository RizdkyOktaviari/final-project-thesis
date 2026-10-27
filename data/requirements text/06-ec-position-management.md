# Kebutuhan Riset: Pengelolaan Posisi (EC Position Management)

## Sumber dan ruang lingkup

- Source: `data/raw/BRD - EC Position Management.md`
- Tujuan: mengelola siklus hidup dan hierarki posisi, atribut unit organisasi, tanggal berlaku, riwayat, bagan posisi, migrasi, impor dan ekspor, serta referensi posisi bagi modul lain.
- Aktor: OD Admin untuk pengelolaan posisi, hierarki, bagan, impor dan ekspor; Comben untuk pengelolaan Cost Code/Cost Center; karyawan untuk membaca data bagan posisinya sendiri sesuai hak akses.
- Istilah: posisi induk disebut Higher-Level Position, posisi bawahan disebut subordinate position, dan pemangku posisi disebut incumbent. Nama fitur dipertahankan apabila diperlukan untuk mencocokkan narasi dengan BRD.

## Skenario kebutuhan

### REQ-POS-001: Membuat posisi secara umum

**Rujukan:** §4.1 Create Position; §5.1 Position Management Policies / Business Rules.

**Kebutuhan:** OD Admin harus dapat membuka fitur Create Position dan mengisi data posisi secara manual, termasuk Position Code, Position Title, Job Code, unit organisasi, jalur pelaporan, dan atribut lain yang diperlukan. Setelah OD Admin mengirimkan formulir, sistem harus memeriksa kelengkapan data wajib, format, keunikan kode posisi, konsistensi informasi organisasi, validitas hubungan dengan posisi induk apabila diisi, dan aturan bisnis yang berlaku. Jika data tidak valid, sistem harus menampilkan pesan kesalahan dan mengembalikan formulir untuk diperbaiki serta dikirim ulang. Jika data valid, sistem harus menyimpan posisi baru sehingga dapat digunakan dalam struktur organisasi sesuai hak akses.

### REQ-POS-002: Membuat posisi bawahan dari bagan posisi

**Rujukan:** §4.2 Add Position Below; §5.1 Position Management Policies / Business Rules.

**Kebutuhan:** OD Admin harus dapat memilih Add Position Below pada suatu posisi di Position Chart. Sistem harus mengidentifikasi posisi induk yang dipilih dan mengisi otomatis Higher-Level Position, Division, Department, serta informasi organisasi relevan sesuai konfigurasi. OD Admin kemudian melengkapi data posisi baru dan mengirimkan formulir. Sistem harus memeriksa data wajib, format, keunikan kode posisi, dan validitas struktur organisasi. Jika data tidak valid, sistem harus menampilkan pesan kesalahan dan mengembalikan formulir agar OD Admin dapat memperbaiki serta mengirimkannya ulang. Jika data valid, sistem harus menyimpan posisi baru sebagai posisi bawahan dari posisi induk yang telah dipilih.

### REQ-POS-003: Memperbarui posisi dan hubungan pelaporannya

**Rujukan:** §4.3 Edit Position; §5.1 Position Management Policies / Business Rules.

**Kebutuhan:** OD Admin harus dapat memilih posisi dari daftar atau Position Chart. Sistem harus menampilkan informasi posisi yang tersimpan agar dapat ditinjau dan diperbarui. Pengguna yang berwenang dapat mengubah Position Title, Job Code, Cost Center, Location, Position Level, atau Reporting Line sesuai kewenangannya, lalu mengirimkan perubahan. Sistem harus memeriksa kelengkapan data wajib, konsistensi organisasi, validitas Higher-Level Position, dan aturan bisnis posisi. Jika data tidak valid, sistem harus menampilkan pesan kesalahan dan mengembalikan formulir untuk diperbaiki serta dikirim ulang. Jika data valid, sistem harus menyimpan perubahan, memperbarui informasi posisi dan struktur organisasi terkait, mencatat jejak audit, serta mempertahankan data sebelumnya melalui tanggal berlaku. Perubahan jalur pelaporan harus memperbarui Position Chart dan Organization Chart sesuai tanggal berlaku tersebut.

### REQ-POS-004: Mengaktifkan dan menonaktifkan posisi

**Rujukan:** §2.2.1 In Scope; §2.4 Roles and Accessibilities, Organization Development (OD) Admin; §5.1 Position Management Policies / Business Rules, butir 3, 10, dan 11.

**Kebutuhan:** Sistem harus memungkinkan OD mengaktifkan dan menonaktifkan posisi. Sistem hanya boleh menonaktifkan posisi apabila posisi tersebut tidak memiliki pemangku aktif, kandidat aktif, maupun posisi bawahan yang masih aktif. Sistem tidak boleh menghapus posisi yang memiliki riwayat transaksi, riwayat organisasi, atau pernah digunakan oleh karyawan. Untuk posisi yang memiliki riwayat tersebut, penonaktifan tetap harus memenuhi batasan pemangku, kandidat, dan posisi bawahan aktif.

### REQ-POS-005: Mencari dan melihat bagan posisi beserta riwayatnya

**Rujukan:** §2.2.1 In Scope; §2.4 Roles and Accessibilities; §5.1 Position Management Policies / Business Rules, butir 12, 13, 17, dan 18.

**Kebutuhan:** Sistem harus memungkinkan pengguna mencari posisi berdasarkan Position Code, Position Title, nama karyawan yang menempati posisi, atau ID karyawan. Sistem harus menyediakan Position Chart dan tampilan historis organisasi serta posisi berdasarkan tanggal berlaku yang dipilih. OD dapat melihat dan mengelola seluruh posisi, sedangkan karyawan hanya dapat membaca data bagan posisi miliknya sendiri sesuai hak akses. Pengguna umum hanya boleh melihat posisi dan struktur organisasi yang diizinkan untuknya.

### REQ-POS-006: Mengelola data unit organisasi dan kode biaya

**Rujukan:** §2.2.1 In Scope, butir 7; §2.4 Roles and Accessibilities, Organization Development (OD) Admin dan Comben.

**Kebutuhan:** Sistem harus menyediakan pengelolaan data unit organisasi yang mencakup Company, Directorate, Division, Department, Section, serta Cost Code/Cost Center. OD Admin harus dapat membuat, membaca, dan memperbarui unit organisasi selain kode biaya. Comben harus dapat membuat, membaca, dan memperbarui kode biaya sesuai pembagian kewenangan yang ditetapkan. Sistem harus menerapkan batas peran tersebut ketika pengguna mengelola data unit organisasi.

### REQ-POS-007: Mengimpor data posisi dan mengekspor bagan

**Rujukan:** §2.2.1 In Scope, butir 9 sampai 11; §2.4 Roles and Accessibilities, Organization Development (OD) Admin.

**Kebutuhan:** Sistem harus memungkinkan OD Admin mengimpor data posisi secara massal dan menjalankan ekspor data posisi sesuai kewenangannya. Sistem juga harus menyediakan ekspor Position Chart dalam format PDF dan PNG. Sistem harus mendukung migrasi data posisi dari SAP SuccessFactors ke Mata Air Hub.

## Ketentuan pendukung

### KON-POS-001: Identitas posisi dan validitas hierarki

**Rujukan:** §2.5 Risks and Mitigation, Mitigasi; §4.1 Create Position, Validasi; §5.1 Position Management Policies / Business Rules, butir 1, 2, 5, 6, 14, dan 16.

**Ketentuan:** Position Code harus unik. Position Title harus sesuai dengan struktur organisasi dan kebutuhan bisnis. Setiap posisi harus terhubung dengan unit Directorate, Division, Department, dan Section yang valid sesuai struktur yang berlaku. Hubungan pelaporan harus valid dan tidak boleh membentuk siklus. Satu posisi paling banyak memiliki satu Higher-Level Position yang aktif dalam periode efektif yang sama. Data wajib harus lengkap sebelum posisi disimpan. Pemeriksaan keunikan, referensi organisasi, format, dan aturan bisnis yang disebutkan sumber harus dipertahankan pada alur pembuatan dan pembaruan yang relevan.

### KON-POS-002: Riwayat perubahan dan jejak audit

**Rujukan:** §2.2.1 In Scope, butir 3 dan 8; §4.3 Edit Position; §5.1 Position Management Policies / Business Rules, butir 4 dan 9.

**Ketentuan:** Sistem harus mencatat setiap perubahan posisi dalam jejak audit yang memuat pengguna, waktu, dan rincian data yang diubah. Perubahan tidak boleh menghapus data sebelumnya dan harus mempertahankan riwayat melalui tanggal berlaku. Riwayat tersebut mendukung penelusuran keadaan posisi dan organisasi pada tanggal efektif yang dipilih.

### KON-POS-003: Referensi posisi bagi modul lain

**Rujukan:** §2.2.1 In Scope, butir 12; §5.1 Position Management Policies / Business Rules, butir 19.

**Ketentuan:** Data posisi yang digunakan proses bisnis lain harus menjadi referensi tunggal bagi modul Employee Central dan Mata Air Hub terkait. Penggunaan posisi sebagai referensi tidak memindahkan transaksi rekrutmen, RTE, atau ESC ke dalam cakupan Position Management.

## Batas cakupan

Pembuatan otomatis Job Code Framework, rekrutmen termasuk penerimaan karyawan baru, penggantian dan pengelolaan kandidat, RTE, transaksi ESC seperti promosi, transfer dan reklasifikasi, data pribadi dan hubungan kerja karyawan, serta anggaran tenaga kerja tidak termasuk cakupan. Pengelolaan payroll dan kompensasi, alur persetujuan penambahan atau perubahan posisi, kontrak kerja dan perpanjangannya, data kandidat atau kumpulan talenta, serta perubahan jalur pelaporan dengan seret dan lepas (drag and drop) juga berada di luar cakupan.

## Ambiguitas dan batas interpretasi

- BRD tidak memiliki bab kebutuhan fungsional yang rinci atau katalog lengkap data posisi. Kebutuhan diturunkan dari ruang lingkup, peran, alur yang diharapkan, mitigasi risiko, dan kebijakan bisnis. Contoh atribut pada alur tidak diperlakukan sebagai katalog lengkap.
- Sumber menetapkan migrasi dari SAP SuccessFactors, impor massal, dan kewenangan impor/ekspor data posisi, tetapi tidak menjelaskan format berkas, pemetaan migrasi, penanganan kegagalan per baris, atau format ekspor data selain PDF dan PNG untuk bagan. Rincian tersebut tidak diisi dengan asumsi.
- Penonaktifan memiliki prasyarat eksplisit, sedangkan alur dan prasyarat rinci aktivasi belum dijelaskan. Ketentuan penonaktifan tidak otomatis dianggap sebagai ketentuan aktivasi.
- Katalog peran menempatkan Cost Code pada Comben dan pengelolaan posisi pada OD, sementara alur Edit Position mencantumkan Cost Center sebagai atribut yang dapat diperbarui sesuai kewenangan. Batas antara pemeliharaan master kode biaya dan pemilihan kode biaya pada posisi perlu dipertahankan saat menyusun model; dokumen ini tidak memberikan hak pengelolaan master kepada peran lain.

