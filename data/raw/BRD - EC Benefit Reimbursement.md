# BRD — EC Benefit Reimbursement

[Ilustrasi sumber dihapus dari korpus publik: Perusahaan A]

**IT SYSTEM DEVELOPMENT — BUSINESS REQUIREMENT ASSESSMENT**

**Project:** Sistem HRIS

**Module:** Benefits Submission

**Document version (footer):** 1.1

**Organization:** Perusahaan A

## Business Requirement Record

| Start Date | End Date | Author | Version Doc | Change Reference |
| --- | --- | --- | --- | --- |
| 26 Aug 2026 |   | Analis Bisnis A | 0.1 | Drafting |
| 28 Sep 2026 |   | Analis Bisnis A | 1.0 | Issued for Review |

## Log Changes

Describe the changes which impact to the Module

**Guidance (dokumen sumber):**

- Provide the name, detail changes and severity of the changes, e.g. Mr. X request for change on workflow due to new policy on dd/mmm/yyyy, etc

- Please identify all the changes clearly include impact to another module or infrastructure (if any).

### Change Record

| Date | Requested by | Description | Severity (major/minor) | Status |
| --- | --- | --- | --- | --- |
|   |   |   |   |   |
|   |   |   |   |   |

## Project and Module Information

| Item | Value |
| --- | --- |
| Project Description | Sistem HRIS |
| Business User Expert | Narasumber Bisnis A/ Narasumber Bisnis B |
| Assessment Date | 8 Sep 2026 |
| Module Description | Benefits Submission |

## Requirement Identification

### WHY — Module Objectives & Benefits

*Explain why this module is needed*

**Guidance (dokumen sumber):**

- Module Objectives/Goals: Your expected objectives on this module

e.g. decreasing numbers of paper used

- Module Benefits: The outcome of successful objectives/goals e.g. reducing the paper consumption cost

#### Module Objectives/Goals and Module Benefits

| Module Objectives/Goals | Module Benefits |
| --- | --- |
| Mempermudah proses pengajuan Benefit Assistance oleh karyawan secara terstruktur dan terpusat. | Proses pengajuan benefit menjadi lebih mudah, cepat, dan terdokumentasi dalam satu sistem. |
| Memastikan pengajuan benefit mengikuti ketentuan eligibility, periode, dan batas waktu yang berlaku dalam suatu proses yang terstruktur. | Mengurangi risiko kesalahan, duplicate claim, pengajuan yang tidak sesuai ketentuan dan memudahkan HR dalam memantau status pengajuan. |
| Menyediakan data benefit yang terstruktur untuk kebutuhan administrasi, pelaporan, dan pembayaran. | Mempermudah HR dan Finance dalam melakukan monitoring, rekonsiliasi, dan reporting benefit. |

### WHAT — Scope

*Describe the expected function or features on the app*

**Guidance (dokumen sumber):**

- In scope: Explain the expected function / feature to be included e.g.the reporting must in excel, must be easy to use in mobile, etc

- Out scope: Explain what function that exist on the current/manual system that should not be considered e.g. no need to add 3rd party account on login, etc

- Make sure to put anything that you can think about the scope

#### In Scope

##### Benefit Submission

Pembuatan form pengajuan Benefit Assistance oleh employee, meliputi:

- Education Assistance
- Informasi periode benefit dan claim date
- Informasi nominal benefit/entitlement
- Detail benefit sesuai jenis assistance
- Attachment supporting document
- Remarks

##### Benefit Eligibility & Calculation

- Validasi eligibility benefit berdasarkan data employee dan dependent.
- Perhitungan nominal benefit berdasarkan ketentuan benefit yang berlaku.
- Perhitungan benefit Education Assistance berdasarkan data dependent, termasuk maksimal 3 tanggungan.
- Perhitungan prorata benefit bagi employee baru dan employee status kontrak berdasarkan Date of Hire dan periode cutoff.
- Validasi data dependent pada Education Assistance dengan data dependent pada employee profile.
- Validasi untuk mencegah duplicate claim untuk dependent yang sama sesuai ketentuan benefit.
- Penentuan kategori dan plafon Education Assistance berdasarkan tingkat sekolah.
- Penyediaan konfigurasi kategori benefit berdasarkan level jabatan untuk kebutuhan pengembangan kebijakan di masa mendatang.
- Validasi plafon benefit berdasarkan periode yang berlaku.
- Validasi dependent untuk mencegah double claim antar employee.
- Validasi frekuensi pengajuan Education Assistance berdasarkan jenjang pendidikan.
- Validasi eligibility dependent berdasarkan usia.
- Validasi pengajuan berulang bagi karyawan kontrak selama masih memiliki sisa plafon benefit.

##### Supporting Document

- Upload dokumen pendukung sesuai jenis benefit.
- Validasi dokumen pendukung sesuai ketentuan benefit.
- Supporting document wajib dalam format PDF, dan JPG.
- Size supporting document 10 mb.
- Penyimpanan dokumen sebagai bagian dari data pengajuan benefit.
- Penyediaan form Education Assistance yang dapat di-download sebagai referensi pengajuan.

##### Approval Workflow

- Proses review dan approval pengajuan benefit oleh HR Compensation & Benefit melalui system workflow.
- Fitur Approve dan Send Back terhadap pengajuan benefit.
- Employee dapat melakukan perbaikan dan submit ulang untuk pengajuan yang berstatus Send Back.
- Super Admin dapat melakukan pembatalan terhadap pengajuan yang telah approved.

##### Benefit Period & Cut-off

- Pengajuan benefit menggunakan periode benefit/academic year yang berlaku.
- Sistem memungkinkan pengajuan untuk periode benefit yang berbeda sesuai ketentuan, termasuk periode tahun berjalan dan periode berikutnya.
- Validasi cut-off date untuk setiap periode benefit.
- Periode pengajuan mulai tanggal 1 juli – 15 juni tahun berikutnya
- Sistem tidak mengizinkan pengajuan employee pada periode 16–30 Juni.
- Sistem menyediakan mekanisme backdate submission oleh Super Admin atas nama employee sesuai kewenangan yang diberikan.

##### Notification & Reminder

- Notifikasi kepada HR Compensation & Benefit ketika terdapat pengajuan benefit baru.
- Notifikasi kepada employee ketika pengajuan disetujui.
- Notifikasi kepada employee ketika pengajuan dikembalikan (Send Back) beserta komentar reviewer.
- Notifikasi/warning terkait pengajuan yang melewati cut-off period.

##### Reporting & Data Export

- Penyediaan data Benefit Assistance untuk kebutuhan monitoring dan administrasi.
- Export data claim benefit dalam format Excel.
- Data export dapat digunakan sebagai compilation dari beberapa assistance claim untuk kebutuhan proses selanjutnya.

##### Data Migration

- Migrasi data historis Benfit Reimbursement 2021-latest

##### Integration

- Integrasi dengan Employee Central – Personal Data, khususnya data Dependents, sebagai dasar eligibility dan validasi Education Assistance.
- Penggunaan Employment Information, khususnya Date of Hire, untuk kebutuhan perhitungan benefit prorata.
- Penyediaan data benefit yang telah approved untuk kebutuhan proses pembayaran dan administrasi Finance.
- Penggunaan data dependent dari Employee Central sebagai dasar pengajuan dan validasi Education Assistance.
- Penggunaan employment information untuk kebutuhan perhitungan benefit prorata bagi karyawan kontrak.

#### Out Scope

##### Benefit Submission:

- Condolence Assistance

##### Employee & Dependent Data::

- Perubahan atau maintenance data employee.
- Penambahan, perubahan, atau penghapusan data dependent.

> Proses tersebut tetap dikelola melalui modul Personal Information.

##### Benefit Policy & Configuration:

- Perubahan kebijakan dan ketentuan Benefit Assistance.
- Penentuan atau perubahan nominal benefit dan eligibility policy.
- Perubahan tersebut menjadi tanggung jawab HR Compensation & Benefit.

##### Payroll & Payment Processing:

- Perhitungan dan pembayaran benefit secara langsung melalui sistem Payroll.
- Proses pembayaran benefit oleh tim HR Compensation & Benefit.

> Proses pembayaran tetap dilakukan sesuai prosedur dan sistem yang berlaku.

##### Offline Benefit Processing:

- Pengelolaan dan monitoring proses benefit yang dilakukan sepenuhnya di luar sistem.
- Proses administrasi setelah melewati cut-off yang dilakukan di luar sistem

### WHEN — Milestones

*Describe the expected completion dates on required milestone*

**Guidance (dokumen sumber):**

- Explain the expected milestone complete with expected start and end dates e.g. system must ready to used in dd/mm/yyyy, should be presented on management meeting on dd/mm/yyyy

| Milestones | Due Date | Remarks |
| --- | --- | --- |
| User Requirement | 15 Jul 2026 | Benefits Submission |

### WHO — Roles & Accessibilities

*Describe how many roles will be interact with this Module*

**Guidance (dokumen sumber):**

- Provide the role, assigned to and accessibilities on each role that will be included in the module e.g. HR as admin apps will be responsible to provide setting on the current process.

- Please identify all the participated person in your area to have a clear roles assignment.

#### Employee

Benefit Submission:

- Submit Benefit Assistance Request
- View Benefit Submission Status
- Update and Resubmit request yang ber-status Send Back
- Withdraw request yang ber-status Send Back
- View Benefit Submission History

#### HR Admin / HR Compensation & Benefit

Benefit Submission:

- View Benefit Submission Request
- Approve Benefit Submission Request
- Send Back Benefit Submission Request
- View Benefit Submission History
- Download & Extract Benefit Submission Report

#### Super Admin

Benefit Submission:

- View Benefit Submission Request
- Cancel approved Benefit Submission Request
- View Benefit Submission History
- Create backdate Benefit Submission Request for Employee

### WHAT IF — Risks & Mitigation

*Identify the risk and impact of the module*

**Guidance (dokumen sumber):**

- Explain the risk that might be a barrier / obstacle for this module. e.g. the procedure does not exist, need to be confirmed by BOD, etc

- Please think of any risk that might be impacted related to this module

#### Risks

| Risk | Level (Hi, Med, Low) |
| --- | --- |
| Employee mengajukan claim yang sama untuk dependent yang sama sehingga terjadi duplicate claim. | Hi |
| Pengajuan benefit melewati cut-off sehingga proses benefit tidak dapat dilakukan pada periode yang seharusnya. | Med |
| Karyawan berstatus kontrak yang diperpanjang/di-permanen-kan tidak mendapatkan hak benefit sepenuhnya. | Hi |

#### Mitigasi

- Sistem melakukan validasi terhadap riwayat claim untuk mencegah duplicate claim berdasarkan dependent dan periode benefit.

- Sistem memberikan warning apabila pengajuan dilakukan mendekati atau setelah cut-off.

- Karyawan kontrak dapat mengajukan benefit reimbursment kembali selamat plafon masih mencukupi.

## Current System Business Flow

***Guidance:***

* Please describe the current system that running / being used in essay.

* To maximize the understanding of current system, consider explaining with process flow in mind.

* Do it step by step from beginning to the end of process

* Example on essay (in Bahasa) :

> “Mr. X mengisi formulir exit form kemudian memintakan approval kepada department head. Setelah di approve, form kemudian diserahkan pada security pada saat user x berada di gerbang dan akan keluar dari area camp.”

* More complete the explanation will affect the next visual modelling process.

#### Benefits Submission

1. **Employee** menyiapkan dokumen pendukung sesuai dengan jenis benefit yang akan diajukan.
2. **Employee** mengajukan Benefit Assistance melalui sistem dengan melengkapi data dan dokumen yang diperlukan.
3. **HR Compensation & Benefit** melakukan review terhadap pengajuan benefit beserta dokumen pendukung.
4. Jika pengajuan **tidak disetujui,** pengajuan dikembalikan kepada Employee untuk diperbaiki dan diajukan kembali.
5. Jika pengajuan **disetujui**, data pengajuan diteruskan untuk proses pembayaran oleh **Finance.**
6. **Finance** melakukan proses pembayaran benefit sesuai dengan pengajuan yang telah disetujui.
7. Setelah proses pembayaran selesai, Benefit Submission process berakhir.

[Ilustrasi sumber dihapus dari korpus publik: Benefits Submission workflow]

## Expected New System Business Flow

***Guidance:***

* Please describe the expected improved system flow.

* To maximize the understanding of expected new system, consider explaining with process flow in mind.

* Do it step by step from beginning to the end of process

* More complete the explanation will affect the next visual modelling process.

#### Benefits Submission

1. **Employee** menyiapkan dokumen pendukung sesuai dengan jenis benefit yang akan diajukan.
2. **Employee** mengajukan Benefit Assistance melalui sistem dengan melengkapi data dan dokumen yang diperlukan.
3. **HR Compensation & Benefit** melakukan review terhadap pengajuan benefit beserta dokumen pendukung.
4. Jika pengajuan **tidak disetujui,** pengajuan dikembalikan kepada Employee untuk diperbaiki dan diajukan kembali.
5. Jika pengajuan **disetujui**, data pengajuan diteruskan untuk proses pembayaran oleh **Finance.**
6. **Finance** melakukan proses pembayaran benefit sesuai dengan pengajuan yang telah disetujui.
7. Setelah proses pembayaran selesai, Benefit Submission process berakhir.

**Untuk backdate:** Super Admin dapat membuat pengajuan atas nama employee sesuai kewenangannya. Sistem tetap mencatat identitas pembuat pengajuan dan employee yang diwakili.

[Ilustrasi sumber dihapus dari korpus publik: Benefits Submission workflow]

## Business Rules

### Business Rules – Benefit Submission

- Pengajuan Benefit Assistance pada kondisi normal hanya dapat dilakukan oleh employee yang bersangkutan melalui sistem.
- Dalam kondisi backdate yang diperbolehkan, Super Admin dapat membuat pengajuan atas nama employee sesuai kewenangan yang diberikan.
- Employee hanya dapat mengajukan jenis benefit yang **eligible** sesuai dengan ketentuan perusahaan.
- Setiap pengajuan benefit harus dilengkapi dengan data dan informasi yang diperlukan sesuai dengan jenis benefit.
- Employee tidak dapat melakukan pengajuan apabila terdapat **claim yang masih aktif atau claim yang sama telah diproses** sesuai dengan ketentuan benefit.

### Business Rules – Benefit Eligibility & Calculation

- Eligibility Education Assistance ditentukan berdasarkan **data dependent** yang tercatat pada Employee Central.
- Data dependent yang digunakan dalam pengajuan harus sesuai dengan data dependent pada Employee Central.
- Perhitungan Education Assistance dilakukan berdasarkan ketentuan benefit yang berlaku dan dapat mencakup maksimal **3 tanggungan**.
- Benefit untuk employee baru dapat dihitung secara **prorata berdasarkan Date of Hire sampai dengan tanggal cutoff**.
- Benefit yang telah diterima oleh employee tidak perlu dikembalikan apabila employee kemudian mengundurkan diri, sesuai dengan ketentuan perusahaan.
- Kategori Education Assistance ditentukan berdasarkan **tingkat sekolah** yang berlaku.
- Plafon benefit dapat berbeda berdasarkan kategori benefit dan periode yang berlaku.
- Employee tidak dapat melakukan claim apabila plafon benefit untuk periode yang sama telah tercapai.
- Anak yang berusia di atas 23 tahun tidak eligible untuk Education Assistance.
- Perhitungan dan pengajuan Education Assistance mengikuti ketentuan plafon benefit yang berlaku.
- Karyawan kontrak dapat mengajukan benefit secara berulang selama masih memiliki sisa plafon benefit.
- Pengajuan benefit harus memenuhi ketentuan frekuensi berdasarkan jenjang pendidikan.

### Business Rules – Dependent & Duplicate Claim

- Data dependent yang digunakan untuk Education Assistance harus sesuai dengan data dependent yang tercatat pada Employee Central.
- Dependent yang sama tidak dapat digunakan untuk claim Education Assistance oleh lebih dari satu employee pada periode yang sama.
- Jika pasangan suami dan istri sama-sama merupakan employee perusahaan, benefit untuk dependent hanya dapat diklaim oleh salah satu employee sesuai status dependent yang tercatat.
- Data dependent yang digunakan untuk Education Assistance harus sesuai dengan data dependent yang tercatat pada Employee Central.
- Setiap employee hanya dapat memiliki maksimal 3 dependent sesuai ketentuan perusahaan.
- Dependent yang sama tidak dapat digunakan untuk pengajuan ganda yang melanggar ketentuan benefit.

### Education Assistance Claim Frequency

- Pengajuan Education Assistance untuk jenjang PAUD hanya dapat dilakukan sebanyak 1 kali per dependent sesuai ketentuan benefit.
- Pengajuan Education Assistance untuk jenjang TK hanya dapat dilakukan sebanyak 2 kali per dependent sesuai ketentuan benefit.
- Pengajuan Education Assistance untuk jenjang SD sampai kuliah tidak dibatasi berdasarkan frekuensi pengajuan, selama plafon benefit masih mencukupi.
- Sistem harus memvalidasi riwayat claim untuk memastikan frekuensi pengajuan tidak melebihi ketentuan yang berlaku.

### Business Rules – Supporting Document

- Setiap pengajuan benefit yang memerlukan dokumen pendukung wajib dilengkapi dengan dokumen sesuai ketentuan benefit.
- Dokumen pendukung yang diunggah harus dalam format **PDF** atau **JPG**.
- Dokumen pendukung harus sesuai dengan jenis benefit yang diajukan.
- Pengajuan tidak dapat diproses apabila dokumen pendukung yang diwajibkan belum tersedia.

### Business Rules – Benefit Period & Cut-off

- Pengajuan Education Assistance dilakukan berdasarkan **periode/academic year** yang berlaku.
- Employee dapat mengajukan benefit untuk periode yang diperbolehkan sesuai dengan ketentuan perusahaan.
- Setiap periode benefit memiliki **cut-off date** yang ditentukan oleh perusahaan (1 Juli – 15 Juni tahun berikutnya).
- Tahun ajaran Education Assistance dikunci pada **15 Juni setiap tahun berjalan**.
- Setelah tahun ajaran dikunci, pengajuan untuk periode tersebut mengikuti ketentuan proses setelah cut-off.
- Sistem memberikan warning apabila pengajuan dilakukan setelah tanggal cut-off.
- Periode pengajuan Education Assistance berlangsung dari 1 Juli sampai dengan 15 Juni tahun berikutnya.
- Pengajuan employee tidak diperbolehkan pada tanggal 16–30 Juni.
- Sistem harus melakukan validasi terhadap tanggal pengajuan berdasarkan periode yang berlaku.
- Pengajuan yang dilakukan di luar periode submission tidak dapat diproses melalui submission normal.
- Super Admin dapat membuat pengajuan secara backdate atas nama employee sesuai kewenangannya.

### Business Rules – Duplicate Claim

- Employee permanent, tidak dapat mengajukan benefit yang sama secara berulang untuk **dependent dan periode yang sama**.
- Employee kontrak dapat mengajukan benefit yang sama secara berulang selama plafon masih mencukupi.
- Sistem harus melakukan validasi terhadap riwayat claim untuk mencegah duplicate claim.
- Education Assistance untuk dependent yang sama harus mengikuti ketentuan jenjang pendidikan dan periode benefit yang berlaku.

### Business Rules – Approval

- Setiap pengajuan benefit harus melalui proses **review dan approval HR Compensation & Benefit**.
- Pengajuan yang di-Send Back wajib diberikan komentar.
- Pengajuan yang di-Send Back dapat diperbaiki dan diajukan kembali oleh employee.
- Pengajuan yang telah disetujui dapat dibatalkan oleh **Super Admin** sesuai kewenangan yang diberikan.
- Pengajuan yang telah approved menjadi dasar untuk proses administrasi pembayaran oleh HR Compensation & Benefit.
- Pengajuan yang dibuat oleh Super Admin atas nama employee harus tetap mengikuti proses review dan approval yang berlaku, kecuali terdapat ketentuan khusus yang telah disetujui perusahaan.

### Business Rules – Withdrawal

- Employee dapat membatalkan (**Withdraw**) pengajuan selama untuk pengajuan dengan status **Sent back**.

### Business Rules – Notification

- Employee menerima notification ketika pengajuan **disetujui, atau di-Send Back**.
- HR Compensation & Benefit menerima notification ketika terdapat pengajuan baru yang memerlukan review.
- Notification terkait cut-off diberikan kepada employee apabila pengajuan dilakukan setelah atau mendekati batas waktu yang ditentukan.
- Employee menerima notification ketika Super Admin membatalkan/cancel pengajuan yang sudah disetujui.

### Business Rules – Integrity

- Data dan informasi pada pengajuan harus sesuai dengan dokumen pendukung yang dilampirkan.
- Employee bertanggung jawab atas kebenaran dan kelengkapan informasi yang disampaikan.
- HR Compensation & Benefit bertanggung jawab melakukan verifikasi terhadap data dan dokumen sebelum memberikan keputusan atas pengajuan.

## Functional Requirements

### Benefit Submission

#### Benefit Submission Form

- Sistem menyediakan form pengajuan Benefit Assistance yang dapat diakses oleh employee.
- Sistem menampilkan informasi Claim Date, Selected Benefit, Currency, dan Benefit Amount/Entitlement.

#### Education Assistance Details

- Sistem menyediakan form Education Assistance Details untuk setiap dependent yang diajukan.
- Sistem menampilkan data dependent yang eligible berdasarkan data dependent pada Employee Central.
- Employee dapat mengajukan maksimal 3 dependent sesuai ketentuan benefit.
- Sistem menyediakan informasi pendidikan yang diperlukan, termasuk nama student, identification number, date of birth, school, grade, education year, dan informasi sekolah.
- Employee dapat menambahkan detail education assistance sesuai jumlah dependent yang eligible.

#### Dependent Data Auto-Fill

- Sistem menampilkan daftar dependent yang eligible berdasarkan data dependent pada Employee Central.
- Employee memilih dependent yang akan digunakan untuk pengajuan Education Assistance.
- Setelah dependent dipilih, sistem secara otomatis mengisi data dependent yang tersedia pada Employee Central ke dalam form Education Assistance.
- Data tambahan yang tidak tersedia pada Employee Central dapat diisi oleh employee sesuai dengan field yang disediakan.

### Benefit Eligibility & Calculation

#### Benefit Eligibility Validation

- Sistem melakukan validasi eligibility employee sebelum pengajuan dapat dilakukan.
- Sistem melakukan validasi eligibility Education Assistance berdasarkan data dependent pada Employee Central.
- Sistem hanya menampilkan dependent yang memenuhi ketentuan untuk pengajuan benefit.
- Sistem melakukan validasi usia dependent berdasarkan data yang tersedia pada Employee Central.
- Sistem tidak mengizinkan dependent yang berusia di atas 23 tahun digunakan untuk pengajuan Education Assistance.
- Sistem memvalidasi kesesuaian data dependent dengan data reimbursement yang diajukan.
- Sistem menolak pengajuan apabila data dependent dan data reimbursement tidak memiliki hubungan satu banding satu sesuai ketentuan perusahaan.

#### Benefit Calculation

- Sistem menyimpan kategori budget Education Assistance berdasarkan tingkat sekolah.
- Sistem menghitung Education Assistance berdasarkan jumlah dependent dan ketentuan pendidikan yang berlaku.
- Sistem menghitung benefit secara prorata untuk employee baru & kontrak berdasarkan Date of Hire dan tanggal cutoff.
- Employee tidak dapat mengubah nominal benefit yang telah dihitung oleh system.

#### Duplicate Claim Validation

- Sistem melakukan validasi terhadap claim yang telah diajukan atau diproses sebelumnya untuk karyawan tetap.
- Sistem mencegah duplicate claim untuk dependent dan periode benefit yang sama untuk karyawan tetap.
- Karyawan kontrak dapat mengajukan claim berulang selama masih memiliki jatah plafon.
- Sistem melakukan validasi terhadap jenjang pendidikan dependent untuk mencegah claim yang tidak sesuai dengan ketentuan benefit untuk karyawan tetap.

#### Education Assistance Claim Frequency

- Sistem melakukan validasi frekuensi pengajuan Education Assistance berdasarkan jenjang pendidikan.
- Sistem membatasi pengajuan PAUD maksimal 1 kali.
- Sistem membatasi pengajuan TK maksimal 2 kali.
- Sistem mengizinkan pengajuan untuk jenjang SD sampai kuliah selama plafon benefit masih mencukupi.
- Sistem memvalidasi riwayat claim sebelum submission dapat dilakukan.

#### Super Admin Backdate Submission

- Sistem menyediakan akses kepada Super Admin untuk membuat pengajuan Benefit Assistance atas nama employee.
- Sistem memungkinkan Super Admin menentukan tanggal pengajuan sesuai kebutuhan backdate.
- Sistem mencatat identitas Super Admin sebagai pembuat pengajuan dan employee sebagai pemilik pengajuan.
- Sistem menyimpan tanggal pembuatan aktual dan tanggal pengajuan untuk kebutuhan audit trail.

### Benefits Submission Field Details

#### Education Claim Form

| **Column/Field Name** | **Data Type** | **Editable** | **Mandatory** | **Note** |
| --- | --- | --- | --- | --- |
| Claim Date | Date Picker | Yes | Yes |  |
| Selected Benefit | Picklist | Yes | Yes | Education Assistance Only |
| Currency | Picklist | No | Yes |  |
| Entitlement Amount | Amount | No | Yes | Calculated by system based on benefit eligibility |
| Name of Student | Text | No | Yes |  |
| Student's Identity Number | Text | Yes | Yes |  |
| Age | Number | No | Yes |  |
| Date of Birth | Date Picker | No | No |  |
| School | Picklist | Yes | Yes |  |
| Grade | Picklist | Yes | No |  |
| Education Year | Text/Number | No | Yes |  |
| Gender of Student | Picklist | No | No |  |
| School's Name | Text | No | Yes |  |
| School Address | Text Area | Yes | No |  |
| Attachment | Attachment | Yes | Yes | Supporting document in PDF format |
| Remarks | Text Area | Yes | No |  |

### Supporting Document

#### Supporting Document Upload

- Sistem menyediakan fitur upload dokumen pendukung pada pengajuan benefit.
- Sistem hanya menerima dokumen dengan format PDF atau JPG sesuai ketentuan.
- Sistem melakukan validasi terhadap kelengkapan dokumen yang diwajibkan.
- Dokumen yang telah di-upload disimpan sebagai bagian dari data pengajuan benefit.

#### Education Assistance Form

- Sistem menyediakan form Education Assistance yang dapat di-download oleh HR Compensation & Benefit.

### Approval Workflow

#### Benefit Review

- Sistem mengirimkan pengajuan yang telah disubmit kepada HR Compensation & Benefit untuk dilakukan review.
- HR Compensation & Benefit dapat melihat data pengajuan dan supporting document yang dilampirkan.

#### Approve / Send Back

- HR Compensation & Benefit dapat melakukan:
  - Approve
  - Send Back
- HR wajib memberikan komentar pada pengajuan yang di-Send Back.
- Pengajuan yang berstatus Send Back dapat diperbaiki dan disubmit kembali oleh employee.

#### Approved Benefit Cancellation

- Super Admin dapat melakukan pembatalan terhadap pengajuan yang telah berstatus Approved.
- Sistem mencatat status pembatalan dan informasi pengguna yang melakukan pembatalan.

### Benefit Period & Cut-off

#### Benefit Period

- Sistem menyediakan informasi periode benefit/academic year pada saat pengajuan.
- Sistem memungkinkan employee mengajukan benefit untuk periode yang masih dibuka sesuai ketentuan.
- Sistem dapat membedakan claim berdasarkan periode benefit untuk mencegah duplicate claim
- Sistem mengizinkan employee melakukan pengajuan pada periode 1 Juli sampai dengan 15 Juni tahun berikutnya.
- Sistem menolak pengajuan employee pada tanggal 16–30 Juni.

#### Cut-off Validation

- Sistem melakukan validasi terhadap cut-off date setiap periode benefit.
- Sistem memberikan warning apabila employee melakukan pengajuan setelah cut-off.

### Notification

#### Submission Notification

- Sistem mengirimkan notification kepada HR Compensation & Benefit ketika terdapat pengajuan baru.

#### Status Notification

- Sistem mengirimkan notification kepada employee berdasarkan perubahan status pengajuan, termasuk:
  - Approved
  - Send Back
  - Cancelled
- Notification Send Back dan Cancelled menampilkan komentar.

### Submission History & Tracking

- Sistem menyediakan informasi riwayat pengajuan Benefit Assistance bagi employee.
- Employee dapat melihat status dan informasi pengajuan yang telah dibuat.
- HR Compensation & Benefit dapat melihat riwayat pengajuan benefit yang menjadi kewenangannya.
- Sistem mencatat status, tanggal pengajuan, tanggal perubahan status, dan pihak yang melakukan tindakan pada pengajuan.

### Reporting & Data Export

#### Benefit Data Export

- Sistem menyediakan fitur export data Benefit Assistance dalam format Excel.
- Data export mencakup informasi claim, employee, benefit type, periode benefit, nominal benefit, status, dan informasi lain yang diperlukan untuk administrasi.
- Data yang telah approved dapat digunakan sebagai dasar compilation dan proses administrasi pembayaran oleh HR Compensation & Benefit.

### Integration

#### Employee Central Data Integration

- Sistem menggunakan data employee dan dependent dari Employee Central untuk kebutuhan eligibility dan validation.
- Sistem menggunakan Date of Hire dari Employee Central untuk kebutuhan perhitungan prorata.
- Sistem melakukan validasi bahwa dependent yang digunakan dalam Education Assistance sesuai dengan data yang tercatat pada Employee Central.

### Execption Handling

Sistem harus menangani kondisi khusus yang dapat terjadi selama proses **Benefits Submission**.

#### Multiple Benefits Submission

Sistem tidak mengizinkan Requestor membuat pengajuan **Benefits Submission** yang sama apabila masih terdapat pengajuan dengan status **In Progress** untuk employee dan dependent yang sama. Pengajuan perubahan yang sama hanya dapat dibuat kembali setelah pengajuan sebelumnya berstatus **Withdrawn,** atau masih memiliki sisa plafon untuk karyawan kontrak.

#### Withdraw

Apabila Requestor melakukan Withdraw, sistem akan:

- Mengubah status pengajuan menjadi **Withdrawn**.
- Mengirimkan notifikasi kepada HR Compensation & Benefit.
- Menyimpan aktivitas tersebut pada Activity Log.

#### Submission Period Validation

- Apabila employee melakukan submission pada tanggal 16–30 Juni, sistem menolak pengajuan dan menampilkan informasi bahwa periode submission sedang ditutup.

#### Claim Frequency Validation

- Apabila employee telah mencapai batas frekuensi claim untuk jenjang pendidikan tertentu, sistem menolak pengajuan.
- Sistem menampilkan informasi bahwa batas frekuensi pengajuan untuk jenjang pendidikan tersebut telah tercapai.

### Notification/Notifikasi

#### 1. Benefit Submission – Submitted

**Trigger** : Employee has submitted a Benefit Assistance request.

**Recipient** : HR Compensation & Benefit

**Subject** : Benefit Submission Request for **{Employee Name}** Requires Your Review

**Email Body :**

Hello **{Approver Name}**,

A Benefit Assistance request for **{Employee Name}** has been submitted by **{Employee Name}** on **{Submission Date}** and requires your review.

Please review the request and take the necessary action through the Benefit Submission application.

**Application Link:**  
{Application URL}

#### 2. Benefit Submission – Send Back

**Trigger** : HR Compensation & Benefit has sent back a Benefit Assistance request for revision.

**Recipient** : Requestor / Employee

**Subject** : Benefit Submission Request for **{Employee Name}** Requires Revision

**Email Body :**

Hello **{Employee Name}**,

Your request has been sent back by **{Approver Name}** and requires revision.

Please review the comments and make the necessary changes before submitting the request again.

**Application Link:**  
{Application URL}

#### 3. Benefit Submission – Approved

**Trigger** : HR Compensation & Benefit has approved a Benefit Assistance request.

**Recipient** : Requestor / Employee

**Subject** : Benefit Submission Request for **{Employee Name}** Has Been Approved

**Email Body :**

Hello **{Requestor Name}**,

Your request has been approved by **{Approver Name}**.

The approved request will proceed to the next process for benefit payment and administration.

**Application Link:**  
{Application URL}

#### 4. Benefit Submission Withdrawn

**Trigger** : Requestor has withdrawn a Benefit Submission.

**Recipient** : HR Compensation & Benefit

**Subject** : Benefit Submission Request for **{Employee Name}** Has Been Withdrawn

**Email Body :**

Hello **{Recipient Name}**,

The Benefit Submission request for **{Employee Name}** has been withdrawn by **{Requestor Name}** on **{Withdrawal Date}**.

The request is no longer available for further approval.

**Application Link**  
{Application URL}

#### 5. Benefit Submission Approval Reminder

**Trigger** : The Benefit Submission request remains pending and the assigned approver has not completed the required approval action within the configured reminder period.

**Recipient**: HR Compensation & Benefit

**Subject** : Reminder: Benefit Submission Request for **{Employee Name}** Requires Your Review

**Email Body :**

Hello **{Approver Name}**,

This is a reminder that the Benefit Submission request for **{Employee Name}** is still pending your review.

Please review the request and take the necessary action through the Benefit Submission application.

**Application Link**

{Application URL}

#### Notification Matrix

| **Event** | **Recipient** |
| --- | --- |
| Submit | HR Compensation & Benefit |
| Send Back | Requestor / Employee |
| Approve | Requestor / Employee |
| Withdraw | HR Compensation & Benefit |
| Reminder | HR Compensation & Benefit |

## User Interface

### Benefits Reimbursement

[Ilustrasi sumber dihapus dari korpus publik: Benefits Reimbursement]

### Claim Education Assistance Form

[Ilustrasi sumber dihapus dari korpus publik: Claim Education Assistance Form]

### Claim Education Assistance Details & History

[Ilustrasi sumber dihapus dari korpus publik: Claim Education Assistance Details & History]

### Benefit Reimbursement Request

[Ilustrasi sumber dihapus dari korpus publik: Benefit Reimbursement Request]

### Benefit Reimbursement Monitoring

[Ilustrasi sumber dihapus dari korpus publik: Benefit Reimbursement Monitoring]

### Workflow Details

[Ilustrasi sumber dihapus dari korpus publik: Workflow Details]

## Validation Rules

### Benefits Reimbursement Validation

| **Validation Rule** | **Error Message** |
| --- | --- |
| Sistem hanya mengizinkan satu pengajuan **Benefit Reimbursement** dengan status **In Progress** untuk dependent yang sama. | *An active request already exists for this Dependent. Please complete or withdraw the existing request before submitting a new one.* |
| Ukuran dokumen pendukung tidak boleh melebihi batas yang ditentukan. | *The file size exceeds the maximum allowed limit.* |

### Mandatory Field Validation

| **Validation Rule** | **Error Message** |
| --- | --- |
| Seluruh mandatory field pada Benefits Reimbursement wajib diisi sebelum Submit. | *Please complete all mandatory fields before submitting the request.* |

### Send Back Validation

| **Validation Rule** | **Error Message** |
| --- | --- |
| Komentar wajib diisi ketika HR melakukan Send Back. | *Please provide a comment before sending the request back.* |

### Withdraw Validation

| **Validation Rule** | **Error Message** |
| --- | --- |
| Employee hanya dapat melakukan Withdraw terhadap request yang masih berstatus sent back. | *This request can no longer be withdrawn because the approval process is in process or has been completed..* |
| Request yang telah berstatus Withdrawn tidak dapat diproses kembali. | *This request has been withdrawn and can no longer be processed.* |

### Submission Validation

| **Validation Rule** | **Error Message** |
| --- | --- |
| Sistem tidak mengizinkan pengajuan Education Assistance untuk dependent yang berusia di atas 23 tahun. | *This dependent is not eligible for Education Assistance.* |
| Sistem memvalidasi bahwa data dependent dan data reimbursement sesuai. | *The dependent information does not match the reimbursement details.* |
| Sistem membatasi pengajuan PAUD maksimal 1 kali. | *The maximum claim frequency for PAUD for this dependent has been reached.* |
| Sistem membatasi pengajuan TK maksimal 2 kali. | *The maximum claim frequency for TK for this dependent has been reached.* |
| Sistem menolak submission employee pada tanggal 16–30 Juni. | *Benefit submission is currently closed. Please submit your request during the applicable submission period.* |
| Sistem menolak pengajuan apabila plafon benefit telah tercapai. | *Your benefit entitlement has been fully utilized for this period.* |

## Security Requirements

### Data Confidentiality

Data Benefit Submission merupakan informasi yang bersifat confidential dan hanya dapat diakses oleh pengguna sesuai dengan kewenangan dan kebutuhan proses bisnis.

Confidential data meliputi, namun tidak terbatas pada:

- Employee Information
- Dependent Information
- Benefit Type dan Benefit Period
- Claim Amount / Entitlement
- Supporting Document
- Approval Information

Akses terhadap data tersebut harus mengikuti prinsip **Role-Based Access Control (RBAC)**.

### Benefit Submission Access

Hak akses terhadap Benefit Submission diatur berdasarkan role dan proses bisnis.

**Employee** hanya dapat:

- Melihat pengajuan benefit miliknya sendiri.
- Membuat dan mengubah pengajuan benefit miliknya sendiri sesuai status pengajuan.
- Melihat status dan history pengajuan benefit miliknya sendiri.
- Melihat supporting document yang terkait dengan pengajuannya.

**HR Compensation & Benefit** dapat:

- Melihat pengajuan benefit yang menjadi tanggung jawabnya.
- Melakukan review dan memberikan keputusan terhadap pengajuan.
- Mengakses supporting document yang diperlukan untuk proses review dan approval.
- Mengakses data benefit yang telah approved untuk kebutuhan proses pembayaran dan administrasi.

**Super Admin** dapat:

- Mengakses pengajuan sesuai kewenangannya.
- Melakukan cancellation terhadap pengajuan yang telah approved sesuai business rules.
- Membuat pengajuan Benefit Submission atas nama employee sesuai kewenangan yang diberikan.

### Document Access

Supporting document yang dilampirkan pada Benefit Submission merupakan informasi confidential.

- Employee hanya dapat mengakses dokumen yang terkait dengan pengajuannya sendiri.
- HR Compensation & Benefit dapat mengakses dokumen yang diperlukan untuk proses review dan approval.
- Pengguna tanpa hak akses tidak dapat melihat atau mengunduh supporting document.

### Audit Trail

Sistem harus mencatat aktivitas pengguna selama proses Benefit Submission berlangsung.

Audit Trail minimal mencatat:

- Submit
- Approve
- Edit
- Send Back
- Resubmit
- Withdraw

Setiap aktivitas harus menyimpan informasi:

- User
- Role
- Activity
- Date & Time
- Request ID

Audit Trail bersifat **read-only** dan tidak dapat diubah maupun dihapus oleh pengguna.

## Approval / Signatures

| Role | Name | Signature | Date |
| --- | --- | --- | --- |
| Business Analyst | Analis Bisnis A | [Ilustrasi sumber dihapus dari korpus publik: Signature] | 28 September 2026 |
| Project Coordinator | Koordinator Proyek A | | |
| Business User Expert | Narasumber Bisnis A | | |
| Business User Expert | Narasumber Bisnis B | | |

*By signing this document, all items contained herein are confirmed as mandatory requirements to be delivered as the agreed-upon product. Any changes or modifications to these requirements will be managed through the change request process.*
