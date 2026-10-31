# Thesis Research Repository

This repository is used to manage the research and development activities related to my master's thesis.

The scope of the research may evolve as the thesis topic, research questions, methodology, and experimental design are refined.

The repository may contain:

- Literature reviews and research notes
- Research gap and problem exploration
- Research questions and hypotheses
- Dataset and experiment preparation
- Research prototypes and implementations
- Evaluation scripts and experimental results
- Supporting diagrams and research artifacts

## Documentation Versioning

Research documentation is maintained by version to preserve the evolution of the thesis work.

Documentation is stored under:

```text
docs/v++/
```

The requirements corpus used for thesis experiments is documented in
[`data/README.md`](data/README.md). It separates original BRD material from
derived requirement breakdowns so that an experiment can be reproduced without
modifying the source evidence.

## Privasi korpus

Dokumen di `data/` merupakan **salinan anonim untuk riset**, bukan BRD asli. Nama organisasi, aplikasi, dan narasumber diganti dengan label umum. Aset visual sumber tidak tersedia di cabang publik. Penghapusan pada revisi sekarang **tidak menghapus riwayat Git terdahulu**, sehingga repository ini tidak boleh dianggap telah bebas sepenuhnya dari paparan dokumen sebelumnya. Pastikan izin penggunaan dan publikasi korpus sebelum membagikannya.

## Implementasi Python multi-agent

[Mulai dari README Python](README-python.md) untuk setup API key lokal, menjalankan
empat agent dan checker R1-R7, mengatur on/off tiap tahap dan log, serta membaca hasil.
[Rincian implementasi dan batas metode](docs/implementation/README.md) menjelaskan
checkpoint, evidence validation, data leakage boundary, dan cakupan prototype.
