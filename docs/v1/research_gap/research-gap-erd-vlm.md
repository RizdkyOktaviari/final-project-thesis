# Research Gap dan Masalah Penelitian Saat Ini
## Rekonstruksi ERD dari Gambar menjadi Representasi Terstruktur dan Editable

Dokumen ini merangkum masalah yang belum sepenuhnya terselesaikan pada penelitian terkait *diagram understanding*, *image-to-diagram reconstruction*, *Vision-Language Models* (VLM), dan transformasi diagram menjadi representasi yang dapat diedit. Fokus diarahkan pada peluang penelitian untuk rekonstruksi **Entity–Relationship Diagram (ERD)** dari gambar dunia nyata.

---

## 1. ERD masih banyak tersedia sebagai gambar, bukan representasi machine-readable

Dalam praktiknya, ERD sering tersedia hanya sebagai gambar yang tertanam pada buku, slide, dokumentasi perangkat lunak, PDF, screenshot, platform kolaborasi, dan repository. Kondisi ini menjadi hambatan ketika diagram perlu digunakan kembali untuk *schema understanding*, dokumentasi, migrasi, modernisasi sistem, atau pemrosesan otomatis.

**Referensi:**  
Ansari et al. (2026), *ERUnderstand: Evaluating Vision-Language Models on Structured ER Diagrams*.

**Kalimat pendukung singkat:**  
> “In practice, however, these diagrams are rarely available in machine-readable form.”

**Lokasi:**  
Section 1 — *Introduction*, halaman 1.

**Potensi research gap:**  
Mengembangkan metode yang mampu merekonstruksi ERD statis menjadi representasi terstruktur dan editable ketika source/raw diagram tidak lagi tersedia.

---

## 2. Kualitas gambar dunia nyata masih menjadi tantangan dalam diagram recognition

Diagram dapat memiliki variasi resolusi, perbedaan style dari berbagai modeling tools, dashed/dotted lines yang sulit dibedakan, serta gradient background yang mengganggu proses pengenalan elemen.

**Referensi:**  
Chen et al. (2022), *Automatically Recognizing the Semantic Elements from UML Class Diagram Images*.

**Kalimat pendukung singkat:**  
> “The diagram images may have different resolutions.”

dan:

> “Gradient colors are common in the image background.”

**Lokasi:**  
Section 1 — *Introduction*, halaman 2; Section 2.1 — *Background: Semantic elements in class diagrams*, halaman 3.

**Potensi research gap:**  
Robustness model modern, khususnya VLM, terhadap **degraded real-world diagram images** seperti blur, low resolution, noise, JPEG compression, low contrast, dan unclear styling masih layak diteliti secara sistematis.

---

## 3. Low-resolution dan ambiguous notation masih menyulitkan interpretasi ERD

ERUnderstand menemukan bahwa proses anotasi manusia sendiri masih membutuhkan joint review pada sejumlah diagram karena notasi ambigu dan kualitas gambar yang rendah.

**Referensi:**  
Ansari et al. (2026), *ERUnderstand*.

**Kalimat pendukung singkat:**  
> “21 diagrams required joint review, primarily due to ambiguous notation or low-resolution images.”

**Lokasi:**  
Section 3.1 — *Curated ERD Collection*, halaman 3.

**Potensi research gap:**  
Meneliti apakah *image preprocessing* atau *adaptive image enhancement* sebelum VLM inference dapat meningkatkan akurasi rekonstruksi struktur ERD.

---

## 4. Relationship reconstruction masih lebih sulit daripada entity recognition

Model VLM relatif baik dalam mengenali entity, tetapi lebih lemah dalam memahami relationship. Kesalahan dapat berupa hubungan yang terlewat, hubungan tambahan yang tidak ada, atau koneksi yang salah.

**Referensi:**  
Ansari et al. (2026), *ERUnderstand*.

**Kalimat pendukung singkat:**  
> “Models achieve high F1-scores for entities (0.90) but perform substantially worse on relationships.”

**Lokasi:**  
Section 5 — *Failure Mode Analysis*, halaman 5.

**Referensi tambahan:**  
Deka & Devereux (2025), *Flowchart2Mermaid*.

**Kalimat pendukung singkat:**  
> “Relationship extraction is consistently more difficult.”

**Lokasi:**  
Section 6 — *Results and Discussion*, halaman 5–6.

**Potensi research gap:**  
Fokus penelitian dapat diarahkan pada **structural relationship reconstruction**, bukan sekadar pengenalan node, entity, atau text.

---

## 5. Advanced ER/EER constructs masih sulit dikenali oleh VLM

ERUnderstand menunjukkan penurunan performa yang sangat besar pada konstruksi ER/EER yang lebih kompleks, seperti weak entity, multivalued attribute, dan n-ary relationship.

**Referensi:**  
Ansari et al. (2026), *ERUnderstand*.

**Kalimat pendukung singkat:**  
> “Performance drops sharply on weak entities (as low as 0.28 F1), multivalued attributes (0.14 F1), and n-ary relationships (0.07 F1).”

**Lokasi:**  
Abstract, halaman 1.

**Potensi research gap:**  
Mengembangkan mekanisme berbasis aturan atau constraint ER/EER untuk memvalidasi dan memperbaiki hasil VLM pada advanced constructs.

---

## 6. VLM mengalami spatial proximity bias

VLM cenderung menghubungkan elemen yang secara visual berdekatan dan dapat kehilangan hubungan yang sebenarnya valid tetapi berjauhan secara posisi.

**Referensi:**  
Ansari et al. (2026), *ERUnderstand*.

**Kalimat pendukung singkat:**  
> “Hallucinated relationships between spatially proximate entities ... and missed relationships between distant but correctly connected entities.”

**Lokasi:**  
Section 5 — *Spatial Proximity Bias in ERDs*, halaman 5.

**Kalimat kesimpulan penulis:**  
> “Current VLMs rely heavily on spatial heuristics rather than explicit visual connectivity.”

**Lokasi:**  
Section 5, halaman 5–6.

**Potensi research gap:**  
Menggabungkan VLM dengan **explicit connector detection**, graph-aware reasoning, atau structure-aware validation.

---

## 7. VLM masih bergantung pada linguistic prior

Model tidak sepenuhnya memahami struktur visual. Ketika label pada entity, attribute, dan relationship diacak atau diubah menjadi string tanpa arti, performa model menurun.

**Referensi:**  
Ansari et al. (2026), *ERUnderstand*.

**Kalimat pendukung singkat:**  
> “All models exhibit significant performance drops, confirming strong reliance on linguistic cues.”

**Lokasi:**  
Section 5 — *Prior-Language Bias in ERDs*, halaman 6.

**Potensi research gap:**  
Mengembangkan pendekatan yang memaksa model lebih mengandalkan **visual connectivity dan diagram structure**, bukan semantic plausibility dari label.

---

## 8. Performa VLM menurun drastis pada diagram yang kompleks

Pada ERD dengan jumlah entity dan relationship yang besar, sebagian model mengalami penurunan performa sangat tajam.

**Referensi:**  
Ansari et al. (2026), *ERUnderstand*.

**Kalimat pendukung singkat:**  
> “Performance degrades across most models, with Macro-F1 dropping to 0.035–0.048 and relationship scores near zero.”

**Lokasi:**  
Section 5 — *Complexity Degradation*, halaman 5.

**Potensi research gap:**  
Mengembangkan **complexity-aware reconstruction**, misalnya:

- diagram decomposition,
- region-based parsing,
- local relationship extraction,
- graph partitioning,
- global graph reconciliation.

---

## 9. Synthetic-to-real-world generalization masih menjadi masalah

Bates et al. menggunakan dataset UML sintetik dalam skala besar, tetapi diagram tersebut dibuat dari random vocabulary dan tidak memiliki coherent application logic.

**Referensi:**  
Bates et al. (2025), *Unified Modeling Language Code Generation from Diagram Images Using Multimodal Large Language Models*.

**Kalimat pendukung singkat:**  
> “The diagrams do not follow any coherent application logic.”

**Lokasi:**  
Section 2.3 — *Synthetic Data Generation*, halaman 4.

Evaluasi real-world pada penelitian tersebut juga relatif kecil.

**Kalimat pendukung singkat:**  
> “29 activity diagrams and 28 sequence diagrams — totaling 57 examples.”

**Lokasi:**  
Section 2.3.2 — *Real-world Testing Evaluation*, halaman 5.

**Potensi research gap:**  
Menguji generalisasi model dari diagram clean/synthetic menuju diagram dunia nyata yang memiliki blur, screenshot artifacts, noise, low resolution, dan styling yang tidak konsisten.

---

## 10. Syntactic validity tidak menjamin semantic correctness

Sebuah diagram dapat valid secara sintaksis dan berhasil dirender tetapi masih salah secara struktur atau makna.

**Referensi:**  
Godwin & Melvin (2026), *UMLBot: Generative AI for Converting Natural Language and Code Excerpts to Editable UML Diagrams*.

**Kalimat pendukung singkat:**  
> “UMLBot ... [is] not a system that guarantees semantically correct diagrams.”

dan:

> “... produce syntactically valid PlantUML that does not accurately represent the intended system.”

**Lokasi:**  
Section 4.1 — *Limitations and Scope*, halaman 6.

**Potensi research gap:**  
Mengembangkan validasi pada level **semantic and structural correctness**, bukan hanya apakah output dapat diparsing atau dirender.

---

## 11. Hubungan masih menjadi bagian yang paling tidak reliable pada generated diagram

UMLBot menunjukkan bahwa LLM relatif mampu menangkap class, method, dan attribute, tetapi relationship masih menjadi bagian yang lebih lemah.

**Referensi:**  
Godwin & Melvin (2026), *UMLBot*.

**Kalimat pendukung singkat:**  
> “... classes, methods, attributes, and relationships, with the latter being the least reliably identified.”

**Lokasi:**  
Figure 4 caption, halaman 4.

**Referensi tambahan:**  
Section 3, halaman 5.

**Kalimat pendukung singkat:**  
> “... less reliable at capturing all relationships.”

**Potensi research gap:**  
Menambahkan relationship-specific extraction atau post-processing untuk memperbaiki structural reconstruction.

---

## 12. Existing validation masih dominan pada format dan renderability

GenAI-DrawIO-Creator menggunakan XML validation untuk memastikan struktur XML valid, tag lengkap, dan connector mengarah ke ID yang tersedia.

**Referensi:**  
Yu & Jiang (2026), *GenAI-DrawIO-Creator: A Framework for Automated Diagram Generation*.

**Kalimat pendukung singkat:**  
> “After receiving Claude’s output, we run it through an XML parser.”

**Lokasi:**  
Section 3.2 — *Optimized XML Generation and Validation*, halaman 3.

Sistem juga memeriksa jumlah elemen dan validitas source/target connector.

**Lokasi:**  
Section 3.6 — *Output Verification and Diagram History*, halaman 4.

**Potensi research gap:**  
Validasi dapat diperluas menjadi **ER-specific structure-aware validation**, misalnya:

- cardinality consistency,
- valid entity–relationship connections,
- weak entity rules,
- identifying relationship rules,
- key constraints,
- multivalued attribute rules,
- n-ary relationship consistency.

---

## 13. Image-to-editable diagram masih kurang presisi pada visualisasi kompleks

GenAI-DrawIO-Creator sudah mampu melakukan image-based diagram replication, tetapi performanya masih terbatas pada diagram kompleks.

**Referensi:**  
Yu & Jiang (2026), *GenAI-DrawIO-Creator*.

**Kalimat pendukung singkat:**  
> “The image-to-diagram feature works for simple cases but lacks precision with complex visualizations.”

**Lokasi:**  
Section 5 — *Discussion and Conclusion*, halaman 4.

Penulis juga menyebut:

> “Claude occasionally misinterprets spatial relationships ... and shows diminishing accuracy with diagrams exceeding 20 components.”

**Lokasi:**  
Section 5, halaman 4.

**Potensi research gap:**  
Menggunakan intermediate semantic representation sebelum menghasilkan format editable seperti Draw.io XML, Mermaid, atau PlantUML.

---

## 14. Direct image-to-code generation masih dapat menghasilkan hallucination atau semantic error

Flowchart2Mermaid menggunakan VLM untuk menghasilkan Mermaid langsung dari flowchart image. Walaupun hasilnya tinggi, model tetap dapat salah memahami atau menghalusinasikan elemen.

**Referensi:**  
Deka & Devereux (2025), *Flowchart2Mermaid*.

**Kalimat pendukung singkat:**  
> “The underlying vision–language models may occasionally hallucinate or misinterpret diagram elements.”

**Lokasi:**  
Section 7 — *Conclusion and Future Work / Limitations*, halaman 6.

Penulis juga menyatakan:

> “It may not exactly match the original diagram’s layout or semantics.”

**Lokasi:**  
Section 7, halaman 6.

**Potensi research gap:**  
Menghindari direct generation:

```text
Image
  ↓
VLM
  ↓
Mermaid
```

dan menggunakan pipeline:

```text
Image
  ↓
Image Preprocessing
  ↓
VLM Semantic Extraction
  ↓
Intermediate ER Representation
  ↓
Structure-Aware Validation
  ↓
Targeted Correction
  ↓
Editable Diagram
```

---

## 15. Structural metrics lebih penting daripada text similarity saja

Flowchart2Mermaid menunjukkan bahwa cosine similarity yang tinggi belum tentu menunjukkan struktur diagram yang benar.

**Referensi:**  
Deka & Devereux (2025), *Flowchart2Mermaid*.

**Kalimat pendukung singkat:**  
> “Text-level similarity can mask important structural errors.”

**Lokasi:**  
Section 6.1 — *Discussion*, halaman 6.

**Potensi research gap:**  
Evaluasi ERD sebaiknya menggunakan metrik berbasis struktur seperti:

- Entity Precision / Recall / F1,
- Attribute F1,
- Relationship F1,
- Cardinality Accuracy,
- Macro-F1,
- Graph Edit Distance,
- Structural Validity,
- Semantic Fidelity.

---

## 16. Existing VLM benchmark belum menyelesaikan reconstruction menjadi editable diagram

ERUnderstand menyediakan benchmark yang sangat kuat untuk memahami struktur ERD dan menggunakan standardized JSON sebagai ground truth. Namun fokus utamanya adalah **benchmarking structured understanding**, bukan membangun end-to-end editable reconstruction framework.

**Referensi:**  
Ansari et al. (2026), *ERUnderstand*.

**Kalimat pendukung singkat:**  
> “Each diagram is paired with a standardized machine-readable JSON representation.”

**Lokasi:**  
Section 3 — *The ERUnderstand Benchmark*, halaman 3.

**Potensi research gap:**  
Memanfaatkan intermediate ER representation sebagai tahap antara VLM understanding dan editable output.

---

## 17. Hybrid rule-based + LLM/VLM masih berpotensi dikembangkan

Pendekatan klasik seperti ReSECDI menunjukkan bahwa image processing dapat membantu menangani perbedaan resolusi dan style. Sementara penelitian berbasis LLM menunjukkan fleksibilitas yang lebih tinggi tetapi masih memiliki masalah hallucination dan structural correctness.

Siala & Lano menunjukkan pola bahwa LLM dapat dikombinasikan dengan rule-based abstraction dan intermediate structured representation.

**Referensi:**  
Siala & Lano (2026), *Leveraging LLMs for Abstracting UML and OCL Representations from Java and Python Programs*.

**Kalimat pendukung singkat:**  
> “Java2JSON parses Java programs and constructs JSON files to represent the elements and relationships of UML class diagrams.”

**Lokasi:**  
Section 1.3 — *Contributions of the paper*, halaman 2.

**Potensi research gap:**  
Mengembangkan pendekatan hybrid:

```text
Image Processing
      +
Vision-Language Model
      +
Intermediate ER Representation
      +
ER/EER Constraint Validation
      +
Automatic Correction
```

Gap ini merupakan **sintesis dari beberapa penelitian**, bukan klaim eksplisit dari satu paper.

---

# Lima Research Gap Utama yang Paling Potensial

## Gap 1 — Degraded Image Robustness

Belum jelas seberapa robust VLM dalam merekonstruksi ERD ketika input mengalami kondisi dunia nyata seperti:

- blur,
- low resolution,
- JPEG compression,
- noise,
- low contrast,
- faded connector,
- unclear styling,
- inconsistent line thickness.

**Dasar utama:**  
Chen et al. (2022) menunjukkan bahwa resolution dan visual styling memengaruhi recognition, sedangkan Ansari et al. (2026) menemukan low-resolution images menjadi salah satu sumber ambiguity.

**Potensi penelitian:**  
Menguji pengaruh berbagai tingkat degradasi gambar terhadap kemampuan VLM dan menilai kontribusi image preprocessing terhadap structural reconstruction accuracy.

---

## Gap 2 — Relationship and Structural Reasoning

Entity recognition sudah relatif kuat, tetapi relationship reconstruction masih menjadi sumber error utama.

**Dasar utama:**

- Ansari et al. (2026)
- Deka & Devereux (2025)
- Godwin & Melvin (2026)

**Potensi penelitian:**  
Mengembangkan mechanism yang berfokus pada explicit connector detection dan graph reconstruction.

---

## Gap 3 — Advanced EER Recognition

Advanced constructs seperti:

- weak entity,
- identifying relationship,
- multivalued attribute,
- n-ary relationship,
- hierarchy,

masih sulit direkonstruksi secara reliable.

**Dasar utama:**  
Ansari et al. (2026).

**Potensi penelitian:**  
Menggunakan ER/EER constraints sebagai validator atau correction mechanism setelah VLM inference.

---

## Gap 4 — Semantic / Structure-Aware Validation

Existing systems sudah mampu memastikan:

```text
Valid XML
Valid Mermaid
Valid PlantUML
```

tetapi belum menjamin:

```text
Correct ERD Structure
```

**Dasar utama:**

- Godwin & Melvin (2026)
- Yu & Jiang (2026)
- Deka & Devereux (2025)

**Potensi penelitian:**  
Mengembangkan **ER-specific structure-aware validator** untuk mendeteksi output VLM yang valid secara syntax tetapi salah secara struktur.

---

## Gap 5 — Hybrid ERD Reconstruction

Masih terdapat peluang untuk menggabungkan:

```text
Degradation-Aware Image Processing
              +
Vision-Language Model
              +
Intermediate ER Representation
              +
ER/EER Structural Constraints
              +
Automatic Targeted Correction
```

menjadi sebuah end-to-end framework.

Gap ini merupakan **research gap sintesis** yang diturunkan dari keterbatasan beberapa penelitian sebelumnya.

---

# Research Gap Utama

> Current Vision-Language Models are capable of recognizing basic elements of Entity–Relationship Diagrams, but reliable reconstruction of degraded real-world ERD images remains unresolved, particularly for relationships, advanced ER/EER constructs, dense diagrams, and semantic correctness. Existing diagram-generation systems also focus largely on syntactic correctness or renderability rather than ER-specific structural validity.

---

# Potensi Novelty Penelitian

> **A degradation-aware hybrid ERD reconstruction framework combining image preprocessing, Vision-Language Model-based semantic extraction, intermediate ER representation, and ER-specific structure-aware validation and correction to generate reliable editable diagrams.**

Versi lebih singkat:

> **Degradation-Aware and Structure-Aware ERD Image Reconstruction using Vision-Language Models.**

---

# Referensi Utama

1. Ansari, A., Mohammadi, Y., Nili, F., Esmaeilkhani, P., Latecki, L. J., & Dragut, E. (2026). *ERUnderstand: Evaluating Vision-Language Models on Structured ER Diagrams*.
2. Chen, F., Zhang, L., Lian, X., & Niu, N. (2022). *Automatically Recognizing the Semantic Elements from UML Class Diagram Images*. The Journal of Systems & Software, 193, 111431.
3. Bates, A., Vavricka, R., Carleton, S., Shao, R., & Pan, C. (2025). *Unified Modeling Language Code Generation from Diagram Images Using Multimodal Large Language Models*. Machine Learning with Applications, 20, 100660.
4. Deka, P., & Devereux, B. (2025). *Flowchart2Mermaid: A Vision-Language Model Powered System for Converting Flowcharts into Editable Diagram Code*.
5. Godwin, R. C., & Melvin, R. L. (2026). *UMLBot: Generative AI for Converting Natural Language and Code Excerpts to Editable UML Diagrams*. SoftwareX, 35, 102789.
6. Yu, J., & Jiang, D. (2026). *GenAI-DrawIO-Creator: A Framework for Automated Diagram Generation*.
7. Siala, H. A., & Lano, K. (2026). *Leveraging LLMs for Abstracting UML and OCL Representations from Java and Python Programs*. The Journal of Systems & Software, 238, 112874.
