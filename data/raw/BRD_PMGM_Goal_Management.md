# IT SYSTEM DEVELOPMENT — BUSINESS REQUIREMENT ASSESSMENT

**Project:** Sistem HRIS - PMGM  
**Module:** Goal Management  
**Dokumen sumber:** BRD PMGM - Goal Management.docx (14 halaman)  
**Versi tercantum pada footer:** 0.1  
**Konversi:** teks revisi yang diterima dari Track Changes; diagram asli dilampirkan sebagai gambar.

## 1. Business Requirement Record

| Start Date | End Date | Author | Version Doc | Change Reference |
| --- | --- | --- | --- | --- |
| 16 Jul 2026 |  | Analis Bisnis B | 0.1 | Draft |
| 03 Aug 2026 |  | Analis Bisnis B | 0.2 | Revision |

### 1.1 LOG Changes

**Deskripsi:** Describe the changes which impact to the Module.

**Guidance:**
- Provide the name, detail changes and severity of the changes, e.g. Mr. X request for change on workflow due to new policy on dd/mm/yyyy, etc.
- Please identify all the changes clearly, including impact to another module or infrastructure (if any).

### 1.2 Change Record

| Date | Requested by | Description | Severity (major/minor) | Status |
| --- | --- | --- | --- | --- |
| 8/28/2026 | Perusahaan A | Penambahan business rules terkait cascade dan submit KPI, poin 8-10 (Halaman 12). | Major |  |

## 2. Project Description

| Field | Value |
| --- | --- |
| Project Description | Sistem HRIS - PMGM |
| Business User Expert |  |
| Assessment Date | 1 Jul 2026 |
| Module Description | Goal Management |

## 3. Requirement Identification

### 3.1 WHY — Module Objectives/Goals dan Module Benefits

**Guidance:**
- Module Objectives/Goals: Your expected objectives on this module, e.g. decreasing numbers of paper used.
- Module Benefits: The outcome of successful objectives/goals, e.g. reducing the paper consumption cost.

| Module Objectives/Goals | Module Benefits |
| --- | --- |
| Menyelaraskan KPI individu, tim, dan departemen dengan target objective perusahaan melalui mekanisme KPI cascade sesuai hierarki organisasi. | Meningkatkan alignment antara target perusahaan dengan kontribusi setiap karyawan sehingga setiap target memiliki arah yang jelas. |
| Menyediakan mekanisme pengelolaan KPI end-to-end yang terstruktur, mulai dari konfigurasi, penyusunan, cascading, approval, hingga monitoring KPI sesuai struktur organisasi dan periode yang ditetapkan. | Memastikan seluruh KPI organisasi tersusun secara konsisten, terukur, dan selaras dengan sasaran strategis perusahaan sehingga meningkatkan efektivitas pencapaian target bisnis. |
| Menyediakan proses penyusunan dan persetujuan KPI yang terdokumentasi, terkontrol, dan mengikuti workflow organisasi. | Mengurangi proses manual, mempercepat proses review dan approval KPI, serta meningkatkan transparansi proses pengelolaan target. |
| Memungkinkan tim Organization Development (OD) mengelola template KPI, business rules, workflow, dan periode KPI secara dinamis. | Meningkatkan fleksibilitas pengelolaan kebijakan KPI sehingga perubahan kebutuhan bisnis dapat diakomodasi lebih cepat. |
| Menyediakan mekanisme monitoring KPI berdasarkan struktur organisasi sehingga Direct Supervisor dapat memantau KPI bawahannya sesuai kewenangan. Khusus Tim Organization Development (OD) dapat melakukan monitoring KPI karyawan lintas department. | Meningkatkan akuntabilitas, kemudahan audit, dan visibilitas terhadap perkembangan KPI di seluruh organisasi. |

### 3.2 WHAT — Scope

**Guidance:**
- In scope: Explain the expected function / feature to be included, e.g. the reporting must in Excel, must be easy to use in mobile, etc.
- Out scope: Explain what function that exists on the current/manual system that should not be considered, e.g. no need to add 3rd party account on login, etc.
- Make sure to put anything that you can think about the scope.

#### 3.2.1 In Scope

1. Pengelolaan periode KPI (Open, Close, dan Re-open KPI Period).
2. Konfigurasi template KPI secara dinamis untuk staff dan non staff beserta field, validation, dan business rules.
3. Penyusunan, penyimpanan draft, submit, edit, dan penghapusan KPI selama periode masih dibuka.
4. KPI cascade sesuai struktur organisasi beserta pengaturan minimum persentase KPI yang wajib di-cascade.
5. Workflow review dan approval KPI berdasarkan struktur organisasi beserta mekanisme bypass (pengalihan) ketika terdapat vacant position.
6. Pengelolaan Activity Plan pada setiap KPI termasuk attachment, status, dan ownership activity.
7. Pengelolaan notifikasi, reminder, dan outstanding KPI yang dapat dikonfigurasi oleh Tim OD.
8. Monitoring KPI beserta histori perubahan (Audit Trail) untuk KPI, cascade, approval, dan Revisi.
9. Pengaturan hak akses (visibility) KPI berdasarkan struktur organisasi.
10. Export KPI karyawan personal ke PDF.
11. Konfigurasi Dynamic Validation Rules, Rating Direction, Workflow Approval, dan KPI Business Rules oleh Tim OD.
   - **Dynamic Validation Rules.** Pengaturan aturan validasi yang dapat dikonfigurasi oleh Tim OD tanpa perubahan aplikasi, seperti mandatory field, jumlah maksimum KPI, batas bobot KPI, serta validasi yang harus dipenuhi sebelum KPI dapat di-submit.
   - **Rating Direction.** Pengaturan arah penilaian KPI untuk menentukan apakah nilai yang lebih tinggi menunjukkan performa yang lebih baik (High is Good) atau sebaliknya nilai yang lebih rendah menunjukkan performa yang lebih buruk (High is Bad), sesuai karakteristik masing-masing KPI.
   - **Workflow Approval.** Pengaturan alur review dan approval KPI, termasuk penentuan approver berdasarkan struktur organisasi serta mekanisme approval yang berlaku.
   - **KPI Business Rules.** Pengaturan aturan bisnis yang diterapkan pada proses Goal Management, seperti aturan KPI Cascade, penggunaan perspective, batas bobot KPI, jumlah KPI yang diperbolehkan, serta ketentuan lain yang berlaku pada periode KPI.

12. Sistem menyediakan opsi Mandatory pada saat proses KPI Cascade yang memungkinkan Direct Supervisor menentukan apakah KPI hasil Cascade dapat diubah oleh subordinate. KPI yang ditandai sebagai Mandatory tidak dapat diubah maupun dihapus oleh subordinate.
13. Fitur konfigurasi daftar peserta pembuatan KPI yang di manage oleh Tim Organization Development (OD), meliputi penentuan karyawan yang wajib dan dikecualikan mengikuti pengisian KPI dari periode KPI tertentu.
14. Bulk Export KPI per department dalam bentuk excel

#### 3.2.2 Out Scope

- Auto forward ketika Due date ke OD.
- Menu Activity dengan kanban Board(drag & drop).
- Pembuataan KPI untuk BoD didalam sistem.
- Request approval launch open/close KPI Form

#### 3.2.3 Additional Scope (if any)

*Tidak diisi dalam dokumen sumber.*

### 3.3 WHEN — Milestones

**Guidance:** Explain the expected milestone complete with expected start and end dates, e.g. system must ready to used in dd/mm/yyyy, should be presented on management meeting on dd/mm/yyyy.

| Milestones | Due Date | Remarks |
| --- | --- | --- |
| Sprint 2 | 3 Aug 2026 | KPI Templating |
| Sprint 3 | 17 Aug 2026 | KPI Creation & Validation, KPI Cascade |
| Sprint 4 | 31 Aug 2026 | KPI Workflow & Approval(Submission – Review OD) |

### 3.4 WHO — Roles and Accessibilities

**Guidance:**
- Provide the role, assigned to and accessibilities on each role that will be included in the module, e.g. HR as admin apps will be responsible to provide setting on the current process.
- Please identify all the participated person in your area to have a clear roles assignment.

#### Organization Development (OD) Admin

**Assigned to:** *Belum dicantumkan*

**Accessibilities:**
- **Form Template:**
  - Create form
  - Edit form
  - Delete form
  - Launch form
  - Close form
  - Re-Open form
  - View Audit Trail form
  - View Employee Goal Form
  - Approve Goal Submission
  - Send Back Goal Submission

#### Staff & Non Staff

**Assigned to:** *Belum dicantumkan*

**Accessibilities:**
- **Goal Form:**
  - Create KPI/Goal
  - Update KPI/Goal
  - Delete KPI/Goal
  - Create Activity
  - Delete Activity
  - Update Activity
  - Submit goal form

#### Direct Supervisor

**Assigned to:** *Belum dicantumkan*

**Accessibilities:**
- **Goal form:**
  - Create KPI/Goal
  - Update KPI/Goal
  - Delete KPI/Goal
  - Create Activity
  - Delete Activity
  - Update Activity
  - Cascade Form
  - View Subordinate Goal form
  - View Subordinate Activity
  - Approve Subordinate Goal submission
  - Send back Subordinate Goal submission

#### One up Supervisor

**Assigned to:** *Belum dicantumkan*

**Accessibilities:**
- **Goal form:**
  - Create KPI/Goal
  - Update KPI/Goal
  - Delete KPI/Goal
  - Create Activity
  - Delete Activity
  - Update Activity
  - Cascade Form
  - View Subordinate Goal form
  - View Subordinate Activity
  - Approve Subordinate Goal submission
  - Send back Subordinate Goal submission

### 3.5 WHAT IF — Risks and Mitigation

**Guidance:**
- Explain the risk that might be a barrier / obstacle for this module, e.g. the procedure does not exist, need to be confirmed by BOD, etc.
- Please think of any risk that might be impacted related to this module.

| Risks | Level (Hi, Med, Low) |
| --- | --- |
| KPI yang disusun tidak selaras dengan target organisasi karena proses KPIcascade tidak dilakukan sesuai ketentuan. | Med |
| Kesalahan pengisian KPI, bobot, atau target menyebabkan hasil penilaian kinerja menjadi tidak akurat. | Hi |
| Perubahan jabatan atau Direct Supervisor selama periode Goal Management menyebabkan proses review KPI terhenti atau tidak sesuai dengan struktur organisasi terbaru. | Hi |

**Mitigation:**
- Memvalidasi bobot minimum KPI hasil cascade sebelum KPI dapat di-submit.
- Menerapkan validasi business rule dan mandatory field sebelum KPI dapat disimpan atau di-submit.
- Menyesuaikan hubungan Direct Supervisor dan bawahan secara otomatis berdasarkan struktur organisasi terbaru sehingga proses cascade, review, dan approval dapat dilanjutkan oleh pihak yang berwenang.

## 4. Current System Business Flow

**Guidance:**
- Please describe the current system that running / being used in essay.
- To maximize the understanding of current system, consider explaining with process flow in mind.
- Do it step by step from beginning to the end of process.
- Example on essay (in Bahasa): “Mr. X mengisi formulir exit form kemudian memintakan approval kepada department head. Setelah di approve, form kemudian diserahkan pada security pada saat user x berada di gerbang dan akan keluar dari area camp.”
- More complete the explanation will affect the next visual modelling process.

Pada sistem Sistem HRIS sebelumnya saat ini, proses Goal Management belum memiliki mekanisme KPI Submission, sehingga KPI yang telah disusun tidak melalui proses submit sebelum memasuki tahap review. Selain itu, sistem belum menerapkan validasi KPI sesuai business rule perusahaan, seperti validasi jumlah KPI, bobot KPI, maupun ketentuan lainnya, sehingga penyusunan KPI belum terkontrol. Sistem juga belum memiliki mekanisme lock KPI, sehingga karyawan masih dapat mengubah atau menghapus KPI kapan saja meskipun KPI telah memasuki proses review atau telah disepakati.

## 5. Expected New System Business Flow

**Guidance:**
- Please describe the expected improved system flow.
- To maximize the understanding of expected new system, consider to explain with process flow in mind.
- Do it step by step from beginning to the end of process.
- More complete the explanation will affect the next visual modelling process.

### 5.1 Goals Management — Diagram

[Ilustrasi sumber dihapus dari korpus publik: Goal Management business flow]

> **Catatan ketidaksesuaian pada sumber:** Diagram menuliskan syarat bobot cascade **40%**, sedangkan ringkasan aturan pada poin 9 menyebut nilai default **50%** (dapat dikonfigurasi OD Section). Kedua informasi dipertahankan sesuai dokumen asal.

### 5.2 Summary

1. OD Section membuat jadwal/periode pengisian KPI beserta tanggal mulai dan due date pengisian KPI.
2. Selama periode pengisian KPI masih aktif/dibuka, setiap karyawan dapat membuat, mengubah, menghapus, dan melakukan submit KPI. Setelah periode pengisian KPI ditutup, karyawan tidak dapat membuat, mengubah, maupun menghapus KPI. Karyawan hanya dapat membuat dan mengubah Activity. OD Section dapat membuka kembali periode pengisian KPI apabila diperlukan dengan persetujuan pejabat yang berwenang (persetujuan dilakukan secara offline/out of system)

#### A. KPI Creation & Validation

3. Setiap karyawan dapat membuat KPI masing-masing. Form KPI yang ditampilkan sistem disesuaikan secara otomatis berdasarkan kategori karyawan (Staff atau Non-Staff).
4. Saat pembuatan KPI, sistem melakukan validasi untuk karyawan Staff sebagai berikut:

   - Jumlah KPI maksimal 10 item.
   - Total bobot KPI harus 100%.
   - Bobot setiap KPI minimal 5% dan maksimal 25%.
   - Total bobot perspective learning & growth maksimal 15%.

5. Saat pembuatan KPI, sistem melakukan validasi untuk karyawan Non-Staff sebagai berikut:

   - Jumlah KPI maksimal 10 item.
   - Total bobot KPI harus 100%.
   - Bobot setiap KPI minimal 5% dan maksimal 30%.
   - Total bobot perspective learning & growth maksimal 15%.

6. Apabila salah satu validasi tidak terpenuhi, sistem akan menampilkan pesan kesalahan sehingga KPI tidak dapat disimpan maupun di-submit.

#### B. Cascade KPI

7. Senior Manager/Division Head yang struktur organisasinya direct ke BoD dapat membuat KPI dengan mengacu pada target objective BoD dan melakukan cascade KPI kepada direct subordinate.
8. Senior Manager/Manager/One Up Supervisor dapat melakukan cascade KPI kepada Direct Subordinate sesuai dengan struktur organisasi dan policy terkait dengan cascade.
9. Sebelum melakukan submit KPI, sistem akan memvalidasi bahwa total bobot KPI hasil cascade yang diterima karyawan telah memenuhi bobot minimum yang ditentukan. Secara default bobot minimum KPI hasil cascade adalah 50% dan dapat dikonfigurasi oleh OD Section.
10. Apabila bobot KPI hasil cascade belum memenuhi ketentuan minimum, sistem tidak mengizinkan karyawan melakukan submit KPI .

#### C. Alur Submit KPI

11. Setelah KPI selesai dibuat, karyawan melakukan submit KPI sehingga status KPI menjadi Submitted.
12. Setelah KPI di-submit, sistem mengirimkan notifikasi kepada Direct Supervisor untuk melakukan review.
13. Selama KPI berada dalam proses review atau sudah di submit, karyawan tidak dapat mengubah KPI hingga menerima status revisi.

#### D. Review Direct Supervisor

14. Direct Supervisor menerima notifikasi ketika subordinate mengajukan (submit) KPI untuk direview. Selain itu, sistem mengirimkan notifikasi pengingat (reminder) apabila masih terdapat KPI subordinate yang belum direview oleh Direct Supervisor.
15. Direct Supervisor melakukan review terhadap KPI yang diajukan oleh subordinate, dengan ketentuan sebagai berikut:

   - Jika KPI telah sesuai, Direct Supervisor memberikan persetujuan (Approve).
   - Jika KPI belum sesuai, Direct Supervisor mengembalikan KPI kepada subordinate dengan memilih aksi Revised dan memberikan catatan revisi. Setelah itu, status KPI berubah menjadi Revise Required sehingga subordinate dapat melakukan perbaikan dan mengajukan kembali KPI.
   - Pada status Revise Required, sistem mengirimkan notifikasi kepada karyawan agar melakukan perbaikan KPI.

16. Setelah karyawan melakukan revisi dan submit ulang, KPI kembali ke proses review Direct Supervisor.

#### E. Review Organization Development Section

17. OD Section menerima notifikasi ketika terdapat KPI yang menunggu review.
18. OD Section melakukan review dan validasi akhir terhadap KPI.

   - Jika KPI telah sesuai, OD section memberikan approval dan status KPI menjadi Completed.
   - Jika KPI belum sesuai, OD Section melakukan Revise disertai catatan revisi.

19. Pada status Revise Required OD, sistem mengirimkan notifikasi kepada karyawan agar melakukan perbaikan terhadap KPI sesuai catatan revisi
20. Setelah direvisi dan di-submit ulang, KPI akan kembali ke alur review Direct Supervisor, kemudian dilanjutkan ke review OD Section
21. Pada status Revise Required OD, sistem mengirimkan notifikasi kepada karyawan agar melakukan perbaikan terhadap KPI sesuai catatan revisi.
22. Pada status compeleted, karyawan tidak dapat mengubah KPI meskipun periode belum berakhir

#### F. Notification

23. Sistem mengirimkan notifikasi kepada karyawan apabila KPI miliknya telah memperoleh status Completed.
24. Sistem akan mengirimkan notifikasi pengingat kepada Direct Supervisor apabila terdapat bawahan yang belum melakukan submit KPI hingga mendekati batas waktu pengisian KPI (due date)
25. Sistem mengirimkan notifikasi sebagai berikut:

  - **a. Submit KPI**
    - In-App Notification: Requestor dan Direct Supervisor.
    - Email: Direct Supervisor.
  - **b. Approval KPI**
    - In-App Notification: Requestor dan Approver.
    - Email: Requestor.
  - **c. Send back KPI/revisi**
    - In-App Notification: Requestor dan Approver.
    - Email: Requestor.
26. Notifikasi dikirimkan secara bertahap sesuai jenjang organisasi, dengan konfigurasi default sebagai berikut:

   - 3 minggu sebelum due date dikirimkan kepada Department Head.
   - 2 minggu sebelum due date dikirimkan kepada Senior Manager/Director.
   - 1 minggu sebelum due date dikirimkan kepada Kepala Operasional/Director.

   Jenjang organisasi akan mengikuti KaryawanStruktur Organisasi.
27. Detail notifikasi (format, durasi, penerima, dan isi) dapat dikonfigurasi oleh OD Section.

#### G. Visibility

28. Karyawan hanya dapat melihat dan mengelola KPI miliknya sendiri.
29. Direct Supervisor dapat melihat KPI seluruh bawahannya sesuai struktur organisasi.
30. Senior Manager/Manager/One Up Supervisor dapat melihat KPI bawahan sesuai struktur organisasi.
31. OD Section dapat melihat KPI seluruh karyawan beserta status, riwayat review yang sesuai dengan Point D. Review Direct Supervisor , dan riwayat revisinya.

#### H. Audit Trail

32. Sistem menyimpan riwayat perubahan KPI, approval, revisi, dan catatan review untuk keperluan audit.

#### I. Export

33. Karyawan dapat mengekspor KPI miliknya ke dalam format PDF.
34. Direct Supervisor dapat mengekspor KPI bawahan sesuai struktur organisasi ke dalam format PDF.
35. OD Section dapat mengekspor data KPI per deparment ke dalam format Excel.

#### J. Revisi Mid-Year

36. Saat OD Section membuka periode revisi (Mid-Year), setiap karyawan dapat melakukan penyesuaian terhadap KPI yang telah dibuat sebelumnya.
37. OD Section dapat mengubah (melakukan override) status KPI karyawan apabila diperlukan selama periode revisi.
38. Jika terjadi perubahan jabatan atau departemen selama periode pengisian KPI, status KPI karyawan akan di-reset menjadi draft sehingga karyawan dapat menyusun kembali KPI sesuai jabatan atau departemen barunya. Apabila perubahan terjadi di luar jadwal periode pengisian KPI, OD Section dapat membuka kembali periode pengisian KPI.

#### K. E- Form

39. Sistem hanya menyediakan dua jenis form KPI, yaitu Form Staff dan Form Non-Staff. Form yang digunakan ditentukan secara otomatis berdasarkan kategori karyawan.

### 5.3 Business Rules

Penomoran pada kolom referensi mempertahankan nomor aktif yang ditampilkan pada dokumen sumber setelah revisi. Nomor 7 dihapus melalui Track Changes, sedangkan nomor 8 muncul dua kali (perubahan posisi dan ketentuan cascade).

| No. pada sumber | Business Rule |
| --- | --- |
| 1 | Level paling bawah yang dapat melakukan KPI Cascade adalah Supervisor. |
| 2 | Pada saat periode pengisian KPI dibuka pertama kali, Tim Organization Development (OD) dapat menentukan karyawan yang dikecualikan dari periode tersebut. Karyawan yang dikecualikan tidak akan menerima notifikasi pengisian KPI dan sehingga tidak perlu mengisi KPI pada periode tersebut. |
| 3 | Direct Supervisor tidak dapat melakukan skip ke level dibawahnya pada proses KPI Cascade.(khusus Staff) |
| 4 | Penyusunan KPI untuk Staff menggunakan empat perspective, yaitu Finance, Stakeholder, Internal Process, serta Learning & Growth. Untuk Non-staff sesuai dengan form yang digunakan saat ini. |
| 5 | Tidak semua perspective digunakan, Staff dapat menyesuaikan perspective yang sesuai dengan pekerjaan atau target yang ditentukan saat penyusunan KPI. |
| 6 | Setelah periode pengisian KPI ditutup, seluruh Karyawan tidak dapat lagi membuat, mengubah, maupun menghapus KPI. Karyawan hanya dapat membuat dan mengubah Activity yang ter-link dengan KPI. Jika diperlukan OD Section dapat membuka akses kembali sesuai dengan persetujuan pejabat yang berwenang. |
| [8.] | Apabila terjadi perubahan posisi di dalam organisasi, seperti perubahan posisi Manager selama periode Goal Management berlangsung, tim OD melakukan penyesuaian workflow, sehingga posisi Manager tersebut dapat melanjutkan proses review dan melakukan perubahan KPI sesuai kewenangannya. |
| 8 | cascade KPI kepada bawahan hanya dapat dilakukan setelah atasan menyelesaikan dan melakukan submit atas KPI miliknya. |
| 9 | Untuk non-staff yang memberikan cascade adalah supervisor |
| 10 | Create KPI dapat dilakukan walau belum ada KPI Cascade, namun tidak dapat disubmit |

## 6. Sign-off / Approval

| Role | Name | Signature | Date |
| --- | --- | --- | --- |
| Business Analyst | Analis Bisnis B | Tercantum pada dokumen asli | 28 Jul 2026 |
| Project Coordinator | Koordinator Proyek A |  |  |
| Business User Expert | Narasumber Bisnis C |  |  |

> By signing this document, all items contained herein are confirmed as mandatory requirements to be delivered as the agreed-upon product. Any changes or modifications to these requirements will be managed through the change request process.

---
*Catatan konversi: struktur ditata ulang agar dapat dibaca sebagai Markdown. Isi business requirement, angka, nomor referensi, dan gambar alur mengikuti dokumen sumber; teks yang dicoret dalam Track Changes tidak dimasukkan sebagai persyaratan aktif.*
