[Ilustrasi sumber dihapus dari korpus publik: Perusahaan A]

# IT SYSTEM DEVELOPMENT — BUSINESS REQUIREMENT ASSESSMENT

**Project:** Sistem HRIS - PMGM  
**Module:** Performance Assessment  
**Document Version:** 0.1

## Business Requirement Record

| Start Date | End Date | Author | Version Doc | Change Reference |
| --- | --- | --- | --- | --- |
| 18 Aug 2026 |  | Analis Bisnis B | 0.1 | Draft |
|  |  |  |  |  |
|  |  |  |  |  |

## LOG Changes

Describe the changes which impact to the Module

**Guidance:**

- Provide the name, detail changes and severity of the changes, e.g. Mr. X request for change on workflow due to new policy on dd/mm/yyyy, etc
- Please identify all the changes clearly include impact to another module or infrastructure (if any).

### Change Record

| Date | Requested by | Description | Severity (major/minor) | Status |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

## Project and Module Details

| Field | Value |
| --- | --- |
| Project Description | Sistem HRIS - PMGM |
| Business User Expert |  |
| Assessment Date | 1 Jul 2026 |
| Module Description | Performance Assessment |

## Requirement Identification

### WHY — Explain why this module is needed

**Guidance:**

- Module Objectives/Goals : Your expected objectives on this module
- e.g. decreasing numbers of paper used
- Module Benefits : The outcome of successful objectives/goals e.g. reducing the paper consumption cost

| Module Objectives/Goals | Module Benefits |
| --- | --- |
| Menyediakan proses Performance Assessment end-to-end mulai dari Self Rating, review Direct Supervisor, review One Up Supervisor, OD Normalization, hingga Final Rating. | Membentuk proses penilaian kinerja yang terstruktur, transparan, terdokumentasi, dan konsisten pada seluruh organisasi. |
| Menyediakan form Performance Assessment yang dapat dikonfigurasi secara dinamis berdasarkan kebutuhan perusahaan, kategori employee, dan periode penilaian. | Meningkatkan fleksibilitas Tim Organization Development (OD) dalam mengelola kebijakan, struktur section, field, workflow, dan rating scale tanpa perubahan aplikasi. |
| Memastikan setiap employee dapat melakukan Self Rating terhadap pencapaian KPI dan memberikan informasi pendukung berupa comment, attachment, serta aspiration. | Meningkatkan kualitas refleksi employee dan menyediakan data pendukung yang lebih lengkap bagi proses review oleh atasan. |
| Menyediakan proses review berjenjang sesuai struktur organisasi, termasuk dukungan satu atau dua layer review untuk Non-Staff. | Memastikan rating dan feedback diberikan oleh pihak yang berwenang sesuai hubungan employee, Direct Supervisor, dan One Up Supervisor. |
| Menyimpan histori rating, approval, comment, status, dan perubahan reviewer sebagai audit trail. | Meningkatkan akuntabilitas, kemudahan monitoring, dan ketersediaan bukti audit atas seluruh proses Performance Asessment. |

### WHAT — Describe the expected function or features on the app

**Guidance:**

- In scope : Explain the expected function / feature to be included e.g.the reporting must in excel, must be easy to use in mobile, etc
- Out scope : Explain what function that exist on the current/manual system that should not be considered e.g. no need to add 3rd party account on login, etc
- Make sure to put anything that you can think about the scope

| In Scope | Out Scope |
| --- | --- |
| Konfigurasi template PA secara dinamis: General Setting, Preview, Workflow, Rating Scale, Language, Sections, dan Fields. | Tampilan GAP antara Self Rating dan rating Supervisor. |
| Pengelolaan participant/employee yang mengikuti periode PA sesuai data organisasi dan konfigurasi dari tim OD. | Signature Section. |
| Self Rating oleh employee, termasuk rating, mandatory comment, optional attachment, aspiration, Save Draft, Save, dan Submit. | Acknowledge Section. |
| Review dan pemberian rating dan comment untuk performance, strength dan Area of Improvement oleh Direct Supervisor serta One Up Supervisor. | Integrasi Activity Plan dengan proses Performance Assessment. |
| Dukungan satu atau dua layer review untuk Non-Staff sesuai struktur organisasi. | Auto Rating apabila employee belum mengisi Self Assessment. |
| Master Rating Scale 1-6 beserta name, description, dan penggunaan sebagai dropdown penilaian. | Pelaksanaan normalisasi department di dalam system(normalisasi dilakukan di luar sistem.) |
| Summary Section dan perhitungan Overall Form Rating yang dapat diubah secara manual. |  |
| Notification, reminder, dan escalation yang dapat dikonfigurasi oleh OD. |  |
| Visibility berdasarkan role dan struktur organisasi. |  |
| Rating History dan Audit Trail atas rating, comment, approval, send back, import, serta finalization. |  |
| Employee Transfer handling, Supervisor Resignation handling, dan vacant-position bypass. |  |
| Tim OD dapat melakukan export data PA per department ke file/format Excel. |  |
| Normalization batch yang memiliki nama, file import, validation result, dan import history. |  |
| Tim OD dapat melakukan import/re-import hasil normalisasi rating karyawan per department |  |
| Final Rating setelah hasil normalisasi divalidasi dan difinalisasi oleh tim OD. |  |
| Tim OD dapat melakukan monitoring status PA seluruh karyawan. |  |

### WHEN — Describe the expected completion dates on required milestone

**Guidance:**

- Explain the expected milestone complete with expected start and end dates e.g. system must ready to used in dd/mm/yyyy, should be presented on management meeting on dd/mm/yyyy

| Milestones | Due Date | Remarks |
| --- | --- | --- |
| Sprint 5 | 14 Sep 2026 | Form, Timeframe, Self Rating |
| Sprint 6 | 28 Sep 2026 | Timeframe, Notifications & Audit |
| Sprint 7 | 12 Oct 2026 | Review & Rating |
| Sprint 8 | 26 Oct 2026 | Export, Import, & Notifications |

### WHO — Describe how many roles will interact with this Module

**Guidance:**

- Provide the role, assigned to and accessibilities on each role that will be included in the module e.g. HR as admin apps will be responsible to provide setting on the current process.
- Please identify all the participated person in your area to have a clear roles assignment.

#### Organization Development (OD) Admin

- Create, edit, duplicate, preview, launch, close PA period/template.
- Configure General Setting, Workflow, Rating Scale, Language, Sections, Fields, Participants, dan notification.
- View seluruh employee PA, status, rating history, comment history, dan audit trail.
- Override reviewer mapping apabila terdapat perubahan organisasi atau kebutuhan operasional yang sah.
- Export data PA per department.
- Create normalization batch, import/re-import file per department, review validation result.
- Finalize normalization dan menetapkan Final Rating.
- Monitor transferred employee, resigned supervisor, overdue assessment, dan outstanding department normalization.

#### Employee (Staff & Non-Staff)

- View Employee Information, Review Dates, template section, Self Rating, dan Final Rating sesuai stage.
- Provide Self Rating dan mandatory comment pada setiap item yang diwajibkan.
- Upload optional attachment dan mengisi Aspirations.
- Save Draft, dan Submit Self Assessment selama period/stage mengizinkan.
- Receive Send Back notes, revise assessment, dan re-submit.
- Tidak dapat melihat rating/comment One Up Supervisor sebelum diizinkan oleh stage Final Rating.

#### Direct Supervisor

- View Self Rating dan comment milik direct subordinate.
- Provide/edit Supervisor Rating dan Supervisor Comment.
- Fill Strength dan Area Improvement.
- Save Draft, Send Back, dan Submit assessment subordinate.
- View Approval History dan rating history yang diizinkan.
- Tidak dapat melihat penilaian One Up Supervisor.

#### One Up Supervisor

- View Self Rating employee dan penilaian Direct Supervisor.
- Review, provide/adjust rating, dan provide comment sesuai workflow.
- View Summary Section secara read-only.
- Save Draft, Send Back, dan Approve sesuai kewenangan.

### WHAT IF — Identify the risk and impact of the module

**Guidance:**

- Explain the risk that might be a barrier / obstacle for this module. e.g. the procedure does not exist, need to be confirmed by BOD, etc
- Please think of any risk that might be impacted related to this module

#### Risks

| Risks | Level (Hi, Med, Low) |
| --- | --- |
| Perubahan jabatan, department, atau atasan selama periode PA dapat menyebabkan penentuan reviewer tidak sesuai dan proses review atau approval terhenti. | Hi |
| Kesalahan atau ketidaklengkapan pengisian rating, komentar, dan data penilaian dapat menyebabkan hasil Performance Assessment menjadi tidak akurat. | Hi |

#### Mitigation

- Memperbarui hubungan atasan dan bawahan secara otomatis berdasarkan struktur organisasi terbaru serta menyediakan proses reassignment atau perubahan reviewer oleh OD Section dengan pencatatan riwayat perubahan.
- Menerapkan validasi untuk rating 1–6, mandatory field, komentar, dan data penilaian sebelum PA dapat di-submit atau di-approve.

## Current System Business Flow

**Guidance:**

- Please describe the current system that running / being used in essay.
- To maximize the understanding of current system, consider explaining with process flow in mind.
- Do it step by step from beginning to the end of process
- Example on essay (in Bahasa) :
“Mr. X mengisi formulir exit form kemudian memintakan approval kepada department head. Setelah di approve, form kemudian diserahkan pada security pada saat user x berada di gerbang dan akan keluar dari area camp.”
- More complete the explanation will affect the next visual modelling process.

Pada sistem Sistem HRIS sebelumnya saat ini, proses Performance Appraisal sudah tersedia mulai dari Self-Rating, review oleh Direct Supervisor dan One-Up Supervisor, hingga penetapan Final Rating. Namun, masih terdapat beberapa keterbatasan sebagai berikut:

1. Konfigurasi template, field, section, dan bobot penilaian masih ditentukan oleh vendor NTT sehingga OD Section belum dapat mengelolanya secara mandiri.
2. Periode PA masih terbuka sepanjang waktu dan belum dapat diluncurkan berdasarkan jadwal maupun participant tertentu.
3. Alur reviewer Non-Staff belum terstandarisasi dan dapat melibatkan satu sampai tiga reviewer, tergantung struktur masing-masing department.
4. Pengaturan workflow, mandatory field, locking berdasarkan stage, notification, dan reminder belum dapat dikonfigurasi secara fleksibel oleh OD Section.

## Expected New System Business Flow

**Guidance:**

- Please describe the expected improved system flow.
- To maximize the understanding of expected new system, consider to explain with process flow in mind.
- Do it step by step from beginning to the end of process
- More complete the explanation will affect the next visual modelling process.

[Ilustrasi sumber dihapus dari korpus publik: Performance Assessment business flow]


### Template and Launch

1. OD Section membuat dan mengonfigurasi template Performance Assessment (PA) secara terpisah untuk kategori Staff dan Non-Staff.
2. Konfigurasi template mencakup General Setting, Rating Scale, Route Map, periode, notification, participant, serta pengaturan section dan field.
3. Staff mengikuti struktur organisasi dari Sistem HRIS. Non-Staff menggunakan Route Map yang dikonfigurasi secara manual oleh OD Section per department pada saat launch berdasarkan matriks yang berlaku. Non-Staff menggunakan maksimal dua layer review, namun jika hanya terdapat satu reviewer yang memenuhi kriteria, proses review dilakukan menggunakan satu layer.OD Section menentukan participant, melakukan preview, kemudian melakukan launch template untuk membuka periode PA.

### Self-Rating

4. Employee membuka form PA sesuai kategori dan language preference, serta dapat melihat Route Map yang menunjukkan current stage dan next stage.
5. Employee memberikan rating dan comment pada setiap goal, mengunggah attachment jika diperlukan, serta mengisi Aspiration.
6. Employee dapat menggunakan Save Draft. Sebelum Submit, sistem memvalidasi seluruh mandatory field dan menampilkan warning apabila masih terdapat data yang belum diisi.
7. Setelah Submit, status PA berubah menjadi Pending Direct Supervisor Review dan form dikunci dari perubahan oleh employee.

### Direct Supervisor Review

8. Direct Supervisor menerima notifikasi dan melakukan review terhadap Self Rating milik direct subordinate.
9. Direct Supervisor dapat menyesuaikan rating, memberikan comment, mengisi Strength dan Area for Improvement.
10. Direct Supervisor dapat melakukan Submit untuk meneruskan PA kepada One-Up Supervisor.

### One-Up Supervisor Review

11. One-Up Supervisor dapat melihat Self Rating serta penilaian Direct Supervisor, kemudian menyesuaikan rating, memberikan comment, mengisi Strength dan Area of Improvement sesuai kewenangannya.
12. Setelah reviewer terakhir melakukan Submit, status PA berubah menjadi Ready for Normalization. OD Section tidak melakukan approval terhadap PA.

### Notification and Monitoring

13. Sistem mengirimkan notification dan reminder secara kolektif kepada employee dan reviewer berdasarkan action, outstanding task, dan due date setiap tahap. Waktu, penerima, subject, dan frekuensi notification dapat dikonfigurasi oleh OD Section.

### Normalization

14. OD Section mengekspor data PA per department. OD dapat memilih beberapa department, tetapi sistem menghasilkan satu file terpisah untuk setiap department dalam format XLSX atau CSV.
15. Department Head atau Senior Manager melakukan normalisasi dan diskusi di luar sistem, kemudian mengembalikan file hasil normalisasi kepada OD Section.
16. Pada import pertama, OD Section membuat data normalisasi dengan mengisi nama normalisasi. Periode normalisasi otomatis mengikuti periode PA yang sedang berjalan.
17. OD Section melakukan import atau re-import hasil normalisasi per department. Setiap import wajib disertai remarks dan dapat dilengkapi attachment.
18. Hasil import terakhir yang berhasil menjadi rating normalisasi aktif. Seluruh file sebelumnya tetap disimpan sebagai import history dan audit log.
19. Jika hanya terdapat beberapa employee yang perlu disesuaikan, OD Section dapat mengubah Final Rating secara individual dengan remarks wajib dan attachment opsional.

### Finalization and Report

20. Setelah seluruh department menyelesaikan normalisasi, OD Section melakukan finalization. Status PA berubah menjadi Completed dan Final Rating dikunci.
21. Employee hanya dapat melihat Final Rating setelah PA berstatus Completed dan tidak dapat melihat penilaian detail atau Rating History.
22. Final Rating masuk ke modul Report PA yang dapat difilter berdasarkan periode, Staff/Non-Staff, level jabatan, department, employee, dan status PA, serta dapat diunduh dalam format XLSX atau CSV.

### Employee and Reviewer Changes

23. Employee yang mengalami transfer atau promotion tetap menggunakan goal yang telah disubmit, diberikan flag Is Transferred, dan dinilai oleh supervisor baru.
24. Employee yang resign atau termination dikeluarkan dari participant aktif. Jika supervisor resign setelah menilai, rating tetap digunakan; jika resign sebelum menilai, sistem melakukan bypass atau OD Section menentukan reviewer pengganti.

## Business Rules

1. Template dan launch PA untuk Staff dan Non-Staff dibuat secara terpisah.
2. Staff mengikuti struktur organisasi dari Sistem HRIS. Non-Staff menggunakan Route Map yang dikonfigurasi manual oleh OD Section per department pada saat launch berdasarkan matriks yang berlaku.
3. Non-Staff menggunakan maksimal dua layer review, namun bisa juga hanya satu layer apabila hanya terdapat satu reviewer yang memenuhi kriteria.
4. Administrator menggunakan satu layer review oleh Manager. Director dapat menjadi reviewer pada layer terakhir apabila dikonfigurasi oleh OD Section.
5. OD Section dapat mengubah reviewer apabila terdapat transfer, promotion, perubahan organisasi, supervisor resign, atau kebutuhan operasional lainnya. Perubahan wajib disertai remarks dan disimpan dalam audit trail.
6. Rating Scale menggunakan nilai 1 sampai 6 dan dipilih melalui dropdown. Setiap rating memiliki name dan description.
7. Comment pada setiap goal bersifat mandatory, sedangkan attachment bersifat optional. Aspiration diisi employee, sedangkan Strength dan Area for Improvement diisi supervisor.
8. Save Draft tidak memindahkan PA ke tahap berikutnya. Submit hanya dapat dilakukan jika seluruh mandatory field telah diisi.
9. Setelah Submit, form employee dikunci dan hanya dapat diubah kembali jika PA dikembalikan melalui Send Back.
10. Direct Supervisor dapat melihat Self Rating tetapi tidak dapat melihat penilaian One-Up Supervisor. One-Up Supervisor dapat melihat Self Rating dan penilaian Direct Supervisor.
11. Employee, Direct Supervisor, dan One-Up Supervisor tidak dapat melihat Rating History. Seluruh history perubahan hanya dapat dilihat oleh OD Section.
12. OD Section tidak memiliki kewenangan approval. Bulk action OD hanya digunakan untuk memindahkan PA ke tahap Normalization.
13. Summary Section tersedia pada seluruh role sesuai stage. Direct Supervisor dapat memberikan manual rating per section, sedangkan Overall Form Rating dihitung otomatis oleh sistem.
14. Sebelum PA Completed, Overall Form Rating pada sisi employee ditampilkan dalam bentuk tanda strip (-).
15. Overall Form Rating dihitung menggunakan rumus:
    `Overall Form Rating = Σ(Section Rating × Section Weight) / Σ(Section Weight)`
16. Normalisasi dilakukan di luar sistem. Hanya OD Section yang dapat melakukan export, import, re-import, individual adjustment, dan finalization.
17. OD dapat memilih beberapa department saat export, tetapi sistem menghasilkan satu file terpisah untuk setiap department dalam format XLSX atau CSV.
18. Data normalisasi hanya memerlukan nama normalisasi dan otomatis mengikuti periode PA aktif tanpa memiliki periode open atau close tersendiri.
19. Setiap import, re-import, dan perubahan Final Rating individual wajib disertai remarks serta dapat dilengkapi attachment. Seluruh versi perubahan disimpan sebagai audit log.
20. Goal yang telah disubmit tetap digunakan jika employee mengalami transfer atau promotion. Employee yang resign atau termination dikeluarkan dari proses PA.
21. Jika supervisor resign setelah memberikan penilaian, rating tetap digunakan. Jika resign sebelum memberikan penilaian, sistem melakukan bypass atau OD Section menentukan reviewer pengganti.
22. Activity pada Goal Management tidak memengaruhi rating maupun perhitungan PA.
23. Auto Rating untuk employee yang belum menyelesaikan Self-Rating tidak termasuk dalam scope saat ini.
24. GAP antara Self Rating dan Supervisor Rating, Signature Section, serta Acknowledge Section tidak ditampilkan dalam PA.
25. Template tidak bisa dirubah jika sudah di launch

## Sign-off / Approval

**Business Analyst signature:**

[Ilustrasi sumber dihapus dari korpus publik: Business Analyst signature]

| Role | Name | Date |
| --- | --- | --- |
| Business Analyst | Analis Bisnis B | Aug 2026 |
| Project Coordinator | Koordinator Proyek A |  |
| Business User Expert | Narasumber Bisnis C |  |

*By signing this document, all items contained herein are confirmed as mandatory requirements to be delivered as the agreed-upon product. Any changes or modifications to these requirements will be managed through the change request process.*
