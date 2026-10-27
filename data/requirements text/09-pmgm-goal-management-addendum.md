# Kebutuhan Riset: Adendum Pengelolaan Sasaran Kinerja (PMGM Goal Management Addendum)

## Sumber dan ruang lingkup

- Source: `data/raw/BRD20Goal20-%20Adendum.md`
- Aktor: atasan yang berwenang melakukan cascade, Supervisor, serta karyawan Staff dan Non-Staff.
- Cakupan: tiga aturan bisnis tambahan mengenai urutan cascade, kewenangan cascade untuk Non-Staff, dan penyimpanan draf sebelum menerima cascade.
- Dokumen terkait: `08-pmgm-goal-management.md` dan BRD utamanya, `data/raw/BRD_PMGM_Goal_Management.md`. Aturan adendum dibaca bersama dokumen utama.

## Skenario kebutuhan

### REQ-GMA-001: Melakukan cascade setelah pengajuan KPI atasan

**Rujukan:** Expected New System Business Flow, Business Rule, butir 8.

**Kebutuhan:** Atasan mengajukan KPI miliknya sebelum menurunkan KPI kepada bawahan melalui cascade. Sistem harus mengizinkan cascade dari atasan kepada bawahan hanya setelah atasan mengajukan KPI tersebut.

### REQ-GMA-002: Membatasi cascade kepada karyawan Non-Staff

**Rujukan:** Expected New System Business Flow, Business Rule, butir 9.

**Kebutuhan:** Supervisor melakukan cascade KPI kepada karyawan Non-Staff. Sistem harus membatasi kewenangan melakukan cascade kepada karyawan Non-Staff hanya pada Supervisor.

### REQ-GMA-003: Menyimpan draf sebelum menerima cascade

**Rujukan:** Expected New System Business Flow, Business Rule, butir 10.

**Kebutuhan:** Karyawan Staff maupun Non-Staff membuat dan menyimpan draf KPI meskipun belum menerima KPI hasil cascade dari atasan. Sistem harus menyediakan kemampuan membuat dan menyimpan draf tersebut tanpa mensyaratkan penerimaan cascade.

## Ketentuan pendukung

### KON-GMA-001: Membedakan penyimpanan draf dari pengajuan KPI

**Rujukan:** Adendum, Business Rule butir 10; BRD utama, 5.2 Summary, A. KPI Creation & Validation dan B. Cascade KPI; 5.3 Business Rules, butir 10.

**Ketentuan:** Sebagai interpretasi gabungan adendum dan BRD utama, kemampuan menyimpan draf tanpa menerima cascade harus dibedakan dari kemampuan mengajukan KPI. Izin menyimpan draf tidak menghapus validasi jumlah dan bobot KPI pada BRD utama. Pengajuan tetap mengikuti validasi bobot total dan bobot minimum cascade yang telah dikonfirmasi. Adendum sendiri tidak menyebut nilai ambang minimum cascade. Ketentuan pengajuan yang bergantung pada ambang tersebut belum dapat dijadikan acuan penilaian konsistensi berbasis nilai tertentu sebelum konflik pada BRD utama diselesaikan.

## Batas cakupan

Dokumen ini memuat tiga penegasan aturan bisnis, bukan spesifikasi mandiri untuk seluruh Goal Management. Proses peninjauan, persetujuan, notifikasi, pengaturan periode, dan validasi lain tetap dirujuk dari BRD utama. Skenario yang sama pada dokumen utama dan adendum memiliki sumber yang saling berkaitan dan tidak boleh dianggap sebagai dua bukti independen tanpa penandaan hubungan sumber.

## Ambiguitas dan batas interpretasi

- Adendum tidak menyelesaikan perbedaan minimum bobot cascade antara 40% pada diagram dan 50% pada teks BRD utama.
- Adendum menegaskan pengajuan KPI atasan sebelum cascade, kewenangan Supervisor untuk Non-Staff, serta pembuatan dan penyimpanan draf tanpa cascade. Adendum tidak menyatakan bahwa seluruh aturan lain pada BRD utama digantikan.
- KON-GMA-001 merupakan interpretasi gabungan dua dokumen. Validasi pengajuan di dalamnya tidak boleh diatribusikan sebagai aturan yang tertulis seluruhnya dalam adendum.

