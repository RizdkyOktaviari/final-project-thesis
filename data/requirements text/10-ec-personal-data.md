# Penjabaran Kebutuhan: EC Data Pribadi (Personal Data)

## Sumber dan cakupan

- Source: `data/raw/BRD - EC Personal Data.md`
- Peran: Karyawan/Pemohon (Employee/Requestor) dan HR Compensation & Benefit.
- Model: perubahan data pribadi yang dimohonkan mengikuti siklus pengajuan, peninjauan, persetujuan, pencatatan riwayat, dan integrasi, bukan perubahan langsung oleh karyawan.

## Kebutuhan Fungsional

1. Memungkinkan karyawan mengajukan pembaruan pada bagian Data Pribadi yang tercantum, meliputi data pribadi/biografis, alamat, kontak, identitas nasional (National ID), kontak darurat, tanggungan, pembayaran, posisi/organisasi, data pekerjaan/kepegawaian/waktu kerja, dokumen, kompensasi, pendidikan, latar belakang karier, serta keanggotaan/kegiatan sukarela.
2. Menggunakan formulir Data Pribadi yang khusus untuk setiap bagian, memvalidasi kolom wajib dan bukti pendukung, serta hanya mengizinkan satu permohonan berstatus `In Progress` untuk bagian Data Pribadi dan karyawan yang sama.
3. Memungkinkan HR Compensation & Benefit meninjau seluruh perubahan yang dimohonkan beserta buktinya, menyetujui dengan komentar opsional, atau mengembalikan dengan komentar wajib. Karyawan dapat mengedit permohonan yang dikembalikan, mengajukannya kembali, atau menarik kembali permohonan tersebut.
4. Setelah persetujuan, menerapkan perubahan, menyelesaikan alur kerja, mencatat riwayat perubahan, dan memicu pembaruan pada modul lanjutan hanya setelah persetujuan akhir.
5. Mendukung lampiran yang terikat pada permohonan dan mengikuti kebijakan perusahaan, misalnya bukti buku nikah/kartu keluarga untuk perubahan status perkawinan dan bukti kartu keluarga untuk perubahan data anak.
6. Menyediakan status permohonan, riwayat karyawan, riwayat HR, serta log aktivitas yang mencakup pengajuan, persetujuan, pengeditan, pengembalian, pengajuan ulang, penarikan kembali, perubahan data, dan komentar peninjauan.
7. Mengirimkan notifikasi pengajuan, pengajuan ulang, penarikan kembali, dan pengingat kepada HR; serta notifikasi pengembalian dan penyelesaian kepada karyawan.

**Masukan, keluaran, dan batasan kolom fungsional**

- Informasi Pribadi mencakup tanggal berlaku, nama, nama lengkap yang diisi otomatis, sapaan, agama, jenis kelamin, status perkawinan, kewarganegaraan/pengaturan lokal (locale), dan bukti kartu keluarga yang opsional.
- Alamat berupa alamat rumah dengan data geografis, kode pos, dan penanda utama. Kontak mendukung jenis nomor telepon dan email pribadi/kantor.
- Identitas Nasional mendukung KTP dan Paspor, negara, nomor identitas, lampiran, serta penanda utama.
- Kontak Darurat dapat berisi beberapa entri dengan jumlah maksimal dua. Tanggungan memerlukan tanggal berlaku, nama, hubungan, tanggal lahir, dan dapat memiliki lampiran; hanya HR yang dapat menetapkan kelayakan tanggungan saat peninjauan.
- Informasi Pembayaran memuat tanggal mulai/akhir berlaku serta informasi bank/rekening untuk Penggajian/Asuransi. BRD menyatakan bahwa perubahan rekening bank hanya dapat diajukan sekali per tahun.
- Informasi pekerjaan, organisasi, waktu kerja, dan hubungan pekerjaan tercantum sebagai tidak dapat diedit dalam katalog kolom, meskipun muncul dalam daftar bagian yang dapat diajukan secara lebih luas. Gunakan tabel izin pengeditan pada tingkat kolom sebagai aturan yang lebih spesifik, kecuali pihak bisnis mengonfirmasi ketentuan lain.

**Perilaku fungsional tambahan**

- Identitas Nasional dapat memiliki beberapa entri; KTP wajib diisi dan Paspor juga didukung. Satu entri mencakup negara, nomor identitas, lampiran opsional, dan penanda utama. Sumber menyebutkan bahwa ekspatriat dapat memasukkan nomor paspor pada bagian KTP, yang memerlukan keputusan bisnis sebelum implementasi.
- Tanggungan dibatasi maksimal tiga, sedangkan Kontak Darurat dibatasi maksimal dua. Data tanggungan mendukung hubungan antarorang, data pribadi/biografis, Identitas Nasional, alamat, dan beberapa lampiran; kelayakan tanggungan tetap hanya dapat ditetapkan oleh HR. Lampiran tanggungan berbeda dari lampiran karyawan.
- Informasi Pembayaran mengizinkan lebih dari satu rekening. Rekening Asuransi secara bawaan mengikuti rekening Penggajian; kumpulan kolomnya mencakup jenis/klasifikasi asuransi selain data bank/pembayaran. Kolom tanggal akhir berlaku dinonaktifkan oleh sistem.
- Kelompok kolom yang dapat dikelola dan diedit karyawan mencakup data pribadi/biografis, alamat rumah, telepon, Identitas Nasional, kontak darurat, tanggungan, dokumen pribadi, dan jumlah kompensasi yang ditentukan. Email kontak, posisi, organisasi, detail pekerjaan, informasi waktu kerja, hubungan pekerjaan, dan Target Pembayaran (Pay Targets) ditandai sebagai hanya baca dalam katalog terperinci.
- Kolom dokumen pribadi mencakup negara/wilayah, jenis, judul, nomor, tanggal/tempat/otoritas penerbitan, tanggal kedaluwarsa, dan lampiran. Pendidikan, tanda kehormatan/penghargaan, pengalaman kerja internal, pekerjaan sebelumnya, kursus, sertifikasi, keanggotaan profesi, dan keterlibatan dalam kegiatan sukarela merupakan bagian permohonan yang tercantum dalam sumber; katalog kolom terperincinya tetap tersedia dalam BRD.

**Aturan perilaku dan prasyarat**

- Kolom wajib harus lengkap sebelum pengajuan. Ukuran file tidak boleh melebihi batas yang dikonfigurasi.
- Pengembalian memerlukan komentar. Penarikan kembali hanya diperbolehkan untuk status `Sent Back`; permohonan yang telah ditarik kembali tidak dapat diproses lagi.
- Perubahan rekening bank dapat diajukan sekali per tahun.
- HR dapat menandai tanggungan sebagai `Eligible` atau `Not Eligible` saat peninjauan/persetujuan.
- Permohonan hanya memperbarui data resmi setelah persetujuan dan tanggal berlaku (Effective Date) yang ditetapkan. Administrator HR yang berwenang juga dapat mengajukan perubahan yang diizinkan; hal ini tidak mengesampingkan aturan kepemilikan permohonan oleh karyawan dalam layanan mandiri biasa.
- Setelah persetujuan, integrasi dapat memperbarui Struktur Organisasi, Pengelolaan Posisi, Penggajian & Kompensasi, serta Penggantian Biaya Tunjangan (Benefit Reimbursement), bergantung pada jenis perubahan.

**Perilaku akses, audit, dan kerahasiaan**

- Identitas Nasional, tanggal lahir, alamat, kontak pribadi, kontak darurat, pembayaran, tanggungan, penggolongan (grading), dan gaji pokok bersifat rahasia. Terapkan RBAC dan tolak pembacaan atau perubahan tanpa kewenangan.
- Karyawan hanya melihat data pribadi, permohonan, dan riwayatnya sendiri. HR Compensation & Benefit melihat permohonan/bukti yang berada dalam lingkup tanggung jawabnya.
- Dokumen pendukung tetap bersifat rahasia dan terikat pada permohonan. Karyawan tidak dapat mengubah atau menghapus bukti yang tersimpan setelah permohonan memasuki proses persetujuan, kecuali melalui mekanisme perubahan yang disediakan.
- Jejak audit bersifat hanya baca dan mencakup pengguna, peran, aktivitas, waktu, dan ID permohonan. Riwayat perubahan mencakup bagian, kolom yang berubah, nilai sebelumnya, nilai baru, pelaku, waktu, dan ID permohonan.
- Migrasi riwayat Data Pribadi mencakup tahun 2021 hingga catatan terbaru yang tersedia. Pemutusan hubungan kerja, pelaksanaan penggajian, rekrutmen, evaluasi kinerja, pengelolaan organisasi/posisi, dan ESC berada di luar modul ini, meskipun menggunakan data yang telah disetujui dari modul ini.

**Skenario kasus penggunaan**

1. Karyawan mengajukan perubahan alamat yang valid. Permohonan alamat kedua yang masih dalam proses diblokir, sedangkan permohonan untuk bagian lain yang memenuhi syarat tetap dapat diajukan.
2. HR mencoba mengembalikan permohonan tanpa komentar dan tindakan tersebut diblokir; setelah komentar diberikan, karyawan memperbaiki dan mengajukan ulang permohonan.
3. Permohonan yang dikembalikan dapat ditarik kembali dan menjadi tidak dapat diproses.
4. Pengguna yang tidak berwenang tidak dapat melihat Identitas Nasional, data pembayaran, atau bukti terlampir.
5. Perubahan relevan yang telah disetujui memperbarui modul lanjutan yang sesuai hanya setelah alur kerja selesai.

## Ambiguitas sumber di luar himpunan kebutuhan yang dapat dieksekusi

- Konfirmasikan bagian mana dalam daftar yang memang dapat diedit oleh karyawan ketika tabel kolom terperinci menandai kolom tersebut sebagai hanya baca.
- Konfirmasikan format file yang diizinkan dan batas ukuran yang dikonfigurasi.
- Konfirmasikan apakah aturan pembayaran sekali per tahun berlaku untuk seluruh perubahan rekening atau hanya subjenis pembayaran tertentu.
