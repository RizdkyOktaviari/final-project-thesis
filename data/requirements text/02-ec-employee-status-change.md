# Penjabaran Kebutuhan: EC Perubahan Status Karyawan (Employee Status Change)

## Sumber dan cakupan

- Source: `data/raw/BRD - EC Employee Status Change.md`
- Jenis perubahan yang didukung: reklasifikasi, mutasi, perubahan jam atau jadwal kerja, perpanjangan kontrak, promosi, dan demosi.
- Peran utama: Pemohon (Requestor), Organization Development, HR Admin, pemberi persetujuan, penerima delegasi persetujuan, dan karyawan yang bersangkutan.

## Kebutuhan Fungsional

1. Memungkinkan pemohon membuat satu permohonan Employee Status Change (ESC) per karyawan pada satu waktu, melengkapi kolom dan bukti wajib, mengajukan permohonan, merevisi setelah permohonan dikembalikan, atau menarik kembali permohonan sebelum proses persetujuan selesai.
2. Menggunakan satu formulir ESC dengan perilaku sesuai peran. Pemohon mengedit status karyawan, nama jabatan, departemen, atasan pelaporan, serta jadwal atau jam kerja. OD meninjau nama jabatan, atasan pelaporan, Position Description, dan CAM. HR Admin meninjau seluruh data, dapat menetapkan Annual Bonus dan Vehicle Allowance, serta dapat mengganti pemberi persetujuan berikutnya.
3. Menampilkan status lama karyawan dari data terkini dan mengumpulkan status kepegawaian baru, jabatan, departemen, atasan pelaporan, golongan penggajian, klasifikasi upah, jadwal kerja, jam kerja, tanggal berlaku, data gaji khusus HR, persentase kenaikan, dan nomor referensi.
4. Mewajibkan Position Description dalam format PDF untuk setiap ESC. Mewajibkan CAM dalam format PDF untuk Non-Staff, tetapi tidak untuk Staff.
5. Mendukung persetujuan berurutan, persetujuan dengan komentar opsional, pengembalian dengan komentar wajib, pengajuan ulang, delegasi persetujuan, dan penggantian pemberi persetujuan berikutnya oleh HR Admin. Mencatat setiap perubahan alur kerja atau data dalam log aktivitas.
6. Menghasilkan Laporan ESC Individu dengan tanda tangan digital dalam format PDF, laporan pemantauan dalam format XLSX berdasarkan periode yang dipilih, dan memorandum HR Admin dalam format PDF dan DOC setelah mencapai status persetujuan yang relevan.
7. Menyediakan pemantauan status, informasi pemberi persetujuan yang masih menunggu tindakan, riwayat, log aktivitas, serta pencarian/filter berdasarkan karyawan, organisasi, jenis/status ESC, tanggal permohonan, dan tanggal berlaku.
8. Memberi tahu pemberi persetujuan berikutnya saat pengajuan atau persetujuan, pemohon dan pemberi persetujuan sebelumnya saat pengembalian, HR Admin saat penarikan kembali, serta pemohon, karyawan, dan HR Admin setelah penyelesaian akhir. Mengirim email pengingat dan notifikasi dalam aplikasi setiap dua hari hingga ada tindakan, dengan interval yang disebut dapat dikonfigurasi.
9. Setelah persetujuan akhir dan tanggal berlaku tercapai, memperbarui data terkait organisasi, jabatan, pekerjaan, jalur pelaporan, penggajian dan kompensasi, pengelolaan waktu, serta PMGM.

**Aturan perilaku dan prasyarat**

- Satu ESC berstatus `In Progress` per karyawan menghalangi ESC baru hingga permohonan sebelumnya disetujui atau ditarik kembali.
- Seluruh kolom ESC wajib diisi kecuali CAM, yang hanya wajib untuk Non-Staff. Annual Bonus dan Vehicle Allowance hanya dapat diakses HR Admin dan hanya ditampilkan untuk Senior Manager ke atas.
- Pengembalian wajib disertai komentar; persetujuan tidak mewajibkan komentar. Hanya pemohon yang dapat merevisi permohonan yang dikembalikan.
- Akses delegasi hanya berlaku untuk tugas persetujuan milik pemberi persetujuan tersebut. HR Admin dapat mengganti pemberi persetujuan berikutnya selama proses persetujuan berlangsung.
- Promosi dan mutasi memerlukan tinjauan OD sebelum alur persetujuan utama. Jenis ESC lainnya langsung mengikuti alur kerja yang telah dikonfigurasi.
- Perubahan hanya berlaku setelah persetujuan akhir dan tanggal berlaku tercapai. Sumber mengizinkan tanggal mundur dan tanggal mendatang sesuai kebijakan perusahaan, tetapi tidak memberikan aturan batas yang terperinci.
- Karyawan yang bersangkutan hanya dapat melihat ESC terbarunya. ESC yang diajukan oleh Department Head tidak dapat diakses oleh karyawan tersebut.
- Demosi dapat bersifat sukarela atau tidak sukarela dan dapat didasarkan pada disiplin, etika, atau kinerja. Demosi dapat mengubah golongan, tanggung jawab pekerjaan, serta kompensasi/tunjangan.

**Perilaku akses, audit, dan kerahasiaan**

- Laporan ESC individu hanya dapat diakses oleh HR Admin dan karyawan yang bersangkutan.
- Tanda tangan digital yang digunakan dalam dokumen yang dihasilkan harus disimpan dalam keadaan terenkripsi.
- Riwayat persetujuan dan komentar tidak dapat dihapus. Log audit mencakup pengajuan, persetujuan, pengembalian, penarikan kembali, penggantian pemberi persetujuan, perubahan data, dan komentar.

**Perilaku fungsional tambahan**

- Formulir ESC bersama juga mewajibkan alasan, Position Description, justifikasi, dan CAM jika berlaku. Formulir menampilkan nama karyawan, ID, serta tanggal mulai bekerja sebagai data sumber; status lama dibaca dari data terkini dan tidak diedit langsung.
- Kolom status baru yang diminta meliputi status kepegawaian, nama jabatan, departemen, atasan pelaporan, golongan penggajian, klasifikasi upah, jadwal kerja, jam kerja, tanggal berlaku, Base Salary, Percentage Increase, dan Reference Number. Base Salary, Percentage Increase, dan Reference Number hanya untuk HR; Annual Bonus dan Vehicle Allowance hanya untuk HR dan hanya ditampilkan untuk Senior Manager ke atas.
- Hanya HR Admin dan karyawan yang bersangkutan yang dapat mengakses laporan individu. Department Head dapat melihat seluruh riwayat ESC bawahannya; karyawan hanya melihat ringkasan dan laporan ESC miliknya yang terbaru, dengan tetap mengikuti pengecualian terkait Department Head yang telah disebutkan.
- Penerima delegasi harus merupakan pengguna aktif; hanya satu penerima delegasi aktif yang boleh ada untuk satu tugas persetujuan; delegasi tidak mengubah urutan persetujuan maupun menghilangkan pencatatan keterkaitan dengan pemberi persetujuan awal. Keputusan melalui delegasi harus mencatat penerima delegasi dan pemberi persetujuan yang mendelegasikan tugas.
- Memigrasikan riwayat ESC dari 2021 hingga data sumber terbaru. ESC memasok perubahan yang telah disetujui ke data organisasi, pekerjaan/jabatan, jalur pelaporan, penggajian/kompensasi, roster/shift/pengelolaan waktu, dan penanda mutasi/promosi PMGM; ESC tidak bertanggung jawab atas pemutusan hubungan kerja, perhitungan penggajian, perekrutan, evaluasi kinerja, pembuatan organisasi/jabatan, atau layanan mandiri di luar ESC.
- Gaji pokok, bonus tahunan, tunjangan kendaraan, persentase kenaikan, informasi persetujuan, dokumen pendukung, dan tanda tangan digital memerlukan penanganan rahasia sesuai lingkup peran. Tanda tangan digital tetap terenkripsi saat tersimpan.

**Skenario kasus penggunaan**

1. Permohonan promosi harus melalui tinjauan OD dan tidak dapat diajukan tanpa Position Description.
2. Permohonan Non-Staff tanpa CAM ditolak; permohonan Staff tidak memerlukan CAM.
3. Pemberi persetujuan mengembalikan permohonan dengan komentar, pemohon merevisi, lalu permohonan kembali kepada pemberi persetujuan pertama/berikutnya sesuai konfigurasi.
4. Permohonan disetujui sebelum tanggal berlakunya dan hanya mengubah data induk ketika tanggal berlaku tercapai.
5. HR Admin mengganti pemberi persetujuan berikutnya dan aktivitas tersebut dapat diaudit.

## Ambiguitas sumber di luar himpunan kebutuhan yang dapat dieksekusi

- Menetapkan konfigurasi alur kerja lengkap untuk setiap jenis ESC dan pihak yang bertanggung jawab atas eskalasi.
- Memperjelas perbedaan `Withdraw` dan `Withdrawn` serta status yang belum selesai yang mengizinkan tindakan tersebut.
- Menetapkan akses laporan persetujuan bagi penerima delegasi dan pelaku penggantian pemberi persetujuan.
- Menyelaraskan konflik penarikan kembali: bagian fungsional mengizinkan penarikan kembali selama persetujuan belum selesai, sedangkan tabel validasi membatasinya pada tahap pemohon.
