# Kebutuhan Riset: Penilaian Kinerja (PMGM Performance Assessment)

## Sumber dan ruang lingkup

- Source: `data/raw/BRD PMGM - Performance Assessment.md`
- Aktor: administrator Organization Development (OD), karyawan, atasan langsung (Direct Supervisor), dan atasan satu tingkat di atas atasan langsung (One-Up Supervisor). Department Head atau Senior Manager membahas normalisasi di luar sistem.
- Cakupan: konfigurasi dan peluncuran formulir, penilaian diri, penilaian atasan, administrasi normalisasi, finalisasi, pelaporan, dan jejak audit.
- Istilah: PA berarti Performance Assessment. Nama status dan kolom tertentu dipertahankan untuk ketertelusuran.

## Skenario kebutuhan

### REQ-PA-001: Mengonfigurasi dan meluncurkan penilaian kinerja

**Rujukan:** WHO, Organization Development (OD) Admin; Expected New System Business Flow, Template and Launch, butir 1 sampai 3; Business Rules, butir 25.

**Kebutuhan:** OD harus dapat membuat, mengubah, menggandakan, dan meninjau pratinjau templat PA yang terpisah untuk Staff dan Non-Staff. OD mengatur pengaturan umum, skala penilaian, alur peninjauan, periode, notifikasi, peserta, bahasa, bagian formulir, dan kolom formulir. Setelah menentukan peserta dan meninjau pratinjau, OD meluncurkan templat untuk membuka periode PA. Sistem harus mencegah perubahan templat yang sudah diluncurkan. OD harus dapat menutup periode atau templat PA sesuai kewenangannya.

### REQ-PA-002: Mengisi dan mengajukan penilaian diri

**Rujukan:** WHO, Employee (Staff & Non-Staff); Expected New System Business Flow, Self-Rating, butir 4 sampai 7; Business Rules, butir 6 sampai 9.

**Kebutuhan:** Karyawan membuka formulir PA sesuai kategori dan preferensi bahasanya. Sistem harus menampilkan informasi karyawan, tanggal penilaian, serta alur yang menunjukkan tahap saat ini dan tahap berikutnya. Karyawan mengisi nilai dalam rentang 1 sampai 6, komentar wajib pada setiap sasaran, dan aspirasi; karyawan dapat mengunggah lampiran opsional. Karyawan dapat menyimpan draf tanpa memindahkan PA ke tahap berikutnya. Ketika karyawan mengajukan penilaian diri, sistem harus memvalidasi seluruh kolom wajib dan menampilkan peringatan jika ada data yang belum diisi. Jika persyaratan pengajuan terpenuhi, sistem harus mengubah status menjadi `Pending Direct Supervisor Review` dan mengunci perubahan formulir oleh karyawan.

### REQ-PA-003: Meninjau penilaian oleh atasan langsung

**Rujukan:** WHO, Direct Supervisor; Expected New System Business Flow, Direct Supervisor Review, butir 8 sampai 10; Business Rules, butir 10.

**Kebutuhan:** Atasan langsung menerima notifikasi dan meninjau nilai serta komentar penilaian diri bawahannya. Sistem harus memungkinkan atasan langsung menyesuaikan nilai, memberikan komentar, serta mengisi kekuatan dan area perbaikan karyawan. Atasan langsung dapat menyimpan draf penilaian, mengembalikan penilaian melalui `Send Back`, atau mengajukan hasil peninjauan. Pada alur yang menggunakan One-Up Supervisor, pengajuan atasan langsung harus meneruskan PA kepada One-Up Supervisor. Sistem harus mencegah atasan langsung melihat penilaian One-Up Supervisor.

### REQ-PA-004: Menyelesaikan peninjauan oleh One-Up Supervisor

**Rujukan:** WHO, One Up Supervisor; Expected New System Business Flow, One-Up Supervisor Review, butir 11 dan 12; Business Rules, butir 10 sampai 12.

**Kebutuhan:** One-Up Supervisor harus dapat melihat penilaian diri karyawan dan penilaian atasan langsung. Sesuai kewenangannya dalam alur, One-Up Supervisor dapat menyesuaikan nilai, memberikan komentar, mengisi kekuatan dan area perbaikan, menyimpan draf, mengembalikan penilaian, serta menyelesaikan peninjauan. Setelah peninjau terakhir mengajukan hasil penilaian, sistem harus mengubah status PA menjadi `Ready for Normalization`. OD tidak melakukan persetujuan penilaian dalam alur PA. Sumber menggunakan nama aksi `Approve` pada uraian peran dan `Submit` pada uraian alur; nama dan makna transisi ini perlu dikonfirmasi sebelum digunakan sebagai acuan penilaian konsistensi.

### REQ-PA-005: Memperbaiki penilaian yang dikembalikan

**Rujukan:** WHO, Employee (Staff & Non-Staff), Direct Supervisor, dan One Up Supervisor; Business Rules, butir 8 dan 9.

**Kebutuhan:** Peninjau yang berwenang dapat mengembalikan PA melalui `Send Back`. Karyawan menerima catatan pengembalian, memperbaiki penilaian, dan mengajukannya kembali selama periode serta tahap mengizinkan. Sistem harus membuka kembali pengeditan formulir karyawan ketika PA dikembalikan. Sebelum pengajuan ulang, sistem harus tetap memvalidasi kelengkapan kolom wajib.

### REQ-PA-006: Mengirim notifikasi dan memantau proses penilaian

**Rujukan:** WHO, Organization Development (OD) Admin; Expected New System Business Flow, Notification and Monitoring, butir 13; WHAT, tabel In Scope.

**Kebutuhan:** Sistem harus mengirimkan notifikasi dan pengingat secara kolektif kepada karyawan dan peninjau berdasarkan tindakan, pekerjaan yang belum diselesaikan, serta tenggat setiap tahap. OD harus dapat mengatur waktu, penerima, subjek, frekuensi, dan eskalasi notifikasi. Sistem harus memungkinkan OD memantau status PA seluruh karyawan, karyawan yang dipindahkan, atasan yang mengundurkan diri, penilaian yang melewati tenggat, serta departemen yang belum menyelesaikan normalisasi.

### REQ-PA-007: Mengekspor data untuk normalisasi departemen

**Rujukan:** Expected New System Business Flow, Normalization, butir 14 dan 15; Business Rules, butir 16 dan 17.

**Kebutuhan:** OD memilih satu atau beberapa departemen untuk mengekspor data PA. Sistem harus menghasilkan satu berkas terpisah bagi setiap departemen dalam format XLSX atau CSV. Department Head atau Senior Manager membahas dan melakukan normalisasi di luar sistem, kemudian menyerahkan hasil normalisasi kepada OD.

### REQ-PA-008: Mengimpor dan memperbarui hasil normalisasi

**Rujukan:** WHO, Organization Development (OD) Admin; Expected New System Business Flow, Normalization, butir 16 sampai 18; Business Rules, butir 18 dan 19.

**Kebutuhan:** Pada impor pertama, OD membuat kelompok normalisasi dengan mengisi nama normalisasi. Sistem harus menggunakan periode PA yang sedang aktif tanpa periode pembukaan atau penutupan tersendiri untuk kelompok tersebut. OD mengimpor atau mengimpor ulang hasil normalisasi per departemen dengan keterangan wajib dan lampiran opsional, lalu meninjau hasil validasi impor. Sistem harus menjadikan hasil impor terakhir yang berhasil sebagai nilai normalisasi aktif. Sistem harus mempertahankan seluruh berkas sebelumnya dalam riwayat impor dan log audit.

### REQ-PA-009: Menyesuaikan nilai akhir secara individual

**Rujukan:** Expected New System Business Flow, Normalization, butir 19; Business Rules, butir 16 dan 19.

**Kebutuhan:** Jika hanya beberapa karyawan memerlukan penyesuaian hasil normalisasi, OD harus dapat mengubah nilai akhir karyawan tersebut secara individual. OD wajib mengisi keterangan perubahan dan dapat menyertakan lampiran. Sistem harus menyimpan seluruh versi perubahan sebagai log audit. Kewenangan penyesuaian nilai individual ini hanya diberikan kepada OD.

### REQ-PA-010: Memfinalisasi hasil penilaian

**Rujukan:** Expected New System Business Flow, Finalization and Report, butir 20 dan 21; Business Rules, butir 16.

**Kebutuhan:** Setelah seluruh departemen menyelesaikan normalisasi, OD melakukan finalisasi. Sistem harus mengubah status PA menjadi `Completed` dan mengunci nilai akhir. Setelah PA berstatus `Completed`, sistem harus menampilkan nilai akhir kepada karyawan. Sistem harus membatasi hasil yang ditampilkan kepada karyawan pada nilai akhir, tanpa penilaian detail atau riwayat perubahan nilai.

### REQ-PA-011: Mengakses dan mengekspor laporan penilaian

**Rujukan:** Expected New System Business Flow, Finalization and Report, butir 22; WHO, Organization Development (OD) Admin.

**Kebutuhan:** Sistem harus memasukkan nilai akhir ke dalam laporan PA. OD harus dapat memfilter laporan berdasarkan periode, kategori Staff atau Non-Staff, tingkat jabatan, departemen, karyawan, dan status PA. Sistem harus menyediakan unduhan laporan dalam format XLSX atau CSV.

### REQ-PA-012: Menangani perubahan status karyawan

**Rujukan:** Expected New System Business Flow, Employee and Reviewer Changes, butir 23 dan 24; Business Rules, butir 5 dan 20; WHAT IF, Mitigation.

**Kebutuhan:** Ketika karyawan mengalami perpindahan atau promosi, sistem harus mempertahankan sasaran yang telah diajukan, memberikan penanda `Is Transferred`, dan menggunakan atasan baru untuk penilaian. Sistem harus memperbarui hubungan atasan dan bawahan berdasarkan struktur organisasi terbaru. OD dapat menyesuaikan peninjau karena perpindahan, promosi, perubahan organisasi, atau kebutuhan operasional yang sah, dengan keterangan wajib dan pencatatan dalam jejak audit. Jika karyawan mengundurkan diri atau mengalami pemutusan hubungan kerja, sistem harus mengeluarkannya dari peserta PA aktif.

### REQ-PA-013: Menangani atasan yang mengundurkan diri

**Rujukan:** Expected New System Business Flow, Employee and Reviewer Changes, butir 24; Business Rules, butir 5 dan 21.

**Kebutuhan:** Jika atasan mengundurkan diri setelah memberikan penilaian, sistem harus tetap menggunakan nilai yang sudah diberikan. Jika atasan mengundurkan diri sebelum memberikan penilaian, sumber menyediakan pilihan sistem melewati peninjau tersebut atau OD menentukan peninjau pengganti. Perubahan peninjau oleh OD harus disertai keterangan dan disimpan dalam jejak audit. Kriteria pemilihan antara kedua jalur tersebut belum dirinci dalam sumber dan harus dikonfirmasi sebelum salah satunya digunakan sebagai acuan penilaian konsistensi.

## Ketentuan pendukung

### KON-PA-001: Menentukan alur peninjauan menurut kategori peserta

**Rujukan:** Expected New System Business Flow, Template and Launch; Business Rules, butir 1 sampai 4 dan 12.

**Ketentuan:** Templat dan peluncuran PA Staff harus terpisah dari Non-Staff. Alur Staff mengikuti struktur organisasi Sistem HRIS. OD mengonfigurasi alur Non-Staff secara manual per departemen saat peluncuran berdasarkan matriks yang berlaku. Non-Staff menggunakan paling banyak dua lapis peninjauan, atau satu lapis jika hanya satu peninjau memenuhi kriteria. Jalur Administrator menggunakan satu lapis peninjauan oleh Manager; Director dapat menjadi peninjau pada lapis terakhir apabila dikonfigurasi OD. Tindakan massal OD hanya digunakan untuk memindahkan PA ke tahap `Normalization`, bukan sebagai persetujuan penilaian.

### KON-PA-002: Menyediakan data penilaian

**Rujukan:** Business Rules, butir 6 sampai 8; WHO, Employee (Staff & Non-Staff).

**Ketentuan:** Sistem harus menyediakan skala nilai 1 sampai 6 melalui daftar pilihan, beserta nama dan deskripsi setiap nilai. Komentar pada setiap sasaran bersifat wajib dan lampiran bersifat opsional. Karyawan mengisi aspirasi; atasan mengisi kekuatan dan area perbaikan. Penyimpanan draf tidak mengubah tahap proses. Pengajuan harus memenuhi kelengkapan kolom wajib.

### KON-PA-003: Menghitung ringkasan nilai

**Rujukan:** Business Rules, butir 13 sampai 15; WHO, One Up Supervisor; WHAT, tabel In Scope.

**Ketentuan:** Business Rules menetapkan bagian ringkasan sesuai peran dan tahap, nilai bagian yang dapat dimasukkan secara manual oleh atasan langsung, serta perhitungan otomatis nilai keseluruhan dengan rumus `Overall Form Rating = Σ(Section Rating × Section Weight) / Σ(Section Weight)`. Sebelum PA berstatus `Completed`, sistem harus menampilkan tanda `-` sebagai nilai keseluruhan pada tampilan karyawan. Bagian peran One-Up Supervisor menetapkan ringkasan sebagai hanya baca. Tabel In Scope berbeda karena menyebut nilai keseluruhan dapat diubah secara manual. Kedua rumusan dipertahankan; kewenangan perubahan nilai keseluruhan perlu dikonfirmasi sebelum ketentuan ini digunakan sebagai acuan penilaian konsistensi.

### KON-PA-004: Membatasi akses dan merekam jejak audit

**Rujukan:** WHO, Organization Development (OD) Admin dan Direct Supervisor; Business Rules, butir 5, 10, 11, 16, dan 19; WHAT, tabel In Scope.

**Ketentuan:** Sistem harus memberi OD akses ke seluruh PA, status, riwayat nilai, riwayat komentar, dan jejak audit. Ekspor untuk normalisasi, impor, impor ulang, penyesuaian nilai individual, dan finalisasi hanya dapat dilakukan OD. Karyawan mengakses penilaiannya sendiri sesuai tahap. Atasan langsung dapat melihat penilaian diri bawahan, sedangkan One-Up Supervisor dapat melihat penilaian diri dan penilaian atasan langsung. Business Rules butir 11 membatasi riwayat perubahan nilai hanya kepada OD, sedangkan uraian peran Direct Supervisor menyebut akses terhadap riwayat persetujuan dan riwayat nilai yang diizinkan. Perbedaan akses riwayat nilai ini belum terselesaikan dan perlu dikonfirmasi sebelum menjadi acuan penilaian konsistensi. Sistem harus mencatat perubahan nilai, komentar, persetujuan atau penyelesaian peninjauan, pengembalian, perubahan peninjau, impor, impor ulang, dan finalisasi dalam jejak audit.

## Batas cakupan

Aktivitas pada Goal Management tidak memengaruhi nilai atau perhitungan PA. Integrasi Activity Plan dengan PA, pemberian nilai otomatis ketika penilaian diri belum selesai, tampilan selisih antara nilai diri dan nilai atasan, bagian tanda tangan, serta bagian pengakuan (`Acknowledge Section`) berada di luar cakupan. Pembahasan normalisasi departemen dilakukan di luar sistem. Rujukan batas ini adalah WHAT, tabel Out Scope, dan Business Rules butir 16 serta 22 sampai 24.

## Ambiguitas dan batas interpretasi

- Tabel In Scope menyebut `Overall Form Rating` dapat diubah secara manual, sedangkan Business Rules butir 13 dan 15 menetapkan perhitungan otomatis serta nilai manual pada tingkat bagian. KON-PA-003 mencatat kedua rumusan tanpa memilih salah satunya sebagai keputusan bisnis.
- Uraian peran Direct Supervisor mengizinkan akses riwayat nilai yang diperbolehkan, sedangkan Business Rules butir 11 membatasi seluruh riwayat perubahan kepada OD. KON-PA-004 mempertahankan kedua pernyataan.
- Uraian peran One-Up Supervisor menyebut aksi `Approve`, sedangkan alur One-Up Supervisor Review menyebut `Submit` oleh peninjau terakhir. REQ-PA-004 menggunakan istilah menyelesaikan peninjauan; nama dan arti transisinya perlu diselaraskan jika menjadi objek diagram.
- Sumber menyediakan pilihan melewati peninjau atau menunjuk pengganti jika atasan mengundurkan diri sebelum menilai, tetapi belum merinci kondisi pemilihan masing-masing jalur. REQ-PA-013 tidak menentukan pilihan secara sepihak.

