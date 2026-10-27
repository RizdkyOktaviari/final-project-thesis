# Kebutuhan Riset: Perubahan Status Kepegawaian (EC Employee Status Change)

## Sumber dan ruang lingkup

- Source: `data/raw/BRD - EC Employee Status Change.md`
- Cakupan: pengajuan reklasifikasi, transfer, perubahan jam atau jadwal kerja, perpanjangan kontrak, promosi, dan demosi beserta persetujuan dan penerapan perubahan yang telah disetujui.
- Aktor: pengaju (Requestor, termasuk Superintendent atau Department Head pada alur sumber), Organization Development (OD), HR Admin, pemberi persetujuan, penerima delegasi, pegawai yang menjadi subjek perubahan, dan pejabat penandatangan sesuai kewenangannya.

## Skenario kebutuhan

### REQ-ESC-001: Membuat pengajuan perubahan status

**Rujukan:** Functional Requirements / ESC Request / Create Employee Status Change; Execption Handling / Multiple Employee Status Change; Validation Rules / Mandatory Field Validation dan Attachment Validation.

**Kebutuhan:** Pengaju harus dapat membuat pengajuan Employee Status Change (ESC) untuk salah satu jenis perubahan dalam cakupan dengan melengkapi informasi dan bukti yang diwajibkan. Sistem harus mencegah pengajuan baru apabila pegawai yang sama masih memiliki pengajuan berstatus In Progress. Sistem harus mewajibkan lampiran Position Description dalam format PDF untuk setiap ESC dan lampiran Competency Assessment Matrix (CAM) dalam format PDF untuk pegawai Non-Staff; CAM tidak wajib untuk Staff. Pengajuan baru hanya boleh dibuat setelah pengajuan sebelumnya disetujui atau ditarik sesuai ketentuan sumber. Perbedaan istilah status penarikan dan penandaan kolom wajib tetap dicatat pada bagian ambiguitas.

### REQ-ESC-002: Menjalankan alur persetujuan standar

**Rujukan:** Expected New System Business Flow / Employee Status Change (Standard Workflow); Validation Rules / Workflow Validation.

**Kebutuhan:** Superintendent atau Department Head mengajukan ESC selain promosi dan transfer. HR Admin harus melakukan pemeriksaan awal dan menentukan alur persetujuan. Sistem harus meneruskan pengajuan melalui pemberi persetujuan secara berjenjang sesuai alur yang ditentukan HR Admin; sumber menyebut jenjang sampai Vice President bergantung pada konfigurasi tersebut. Pada setiap tahap, pemberi persetujuan harus dapat menyetujui atau mengembalikan pengajuan. Sistem harus menampilkan status proses dan mengirimkan notifikasi selama proses persetujuan berlangsung.

### REQ-ESC-003: Meninjau pengajuan promosi atau transfer

**Rujukan:** Expected New System Business Flow / Employee Status Change (Promotion & Transfer); Validation Rules / Workflow Validation.

**Kebutuhan:** Setelah Superintendent atau Department Head mengajukan promosi atau transfer, OD harus terlebih dahulu memeriksa pengajuan terhadap anggaran tenaga kerja (manning budget) dan kelayakan pegawai. Pengajuan yang melanjutkan proses harus diperiksa oleh HR Admin untuk penentuan alur persetujuan sebelum memasuki persetujuan utama secara berjenjang. Sistem tidak boleh melewati pemeriksaan awal OD untuk pengajuan promosi atau transfer. Urutan pemberi persetujuan setelah pemeriksaan HR Admin harus mengikuti konfigurasi yang berlaku.

### REQ-ESC-004: Mengembalikan, memperbaiki, dan mengajukan ulang ESC

**Rujukan:** Functional Requirements / ESC Request / Edit Employee Status Change; Approval / Send Back; Expected New System Business Flow / Employee Status Change (Standard Workflow) dan Employee Status Change (Promotion & Transfer).

**Kebutuhan:** Jika pengajuan memerlukan revisi, pemberi persetujuan harus dapat melakukan Send Back dengan komentar wajib. Sistem harus mengembalikan pengajuan kepada pengaju dan memberitahukan pengaju serta pemberi persetujuan yang telah menyetujui tahap sebelumnya. Hanya pengaju yang boleh merevisi pengajuan yang dikembalikan. Sistem harus menyimpan perubahan pada log aktivitas dan memungkinkan pengaju mengajukan ulang. Pada alur standar, pengajuan ulang kembali ke HR Admin. Pada promosi atau transfer, pengajuan yang dikembalikan saat pemeriksaan OD kembali ke OD; pengajuan yang dikembalikan pada alur persetujuan utama kembali ke HR Admin dengan melewati pemeriksaan OD ulang, sebagaimana dijelaskan dalam alur sumber.

### REQ-ESC-005: Menyetujui pengajuan secara berjenjang

**Rujukan:** Functional Requirements / Approval / Approve; Business Rules / Employee Status Changes Policies / Business Rules.

**Kebutuhan:** Pemberi persetujuan harus dapat menyetujui pengajuan yang memenuhi persyaratan tanpa diwajibkan mengisi komentar. Setelah suatu tahap disetujui, sistem harus meneruskan pengajuan dan mengirimkan notifikasi kepada pemberi persetujuan berikutnya sesuai konfigurasi. Sistem harus menyimpan riwayat keputusan dan komentar. Persetujuan suatu tahap belum boleh menerapkan perubahan data resmi sebelum seluruh persetujuan selesai dan tanggal efektif berlaku.

### REQ-ESC-006: Mendelegasikan tugas persetujuan

**Rujukan:** Functional Requirements / Approval / Delegate Approval; Validation Rules / Delegate Validation.

**Kebutuhan:** Selama ESC berstatus In Progress, pemberi persetujuan yang sedang memiliki tugas harus dapat mendelegasikan tugas miliknya sendiri kepada pengguna aktif sesuai kewenangan. Sistem harus membatasi satu penerima delegasi aktif untuk setiap tugas pada waktu yang sama. Delegasi tidak boleh mengubah alur atau urutan persetujuan yang telah dikonfigurasi. Penerima delegasi bertindak atas nama pemberi persetujuan asal; sistem harus mencatat tindakan dan keputusan atas nama penerima delegasi, referensi pemberi persetujuan asal, serta waktu perubahan pada log aktivitas.

### REQ-ESC-007: Mengganti pemberi persetujuan berikutnya

**Rujukan:** Functional Requirements / Approval / Override Approver; Business Rules / Employee Status Changes Policies / Business Rules.

**Kebutuhan:** HR Admin harus dapat mengganti pemberi persetujuan berikutnya selama proses persetujuan masih berlangsung. Sistem harus mencatat perubahan pemberi persetujuan pada log aktivitas. Penggantian hanya berlaku terhadap tahap yang belum disetujui sesuai cakupan penggantian pada sumber; dokumen ini tidak memberikan hak penggantian tersebut kepada peran lain.

### REQ-ESC-008: Menarik pengajuan ESC

**Rujukan:** Functional Requirements / ESC Request / Withdraw Employee Status Change; Execption Handling / Withdraw; Validation Rules / Withdrawal Validation.

**Kebutuhan:** Apabila pengaju melakukan penarikan yang diizinkan, sistem harus menghentikan proses persetujuan, mencatat status penarikan dan tindakannya pada log aktivitas, serta mengirimkan notifikasi kepada HR Admin sebagai penerima bawaan sesuai konfigurasi. Pengajuan yang telah ditarik tidak boleh diproses atau diajukan ulang. Bagian fungsional mengizinkan penarikan selama persetujuan belum selesai, sedangkan tabel validasi membatasi tindakan ketika proses berada pada pengaju. Skenario ini menetapkan akibat penarikan; syarat status dan istilah status final masih memerlukan konfirmasi pada bagian ambiguitas.

### REQ-ESC-009: Menghasilkan dokumen ESC

**Rujukan:** Functional Requirements / Document Generation; Reports / Individual ESC Report, Employee Status Change Monitoring Report, dan Memorandum.

**Kebutuhan:** Setelah persetujuan akhir selesai, HR Admin harus dapat menghasilkan dan mengunduh laporan individual ESC dalam format PDF yang memuat tanda tangan digital tersimpan. Sistem harus membatasi akses laporan individual kepada HR Admin dan pegawai terkait sesuai aturan akses serta pengecualian pengajuan oleh Department Head. HR Admin harus dapat menghasilkan laporan pemantauan dalam format XLSX berdasarkan periode pilihan, mencakup pengajuan yang masih tertunda dan yang sudah selesai. HR Admin juga harus dapat menghasilkan memorandum untuk ESC yang telah memperoleh persetujuan dalam periode pilihan dengan tanda tangan digital. Sumber menyebut keluaran memorandum PDF dan DOC pada bagian fungsional, tetapi DOCX pada cakupan; format Word final dicatat sebagai ambiguitas.

### REQ-ESC-010: Memantau dan mencari pengajuan ESC

**Rujukan:** Functional Requirements / Monitoring dan Search & Filter; Requirement Identification / WHO / Dept Head dan Employee.

**Kebutuhan:** Sistem harus menampilkan status terkini, tahap persetujuan terakhir, dan pemberi persetujuan yang sedang menunggu tindakan. Pengaju harus dapat melihat riwayat ESC yang pernah diajukan, dan Department Head harus dapat melihat riwayat ESC bawahannya sesuai kewenangan. Pegawai hanya boleh melihat ESC terakhir miliknya, dengan pengecualian akses untuk pengajuan yang dibuat oleh Department Head. Sistem harus menyediakan pencarian dan penyaringan berdasarkan ID atau nama pegawai, departemen, posisi, jenis ESC, status ESC, tanggal pengajuan, tanggal efektif, dan periode untuk pemantauan atau pelaporan.

### REQ-ESC-011: Memberitahukan perkembangan persetujuan

**Rujukan:** Business Rules / Employee Status Changes Policies / Business Rules; Notification/Notifikasi / 1. Employee Status Change Submitted sampai 6. Employee Status Change Completed serta Notification Matrix.

**Kebutuhan:** Sistem harus mengirimkan notifikasi kepada pemberi persetujuan berikutnya saat pengajuan, persetujuan tahap, atau pengajuan ulang. Saat Send Back, sistem harus memberitahukan pengaju dan pemberi persetujuan sebelumnya. Saat penarikan, sistem harus memberitahukan peran yang dikonfigurasi dengan HR Admin sebagai penerima bawaan. Selama pemberi persetujuan belum bertindak, sistem harus mengirimkan pengingat melalui email dan aplikasi setiap dua hari; sumber menyebut interval tersebut dapat dikonfigurasi. Ketika seluruh persetujuan selesai, sistem harus mengirimkan notifikasi penyelesaian. Template penyelesaian mencantumkan pengaju, pegawai, dan HR Admin, sementara matriks hanya mencantumkan pengaju dan HR Admin; daftar penerima final tetap dicatat sebagai konflik sumber.

### REQ-ESC-012: Menerapkan perubahan yang telah disetujui

**Rujukan:** Business Rules / Employee Status Changes Policies / Business Rules; Functional Requirements / Integration Trigger; Requirement Identification / In Scope / Integration.

**Kebutuhan:** Sistem hanya boleh menerapkan perubahan ESC setelah persetujuan akhir selesai dan tanggal efektif berlaku. Jika persetujuan selesai sebelum tanggal efektif, perubahan data resmi harus menunggu tanggal efektif tersebut. Sesuai jenis perubahan, sistem harus memperbarui struktur organisasi, posisi, informasi pekerjaan, hubungan pelaporan, penggajian dan kompensasi, serta roster, shift, atau pengelolaan waktu. Untuk transfer atau promosi, sistem harus menyediakan penanda perubahan terkait kepada PMGM. Data yang diteruskan tidak menjadikan perhitungan penggajian atau penilaian kinerja sebagai fungsi ESC.

### REQ-ESC-013: Menyimpan dan menggunakan tanda tangan digital

**Rujukan:** Security Requirements / Encryption / Digital Signature; Functional Requirements / Document Generation.

**Kebutuhan:** Pejabat penandatangan yang berwenang harus dapat mengunggah gambar tanda tangan dalam format PNG. Sistem harus menyimpan tanda tangan dalam bentuk Base64 yang dienkripsi dan menggunakannya secara otomatis ketika menghasilkan laporan yang memerlukan tanda tangan sesuai sumber. Sistem harus membatasi pengelolaan tanda tangan kepada pengguna yang berwenang dan mencatat pembaruannya pada jejak audit.

## Ketentuan pendukung

### KON-ESC-001: Data pengajuan dan perbandingan status

**Rujukan:** Functional Requirements / Employee Status Change Form / ESC Field Details, Employee Old Status, dan Employee New Status.

**Ketentuan:** Formulir harus menampilkan nama pegawai, ID, dan tanggal mulai bekerja dari data sumber serta memuat alasan perubahan, Position Description, justifikasi, dan CAM bila berlaku. Status lama harus bersumber dari data pegawai saat ini. Status baru mencakup status kepegawaian, posisi, departemen, atasan, tingkat gaji (Pay Grade), klasifikasi upah, jadwal kerja, jam kerja, tanggal efektif, gaji pokok, persentase kenaikan, nomor referensi, bonus tahunan, dan tunjangan kendaraan. Tabel sumber menandai sebagian kolom status lama tidak dapat diedit tetapi memberi penanda dapat diedit pada Report To dan Work hours; perbedaan ini dengan penjabaran terdahulu dicatat pada bagian ambiguitas.

### KON-ESC-002: Formulir berdasarkan peran

**Rujukan:** Functional Requirements / Employee Status Change Form / Requestor, Organization Development (OD), dan HR Admin; Employee New Status; Business Rules / Employee Status Changes Policies / Business Rules.

**Ketentuan:** Sistem harus menggunakan satu formulir ESC dengan kewenangan sesuai peran dan tahap. Pengaju dapat mengisi atau mengubah status pegawai, posisi, departemen, atasan, jadwal kerja, dan jam kerja. OD dapat meninjau posisi, atasan, Position Description atau Position Detail sebagaimana istilah sumber, serta CAM. HR Admin dapat meninjau seluruh informasi dan mengganti pemberi persetujuan berikutnya. Gaji pokok, persentase kenaikan, dan nomor referensi ditandai khusus HR. Bonus tahunan dan tunjangan kendaraan hanya boleh diisi atau diperbarui HR Admin dan hanya ditampilkan untuk Senior Manager serta jenjang di atasnya. Klaim perhitungan persentase otomatis pada cakupan dan penandaan kolom yang dapat diisi HR perlu direkonsiliasi sebagaimana bagian ambiguitas.

### KON-ESC-003: Kelengkapan dan tanggal efektif

**Rujukan:** Business Rules / Employee Status Changes Policies / Business Rules; Functional Requirements / Attachment; Validation Rules / Employee Status Change Validation, Mandatory Field Validation, dan Attachment Validation.

**Ketentuan:** Kolom wajib dan dokumen wajib harus lengkap sebelum pengajuan. Position Description wajib untuk seluruh ESC; CAM wajib untuk Non-Staff dan tidak wajib untuk Staff. Sumber memuat aturan umum seluruh kolom wajib, tetapi tabel mencantumkan sejumlah pengecualian sehingga kewajiban per kolom harus diperlakukan bersama catatan konflik. Tabel validasi mengizinkan tanggal mundur maupun tanggal mendatang sesuai kebijakan perusahaan tanpa memberikan batas rinci. Pernyataan tersebut bertentangan dengan pencantuman Backdate Request ESC dan Backdate Approval ESC di luar cakupan; dokumen ini tidak memilih salah satu sebagai kebijakan final.

### KON-ESC-004: Kebijakan demosi

**Rujukan:** Business Rules / Demotion Policy.

**Ketentuan:** Demosi dapat bersifat sukarela berdasarkan persetujuan atau permintaan pegawai, atau tidak sukarela berdasarkan keputusan perusahaan. Alasan dapat berkaitan dengan disiplin, etika, atau kinerja, dan perubahan dapat memengaruhi tingkat jabatan, posisi, tanggung jawab pekerjaan, kompensasi, serta manfaat. Sumber mewajibkan perusahaan lebih dahulu mengupayakan tindakan perbaikan yang sesuai sebelum menggunakan demosi sebagai alternatif. Ketentuan ini merupakan prasyarat kebijakan bisnis, bukan urutan layanan perangkat lunak tambahan.

### KON-ESC-005: Hak akses dan kerahasiaan

**Rujukan:** Requirement Identification / WHO / Dept Head dan Employee; Business Rules / Employee Status Changes Policies / Business Rules; Security Requirements / Confidential Field, Report Access, dan Document Access; Validation Rules / Access Validation.

**Ketentuan:** Sistem harus membatasi akses terhadap gaji, bonus tahunan, tunjangan kendaraan, dan Paygrade berdasarkan kewenangan. Informasi pengajuan yang mencakup persentase kenaikan, persetujuan, dan dokumen pendukung harus mengikuti pembatasan akses berdasarkan peran; ringkasan terdahulu mengelompokkan informasi tersebut sebagai rahasia, sementara daftar Confidential Field sumber secara eksplisit menyebut empat kolom sebelumnya. Pengguna tanpa kewenangan tidak boleh menghasilkan, mengunduh, atau membagikan laporan. Laporan individual dibatasi kepada HR Admin dan pegawai terkait. Pegawai hanya dapat melihat ESC terakhir miliknya, tetapi aturan bisnis melarang pegawai mengakses ESC yang diajukan Department Head. Hubungan pengecualian ini dengan hak laporan dan notifikasi penyelesaian memerlukan konfirmasi.

### KON-ESC-006: Jejak audit dan riwayat

**Rujukan:** Business Rules / Employee Status Changes Policies / Business Rules; Functional Requirements / Monitoring / Activity Log; Security Requirements / Audit Trail.

**Ketentuan:** Sistem harus menyimpan seluruh perubahan ESC sebagai riwayat. Riwayat persetujuan dan komentar tidak boleh dihapus. Jejak audit harus bersifat hanya baca bagi pengguna aplikasi dan mencakup pembuatan, perubahan, pengajuan, persetujuan, pengembalian, penarikan, delegasi, penggantian pemberi persetujuan, perubahan data, komentar, pembuatan laporan, serta pembaruan tanda tangan digital. Catatan harus menyimpan pengguna, peran, aktivitas, tanggal, dan waktu. Catatan delegasi harus mempertahankan identitas penerima delegasi dan pemberi persetujuan asal.

### KON-ESC-007: Migrasi riwayat

**Rujukan:** Requirement Identification / In Scope / Data Migration.

**Ketentuan:** Sistem harus mendukung migrasi riwayat ESC sejak 2021 sampai data sumber terbaru yang tersedia.

## Batas cakupan

ESC tidak menjalankan pengunduran diri, pemberhentian, pemutusan hubungan kerja, atau penyelesaian keluar pegawai; perhitungan gaji, bonus, tunjangan, dan pajak; rekrutmen; penilaian kinerja atau talenta; pembuatan struktur organisasi, pembuatan atau penghapusan posisi; maupun layanan mandiri di luar ESC seperti perubahan data pribadi, cuti, kehadiran, dan klaim. ESC memasok perubahan yang telah disetujui kepada modul terkait. Sumber juga mencantumkan pengajuan dan persetujuan bertanggal mundur di luar cakupan; konflik dengan tabel validasi dijelaskan di bawah. Rujukan: Requirement Identification / Out Scope.

## Ambiguitas dan batas interpretasi

- **Konfigurasi alur:** sumber memberi urutan umum, pemeriksaan OD untuk promosi atau transfer, dan kewenangan HR Admin, tetapi belum menentukan susunan lengkap pemberi persetujuan serta penanggung jawab eskalasi untuk setiap jenis ESC. REQ-ESC-002 sampai REQ-ESC-005 tidak menambahkan konfigurasi tersebut.
- **Penarikan:** Withdraw Employee Status Change mengizinkan tindakan selama persetujuan belum selesai; Withdrawal Validation membatasinya ketika proses berada pada pengaju. Sumber menggunakan Withdraw dan Withdrawed, sedangkan pesan validasi serta penjabaran terdahulu juga menggunakan Withdrawn. Status dan batas tindakan REQ-ESC-008 harus dikonfirmasi.
- **Hak akses laporan:** hak laporan bagi penerima delegasi atau pelaku penggantian pemberi persetujuan tidak dirinci. Larangan akses pegawai untuk pengajuan Department Head harus direkonsiliasi dengan hak laporan individual dan notifikasi kepada pegawai. REQ-ESC-009, REQ-ESC-010, dan KON-ESC-005 mempertahankan batas ini.
- **Penerima notifikasi selesai:** template Employee Status Change Completed mencantumkan pengaju, pegawai, dan HR Admin; Notification Matrix mencantumkan pengaju dan HR Admin. REQ-ESC-011 tidak menyamakan kedua daftar secara sepihak.
- **Kolom wajib dan peran:** aturan umum menyebut seluruh kolom wajib kecuali CAM bersyarat, tetapi tabel menandai CAM, Annual Bonus, Vehicle Allowance, dan beberapa data tampilan sebagai tidak wajib. Daftar kolom pengaju juga lebih sempit daripada seluruh informasi wajib pengajuan. KON-ESC-001 sampai KON-ESC-003 mempertahankan rincian ini tanpa menetapkan kewajiban baru pada pengaju.
- **Data status lama:** penjabaran terdahulu memperlakukan status lama sebagai tidak dapat diedit, sedangkan tabel Employee Old Status menandai Report To dan Work hours dapat diedit. KON-ESC-001 mengikuti bukti tabel dan tidak menyimpulkan bahwa seluruh status lama boleh diubah.
- **Persentase kenaikan:** In Scope menyebut perhitungan otomatis berdasarkan gaji lama dan baru; tabel Employee New Status menandai Percentage Increase dapat diisi dan khusus HR. Hubungan hasil perhitungan dengan kewenangan pengubahan pada KON-ESC-002 belum dijelaskan.
- **Tanggal mundur:** Out Scope memuat Backdate Request ESC dan Backdate Approval ESC, tetapi Employee Status Change Validation mengizinkan Backdate dan Future Date menurut kebijakan perusahaan. KON-ESC-003 memerlukan keputusan bisnis sebelum skenario tanggal mundur dipakai sebagai acuan eksperimen.
- **Format memorandum:** Document Generation menyebut PDF dan DOC; In Scope menyebut PDF dan DOCX. REQ-ESC-009 mempertahankan PDF serta menandai ekstensi Word yang belum konsisten.
