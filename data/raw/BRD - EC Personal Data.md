# BRD - EC Personal Data

IT SYSTEM DEVELOPMENT — BUSINESS REQUIREMENT ASSESSMENT

Business Requirement Assessment Document — Document version: 1.1

## Business Requirement Record

| **Start Date** | **End Date** | **Author** | **Version Doc** | **Change Reference** |
| --- | --- | --- | --- | --- |
| 07 Aug 2026 |  | Analis Bisnis A | 0.1 | Drafting |
| 11 Sep 2026 |  | Analis Bisnis A | 1.0 | Submitted for Review |

## Log Changes

Describe the changes which impact to the Module

> ***Guidance:***
>
> \* Provide the name, detail changes and severity of the changes, e.g. Mr. X request for change on workflow due to new policy on dd/mmm/yyyy, etc
>
> \* Please identify all the changes clearly include impact to another module or infrastructure (if any).

### Change Record

| Date | Requested by | Description | Severity (major/minor) | Status |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
|  |  |  |  |  |

## Project Information

| Item | Value |
| --- | --- |
| Project Description | Sistem HRIS |
| Module Description | Personal Data |
| Business User Expert | Narasumber Bisnis A/Narasumber Bisnis C |
| Assessment Date | 15 Juli 2026 – 3 Sep 2026 |

## Requirement Identification

### WHY

Explain why this module is needed

> ***Guidance:***
>
> \*Module Objectives/Goals: Your expected objectives on this module
>
> e.g. decreasing numbers of paper used
>
> \* Module Benefits: The outcome of successful objectives/goals e.g. reducing the paper consumption cost

| Module Objectives/Goals | Module Benefits |
| --- | --- |
| Memberikan kemudahan bagi karyawan untuk mengajukan perubahan data pribadi secara mandiri melalui sistem. | Mempermudah proses pengajuan perubahan data tanpa harus dilakukan secara manual melalui HR. |
| Memastikan setiap perubahan data pribadi melalui proses verifikasi dan persetujuan HR sebelum diterapkan ke sistem. | Meningkatkan akurasi dan validitas data karyawan yang tersimpan di sistem. |
| Menyediakan proses pengelolaan perubahan data yang terdokumentasi dan dapat ditelusuri. | Memudahkan pelacakan riwayat perubahan data untuk kebutuhan audit dan administrasi. |
| Mendukung proses administrasi personalia yang lebih terstandarisasi dan terdigitalisasi. | Meningkatkan efisiensi proses administrasi serta mengurangi penggunaan dokumen dan proses manual. |

### WHAT

Describe the expected function or features on the app

> ***Guidance:***
>
> \* In scope: Explain the expected function / feature to be included e.g.the reporting must in excel, must be easy to use in mobile, etc
>
> \* Out scope: Explain what function that exist on the current/manual system that should not be considered e.g. no need to add 3<sup>rd</sup> party account on login, etc
>
> \* Make sure to put anything that you can think about the scope

#### In Scope

##### Pengajuan Perubahan Data Personal

- Pembuatan form pengajuan perubahan data personal oleh employee, meliputi:

  - Personal Information

  - Biographical Information

  - Address

  - Contact Information

  - National ID Information

  - Primary Emergency Contact

  - Dependents

  - Payment Information

  - Position and Organisation Information

  - Job Details

  - Job Relationships

  - Employment Details

  - Personal Documents

  - Compensation Information

  - Non Recurring Pay Component

  - Time Information

  - Basic Information

  - Details Information

  - Education

  - Honors/Awards

  - Work Experience Within Company

  - Previous Employment

  - Courses

  - Certifications

  - Professional Memberships

  - Volunteer Involvement

##### Attachment Supporting Document

- Upload dokumen pendukung sesuai jenis perubahan data.

- Validasi dokumen pendukung berdasarkan ketentuan perusahaan.

- Penyimpanan dokumen sebagai bagian dari pengajuan perubahan data.

##### Approval Workflow

- Proses review dan approval oleh HR Compensation & Benefit melalui sistem workflow.

- Fitur Approve dan Send Back terhadap pengajuan perubahan data.

- Employee dapat melakukan perbaikan dan submit ulang untuk pengajuan yang berstatus Send Back.

- Employee dapat melakukan Withdraw terhadap pengajuan yang berstatus Send Back.

##### Notification & Reminder

- Notifikasi kepada HR Compensation & Benefit ketika terdapat pengajuan baru.

- Notifikasi kepada employee ketika pengajuan disetujui.

- Notifikasi kepada employee ketika pengajuan dikembalikan (Send Back) beserta komentar reviewer.

- Notifikasi kepada HR ketika pengajuan di-withdraw oleh Employee.

- Reminder kepada HR Compensation & Benefits ketika pengajuan belum di-action.

##### Personal Data History

- Penyimpanan riwayat perubahan data personal.

- Informasi nilai sebelum dan sesudah perubahan.

- Informasi status pengajuan, tanggal perubahan, dan approver.

- Riwayat perubahan dapat ditelusuri untuk kebutuhan audit.

##### Data Migration

- Migrasi data historis Personal Data 2021-latest

##### Integration

###### Payroll & Compensation

- Perubahan data yang berkaitan dengan informasi pembayaran (Payment Information) diperbarui sesuai hasil approval.

- Perubahan data yang memengaruhi administrasi payroll (apabila ada) mengikuti hasil approval.

###### Benefits

- Perubahan status pernikahan dan data tanggungan (Dependents) diperbarui sesuai hasil approval.

- Data yang digunakan sebagai dasar administrasi benefit mengikuti data terbaru yang telah disetujui.

#### Out Scope

##### Employee Termination:

- Proses pengunduran diri.

- Pemberhentian karyawan.

- Pemutusan hubungan kerja (Termination).

- Exit clearance.

**\* Seluruh proses tersebut akan dikelola pada modul Manage Termination.**

##### Payroll Processing:

- Perhitungan gaji.

- Perhitungan bonus.

- Perhitungan tunjangan.

- Perhitungan pajak.

##### Recruitment Process:

- Recruitment Requisition.

- Candidate Management.

- Hiring Process.

##### Performance Evaluation

- Performance Review.

- Goal Management.

- Talent Assessment.

**\* Seluruh proses tersebut akan dikelola pada modul PMGM.**

##### Organization

- Pembuatan struktur organisasi baru.

- Pembuatan posisi baru.

- Penghapusan posisi.

**\* Perubahan tersebut dikelola melalui modul Organization Structure dan Position Management.**

##### Employee Status Change

- Promotion

- Transfer

- Demotion

- Reclassification

- Contract Renewal

- Working Hours & Work Schedule

- Termination

- Position Management

**\* Perubahan tersebut dikelola melalui modul Employee Status Change.**

### WHEN

Describe the expected completion dates on required milestone

> ***Guidance:***
>
> \* Explain the expected milestone complete with expected start and end dates e.g. system must ready to used in dd/mm/yyyy, should be presented on management meeting on dd/mm/yyyy

| Milestones | Due Date | Remarks |
| --- | --- | --- |
| User Requirement | 15 Jul 2026 | Personal Data |
|  |  |  |

### WHO

Describe how many roles will be interact with this Module

> ***Guidance:***
>
> \* Provide the role, assigned to and accessibilities on each role that will be included in the module e.g. HR as admin apps will be responsible to provide setting on the current process.
>
> \* Please identify all the participated person in your area to have a clear roles assignment.

#### HR Admin

Personal Data:

- Update Personal Data Update Request

- Approve Personal Data Update Request

- Send Back Personal Data Update

- View all Personal Data history

#### Requestor

Personal Data:

- Request Personal Data Update

- View Personal Data History

### WHAT IF

Identify the risk and impact of the module

> ***Guidance:***
>
> \* Explain the risk that might be a barrier / obstacle for this module. e.g. the procedure does not exist, need to be confirmed by BOD, etc
>
> \* Please think of any risk that might be impacted related to this module

| Risks | Level (Hi, Med, Low) |
| --- | --- |
| Keterlambatan proses approval menyebabkan data karyawan tidak segera diperbarui. | Med |
| Employee mengajukan perubahan yang sama ketika masih terdapat pengajuan yang sedang diproses. | Hi |

#### Mitigasi

Sistem menyediakan notifikasi kepada approver serta reminder untuk pengajuan yang belum diproses.

Sistem melakukan validasi terhadap pengajuan yang masih aktif atau memberikan informasi status pengajuan yang sedang berjalan (sesuai business rule).

## Current System Business Flow

***Guidance:***

\* Please describe the current system that running / being used in essay.

\* To maximize the understanding of current system, consider explaining with process flow in mind.

\* Do it step by step from beginning to the end of process

\* Example on essay (in Bahasa) :

> “Mr. X mengisi formulir exit form kemudian memintakan approval kepada department head. Setelah di approve, form kemudian diserahkan pada security pada saat user x berada di gerbang dan akan keluar dari area camp.”

\* More complete the explanation will affect the next visual modelling process.

### Update Personal Data

1.  **Employee menyiapkan dokumen pendukung** (Manual Process)

    - Employee mempersiapkan dokumen pendukung sesuai dengan jenis perubahan data yang akan diajukan (misalnya Kartu Keluarga, Buku Nikah, atau dokumen lainnya sesuai kebijakan perusahaan).

2.  **Employee mengisi data perubahan** (Application Process)

    - Employee membuka menu **Personal Data** pada Sistem HRIS.

    - Employee melakukan perubahan data sesuai kebutuhan.

    - Employee mengunggah dokumen pendukung yang dipersyaratkan.

    - Employee mengirimkan (submit/save) pengajuan perubahan data.

3.  **HR Compensation & Benefit melakukan review** (Application Process)

    - Sistem meneruskan pengajuan kepada HR Compensation & Benefit.

    - HR melakukan review terhadap data yang diajukan beserta dokumen pendukung.

    - HR memvalidasi kelengkapan dan kesesuaian informasi yang diajukan.

4.  **HR memberikan keputusan** (Application Process)

    - Jika pengajuan **disetujui (Approve)**, sistem akan memperbarui data personal karyawan pada **Sistem HRIS terintegrasi** dan menyelesaikan proses pengajuan.

    - Jika pengajuan **dikembalikan (Send Back)**, sistem mengembalikan pengajuan kepada employee disertai komentar atau alasan perbaikan (kembali ke poin 2).

5.  Proses selesai (Application Process)

    - Setelah pengajuan disetujui, sistem memperbarui data personal karyawan, menyimpan riwayat perubahan (history), dan mengakhiri proses pengajuan.

[Ilustrasi sumber dihapus dari korpus publik: Current System Business Flow - Update Personal Data]

## Expected New System Business Flow

***Guidance:***

\* Please describe the expected improved system flow.

\* To maximize the understanding of expected new system, consider explaining with process flow in mind.

\* Do it step by step from beginning to the end of process

\* More complete the explanation will affect the next visual modelling process.

### Update Personal Data

1.  **Employee menyiapkan dokumen pendukung** (Manual Process)

    - Employee mempersiapkan dokumen pendukung sesuai dengan jenis perubahan data yang akan diajukan (misalnya Kartu Keluarga, Buku Nikah, atau dokumen lainnya sesuai kebijakan perusahaan).

2.  **Employee mengisi data perubahan** (Application Process)

    - Employee membuka menu **Personal Data** pada Sistem HRIS.

    - Employee melakukan perubahan data sesuai kebutuhan.

    - Employee mengunggah dokumen pendukung yang dipersyaratkan.

    - Employee mengirimkan (submit/save) pengajuan perubahan data.

3.  **HR Compensation & Benefit melakukan review** (Application Process)

    - Sistem meneruskan pengajuan kepada HR Compensation & Benefit.

    - HR melakukan review terhadap data yang diajukan beserta dokumen pendukung.

    - HR memvalidasi kelengkapan dan kesesuaian informasi yang diajukan.

4.  **HR memberikan keputusan** (Application Process)

    - Jika pengajuan **disetujui (Approve)**, sistem akan memperbarui data personal karyawan pada **Sistem HRIS** dan menyelesaikan proses pengajuan.

    - Jika pengajuan **dikembalikan (Send Back)**, sistem mengembalikan pengajuan kepada employee disertai komentar atau alasan perbaikan (kembali ke poin 2).

5.  Proses selesai (Application Process)

    - Setelah pengajuan disetujui, sistem menyimpan riwayat perubahan (history), dan mengakhiri proses pengajuan.

    - Data akan berubah ketika Effective date berlaku

[Ilustrasi sumber dihapus dari korpus publik: Expected New System Business Flow - Update Personal Data]

## Business Rules

### Business Rules – Personal Data Change

- Perubahan data personal hanya dapat diajukan oleh **employee yang bersangkutan** atau **administrator HR yang memiliki kewenangan**.

- Perubahan data hanya dapat diajukan untuk informasi yang **diperbolehkan oleh perusahaan**.

- Setiap pengajuan perubahan data dianggap sebagai **permohonan perubahan** dan belum menjadi data resmi sebelum memperoleh persetujuan.

### Business Rules – National ID

- Employee dapat memiliki lebih dari satu National ID.

- KTP menjadi mandatory (expatriate akan menulis passport number di section KTP).

- ID Type tidak lagi hanya KTP; harus mencakup Passport.

### Business Rules – Payment Information

- Payment Information dapat memiliki lebih dari satu rekening untuk employee yang sama.

- Perubahan rekening bank hanya dapat diajukan maksimal 1 kali dalam satu tahun untuk employee yang sama.

- Secara default rekening insurance akan sama dengan rekening payroll.

### Business Rules – Emergency Contact

- Employee dapat memiliki maksimal **2 Emergency Contact**.

### Business Rules – Dependents

- Employee dapat memiliki maksimal **3 Dependents**.

- Eligibility ditentukan oleh **HR saat approval**

### Business Rules – Time Management

- Time management menampilkan informasi Roster Type dan Work Schedule.

- Roster/Work Schedule pada Sistem HRIS mengikuti jam kerja yang tercantum dalam kontrak employee.

### Business Rules – Supporting Document

- Perubahan data tertentu wajib disertai dokumen pendukung sesuai kebijakan perusahaan.

- Dokumen pendukung yang diunggah harus sesuai dengan jenis perubahan data yang diajukan.

- Pengajuan yang memerlukan dokumen pendukung tidak dapat diproses apabila dokumen yang dipersyaratkan tidak tersedia.

### Business Rules – Approval

- Seluruh pengajuan perubahan data personal wajib melalui proses review dan approval oleh HR Compensation & Benefit.

- Data personal hanya akan diperbarui setelah pengajuan memiliki status **Approved** dan telah mencapai **Effective Date** yang ditentukan.

- HR berhak menyetujui atau mengembalikan pengajuan apabila diperlukan perbaikan atau kelengkapan data.

### Business Rules – Send Back & Resubmission

- Pengajuan yang dikembalikan (**Send Back**) dapat diperbaiki dan diajukan kembali oleh employee.

- Employee dapat melakukan perbaikan sesuai catatan yang diberikan oleh HR.

- Pengajuan yang diajukan kembali akan mengikuti proses approval dari awal.

### Business Rules – Withdrawal

- Employee dapat membatalkan (**Withdraw**) pengajuan selama untuk pengajuan dengan status **Sent back**.

- HR akan menerima notifikasi pada saat karyawan melakukan withdraw.

### Business Rules – History & Audit Trail

- Seluruh perubahan data personal wajib memiliki riwayat perubahan.

- Riwayat perubahan harus dapat digunakan sebagai referensi untuk kebutuhan audit dan administrasi.

- Riwayat perubahan tidak dapat dihapus melalui proses pengajuan.

### Business Rules – Notification

- Setiap perubahan status pengajuan harus diinformasikan kepada pihak yang berkepentingan.

- Notification mengikuti status proses pengajuan sesuai workflow yang berlaku.

### Business Rules – Integrity

- Informasi yang diajukan harus sesuai dengan dokumen pendukung yang dilampirkan.

- Employee bertanggung jawab atas kebenaran data yang diajukan.

- HR bertanggung jawab melakukan verifikasi sebelum memberikan keputusan terhadap pengajuan

## Functional Requirements

### Personal Data Request

#### Update Personal Data Request

Sistem harus memungkinkan Employee membuat pengajuan perubahan Personal Data untuk informasi berikut:

- Personal Information

- Biographical Information

- Address

- Contact Information

- National ID Information

- Primary Emergency Contact

- Dependents

- Payment Information

- Position and Organisation Information

- Job Details

- Job Relationships

- Employment Details

- Personal Documents

- Compensation Information

- Non Recurring Pay Component

- Time Information

- Basic Information

- Details Information

- Education

- Honors/Awards

- Work Experience Within Company

- Previous Employment

- Courses

- Certifications

- Professional Memberships

- Volunteer Involvement

Pada saat membuat pengajuan, employee harus melengkapi seluruh informasi yang diwajibkan serta mengunggah dokumen pendukung sesuai jenis perubahan data.

Sistem hanya mengizinkan satu pengajuan **Personal Data Section** yang masih berstatus **In Progress** untuk setiap employee.

#### Approval

##### Approve:

HR Compensation & Benefit dapat memberikan persetujuan apabila pengajuan telah memenuhi seluruh persyaratan.

Setelah approval diberikan, sistem memperbarui data personal employee dan menyelesaikan proses workflow.

Komentar bersifat opsional pada proses Approve.

##### Send Back

HR Compensation & Benefit dapat mengembalikan pengajuan kepada employee apabila diperlukan perbaikan data atau dokumen pendukung.

Komentar wajib diisi ketika melakukan **Send Back**.

Employee dapat melakukan perbaikan dan mengirimkan kembali pengajuan melalui sistem.

#### Edit Personal Data Request

Sistem harus memungkinkan employee melakukan perubahan terhadap pengajuan yang telah dikembalikan (**Send Back**) oleh HR.

Seluruh perubahan yang dilakukan terhadap pengajuan harus tercatat pada **Activity Log**.

#### Withdraw Personal Data Request

Sistem harus memungkinkan employee membatalkan (**Withdraw**) pengajuan untuk pengajuan yang berstatus **Sent back**.

Setelah status berubah menjadi **Withdraw**, proses approval dihentikan dan pengajuan tidak dapat diproses kembali.

Sistem mengirimkan notifikasi kepada HR setelah employee melakukan withdraw.

#### Personal Data Form

Sistem menyediakan formulir **Personal Data** yang digunakan untuk seluruh proses pengajuan perubahan data personal.

Form yang ditampilkan kepada employee disesuaikan dengan jenis data yang akan diperbarui.

##### Employee

Employee memiliki hak untuk mengubah informasi berikut sesuai kebijakan perusahaan:

- Personal Information

- Biographical Information

- Address

- Contact Information

- National ID Information

- Primary Emergency Contact

- Dependents

- Payment Information

- Position and Organisation Information

- Job Details

- Job Relationships

- Employment Details

- Personal Documents

- Compensation Information

- Non Recurring Pay Component

- Time Information

- Basic Information

- Details Information

- Education

- Honors/Awards

- Work Experience Within Company

- Previous Employment

- Courses

- Certifications

- Professional Memberships

- Volunteer Involvement

##### HR Compensation & Benefit

Pada tahap review, HR memiliki hak untuk:

- Melakukan review seluruh informasi perubahan data.

- Melihat dokumen pendukung yang dilampirkan.

- Memberikan keputusan **Approve** atau **Send Back**.

- Memberikan komentar pada proses review.

- Melihat riwayat perubahan data.

- HR Compensation & Benefit dapat menentukan status eligibility dependent menjadi **Eligible** atau **Not Eligible** pada tahap review/approval.

### Personal Data Field Details

#### Personal Information

| Field | Type | Editable | Mandatory | Note |
| --- | --- | --- | --- | --- |
| Effective date | Date | Yes | Yes |  |
| First Name | Text | Yes | Yes |  |
| Last Name | Text | Yes | No |  |
| Middle Name | Text | Yes | No |  |
| Salutation | Picklist | Yes | Yes |  |
| Full Name | Text | No | Yes | Auto fill: First + Middle + Last Name |
| Religion | Picklist | Yes | Yes |  |
| Gender | Picklist | Yes | Yes |  |
| Marital Status | Picklist | Yes | Yes |  |
| Marital Status Since | Date | Yes | No |  |
| Nationality | Text | Yes | No |  |
| Default Locale | Text | Yes | No |  |
| Attachment | JPG/PDF | Yes | No | Berisi Kartu Keluarga |

#### Biographical Information

| Field | Type | Editable | Mandatory | Note |
| --- | --- | --- | --- | --- |
| Place of Birth | Text | Yes | Yes |  |
| Date of Birth | Date | Yes | Yes |  |
| Date of Death | Date | Yes | No |  |

#### Addresses

| Field | Type | Editable | Mandatory | Note |
| --- | --- | --- | --- | --- |
| Address Type | Picklist | Yes | Yes | →hanya ada home |
| Alamat | Text | Yes | Yes | multi line = text area |
| RT/RW | Text | Yes | No |  |
| Country | Dropdown | Yes | Yes | Geographic table |
| Provinsi | Dropdown | Yes | Yes | Geographic table |
| Kota | Dropdown | Yes | Yes | Geographic table |
| Kecamatan | Dropdown | Yes | No | Geographic table |
| Kelurahan/Desa | Dropdown | Yes | No | Geographic table |
| Kode Post | Text | Yes | Yes |  |
| Is Primary | Boolean | Yes | Yes |  |

#### Contact Information

##### Phone Information

| Field | Type | Editable | Mandatory | Note |
| --- | --- | --- | --- | --- |
| Phone Type | Picklist | Yes | Yes | Personal or Work |
| Full phone number | Text | Yes | Yes |  |
| Is Primary | Boolean | Yes | No |  |

##### Email Information

| Field | Type | Editable | Mandatory | Note |
| --- | --- | --- | --- | --- |
| Email Type | Picklist | No | Yes | Personal or Work |
| Email Address | Text | No | Yes |  |
| Is Primary | Boolean | No | No |  |

#### National ID Information

| Field | Type | Editable | Mandatory | Note |
| --- | --- | --- | --- | --- |
| Type | Picklist | Yes | Yes | KTP & Passport |
| Country | Picklist | Yes | Yes |  |
| National ID | Text | Yes | Yes |  |
| Attachment | Pdf | Yes | No |  |
| Is Primary | Boolean | Yes | Yes |  |

#### Emergency Contact

| Field | Type | Editable | Mandatory | Note |
| --- | --- | --- | --- | --- |
| **Emergency Contact** |  |  |  | Multiple, max 2 |
| Name | Text | Yes | Yes |  |
| Relationship | Picklist | Yes | Yes |  |
| Phone | Text | Yes | Yes |  |
| Alternative Phone | Text | Yes | No |  |
| Gender | Picklist | Yes | No |  |
| Date of Birth | Date | Yes | No |  |
| Email | Text | Yes | No |  |
| Is Primary | Boolean | Yes | No |  |

#### Dependants

| Field | Type | Editable | Mandatory | Note |
| --- | --- | --- | --- | --- |
| Is Eligible? | Boolean | No | No | (Editable by HR during approval) |
| Effective date | Date | Yes | Yes |  |
| First name | Text | Yes | Yes |  |
| Last name | Text | Yes | Yes |  |
| Middle name | Text | Yes | No |  |
| Relationship | Picklist | Yes | Yes |  |
| Date of birth | Date | Yes | Yes |  |
| Attachments | Attachment | Yes | No | Multiple file |

##### Person Relationships

| Field | Type | Editable | Mandatory | Note |
| --- | --- | --- | --- | --- |
| Relationship | Picklist | Yes | Yes |  |
| Copy Address from Employee | Picklist | Yes | No |  |
| Attachments | Attachment | Yes | No | Multiple file |

##### Personal Information

| Field | Type | Editable | Mandatory | Note |
| --- | --- | --- | --- | --- |
| First Name | Text | Yes | Yes |  |
| Last Name | Text | Yes | Yes |  |
| Middle Name | Text | Yes | No |  |
| Gender | Picklist | Yes | Yes |  |
| Order of Child | Picklist | Yes | No |  |
| School | Picklist | Yes | No |  |
| Grade | Picklist | Yes | No |  |

##### Biographical Information

| Field | Type | Editable | Mandatory | Note |
| --- | --- | --- | --- | --- |
| Date of Birth | Date | Yes | Yes |  |
| Place of Birth | Text | Yes | Yes |  |

##### National ID Information

| Field | Type | Editable | Mandatory | Note |
| --- | --- | --- | --- | --- |
| Country/Region |  | Yes | Yes |  |
| National ID Card Type |  | Yes | Yes |  |
| National ID |  | Yes | Yes |  |
| Is Primary |  | Yes | Yes |  |
| Attachments |  | Yes | No |  |

##### Address

| Field | Type | Editable | Mandatory | Note |
| --- | --- | --- | --- | --- |
| Country/Region | Picklist | Yes | Yes |  |
| Alamat | Text | Yes | Yes |  |
| RT/RW | Text | Yes | No |  |
| Kelurahan/Desa | Text | Yes | No |  |
| Kecamatan | Text | Yes | No |  |
| Kota | Text | Yes | Yes |  |
| Provinsi | Picklist | Yes | Yes |  |
| Kode Pos | Text | Yes | Yes |  |

#### Payment Informations

| Field | Type | Editable | Mandatory | Note |
| --- | --- | --- | --- | --- |
| Effective start date | Date | Yes | Yes | Mandatory |
| Effective end date | Date | No | No | Disabled |

##### Payroll

| Field | Type | Editable | Mandatory | Note |
| --- | --- | --- | --- | --- |
| Payment Type | Picklist | Yes | No |  |
| Payment Method | Picklist | Yes | Yes | Mandatory |
| Currrency | Picklist | Yes | No |  |
| Bank Country | Picklist | Yes | No | Can add multiple |
| Account Owner | Text | Yes | No |  |
| Account Number | Text | Yes | No |  |

##### Insurance

| Field | Type | Editable | Mandatory | Note |
| --- | --- | --- | --- | --- |
| Payment Type | Picklist | Yes | No |  |
| Insurance Type | Picklist | Yes | No |  |
| Insurance classification/grouping | Picklist | Yes | No |  |
| Payment Method | Picklist | Yes | Yes |  |
| Currrency | Picklist | Yes | No |  |
| Bank Country | Picklist | Yes | No |  |
| Bank Country | Picklist | Yes | No |  |
| Account Owner | Text | Yes | No |  |
| Account Number | Text | Yes | No |  |

#### Position Information

| Field | Type | Editable | Mandatory | Note |
| --- | --- | --- | --- | --- |
| Position | Text | No | Yes |  |
| Position Entry Date | Date | No | Yes |  |
| Time in Position | Duration / Calculated | No | Yes |  |

#### Organisational Information

| Field | Type | Editable | Mandatory | Note |
| --- | --- | --- | --- | --- |
| Time in Position | Duration / Calculated | No | Yes |  |
| Company | Picklist | No | Yes |  |
| Department | Picklist | No | Yes |  |
| Directorate | Picklist | No | Yes |  |
| Division | Picklist | No | Yes |  |
| Section | Picklist | No | Yes |  |
| Cost Centre | Picklist | No | No |  |
| Location | Picklist | No | Yes |  |

#### Job Details

| Field | Type | Editable | Mandatory | Note |
| --- | --- | --- | --- | --- |
| Supervisor | Picklist | No | Yes |  |
| Job Classification | Picklist | No | Yes |  |
| Title | Text | No | Yes |  |
| ESDM Title | Text | No | No |  |
| Contingent Worker | Picklist | No | No |  |
| Pay Group | Picklist | No | Yes |  |
| Pay Grade | Picklist | No | Yes |  |
| Employment Type | Picklist | No | Yes |  |
| Employment Status | Picklist | No | Yes |  |
| Insurance Category | Picklist | No | Yes |  |
| Point of Hire | Picklist | No | Yes |  |
| Local/Non Local | Picklist | No | Yes |  |
| Ring Transport | Picklist | No | Yes |  |
| Tax Status | Picklist | No | Yes |  |
| Contract Status | Picklist | No | Yes |  |
| FTC 1 Start Date | Date | No | Yes |  |
| FTC 1 End Date | Date | No | Yes |  |
| FTC 2 Start Date | Date | No | No |  |
| FTC 2 End Date | Date | No | No |  |
| Country/Region | Picklist | No | Yes |  |
| Attachment | File / Attachment | No | No |  |

#### Time Information

| Field | Type | Editable | Mandatory | Note |
| --- | --- | --- | --- | --- |
| Holiday Calendar | Picklist | No | Yes |  |
| Work Schedule | Picklist | No | Yes |  |
| Roster Type | Picklist | No | Yes |  |
| Is Shift Employee | Boolean | No | Yes |  |
| Shift Code | Picklist / Text | No | No |  |

#### Job Relationships

| Field | Type | Editable | Mandatory | Note |
| --- | --- | --- | --- | --- |
| Effective Date | Date | No | Yes |  |
| Relationship Type | Picklist | No | Yes |  |
| Name | Picklist | No | Yes |  |

#### Personal Documents

| Field | Type | Editable | Mandatory | Note |
| --- | --- | --- | --- | --- |
| Country/Region | Picklist | Yes | No |  |
| Document Type | Picklist | Yes | No |  |
| Document Title | Text | Yes | No |  |
| Document Number | Text | Yes | No |  |
| Issue Date | Date | Yes | Yes |  |
| Issue Place | Text | Yes | No |  |
| Issuing Authority | Text | Yes | No |  |
| Expiry Date | Date | Yes | No |  |
| Attachments | File Upload | Yes | No |  |

#### Compensations

| Field | Type | Editable | Mandatory | Note |
| --- | --- | --- | --- | --- |
| Pay Component | Picklist | No | Yes |  |
| Frequency | Picklist | No | Yes |  |
| Percentage | Decimal / Percentage | No | No |  |
| Amount | Numeric | Yes | No |  |

#### Pay Targets

| Field | Type | Editable | Mandatory | Note |
| --- | --- | --- | --- | --- |
| Pay Component | Picklist | No | No |  |
| Frequency | Picklist | No | No |  |
| Percentage | Decimal / Percentage | No | No |  |
| Amount | Numeric / Currency | No | No |  |

#### Education

| Field | Type | Editable | Mandatory | Note |
| --- | --- | --- | --- | --- |
| From Date | Date | Yes | No |  |
| End Date | Date | Yes | No |  |
| School | Text | Yes | Yes |  |
| Major | Picklist | Yes | Yes |  |
| Degree | Picklist | Yes | Yes |  |
| Certificate of Graduation | File Upload | Yes | Yes |  |
| Browse | Action / Button | Yes | No |  |

#### Honors / Awards

| Field | Type | Editable | Mandatory | Note |
| --- | --- | --- | --- | --- |
| Honour or Award | Text | Yes | Yes |  |
| Institution | Text | Yes | No |  |
| Issue Date | Date | Yes | No |  |
| Description | Text / Long Text | Yes | No |  |

#### Work Exprience Within Company

| Field | Type | Editable | Mandatory | Note |
| --- | --- | --- | --- | --- |
| Start Date | Date | Yes | Yes |  |
| End Date | Date | Yes | No |  |
| Title | Text | Yes | Yes |  |
| Department | Text | Yes | No |  |

#### Previous Employment

| Field | Type | Editable | Mandatory | Note |
| --- | --- | --- | --- | --- |
| Start Date | Date | Yes | Yes |  |
| End Date | Date | Yes | Yes |  |
| Company Name | Text | Yes | Yes |  |
| Title | Text | Yes | Yes |  |
| Type of Business | Picklist | Yes | No |  |
| Functional Experience | Picklist | Yes | No |  |

#### Courses

| Field | Type | Editable | Mandatory | Note |
| --- | --- | --- | --- | --- |
| Course Name | Text | Yes | Yes |  |
| Institution Name | Text | Yes | No |  |
| Type | Picklist | Yes | No |  |
| Length | Picklist | Yes | Yes |  |
| Date Completed | Date | Yes | Yes |  |
| Category | Picklist | Yes | No |  |

#### Certifications

| Field | Type | Editable | Mandatory | Note |
| --- | --- | --- | --- | --- |
| Certification/License | Text | Yes | Yes |  |
| Institution | Text | Yes | No |  |
| Effective Date | Date | Yes | No |  |
| Expiry Date | Date | Yes | No |  |
| Description | Text / Long Text | Yes | No |  |

#### Professional Memberships

| Field | Type | Editable | Mandatory | Note |
| --- | --- | --- | --- | --- |
| Organisation | Text | Yes | Yes |  |
| From Date | Date | Yes | No |  |
| End Date | Date | Yes | No |  |
| Position/Role | Text | Yes | No |  |

#### Volunteer Involvement

| Field | Type | Editable | Mandatory | Note |
| --- | --- | --- | --- | --- |
| From Date | Date | Yes | No |  |
| End Date | Date | Yes | No |  |
| Community/Volunteer Organisation Name | Text | Yes | Yes |  |
| Role | Text | Yes | No |  |

### Attachment

Sistem harus menyediakan fasilitas upload dokumen pendukung pada pengajuan **Personal Data**.

Dokumen yang wajib dilampirkan mengikuti kebijakan perusahaan berdasarkan jenis perubahan data.

Contoh:

- Perubahan Status Pernikahan → Buku Nikah / Kartu Keluarga

- Perubahan Data Anak → Kartu Keluarga

Format file yang diperbolehkan mengikuti konfigurasi sistem.

### Personal Data History

Sistem harus menyimpan seluruh riwayat perubahan data personal.

History minimal mencakup:

- Data setelah perubahan

- Employee

- Approver

- Tanggal pengajuan

- Tanggal approval

- Status pengajuan

### Monitoring

#### Status Monitoring

Sistem menyediakan informasi status pengajuan Personal Data.

Employee dapat mengetahui posisi pengajuan yang sedang berjalan.

#### Activity Log

Sistem mencatat seluruh aktivitas selama proses pengajuan, meliputi:

- Submit

- Approve

- Send Back

- Withdraw

- Resubmit

- Perubahan Data

- Komentar Review

### Integration Trigger

Setelah pengakuan memperoleh persetujuan, sistem akan memperbarui data pada modul terkait sesuai jenis perubahan yang diajukan.

Integrasi dapat mencakup:

- Organization Structure

- Position Management

- Payroll & Compensation

- Benefit Reimbursement

Perubahan hanya dilakukan setelah seluruh proses approval selesai.

### Execption Handling

Sistem harus menangani kondisi khusus yang dapat terjadi selama proses **Personal Data Update**.

#### Multiple Personal Data Section Update

Sistem tidak mengizinkan Requestor membuat pengajuan perubahan pada **Personal Data Section** yang sama apabila masih terdapat pengajuan dengan status **In Progress** untuk employee yang sama.

Contoh:

- Jika terdapat pengajuan **Address Update** dengan status **In Progress**, Requestor tidak dapat membuat pengajuan **Address Update** baru.

- Requestor tetap dapat mengajukan perubahan pada **Personal Data Section** lainnya, seperti **Personal Information** atau **Emergency Contact Information**, selama tidak terdapat pengajuan pada section tersebut yang masih berstatus **In Progress**.

Pengajuan perubahan pada Personal Data Section yang sama hanya dapat dibuat kembali setelah pengajuan sebelumnya berstatus **Approved** atau **Withdrawn**.

#### Withdraw

Apabila Requestor melakukan Withdraw, sistem akan:

- Mengubah status pengajuan menjadi **Withdrawn**.

- Mengirimkan notifikasi kepada HR Compensation & Benefit.

- Menyimpan aktivitas tersebut pada Activity Log.

### Notification/Notifikasi

#### 1. Personal Data Update Submitted

**Trigger** : Requestor has submitted a Personal Data Update request.

**Recipient** : HR Compensation & Benefit

**Subject** : Personal Data Update Request for **{Employee Name}** Requires Your Review

**Email Body :**

-----------------------------------------------------------------------------------------------------------

Hello **{Approver Name}**,

A Personal Data Update request for **{Employee Name}** has been submitted on **{Submission Date}** and requires your review.

Please review the request and take the necessary action through the Personal Data application.

**Application Link:**  
{Application URL}

#### 2. Personal Data Update – Send Back

**Trigger** : HR Compensation & Benefit has sent back a Personal Data Update request for revision.

**Recipient** : Requestor / Employee

**Subject** : Personal Data Update Request for **{Employee Name}** Requires Revision

**Email Body :**

-----------------------------------------------------------------------------------------------------------

Hello **{Employee Name}**,

Your Personal Data Update request has been sent back by **{Approver Name}** and requires revision.

Please review the comments and make the necessary changes before submitting the request again.

**Application Link:**  
{Application URL}

#### 3. Personal Data Update Resubmitted

**Trigger** : Requestor has resubmitted a Personal Data Update request after making the required revision.

**Recipient** : HR Compensation & Benefit

**Subject** : Personal Data Update Request for **{Employee Name}** Has Been Resubmitted

**Email Body :**

-----------------------------------------------------------------------------------------------------------

Hello **{Approver Name}**,

The Personal Data Update request for **{Employee Name}** has been revised and resubmitted on **{Resubmission Date}**.

Please review the updated request and take the necessary action.

**Application Link:**  
{Application URL}

#### 4. Personal Data Update Withdrawn

**Trigger** : Requestor has withdrawn a Personal Data Update request.

**Recipient** : HR Compensation & Benefit

**Subject** : Personal Data Update Request for **{Employee Name}** Has Been Withdrawn

**Email Body :**

-----------------------------------------------------------------------------------------------------------

Hello **{Recipient Name}**,

The Personal Data Update request for **{Employee Name}** has been withdrawn on **{Withdrawal Date}**.

The request is no longer available for further approval.

**Application Link**  
{Application URL}

#### 5. Personal Data Update Approval Reminder

**Trigger** : The Personal Data Update request remains pending and the assigned approver has not completed the required approval action within the configured reminder period.

**Recipient**: HR Compensation & Benefit

**Subject** : Reminder: Personal Data Update Request for **{Employee Name}** Requires Your Review

**Email Body :**

-----------------------------------------------------------------------------------------------------------

Hello **{Approver Name}**,

This is a reminder that the Personal Data Update request for **{Employee Name}** is still pending your review.

Please review the request and take the necessary action through the Personal Data application.

**Application Link**

{Application URL}

#### 6. Personal Data Update Completed

**Trigger** : All required approval processes have been completed and the Personal Data Update has been approved.

**Recipient**: Requestor / Employee

**Subject** : Personal Data Update Request for **{Employee Name}** Has Been Approved

**Email Body :**

-----------------------------------------------------------------------------------------------------------

Hello **{Recipient Name}**,

The Personal Data Update request for **{Employee Name}** has been fully approved.

The updated Personal Data information is now available in the application.

**Application Link**

{Application URL}

#### Notification Matrix

| **Event** | **Recipient** |
| --- | --- |
| Submit Personal Data Update | HR Compensation & Benefit |
| Send Back | Requestor / Employee |
| Resubmit Personal Data Update | HR Compensation & Benefit |
| Withdraw Personal Data Update | HR Compensation & Benefit |
| Reminder | HR Compensation & Benefit |
| Completed | Requestor / Employee |

## User Interface

### User Profile – Personal Data

[Ilustrasi sumber dihapus dari korpus publik: User Profile - Personal Data]

### User Profile – Job Data

[Ilustrasi sumber dihapus dari korpus publik: User Profile - Job Data]

### User Profile – Compensation

[Ilustrasi sumber dihapus dari korpus publik: User Profile - Compensation]

### User Profile – Time Management

[Ilustrasi sumber dihapus dari korpus publik: User Profile - Time Management]

### User Profile – General Information

[Ilustrasi sumber dihapus dari korpus publik: User Profile - General Information]

### User Profile – Background Information

[Ilustrasi sumber dihapus dari korpus publik: User Profile - Background Information]

### Personal Data Change Request

[Ilustrasi sumber dihapus dari korpus publik: Personal Data Change Request]

### Personal Data Change Monitoring

[Ilustrasi sumber dihapus dari korpus publik: Personal Data Change Monitoring]

### Workflow Details

[Ilustrasi sumber dihapus dari korpus publik: Workflow Details]

### Workflow Details with Eligibility Claim

[Ilustrasi sumber dihapus dari korpus publik: Workflow Details with Eligibility Claim]

### Form Example

[Ilustrasi sumber dihapus dari korpus publik: Personal Information Form Example]

## Validation Rules

### Personal Data Update Validation

| **Validation Rule** | **Error Message** |
| --- | --- |
| Sistem hanya mengizinkan satu pengajuan **Personal Data Section** dengan status **In Progress** untuk setiap employee. | *An active request already exists for this Personal Data Section. Please complete or withdraw the existing request before submitting a new one.* |
| Ukuran dokumen pendukung tidak boleh melebihi batas yang ditentukan. | *The file size exceeds the maximum allowed limit.* |

### Mandatory Field Validation

| **Validation Rule** | **Error Message** |
| --- | --- |
| Seluruh mandatory field pada Personal Data Section wajib diisi sebelum Submit. | *Please complete all mandatory fields before submitting the request.* |

### Send Back Validation

| **Validation Rule** | **Error Message** |
| --- | --- |
| Komentar wajib diisi ketika HR melakukan Send Back. | *Please provide a comment before sending the request back.* |

### Withdraw Validation

| **Validation Rule** | **Error Message** |
| --- | --- |
| Employee hanya dapat melakukan Withdraw terhadap request yang masih dalam proses approval dengan status **Sent Back**. | *This request can no longer be withdrawn because the approval process has been completed.* |
| Request yang telah berstatus Withdrawn tidak dapat diproses kembali. | *This request has been withdrawn and can no longer be processed.* |

### Payment Information Change Validation

| **Validation Rule** | **Error Message** |
| --- | --- |
| Perubahan rekening bank hanya dapat diajukan satu kali dalam satu tahun. | *Bank account changes can only be submitted once per year.* |

## Security Requirements

### Data Confidentiality

Beberapa informasi pada Personal Data dikategorikan sebagai **Confidential Information** dan hanya dapat diakses oleh pengguna yang memiliki hak akses sesuai kewenangannya.

Confidential data meliputi, namun tidak terbatas pada:

- National ID

- Date of Birth

- Address

- Personal Contact Information

- Emergency Contact Information

- Payment Information

- Dependent Information

- Grading

- Basic Salary

Akses terhadap data tersebut harus mengikuti prinsip **Role-Based Access Control (RBAC)**.

### Personal Data Access

Hak akses terhadap Personal Data diatur berdasarkan role dan proses bisnis.

**Employee** hanya dapat:

- Melihat data personal miliknya.

- Membuat pengajuan perubahan data personal miliknya.

- Melihat status dan riwayat pengajuan miliknya.

**HR Compensation & Benefit** dapat:

- Melihat pengajuan Personal Data yang menjadi tanggung jawabnya.

- Melakukan review terhadap data dan dokumen pendukung.

- Memberikan keputusan terhadap pengajuan sesuai kewenangannya.

Pengguna tanpa hak akses tidak dapat melihat maupun mengubah Personal Data employee.

### Document Access

Dokumen pendukung yang dilampirkan pada pengajuan Personal Data merupakan informasi yang bersifat confidential.

Akses terhadap dokumen hanya diberikan kepada pengguna yang memiliki kewenangan sesuai proses bisnis.

Employee hanya dapat mengakses dokumen yang terkait dengan pengajuannya sendiri, sedangkan HR Compensation & Benefit dapat mengakses dokumen yang diperlukan untuk proses review dan approval.

### Audit Trail

Sistem harus mencatat aktivitas penting selama proses **Personal Data Update** berlangsung.

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

### Data Change History

Sistem harus menyimpan history perubahan Personal Data setelah pengajuan memperoleh approval.

History minimal mencatat:

- Personal Data Section

- Field yang berubah

- Previous Value

- New Value

- Changed By

- Change Date & Time

- Request ID

Data change history hanya dapat diakses oleh pengguna yang memiliki hak akses sesuai kewenangannya

### Attachment Security

Sistem harus membatasi akses terhadap supporting document berdasarkan role dan hak akses pengguna.

Dokumen yang telah diunggah harus tetap terkait dengan request yang bersangkutan dan tidak dapat diakses oleh pengguna yang tidak memiliki kewenangan.

Dokumen yang telah tersimpan tidak dapat diubah atau dihapus oleh employee setelah request memasuki proses approval, kecuali melalui mekanisme perubahan yang disediakan sistem.

## Sign-off

| Role | Name | Signature | Date |
| --- | --- | --- | --- |
| Business Analyst | Analis Bisnis A | [Ilustrasi sumber dihapus dari korpus publik: Business Analyst Signature] | 14 Sep 2026 |
| Project Coordinator | Koordinator Proyek A |  |  |
| Business User Expert | Narasumber Bisnis A |  |  |
| Business User Expert | Narasumber Bisnis C |  |  |

***\*By signing this document, all items contained herein are confirmed as mandatory requirements to be delivered as the agreed-upon product. Any changes or modifications to these requirements will be managed through the change request process.***
