# Kebutuhan Riset: Layanan Dasar Employee Central (EC Foundation)

## Sumber dan ruang lingkup

- Source: `data/raw/BRD - EC Foundation.md`
- Cakupan: layanan bersama untuk perusahaan, akses perwakilan (proxy), alur persetujuan, autentikasi dan otorisasi, perlindungan data, audit, integrasi, dan migrasi.
- Aktor: HR Administrator, System Administrator atau administrator sesuai kewenangan, pemohon proxy (Requestor), pengguna yang diwakili (Target User), pemberi persetujuan, dan penerima delegasi. PTAR menyediakan data hasil ekspor SAP SuccessFactors untuk migrasi.
- Kedudukan modul: Foundation menyediakan konfigurasi dan layanan bersama bagi modul Employee Central; setiap modul pemakai menetapkan rincian transaksi dan kolom bisnisnya sendiri.

## Skenario kebutuhan

### REQ-FND-001: Mengelola perusahaan

**Rujukan:** Business Rules & Policy / Multi Company; Functional Requirements / Multi Company.

**Kebutuhan:** HR Administrator harus dapat membuat dan memperbarui data perusahaan beserta atribut yang diperlukan. Sistem harus mendukung lebih dari satu perusahaan, memungkinkan aktivasi atau penonaktifan perusahaan tanpa menghapus riwayat data, dan mendukung penugasan pengguna ke satu atau beberapa perusahaan sesuai kewenangan. Konfigurasi perusahaan harus dapat digunakan sebagai referensi oleh seluruh modul Employee Central. Pengaruh penonaktifan terhadap transaksi yang sudah berjalan tidak dirinci dalam sumber dan tetap dicatat pada bagian batas interpretasi.

### REQ-FND-002: Mengajukan akses perwakilan

**Rujukan:** Business Rules & Policy / Proxy Request; Functional Requirements / Manage Proxy Request; Notification & Audit Trail / Proxy Email Notification Templates / 1. Proxy Request Submitted.

**Kebutuhan:** Pemohon harus dapat memilih pengguna yang akan diwakili, menentukan masa berlaku proxy dalam satuan hari, dan mengisi alasan pengajuan melalui Proxy Access. Sistem harus menampilkan rincian pengajuan sebelum pemohon mengirimkannya. Pengajuan harus memenuhi ketentuan akses dan status pengguna yang berlaku. Setelah pengajuan dikirim, sistem harus mengubah statusnya menjadi Pending Approval dan mengirimkan notifikasi kepada pengguna yang akan diwakili untuk meminta keputusan.

### REQ-FND-003: Menyetujui atau menolak akses perwakilan

**Rujukan:** Business Rules & Policy / Proxy Approval; Functional Requirements / Proxy Approval; Proxy Email Notification Templates / 2. Proxy Request Approved dan 3. Proxy Request Rejected.

**Kebutuhan:** Pengguna yang akan diwakili harus dapat melihat rincian pengajuan proxy dan memilih Approve atau Reject. Jika pengguna menyetujui, sistem harus memberitahukan hasil kepada pemohon dan hanya mengaktifkan akses setelah periode efektif yang disetujui dimulai. Jika pengguna menolak, sistem harus mengubah status menjadi Rejected dan memberitahukan penolakan kepada pemohon. Proxy yang ditolak tidak boleh digunakan untuk mengakses akun pengguna tersebut.

### REQ-FND-004: Mengaktifkan proxy dan berganti konteks pengguna

**Rujukan:** Business Rules & Policy / Proxy Activation dan Proxy Access; Functional Requirements / Proxy Activation & Access; Proxy Email Notification Templates / 4. Proxy Access Activated.

**Kebutuhan:** Setelah proxy disetujui dan periode berlakunya dimulai, sistem harus mengaktifkan proxy serta menampilkan pemohon, pengguna yang diwakili, tanggal mulai, dan tanggal berakhir pada informasi proxy aktif. Sistem harus menyediakan Switch User bagi pemohon yang memiliki proxy aktif. Setelah pemohon berganti pengguna, aktivitas harus berlangsung dalam konteks pengguna yang diwakili dan terbatas pada fungsi serta data yang menjadi kewenangan pengguna tersebut. Sistem harus memberitahukan aktivasi kepada pemohon sebagaimana template sumber. Kebutuhan notifikasi aktivasi kepada pengguna yang diwakili masih merupakan perbedaan dengan penjabaran terdahulu dan dicatat pada bagian ambiguitas.

### REQ-FND-005: Mengembalikan akses sebelum berakhir

**Rujukan:** Business Rules & Policy / Proxy Deactivation; Functional Requirements / Proxy Deactivation; Proxy Email Notification Templates / 5. Proxy Access Returned.

**Kebutuhan:** Pemohon harus dapat memilih Return Access untuk mengakhiri proxy sebelum masa berlakunya selesai. Setelah tindakan tersebut, sistem harus menonaktifkan proxy, mencegah pemohon menggunakan Switch User melalui proxy itu, memberitahukan pengembalian kepada pengguna yang diwakili, dan mencatat tindakannya pada jejak audit.

### REQ-FND-006: Mencabut akses perwakilan

**Rujukan:** Business Rules & Policy / Proxy Deactivation; Functional Requirements / Proxy Deactivation; Proxy Email Notification Templates / 6. Proxy Access Revoked.

**Kebutuhan:** Pengguna yang diwakili harus dapat memilih Revoke Access untuk mencabut proxy sebelum masa berlakunya selesai. Setelah pencabutan, sistem harus menonaktifkan proxy, mencegah pemohon menggunakan Switch User melalui proxy itu, memberitahukan pencabutan kepada pemohon, dan mencatat tindakannya pada jejak audit.

### REQ-FND-007: Mengakhiri akses perwakilan secara otomatis

**Rujukan:** Business Rules & Policy / Proxy Activation dan Proxy Deactivation; Functional Requirements / Proxy Deactivation; Proxy Email Notification Templates / 7. Proxy Access Expired.

**Kebutuhan:** Ketika masa berlaku proxy berakhir, sistem harus menonaktifkan proxy secara otomatis melalui Proxy Expiry. Sistem harus mencegah penggunaan Switch User melalui proxy yang telah berakhir, memberitahukan berakhirnya akses kepada pemohon dan pengguna yang diwakili, serta mencatat kejadian tersebut pada jejak audit.

### REQ-FND-008: Mengonfigurasi alur persetujuan bersama

**Rujukan:** Functional Requirements / Workflow & Approval.

**Kebutuhan:** Administrator harus dapat membuat, mengubah, mengaktifkan, dan menonaktifkan konfigurasi alur persetujuan. Sistem harus mendukung satu atau beberapa tingkat persetujuan dengan urutan pemberi persetujuan yang ditetapkan administrator. Administrator harus dapat menentukan pemberi persetujuan berdasarkan pengguna tertentu, posisi, atasan langsung, atasan pada tingkat tertentu, peran, atau unit organisasi apabila diperlukan. Konfigurasi tersebut harus dapat digunakan kembali oleh modul Employee Central sesuai kebutuhan prosesnya.

### REQ-FND-009: Menjalankan alur persetujuan bersama

**Rujukan:** Business Rules & Policy / Workflow & Approval; Functional Requirements / Workflow & Approval.

**Kebutuhan:** Setiap transaksi yang memerlukan persetujuan harus mengikuti alur yang telah ditetapkan perusahaan. Sistem harus mendukung tindakan pengajuan, persetujuan, delegasi, pengembalian, dan penarikan sesuai hak akses serta urutan yang dikonfigurasi. Sistem harus memberitahukan perubahan status proses kepada pemberi persetujuan sesuai konfigurasi. Seluruh aktivitas alur harus tercatat pada jejak audit, termasuk pengajuan, persetujuan, penolakan apabila berlaku, delegasi, pengembalian, dan penarikan. Rincian syarat serta hasil setiap tindakan dalam transaksi bisnis tetap ditentukan oleh BRD modul pemakai.

### REQ-FND-010: Mendelegasikan tugas persetujuan

**Rujukan:** Functional Requirements / Workflow & Approval.

**Kebutuhan:** Pemberi persetujuan harus dapat mendelegasikan tugasnya kepada pengguna lain untuk periode tertentu. Sistem hanya boleh memberikan hak delegasi kepada pengguna aktif yang memiliki kewenangan sesuai kebijakan perusahaan. Aktivitas yang dilakukan penerima delegasi harus dicatat sebagai aktivitas delegasi pada jejak audit. Sumber tidak menetapkan panjang periode delegasi untuk seluruh modul; durasinya tidak boleh diasumsikan sama dengan masa berlaku proxy.

### REQ-FND-011: Membatasi akses aplikasi dan data

**Rujukan:** Business Rules & Policy / Security & Access Rules; Functional Requirements / Security & Access Rules; Business Rules & Policy / Multi Company.

**Kebutuhan:** Sebelum pengguna mengakses aplikasi, sistem harus mendukung autentikasi pengguna. Sistem harus menerapkan kontrol akses berdasarkan peran dan membatasi fungsi serta data sesuai kewenangan, perusahaan yang ditugaskan, dan ruang lingkup organisasi pengguna. Konfigurasi hak akses bersama harus dapat digunakan oleh seluruh modul Employee Central. Rincian matriks peran dan izin harus mengikuti BRD modul terkait serta dokumen desain yang ditetapkan, tanpa menambahkan peran atau izin baru dalam penjabaran ini.

### REQ-FND-012: Mendukung integrasi data

**Rujukan:** Business Rules & Policy / Integration; Functional Requirements / Integration.

**Kebutuhan:** Sistem harus mendukung integrasi dengan aplikasi internal dan sinkronisasi data induk melalui mekanisme yang disepakati. Data induk yang berasal dari sistem lain harus mengikuti sumber data utama yang telah ditetapkan. Apabila data gagal diproses melalui integrasi, sistem harus mencatat kegagalan pada log integrasi. Sumber tidak menetapkan urutan panggilan layanan, protokol, atau mekanisme percobaan ulang untuk setiap modul.

### REQ-FND-013: Memvalidasi dan mengimpor data migrasi

**Rujukan:** Business Rules & Policy / Integration dan Data Migration; Functional Requirements / Data Migration.

**Kebutuhan:** PTAR harus menyediakan data hasil ekspor SAP SuccessFactors sebelum proses impor ke sistem baru. Sistem harus menyediakan validasi sebelum impor dan mekanisme untuk mengimpor data migrasi sesuai strategi yang disepakati. Sistem harus menyediakan hasil validasi dan rekonsiliasi serta mencatat log proses migrasi. Data hasil migrasi harus divalidasi dan direkonsiliasi sebelum digunakan pada sistem baru dan sebelum sistem mulai beroperasi. Data induk aktif serta riwayat yang disepakati pemilik bisnis harus mengikuti cakupan dan periode pada BRD masing-masing modul.

## Ketentuan pendukung

### KON-FND-001: Identitas perusahaan dan ruang lingkup data

**Rujukan:** Business Rules & Policy / Multi Company; Functional Requirements / Multi Company.

**Ketentuan:** Setiap perusahaan harus memiliki identitas unik. Sistem harus mendukung pembatasan data dan proses bisnis berdasarkan perusahaan yang ditetapkan. Pengguna dapat memiliki akses ke satu atau beberapa perusahaan sesuai kewenangan. Aktivasi dan penonaktifan tidak boleh menghapus riwayat perusahaan. Anggapan bahwa perusahaan nonaktif selalu tidak dapat dipakai sebagai ruang lingkup operasional merupakan interpretasi penjabaran terdahulu yang belum dijelaskan secara rinci oleh sumber.

### KON-FND-002: Identitas dan jejak aktivitas proxy

**Rujukan:** Business Rules & Policy / Proxy Access dan Proxy Deactivation; Functional Requirements / Notification & Audit Trail.

**Ketentuan:** Sistem harus mencatat pengajuan, persetujuan, penolakan, aktivasi, Switch User, pengembalian, pencabutan, dan berakhirnya proxy. Catatan aktivitas melalui proxy harus mempertahankan identitas pemohon dan pengguna yang diwakili serta dapat dibedakan dari aktivitas langsung pengguna yang diwakili. Proxy hanya boleh digunakan selama masa berlaku yang disetujui dan harus tetap berada dalam kewenangan pengguna yang diwakili. Ketentuan tersebut tidak menetapkan bahwa izin proxy merupakan irisan dengan seluruh izin akun pribadi pemohon; sumber hanya menetapkan konteks dan batas kewenangan pengguna yang diwakili.

### KON-FND-003: Perlindungan data pribadi dan sensitif

**Rujukan:** Business Rules & Policy / Data Protection; Functional Requirements / Data Protection.

**Ketentuan:** Sistem harus menyediakan enkripsi pada lapisan aplikasi sebelum menyimpan data pribadi atau sensitif ke basis data. Kategori yang wajib dilindungi menurut sumber mencakup identitas nasional, informasi keuangan, informasi kesehatan, data biometrik, data genetik, informasi hukum, data anak, dan riwayat lokasi. Contoh yang tercantum meliputi NIK atau nomor KTP, paspor, SIM, KK, KITAS/KITAP; rekening, kartu kredit atau debit, CVV, gaji, bonus, dan NPWP; rekam medis, MCU, riwayat penyakit, hasil laboratorium, golongan darah, dan BPJS Kesehatan; sidik jari, templat wajah, iris, retina, telapak tangan, dan suara; DNA atau genom; catatan pidana dan SKCK; data pribadi anak; serta riwayat GPS, pelacakan lokasi, dan perjalanan. Kewajiban perlindungan berlaku apabila modul memproses data tersebut. Rincian kolom, penyamaran data, pencarian, migrasi, dan integrasi harus ditetapkan pada BRD modul pemakai.

### KON-FND-004: Jejak audit yang tidak dapat diubah pengguna

**Rujukan:** Business Rules & Policy / Audit Trail; Functional Requirements / Audit Trail.

**Ketentuan:** Sistem harus menyediakan jejak audit bersama untuk seluruh modul Employee Central dan mencatat aktivitas pembuatan, pembaruan, serta penghapusan data induk. Catatan harus memuat pengguna, waktu, aktivitas, dan nilai sebelum serta sesudah perubahan apabila berlaku. Pengguna aplikasi tidak boleh mengubah data jejak audit. Kebutuhan ini berlaku bersama ketentuan pencatatan proxy dan alur persetujuan, dengan identitas pelaku delegasi tetap dapat ditelusuri.

### KON-FND-005: Tanggung jawab lintas modul dan migrasi

**Rujukan:** General Principles; Business Rules & Policy / Module Responsibility, Change Control, Integration, dan Data Migration; Foundation Dependency.

**Ketentuan:** Foundation harus menyediakan kapabilitas perusahaan, alur persetujuan, proxy, keamanan, audit, integrasi, migrasi, dan perlindungan data bersama. Organization Structure, Position Management, Hiring, dan ESC menggunakan konfigurasi perusahaan; Hiring, ESC, Benefit, dan Termination menggunakan alur persetujuan; seluruh proses persetujuan dapat menggunakan proxy; seluruh modul menggunakan keamanan, audit, dan integrasi. Setiap modul pemakai menetapkan kolom, validasi, hak akses, migrasi, integrasi, pelaporan, serta kriteria penerimaannya. Penyimpangan dari kebijakan Foundation harus melalui permintaan perubahan yang disetujui. Migrasi harus menjaga hubungan antara organisasi, posisi, dan pegawai; PTAR bertanggung jawab menyediakan data ekspor, sementara cakupan dan periode riwayat mengikuti kesepakatan pemilik bisnis.

## Batas cakupan

Foundation tidak mengelola transaksi Human Capital secara langsung. Perhitungan dan pemrosesan gaji, pengajuan cuti, timesheet, kalender waktu tidak bekerja, perencanaan suksesi dan talenta, pembelajaran, serta perencanaan tenaga kerja berada di luar cakupannya. Pengelolaan organisasi, posisi, perekrutan, data pribadi, ESC, pembayaran berulang atau tidak berulang, terminasi, pengajuan manfaat, pelaporan bisnis, dan PMGM harus dijelaskan pada BRD modul masing-masing. Rujukan: General Principles dan Requirement Identification / Out Scope.

## Ambiguitas dan batas interpretasi

- **Notifikasi aktivasi proxy:** penjabaran terdahulu menyebut pemohon dan pengguna yang diwakili sebagai penerima aktivasi. Template Proxy Access Activated secara eksplisit hanya mencantumkan Requestor, sedangkan ketentuan umum Notification & Audit Trail menyebut kedua pihak sesuai perubahan status. REQ-FND-004 mempertahankan penerima pada template dan menandai kebutuhan konfirmasi penerima kedua. Notifikasi berakhirnya proxy secara eksplisit ditujukan kepada kedua pihak.
- **Kewenangan proxy:** penjabaran terdahulu menyatakan proxy tidak menambahkan izin pemohon. Sumber mengatur bahwa aktivitas berjalan sebagai Target User dan dibatasi kewenangan Target User. REQ-FND-004 dan KON-FND-002 tidak menambahkan aturan irisan izin pemohon dan pengguna yang diwakili yang tidak dijelaskan pada sumber.
- **Perusahaan nonaktif:** sumber mewajibkan aktivasi atau penonaktifan tanpa kehilangan riwayat, tetapi belum menjelaskan transaksi berjalan, pemilihan ruang lingkup, atau akses baca setelah perusahaan dinonaktifkan. REQ-FND-001 dan KON-FND-001 tidak menetapkan akibat tambahan sebagai aturan final.
- **Konfigurasi modul pemakai:** durasi delegasi, matriks izin rinci, kriteria status pengguna yang memenuhi syarat untuk proxy, rincian integrasi, serta cakupan dan periode migrasi per modul harus mengikuti BRD terkait atau konfigurasi yang disepakati. Foundation tidak menyediakan nilai tunggal untuk seluruh modul.
