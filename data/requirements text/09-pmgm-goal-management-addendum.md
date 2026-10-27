# Penjabaran Kebutuhan: Adendum PMGM Pengelolaan Sasaran (Goal Management Addendum)

## Sumber dan cakupan

- Source: `data/raw/BRD20Goal20-%20Adendum.md`
- Dokumen ini merupakan adendum Goal Management. Dokumen ini memuat tiga aturan bisnis yang berlaku dan sebaiknya dibaca bersama `08-pmgm-goal-management.md`.

## Kebutuhan Fungsional

1. Manajer hanya dapat menurunkan KPI kepada bawahan setelah mengajukan KPI miliknya sendiri.
2. Untuk Non-Staff, hanya Supervisor yang dapat menurunkan KPI kepada karyawan.
3. Karyawan Staff dan Non-Staff dapat membuat dan menyimpan draf KPI bahkan sebelum menerima KPI turunan dari manajer.

**Implikasi terhadap spesifikasi perilaku**

Pisahkan kemampuan membuat dan menyimpan draf dari kemampuan mengajukan. Pembuatan draf tidak boleh mensyaratkan penerimaan KPI turunan. Pengajuan tetap harus menerapkan validasi KPI turunan dan total bobot yang telah dikonfirmasi dari BRD utama Goal Management.

## Ambiguitas sumber di luar himpunan kebutuhan yang dapat dieksekusi

Adendum ini menegaskan kembali urutan penurunan KPI dan aturan draf pada BRD utama. Adendum ini tidak menyelesaikan konflik bobot minimum KPI turunan sebesar 40% versus 50% pada BRD utama.
