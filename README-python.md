# Python Multi-Agent Consistency Checker

Prototype runnable untuk [arsitektur tesis](data/architecture/README.md):
Agent 1 -> Specification IR; Mermaid Parser -> Diagram IR; IR Validator;
Agent 2 -> kandidat mapping; Agent 3 -> verifikasi; Python R1-R7 -> agregasi;
Agent 4 -> narasi. Urutan dikendalikan Python, bukan keputusan bebas LLM.
Parser dijalankan dahulu agar format salah ditemukan sebelum biaya API dikeluarkan.

Panduan lengkap: [setup, konfigurasi dan batas metode](docs/implementation/README.md).
Catatan pengujian: [VALIDATION.md](docs/implementation/VALIDATION.md).

## Setup Windows / PowerShell

Dari root repository, gunakan Python >=3.11:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
Copy-Item .env.example .env
notepad .env
```

Isi `OPENAI_API_KEY` di `.env` lokal. Jangan kirim key ke chat, issue, PR, atau source.
Pilih `OPENAI_MODEL` yang tersedia di project API Anda. Default `gpt-4.1-mini`
adalah pilihan awal yang dapat diganti, bukan klaim model terbaru atau terbaik.
`.env` dan `outputs/` dikecualikan dari Git.

```powershell
# Offline: unit test dan parsing contoh, tidak memanggil API.
.\.venv\Scripts\python.exe -m pytest -q
.\.venv\Scripts\python.exe -m thesis_agents.cli run --case examples/case.json --until parse

# Memanggil OpenAI untuk pasangan dari dataset repository.
.\.venv\Scripts\python.exe -m thesis_agents.cli run --case config/case-pd-02.json
```

Hasil ada di `outputs/<run-id>/`: `report.json`, `report.md`, `traceability.json`,
checkpoint per tahap, `run.json` dan `events.jsonl`.

## Sakelar eksekusi dan logging terpisah

Edit `config/pipeline.toml`:

```toml
[stages.agent2]
enabled = true
log_enabled = false

[stages.agent4]
enabled = false
log_enabled = true
```

Agent 2 tetap bekerja tanpa log; Agent 4 dilewati dan laporan deterministik tetap
tersedia. Tahap wajib yang off harus memakai checkpoint kompatibel, tidak boleh
dilewati diam-diam seolah-olah berhasil.

```powershell
# Reuse hasil Agent 1 dari run sebelumnya.
.\.venv\Scripts\python.exe -m thesis_agents.cli run --disable agent1 --resume outputs/RUN_ID

# Berhenti setelah verifikasi mapping.
.\.venv\Scripts\python.exe -m thesis_agents.cli run --until agent3

# Matikan hanya log tertentu, bukan komputasinya.
.\.venv\Scripts\python.exe -m thesis_agents.cli run --quiet-step agent2 --quiet-step load

# Rule yang dimatikan menjadi abstention, bukan pass.
.\.venv\Scripts\python.exe -m thesis_agents.cli run --disable-rule R6
```

## Batas penting

Ini prototype penelitian, bukan verifikasi lengkap seluruh semantik UML. `alt`/`opt`
dipertahankan sebagai jalur; `loop` diparse tetapi analisis lintas iterasi abstain.
`par` dan konstruk struktural di luar subset ditolak. Kondisi ambigu, obligation
bersyarat yang belum diputuskan, dan mapping yang tidak pasti menghasilkan
`needs_review` otomatis, bukan human-review gate.

Unit test memakai fixture buatan, bukan prediksi LLM atau ukuran akurasi tesis.
Test SDK berjalan ketika dependency terpasang. Pengujian API langsung, gold-standard
annotation, precision/recall, baseline, dan ablation adalah eksperimen terpisah.
Narasi Agent 4 tidak mengubah keputusan deteksi kanonis.
