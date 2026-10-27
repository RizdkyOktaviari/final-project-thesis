# Business Requirement Assessment — Employee Central: Organization Structure

**IT SYSTEM DEVELOPMENT — BUSINESS REQUIREMENT ASSESSMENT**

- **Project:** Sistem HRIS
- **Module:** Employee Central - Organization Structure
- **Business User Expert:** Narasumber Bisnis F / Narasumber Bisnis C
- **Assessment Date:** 3 Juni 2026 - 9 Juni 2026
- **Document version (tertera di footer):** 1.1

## 1. Business Requirement Record

| Start Date | End Date | Author | Version Doc | Change Reference |
| --- | --- | --- | --- | --- |
| 11 Jun 2026 | | Analis Bisnis A | 0.1 | Drafting |
| 19 Jun 2026 | | Analis Bisnis A | 1.0 | Issued for Review |
| 24 Jun 2026 | | Analis Bisnis A | 1.1 | Updated based on Review Comments |
| 9 Jul 2026 | | Analis Bisnis A | 1.2 | Updated based on Review |
| 13 Jul 2026 | | Penelaah A | 1.3 | Updated based on Review |

### 1.1 Log Changes

*Describe the changes which impact to the Module.*

**Guidance:**

- Provide the name, detail changes and severity of the changes, e.g. Mr. X request for change on workflow due to new policy on dd/mmm/yyyy, etc.
- Please identify all the changes clearly include impact to another module or infrastructure (if any).

**Change Record**

| Date | Requested by | Description | Severity (major/minor) | Status |
| --- | --- | --- | --- | --- |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

## 2. Requirement Identification

### 2.1 WHY — Module Objectives/Goals and Benefits

*Explain why this module is needed.*

**Guidance:**

- Module Objectives/Goals: Your expected objectives on this module, e.g. decreasing numbers of paper used.
- Module Benefits: The outcome of successful objectives/goals, e.g. reducing the paper consumption cost.

| Module Objectives/Goals | Module Benefits |
| --- | --- |
| Memusatkan pengelolaan struktur organisasi perusahaan dalam satu sistem yang terintegrasi serta menyediakan hierarki organisasi yang jelas untuk mendukung pengelolaan unit kerja, posisi, karyawan, dan pelaporan perusahaan. | Mengurangi ketidaksesuaian informasi struktur organisasi, meningkatkan transparansi dan konsistensi data di seluruh perusahaan, mempermudah pelacakan hubungan antar unit kerja, meningkatkan akurasi pelaporan, serta mendukung pengambilan keputusan yang lebih efektif. |
| Memungkinkan Tim Organization Development mengelola perubahan organisasi seperti penambahan, penggabungan, atau perubahan struktur organisasi melalui proses yang terstandarisasi. | Memberikan otorisasi pengelolaan organisasi pada fungsi yang tepat dan meningkatkan efisiensi administrasi organisasi, mengurangi pekerjaan manual, serta mempercepat implementasi perubahan organisasi. |
| Menjadi sumber data utama bagi modul HC lainnya yang bergantung pada struktur organisasi perusahaan. | Memastikan konsistensi, tracking data, dan reporting lintas modul, mengurangi duplikasi data, dan meningkatkan integrasi proses bisnis HC secara keseluruhan. |

### 2.2 WHAT — In Scope and Out Scope

*Describe the expected function or features on the app.*

**Guidance:**

- In scope: Explain the expected function / feature to be included e.g. the reporting must in excel, must be easy to use in mobile, etc.
- Out scope: Explain what function that exist on the current/manual system that should not be considered e.g. no need to add 3rd party account on login, etc.
- Make sure to put anything that you can think about the scope.

#### In Scope

Pembuatan dan pengelolaan **Struktur Organisasi** termasuk:

- Visualisasi Struktur Organisasi dalam bentuk hierarki organisasi.
- Visualisasi detail profile employee.
- Integrasi struktur organisasi sebagai referensi bagi modul Employee Central lainnya.
- Penyediaan fungsi expor **Struktur Organisasi** dalam format file pdf & png.
- Visualisasi struktur organisasi berdasarkan periode atau tanggal tertentu dengan mekanisme penyimpanan riwayat (historical records).
- Pengelolaan master data unit organisasi.

#### Out Scope

- Pembuatan dan pengelolaan **Position**.
- Pembuatan dan pengelolaan **Integrated Position System (IPS) Code**.
- Pembuatan transaksi Employee Status Change (ESC) pada perubahan Struktur Organisasi.
- Pengelolaan data personal dan employment karyawan.
- Pengelolaan manager assignment atau reporting line berbasis posisi.
- Rekrutmen dan onboarding karyawan.
- Pengelolaan kompensasi, payroll, dan benefit.
- Pengelolaan target kinerja dan performance management.
- Succession planning dan talent management.
- Workforce planning dan manpower budgeting.
- Integrasi dengan sistem keuangan selain penyediaan referensi Cost Center.
- Pengelolaan security role dan user authorization.
- Pengelolaan struktur posisi (position hierarchy).
- Perubahan struktur organisasi melalui fitur drag & drop.

### 2.3 WHEN — Milestones

*Describe the expected completion dates on required milestone.*

**Guidance:** Explain the expected milestone complete with expected start and end dates e.g. system must ready to used in dd/mm/yyyy, should be presented on management meeting on dd/mm/yyyy.

| Milestones | Due Date | Remarks |
| --- | --- | --- |
| User Requirement | 18 Jun 2026 | Organization Structure |

### 2.4 WHO — User Roles and Accessibilities

*Describe how many roles will be interact with this Module.*

**Guidance:**

- Provide the role, assigned to and accessibilities on each role that will be included in the module e.g. HR as admin apps will be responsible to provide setting on the current process.
- Please identify all the participated person in your area to have a clear roles assignment.

| Role | Assigned to | Accessibilities |
| --- | --- | --- |
| Organization Development (OD) Admin | | Create, Read, Update/Modify |
| Employee | | Read |

### 2.5 WHAT IF — Risks and Mitigation

*Identify the risk and impact of the module.*

**Guidance:**

- Explain the risk that might be a barrier / obstacle for this module, e.g. the procedure does not exist, need to be confirmed by BOD, etc.
- Please think of any risk that might be impacted related to this module.

**Risks**

| Risks | Level (Hi, Med, Low) |
| --- | --- |
| Perubahan struktur organisasi tanpa kontrol yang memadai dapat menyebabkan kesalahan pada jalur pelaporan karyawan dan hilangnya histori organisasi serta kesulitan dalam melakukan audit trail. | Hi |
| Kesalahan penempatan unit organisasi pada hierarki (higher-level and subordinate relationship) dapat menyebabkan struktur organisasi yang tidak valid. | Hi |

**Mitigasi**

1. Menyimpan histori perubahan organisasi menggunakan effective dating dan audit trail untuk menjaga keterlacakan data.
2. Menerapkan validasi higher-level and subordinate relationship untuk mencegah pembentukan hierarki organisasi yang tidak valid.

## 3. Current System Business Flow

**Guidance:**

- Please describe the current system that running / being used in essay.
- To maximize the understanding of current system, consider explaining with process flow in mind.
- Do it step by step from beginning to the end of process.
- Example on essay (in Bahasa):

  > “Dept. Head user mengajukan persetujuan perubahan organisasi kepada Senior Manager user, Kepala Operasional/Director in Charge, Vice President dan President Director. Usulan perubahan organisasi yang sudah mendapatkan persetujuan lengkap akan di sampaikan ke tim Organization Development untuk dilakukan perubahan/penyesuaian di aplikasi/sistem.”

- More complete the explanation will affect the next visual modelling process.

### 3.1 Manage Organizational Structure Business Process

#### A. Flow External (Di Luar Aplikasi / Manual Process)

##### 1. Pengajuan Perubahan Struktur Organisasi

- Requester mengidentifikasi kebutuhan perubahan struktur organisasi.
- Requester menyusun proposal perubahan struktur organisasi.
- Requester melampirkan organizational chart baru beserta justifikasi perubahan.
- Proposal disampaikan kepada OD Section untuk dilakukan review awal.

##### 2. Review Awal oleh OD Section

- OD Section melakukan evaluasi terhadap proposal perubahan struktur organisasi.
- OD Section memverifikasi kelengkapan dokumen, kesesuaian struktur, dan alasan bisnis yang mendasari perubahan.

**Keputusan: Setuju dengan Proposal?**

- **Ya** → Proposal diteruskan kepada Manager Training & Development untuk review berikutnya.
- **Tidak** → OD Section memberikan masukan dan melakukan pembahasan bersama Requester untuk revisi proposal.

##### 3. Revisi Proposal

- Requester dan OD Section melakukan diskusi serta penyempurnaan proposal berdasarkan hasil review.
- Proposal yang telah direvisi diajukan kembali untuk proses review dan persetujuan.

##### 4. Review oleh Manager Training & Development

- Manager Training & Development melakukan review terhadap proposal yang telah disetujui OD Section.

**Keputusan: Setuju dengan Proposal?**

- **Ya** → Proposal diteruskan kepada Senior Manager HCM.
- **Tidak** → Proposal dikembalikan kepada OD Section dan Requester untuk dilakukan revisi.

##### 5. Review oleh Senior Manager HCM

- Senior Manager HCM melakukan review terhadap proposal perubahan struktur organisasi.

**Keputusan: Setuju dengan Proposal?**

- **Ya** → Proposal diteruskan kepada GM Operations / Director in Charge.
- **Tidak** → Proposal dikembalikan kepada OD Section dan Requester untuk dilakukan revisi.

##### 6. Review oleh GM Operations / Director in Charge

- GM Operations / Director in Charge melakukan review akhir terhadap proposal perubahan struktur organisasi.

**Keputusan: Setuju dengan Proposal?**

- **Ya** → Proposal dinyatakan disetujui dan dapat diimplementasikan.
- **Tidak** → Proposal dikembalikan kepada OD Section dan Requester untuk dilakukan revisi.

##### 7. Review oleh Board of Director

- Board of Director melakukan review akhir terhadap proposal perubahan struktur organisasi.

**Keputusan: Setuju dengan Proposal?**

- **Ya** → Proposal dinyatakan disetujui dan dapat diimplementasikan.
- **Tidak** → Proposal dikembalikan kepada OD Section dan Requester untuk dilakukan revisi.

#### Flow Internal (Di Dalam Aplikasi / System Process)

##### 1. Update Organization Structure

- OD Section melakukan pembaruan data struktur organisasi pada aplikasi dengan melakukan import file organization structure dengan ekstension csv/xlsx melalui modul **Position Management**.
- Sistem menyimpan perubahan struktur organisasi yang telah disetujui.
- Struktur organisasi terbaru menjadi struktur organisasi aktif yang digunakan oleh sistem dan modul terkait.

##### 2. End Process

- Sistem mengakhiri proses setelah pembaruan struktur organisasi berhasil disimpan.

**Catatan:**

- Seluruh proses review dan persetujuan dilakukan secara **manual** sebelum perubahan diterapkan pada sistem.
- Pembaruan Struktur Organisasi pada sistem hanya dilakukan oleh **Department TD-OD** setelah seluruh tahapan persetujuan selesai.
- Apabila usulan ditolak/tidak disetujui pada salah satu tahapan persetujuan, maka usulan perubahan organisasi akan dikembalikan kepada **Requester** untuk dilakukan revisi bersama dan diajukan kembali.
- Persetujuan perubahan Struktur Organisasi secara Tahunan atau Quartalan pada level **di bawah Department**, cukup sampai dengan General Manager Operasional (Kepala Operasional) atau Director in Charge sesuai jenjang organisasi yang berlaku. Sedangkan untuk perubahan Struktur Organisasi secara Tahunan atau Quartalan pada level **Department Up**, persetujuannya harus sampai ke Direktur.
- Aktivitas **Update Organization Chart** merupakan proses yang dilakukan di aplikasi/sistem melalui modul **Position Management** setelah seluruh persetujuan telah dipenuhi.
- Penyesuaian jalur pelaporan (line reporting) yang tidak merubah Struktur Organisasi **dapat dilakukan sewaktu-waktu** oleh Tim Organization Development, berdasarkan permintaan dari Business Unit, serendah-rendahnya level Department Head (Manager).

*[Sengaja dikosongkan — sebagaimana tercantum pada dokumen asli]*

### 3.2 Manage Organizational Structure Business Process Flow

[Ilustrasi sumber dihapus dari korpus publik: Manage Organizational Structure Business Process Flow (Current System)]

## 4. Expected New System Business Flow

**Guidance:**

- Please describe the expected improved system flow.
- To maximize the understanding of expected new system, consider explaining with process flow in mind.
- Do it step by step from beginning to the end of process.
- More complete the explanation will affect the next visual modelling process.

### 4.1 Manage Organizational Structure Business Process

#### A. Flow External (Di Luar Aplikasi / Manual Process)

##### 1. Pengajuan Perubahan Struktur Organisasi

- Requester mengidentifikasi kebutuhan perubahan struktur organisasi.
- Requester menyusun proposal perubahan struktur organisasi.
- Requester melampirkan organizational chart baru beserta justifikasi perubahan.
- Proposal disampaikan kepada OD Section untuk dilakukan review awal.

##### 2. Review Awal oleh OD Section

- OD Section melakukan evaluasi terhadap proposal perubahan struktur organisasi.
- OD Section memverifikasi kelengkapan dokumen, kesesuaian struktur, dan alasan bisnis yang mendasari perubahan.

**Keputusan: Setuju dengan Proposal?**

- **Ya** → Proposal diteruskan kepada Manager Training & Development untuk review berikutnya.
- **Tidak** → OD Section memberikan masukan dan melakukan pembahasan bersama Requester untuk revisi proposal.

##### 3. Revisi Proposal

- Requester dan OD Section melakukan diskusi serta penyempurnaan proposal berdasarkan hasil review.
- Proposal yang telah direvisi diajukan kembali untuk proses review dan persetujuan.

##### 4. Review oleh Manager Training & Development

- Manager Training & Development melakukan review terhadap proposal yang telah disetujui OD Section.

**Keputusan: Setuju dengan Proposal?**

- **Ya** → Proposal diteruskan kepada Senior Manager HCM.
- **Tidak** → Proposal dikembalikan kepada OD Section dan Requester untuk dilakukan revisi.

##### 5. Review oleh Senior Manager HCM

- Senior Manager HCM melakukan review terhadap proposal perubahan struktur organisasi.

**Keputusan: Setuju dengan Proposal?**

- **Ya** → Proposal diteruskan kepada GM Operations / Director in Charge.
- **Tidak** → Proposal dikembalikan kepada OD Section dan Requester untuk dilakukan revisi.

##### 6. Review oleh GM Operations / Director in Charge

- GM Operations / Director in Charge melakukan review akhir terhadap proposal perubahan struktur organisasi.

**Keputusan: Setuju dengan Proposal?**

- **Ya** → Proposal dinyatakan disetujui dan dapat diimplementasikan.
- **Tidak** → Proposal dikembalikan kepada OD Section dan Requester untuk dilakukan revisi.

##### 7. Review oleh Board of Director

- Board of Director melakukan review akhir terhadap proposal perubahan struktur organisasi.

**Keputusan: Setuju dengan Proposal?**

- **Ya** → Proposal dinyatakan disetujui dan dapat diimplementasikan.
- **Tidak** → Proposal dikembalikan kepada OD Section dan Requester untuk dilakukan revisi.

#### Flow Internal (Di Dalam Aplikasi / System Process)

##### 1. Update Organization Structure

- OD Section melakukan pembaruan data struktur organisasi pada aplikasi dengan melakukan penambahan/perubahan organisasi atau import file organization structure dengan ekstension csv/xlsx.
- Sistem menyimpan perubahan struktur organisasi yang telah disetujui.
- Struktur organisasi terbaru menjadi struktur organisasi aktif yang digunakan oleh sistem dan modul terkait.

##### 2. End Process

- Sistem mengakhiri proses setelah pembaruan struktur organisasi berhasil disimpan.

**Catatan:**

- Seluruh proses review dan persetujuan dilakukan secara **manual** sebelum perubahan diterapkan pada sistem.
- Pembaruan Struktur Organisasi pada sistem hanya dilakukan oleh **Department TD-OD** setelah seluruh tahapan persetujuan selesai.
- Apabila usulan ditolak/tidak disetujui pada salah satu tahapan persetujuan, maka usulan perubahan organisasi akan dikembalikan kepada **Requester** untuk dilakukan revisi bersama dan diajukan kembali.
- Persetujuan perubahan Struktur Organisasi secara Tahunan atau Quartalan pada level **di bawah Department**, cukup sampai dengan General Manager Operasional (Kepala Operasional) atau Director in Charge sesuai jenjang organisasi yang berlaku. Sedangkan untuk perubahan Struktur Organisasi secara Tahunan atau Quartalan pada level **Department Up**, persetujuannya harus sampai ke Direktur.
- Aktivitas **Update Organization Chart** merupakan proses yang dilakukan di aplikasi/sistem setelah seluruh persetujuan telah dipenuhi.
- Penyesuaian jalur pelaporan (line reporting) yang tidak merubah Struktur Organisasi **dapat dilakukan sewaktu-waktu** oleh Tim Organization Development, berdasarkan permintaan dari Business Unit, serendah-rendahnya level Department Head (Manager).

### 4.2 Manage Organizational Structure Business Process Flow

[Ilustrasi sumber dihapus dari korpus publik: Manage Organizational Structure Business Process Flow (Expected New System)]

## 5. Module Policy

### Organization Structure Policies / Business Rules

- Setiap unit organisasi wajib memiliki identitas yang unik dan tidak boleh duplikat.
- Setiap unit organisasi harus berada dalam hierarki organisasi yang valid.
- Tim Organization Development (OD) dapat mengakses dan melihat seluruh struktur organisasi perusahaan.
- Pengguna lain hanya dapat mengakses informasi struktur organisasi sesuai hak akses yang diberikan (read-only).
- Sistem harus menyediakan visualisasi Org. Chart berdasarkan struktur organisasi yang berlaku pada tanggal yang dipilih.
- Sistem harus menyediakan fungsi pencarian berdasarkan nama department, nama posisi, nama karyawan, ID Pegawai melalui integrasi dengan modul terkait.
- Struktur organisasi menjadi data referensi bagi modul Employee Central lainnya.
- Standarisasi kode organisasi (Directorate, Division, Department, dan Section) akan mengikuti kebijakan yang ditetapkan oleh HR Organization Development.
- Integrasi dengan modul ESC: Perubahan data karyawan melalui proses Employee Status Change (ESC), seperti promosi, transfer, atau reclassification, dapat memengaruhi visualisasi dan penempatan data pada struktur organisasi sesuai konfigurasi yang berlaku.

## 6. Approval / Sign-Off

| Role | Name | Signature | Date |
| --- | --- | --- | --- |
| Business Analyst | Analis Bisnis A | [Ilustrasi sumber dihapus dari korpus publik: Tanda tangan Business Analyst] | 13 Juli 2026 |
| Project Coordinator | Koordinator Proyek A | | |
| Business User Expert | Narasumber Bisnis C | | |

*By signing this document, all items contained herein are confirmed as mandatory requirements to be delivered as the agreed-upon product. Any changes or modifications to these requirements will be managed through the change request process.*
