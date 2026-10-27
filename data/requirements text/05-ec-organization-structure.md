# Kebutuhan Riset: Pengelolaan Struktur Organisasi (EC Organization Structure)

## Sumber dan ruang lingkup

- Source: `data/raw/BRD - EC Organization Structure.md`
- Tujuan: mengelola data induk unit organisasi secara terpusat serta menampilkan struktur dan riwayat organisasi berdasarkan tanggal berlaku.
- Aktor sistem: Organization Development (OD) untuk membuat, membaca, dan memperbarui data; karyawan untuk membaca informasi sesuai hak akses.
- Batas proses: usulan, peninjauan, dan persetujuan perubahan organisasi berlangsung secara manual. Bagian proses di dalam aplikasi mencakup pembaruan struktur yang telah disetujui, penyimpanan, visualisasi, dan penelusuran riwayat.

## Skenario kebutuhan

### REQ-ORG-001: Memperbarui struktur organisasi yang telah disetujui

**Rujukan:** §2.2 In Scope; §2.4 User Roles and Accessibilities; §4.1 Manage Organizational Structure Business Process, Flow Internal, Update Organization Structure; §5 Organization Structure Policies / Business Rules.

**Kebutuhan:** Setelah tahapan persetujuan manual yang berlaku selesai, OD harus dapat menambahkan atau mengubah data organisasi melalui aplikasi. Sistem harus mendukung pembaruan langsung maupun impor berkas struktur organisasi dalam format CSV atau XLSX. Setiap unit yang ditambahkan atau diubah harus memiliki identitas unik dan hubungan hierarki yang valid. Sistem harus menyimpan perubahan struktur yang telah disetujui sehingga struktur terbaru menjadi referensi aktif bagi sistem dan modul terkait. Sistem harus mempertahankan riwayat perubahan menggunakan tanggal berlaku dan jejak audit.

### REQ-ORG-002: Melihat struktur organisasi pada tanggal tertentu

**Rujukan:** §2.2 In Scope; §2.5 Risks and Mitigation, Mitigasi; §5 Organization Structure Policies / Business Rules.

**Kebutuhan:** Pengguna harus dapat memilih tanggal atau periode struktur organisasi yang ingin dilihat. Sistem harus menampilkan bagan organisasi sesuai struktur yang berlaku pada tanggal tersebut, termasuk ketika pengguna memilih tanggal historis. Sistem juga harus menyediakan tampilan detail profil karyawan dalam ruang lingkup visualisasi organisasi. OD dapat melihat seluruh struktur organisasi perusahaan, sedangkan karyawan dan pengguna lain hanya dapat membaca informasi sesuai hak akses yang diberikan.

### REQ-ORG-003: Mencari informasi dalam struktur organisasi

**Rujukan:** §5 Organization Structure Policies / Business Rules.

**Kebutuhan:** Pengguna harus dapat mencari informasi struktur organisasi berdasarkan nama departemen, nama posisi, nama karyawan, atau ID NH. Sistem harus menyediakan pencarian tersebut melalui integrasi dengan modul terkait dan membatasi informasi yang dapat diakses sesuai kewenangan pengguna.

### REQ-ORG-004: Mengekspor struktur organisasi

**Rujukan:** §2.2 In Scope; §5 Organization Structure Policies / Business Rules.

**Kebutuhan:** Sistem harus menyediakan fungsi ekspor struktur organisasi ke format PDF dan PNG. Fungsi ini menggunakan informasi struktur organisasi yang dapat diakses oleh pengguna sesuai hak akses yang berlaku.

### REQ-ORG-005: Menyediakan referensi organisasi dan mencerminkan perubahan ESC

**Rujukan:** §2.2 In Scope; §5 Organization Structure Policies / Business Rules.

**Kebutuhan:** Sistem harus menyediakan struktur organisasi sebagai referensi bagi modul Employee Central lainnya. Jika perubahan data karyawan melalui proses Employee Status Change (ESC), seperti promosi, transfer, atau reklasifikasi, memengaruhi penempatan atau visualisasi organisasi, sistem harus mencerminkan perubahan yang relevan sesuai konfigurasi yang berlaku.

## Ketentuan pendukung

### KON-ORG-001: Identitas unit, hierarki, dan standar kode

**Rujukan:** §2.5 Risks and Mitigation, Mitigasi; §5 Organization Structure Policies / Business Rules.

**Ketentuan:** Setiap unit organisasi harus memiliki identitas unik dan berada dalam hierarki yang valid. Sistem harus memvalidasi hubungan unit induk dan unit bawahan untuk mencegah hierarki yang tidak valid. Standar kode Directorate, Division, Department, dan Section harus mengikuti kebijakan HR Organization Development. Perubahan organisasi harus mempertahankan riwayat melalui tanggal berlaku dan jejak audit agar perubahan tetap dapat ditelusuri.

### KON-ORG-002: Prasyarat persetujuan manual

**Rujukan:** §4.1 Manage Organizational Structure Business Process, Flow External dan Catatan.

**Ketentuan:** Pengaju perubahan harus menyiapkan proposal, bagan organisasi baru, dan justifikasi perubahan untuk ditinjau OD Section. OD menilai kelengkapan dokumen, kesesuaian struktur, dan alasan bisnis sebelum proposal diteruskan kepada Manager Training & Development, Senior Manager HCM, serta GM Operations/GMO atau Director in Charge sesuai jalur yang berlaku. BRD juga mencantumkan peninjauan Board of Director. Untuk perubahan tahunan atau kuartalan pada tingkat di bawah Department, persetujuan cukup sampai GMO atau Director in Charge sesuai jenjang organisasi; perubahan pada tingkat Department dan di atasnya harus mencapai Direktur. Jika proposal tidak disetujui pada salah satu tahap, proposal kembali kepada pengaju dan OD untuk direvisi serta diajukan kembali. Seluruh peninjauan dan persetujuan tersebut berlangsung di luar aplikasi; hanya Department TD-OD yang melakukan pembaruan dalam sistem setelah persetujuan lengkap.

### KON-ORG-003: Penyesuaian jalur pelaporan dan kewenangan akses

**Rujukan:** §2.4 User Roles and Accessibilities; §4.1 Manage Organizational Structure Business Process, Catatan; §5 Organization Structure Policies / Business Rules.

**Ketentuan:** OD berwenang membuat, membaca, dan memperbarui data organisasi, serta mengakses seluruh struktur organisasi perusahaan. Pengguna lain hanya boleh membaca informasi sesuai kewenangannya dan tidak memperoleh hak mengubah struktur. Kebijakan sumber memperbolehkan OD menyesuaikan jalur pelaporan yang tidak mengubah struktur organisasi sewaktu-waktu atas permintaan Business Unit, paling rendah pada tingkat Department Head/Manager. Ketentuan ini merupakan konteks kewenangan bisnis; ruang lingkup modul tetap mengecualikan pengelolaan manager assignment dan jalur pelaporan berbasis posisi.

## Batas cakupan

Modul ini tidak mencakup pembuatan atau pengelolaan posisi, Integrated Position System (IPS) Code, hierarki posisi, penugasan manajer atau jalur pelaporan berbasis posisi, maupun transaksi ESC. Pengelolaan data pribadi dan hubungan kerja karyawan, rekrutmen, orientasi karyawan baru, perencanaan tenaga kerja dan anggarannya, kompensasi, payroll, manfaat, target dan penilaian kinerja, perencanaan suksesi, serta pengelolaan talenta juga berada di luar cakupan.

Integrasi sistem keuangan selain penyediaan referensi Cost Center, administrasi peran keamanan dan otorisasi pengguna, serta perubahan struktur melalui seret dan lepas (drag and drop) tidak termasuk cakupan. Persetujuan proposal organisasi tetap merupakan proses manual yang mendahului pembaruan dalam aplikasi.

## Ambiguitas dan batas interpretasi

- BRD tidak memiliki bab kebutuhan fungsional atau katalog data pembuatan dan perubahan unit yang rinci. Skenario diturunkan dari ruang lingkup, alur To-Be, peran, mitigasi risiko, dan kebijakan modul. Rincian field, pesan validasi, dan perilaku gagal impor belum ditentukan.
- Ketentuan tingkat persetujuan mengikuti Catatan pada §4.1. Hubungan operasional antara istilah Board of Director pada alur dan Direktur pada catatan harus diperjelas jika peneliti akan memodelkan jalur manual secara lebih rinci; dokumen ini tidak menambah tahapan otomatis.
- Sumber menyebut penyesuaian jalur pelaporan sebagai kebijakan OD, tetapi mengecualikan pengelolaan jalur pelaporan berbasis posisi dari modul. Pernyataan tersebut dipertahankan sebagai batas antarmodul, bukan dasar untuk menambahkan fungsi perubahan hierarki posisi di sini.
- Pengaruh ESC pada visualisasi mengikuti konfigurasi yang disebutkan sumber. Detail pemetaan perubahan, waktu sinkronisasi, dan pesan integrasi belum ditetapkan dalam BRD ini.

