# Kebutuhan Riset: Pengelolaan Sasaran Kinerja (PMGM Goal Management)

## Sumber dan ruang lingkup

- Source: `data/raw/BRD_PMGM_Goal_Management.md`
- Aktor: administrator Organization Development (OD), karyawan Staff dan Non-Staff, atasan langsung (Direct Supervisor), atasan satu tingkat di atas atasan langsung (One-Up Supervisor), Manager, dan Senior Manager. Department Head, Senior Manager/Director, serta GMO/Director menerima eskalasi pengingat sesuai konfigurasi.
- Cakupan: pengaturan periode, formulir KPI, penurunan sasaran dari atasan kepada bawahan (cascade), pengajuan, peninjauan, revisi, aktivitas, pemantauan, dan ekspor.
- Dokumen terkait: `09-pmgm-goal-management-addendum.md` memuat tiga penegasan aturan cascade dan penyimpanan draf. Nama status dan istilah konfigurasi tertentu dipertahankan untuk ketertelusuran.

## Skenario kebutuhan

### REQ-GM-001: Mengatur periode dan peserta pengisian KPI

**Rujukan:** 3.2.1 In Scope, butir 1, 2, dan 13; 3.4 WHO, Organization Development (OD) Admin; 5.2 Summary, butir 1 dan 2; 5.3 Business Rules, butir 2 dan 6.

**Kebutuhan:** OD harus dapat membuat periode pengisian KPI dengan tanggal mulai dan tenggat, serta membuat, mengubah, menghapus, meluncurkan, menutup, dan membuka kembali formulir sesuai kewenangannya. OD menentukan karyawan yang wajib mengikuti atau dikecualikan dari periode tersebut. Sistem harus mengecualikan karyawan yang ditetapkan OD dari kewajiban pengisian dan notifikasi periode KPI. Setelah periode ditutup, sistem harus mencegah karyawan membuat, mengubah, dan menghapus KPI. OD dapat membuka kembali periode apabila diperlukan setelah memperoleh persetujuan pejabat yang berwenang di luar sistem.

### REQ-GM-002: Membuat dan menyimpan KPI

**Rujukan:** 5.2 Summary, A. KPI Creation & Validation, butir 3 sampai 6, dan K. E-Form, butir 39; 5.3 Business Rules, butir 10; adendum, Business Rule butir 10.

**Kebutuhan:** Selama periode terbuka, karyawan harus dapat membuat, mengubah, menghapus, dan menyimpan KPI miliknya. Sistem harus memilih formulir Staff atau Non-Staff secara otomatis berdasarkan kategori karyawan. Karyawan Staff maupun Non-Staff dapat membuat dan menyimpan draf meskipun belum menerima cascade dari atasan. Sistem harus memvalidasi paling banyak 10 KPI, total bobot 100%, serta total bobot perspektif Learning & Growth paling besar 15%. Bobot setiap KPI Staff harus berada antara 5% dan 25%, sedangkan bobot setiap KPI Non-Staff antara 5% dan 30%. Jika salah satu validasi tersebut tidak terpenuhi, sistem harus menampilkan pesan kesalahan serta mencegah penyimpanan dan pengajuan KPI. Izin menyimpan draf tanpa cascade tidak menghapus validasi tersebut.

### REQ-GM-003: Menurunkan KPI kepada bawahan

**Rujukan:** 3.2.1 In Scope, butir 12; 5.2 Summary, B. Cascade KPI, butir 7 dan 8; 5.3 Business Rules, butir 1, 3, 8 tentang cascade, dan 9.

**Kebutuhan:** Atasan harus menyelesaikan dan mengajukan KPI miliknya sebelum melakukan cascade kepada bawahan. Sistem harus mengizinkan cascade sesuai struktur organisasi dan kebijakan, dengan Supervisor sebagai tingkat jabatan terendah yang dapat melakukannya. Senior Manager atau Division Head yang langsung berada di bawah BoD dapat mengacu pada sasaran BoD dan menurunkan KPI kepada bawahan langsung. Senior Manager, Manager, atau One-Up Supervisor dapat menurunkan KPI kepada bawahan langsung sesuai kewenangannya. Untuk Staff, Direct Supervisor tidak boleh melompati tingkat organisasi. Untuk Non-Staff, cascade hanya dapat dilakukan oleh Supervisor. Saat melakukan cascade, Direct Supervisor dapat menandai KPI sebagai `Mandatory`; sistem harus mencegah bawahan mengubah atau menghapus KPI yang menerima penanda tersebut.

### REQ-GM-004: Mengajukan KPI untuk ditinjau

**Rujukan:** 5.2 Summary, B. Cascade KPI, butir 9 dan 10, serta C. Alur Submit KPI, butir 11 sampai 13; 5.1 Goals Management, Diagram; 5.3 Business Rules, butir 10.

**Kebutuhan:** Setelah menyusun KPI, karyawan mengajukannya untuk ditinjau. Sistem harus memvalidasi persyaratan jumlah dan bobot KPI serta bobot minimum KPI hasil cascade yang diterima. Jika bobot cascade belum memenuhi ambang yang berlaku, sistem harus mencegah pengajuan. Setelah pengajuan yang memenuhi persyaratan, sistem harus mengubah status menjadi `Submitted`, memberi notifikasi kepada atasan langsung, dan mencegah perubahan KPI oleh karyawan selama pengajuan atau peninjauan berlangsung sampai karyawan menerima status revisi. Nilai ambang cascade belum memiliki satu rumusan yang konsisten: diagram menyebut 40%, sedangkan teks menyebut nilai bawaan 50% yang dapat dikonfigurasi OD. Ambang ini harus dikonfirmasi sebelum skenario dipakai sebagai acuan penilaian konsistensi berbasis nilai tertentu.

### REQ-GM-005: Meninjau KPI oleh atasan langsung

**Rujukan:** 5.2 Summary, D. Review Direct Supervisor, butir 14 sampai 16, dan E. Review Organization Development Section, butir 17 sampai 20.

**Kebutuhan:** Atasan langsung menerima notifikasi ketika bawahan mengajukan KPI, lalu meninjau KPI tersebut. Jika KPI sesuai, atasan langsung memberikan persetujuan agar KPI melanjutkan alur peninjauan OD. Jika KPI perlu diperbaiki, atasan langsung mengembalikan KPI dengan catatan revisi wajib. Sistem harus mengubah status menjadi `Revise Required` dan memberi notifikasi kepada karyawan. Karyawan memperbaiki KPI dan mengajukannya kembali; sistem harus mengembalikannya ke peninjauan atasan langsung. Sistem juga harus mengirimkan pengingat kepada atasan langsung ketika masih ada KPI bawahan yang belum ditinjau.

### REQ-GM-006: Melakukan peninjauan akhir oleh OD

**Rujukan:** 5.2 Summary, E. Review Organization Development Section, butir 17 sampai 22, serta F. Notification, butir 23.

**Kebutuhan:** OD menerima notifikasi atas KPI yang menunggu peninjauan, lalu melakukan peninjauan dan validasi akhir. Jika KPI sesuai, OD memberikan persetujuan. Sistem harus mengubah status menjadi `Completed`, memberi notifikasi kepada karyawan, dan mengunci perubahan KPI meskipun periode belum berakhir. Jika KPI perlu diperbaiki, OD mengembalikannya dengan catatan revisi wajib. Sistem harus menetapkan status `Revise Required OD` dan memberi notifikasi kepada karyawan. Setelah karyawan memperbaiki dan mengajukan ulang, sistem harus mengarahkan KPI kembali ke atasan langsung sebelum peninjauan OD.

### REQ-GM-007: Mengelola aktivitas yang terhubung ke KPI

**Rujukan:** 3.2.1 In Scope, butir 6; 3.4 WHO, Staff & Non Staff, Direct Supervisor, dan One up Supervisor; 5.2 Summary, butir 2; 5.3 Business Rules, butir 6.

**Kebutuhan:** Selama periode pengisian terbuka, sistem harus memungkinkan pengguna yang berwenang membuat, mengubah, dan menghapus aktivitas yang terhubung dengan KPI, termasuk pengelolaan lampiran, status, dan pemilik aktivitas. Atasan harus dapat melihat aktivitas bawahan sesuai kewenangannya. Setelah periode pengisian KPI ditutup, sistem harus tetap memungkinkan karyawan membuat dan mengubah aktivitas yang terhubung ke KPI, sedangkan pembuatan, perubahan, dan penghapusan KPI tidak diizinkan.

### REQ-GM-008: Merevisi KPI pada periode tengah tahun

**Rujukan:** 5.2 Summary, J. Revisi Mid-Year, butir 36 dan 37.

**Kebutuhan:** OD membuka periode revisi tengah tahun (`Mid-Year`). Selama periode revisi tersebut, sistem harus memungkinkan karyawan menyesuaikan KPI yang telah dibuat. OD harus dapat mengubah status KPI karyawan apabila diperlukan untuk proses revisi. Mekanisme ini merupakan proses revisi yang dinyatakan sumber dan tidak memberikan izin pengeditan umum atas KPI `Completed` di luar proses tersebut.

### REQ-GM-009: Menangani perubahan jabatan dan struktur organisasi

**Rujukan:** 3.5 WHAT IF, Mitigation; 5.2 Summary, J. Revisi Mid-Year, butir 38; 5.3 Business Rules, butir [8.] tentang perubahan posisi.

**Kebutuhan:** Jika jabatan atau departemen karyawan berubah selama periode pengisian KPI, sistem harus mengembalikan status KPI menjadi draf agar karyawan dapat menyusun KPI sesuai jabatan atau departemen baru. Jika perubahan terjadi di luar jadwal pengisian, OD dapat membuka kembali periode sesuai persetujuan yang disyaratkan sumber. Sistem harus menyesuaikan hubungan atasan dan bawahan berdasarkan struktur organisasi terbaru. Jika posisi Manager berubah selama Goal Management berlangsung, OD menyesuaikan alur agar pihak yang berwenang dapat melanjutkan peninjauan dan perubahan KPI.

### REQ-GM-010: Mengirim notifikasi tindakan KPI

**Rujukan:** 5.2 Summary, F. Notification, butir 23, 25, dan 27.

**Kebutuhan:** Ketika karyawan mengajukan KPI, sistem harus mengirimkan notifikasi dalam aplikasi kepada pengaju dan atasan langsung, serta surel kepada atasan langsung. Ketika KPI disetujui, sistem harus mengirimkan notifikasi dalam aplikasi kepada pengaju dan pemberi persetujuan, serta surel kepada pengaju. Ketika KPI dikembalikan untuk revisi, sistem harus mengirimkan notifikasi dalam aplikasi kepada pengaju dan pemberi persetujuan, serta surel kepada pengaju. Sistem harus memberi tahu karyawan ketika KPI mencapai status `Completed`. OD harus dapat mengonfigurasi format, durasi, penerima, dan isi notifikasi.

### REQ-GM-011: Mengirim pengingat bertingkat menjelang tenggat

**Rujukan:** 5.2 Summary, F. Notification, butir 24, 26, dan 27.

**Kebutuhan:** Ketika tenggat pengisian mendekat dan ada bawahan yang belum mengajukan KPI, sistem harus mengirimkan pengingat kepada atasan langsung. Sistem harus mendukung pengiriman bertahap menurut struktur organisasi, dengan konfigurasi bawaan tiga minggu sebelum tenggat kepada Department Head, dua minggu sebelum tenggat kepada Senior Manager/Director, dan satu minggu sebelum tenggat kepada GMO/Director. OD harus dapat menyesuaikan konfigurasi pengingat tersebut.

### REQ-GM-012: Mengekspor KPI sesuai kewenangan

**Rujukan:** 5.2 Summary, I. Export, butir 33 sampai 35; 3.2.1 In Scope, butir 14.

**Kebutuhan:** Karyawan harus dapat mengekspor KPI miliknya ke dalam PDF. Atasan langsung harus dapat mengekspor KPI bawahan yang berada dalam lingkup kewenangannya sesuai struktur organisasi ke dalam PDF. OD harus dapat mengekspor data KPI per departemen secara massal ke dalam Excel.

## Ketentuan pendukung

### KON-GM-001: Menggunakan perspektif KPI

**Rujukan:** 5.3 Business Rules, butir 4 dan 5.

**Ketentuan:** Formulir Staff menggunakan perspektif Finance, Stakeholder, Internal Process, dan Learning & Growth. Karyawan Staff tidak wajib menggunakan seluruh perspektif apabila tidak sesuai dengan pekerjaan atau sasaran yang ditentukan. Penggunaan perspektif Non-Staff mengikuti formulir Non-Staff yang dirujuk sumber.

### KON-GM-002: Mengonfigurasi formulir dan aturan bisnis

**Rujukan:** 3.2.1 In Scope, butir 2, 5, 7, dan 11; 3.4 WHO, Organization Development (OD) Admin.

**Ketentuan:** Sistem harus memungkinkan OD mengonfigurasi kolom formulir, validasi dinamis, arah penilaian (`Rating Direction`), alur persetujuan, dan aturan bisnis KPI. Pengaturan validasi mencakup kolom wajib, jumlah maksimum KPI, batas bobot, serta persyaratan pengajuan. Alur persetujuan menggunakan struktur organisasi dan mendukung pengalihan ketika ada posisi kosong. OD juga mengatur aturan cascade, penggunaan perspektif, batas bobot, jumlah KPI, dan notifikasi. Uraian sumber mengenai label `High is Good` dan `High is Bad` belum memberikan pembeda yang konsisten; makna arah penilaian harus dikonfirmasi sebelum digunakan sebagai acuan penilaian konsistensi.

### KON-GM-003: Membatasi akses dan menyimpan riwayat

**Rujukan:** 5.2 Summary, G. Visibility, butir 28 sampai 31, dan H. Audit Trail, butir 32; 3.2.1 In Scope, butir 8.

**Ketentuan:** Sistem harus membatasi karyawan pada akses dan pengelolaan KPI miliknya sendiri. Atasan langsung, Manager, Senior Manager, dan One-Up Supervisor dapat melihat KPI bawahan sesuai struktur organisasi dan kewenangannya. OD dapat melihat KPI seluruh karyawan beserta status, riwayat peninjauan, dan riwayat revisi. Sistem harus menyimpan riwayat perubahan KPI, cascade, persetujuan, revisi, dan catatan peninjauan sebagai jejak audit.

## Batas cakupan

Pengiriman otomatis KPI ke OD saat tenggat tercapai, papan aktivitas Kanban dengan seret dan lepas, pembuatan KPI BoD di dalam sistem, serta permintaan persetujuan peluncuran atau pembukaan dan penutupan formulir di dalam sistem berada di luar cakupan. Persetujuan pejabat untuk membuka kembali periode dilakukan di luar sistem sesuai 5.2 Summary butir 2 dan 5.3 Business Rules butir 6. Rujukan pengecualian adalah 3.2.2 Out Scope.

## Ambiguitas dan batas interpretasi

- Ambang minimum bobot cascade berbeda antara 5.1 Goals Management, Diagram (40%) dan 5.2 Summary, B. Cascade KPI, butir 9 (nilai bawaan 50% yang dapat dikonfigurasi OD). Dokumen ini tidak menetapkan salah satunya sebagai nilai yang benar. Penggunaan nilai tersebut pada REQ-GM-004 memerlukan keputusan bisnis.
- Sumber menyatakan ambang cascade dapat dikonfigurasi OD, tetapi belum menjelaskan apakah konfigurasi berlaku per periode, formulir, atau unit organisasi.
- Adendum menegaskan urutan pengajuan KPI atasan sebelum cascade, kewenangan Supervisor untuk Non-Staff, serta penyimpanan draf tanpa cascade. Adendum tidak menetapkan ambang minimum cascade atau mengganti validasi bobot dari BRD utama.
- Uraian `Rating Direction` pada 3.2.1 In Scope menyebut nilai lebih tinggi lebih baik untuk `High is Good`, tetapi menjelaskan `High is Bad` dengan frasa nilai lebih rendah lebih buruk. Makna kedua arah tidak boleh diperbaiki berdasarkan asumsi; KON-GM-002 mempertahankan kebutuhan konfigurasi sambil menandai definisinya sebagai belum pasti.
- Sumber memakai nomor 8 dua kali pada 5.3 Business Rules. Rujukan di atas membedakan aturan perubahan posisi dari aturan urutan cascade agar ketertelusuran tidak tertukar.
- Ringkasan turunan sebelumnya mengaitkan pengaturan wajib tidaknya KPI cascade dengan OD. BRD 3.2.1 In Scope butir 12 secara eksplisit menyebut Direct Supervisor sebagai pihak yang memilih penanda `Mandatory` saat cascade. REQ-GM-003 mengikuti aktor yang dinyatakan BRD; kewenangan tambahan OD atas pilihan tersebut belum ditetapkan oleh bagian sumber itu.

