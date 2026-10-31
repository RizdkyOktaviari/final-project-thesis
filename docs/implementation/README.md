# Implementasi Python: Structure-Aware Hybrid Consistency Checking

## Pemetaan arsitektur

| Komponen | Modul | Fungsi |
| --- | --- | --- |
| Input boundary | `dataset.py` | Case scoped, path allowlist, ukuran, hash sumber |
| Agent 1 | `llm.py`, `prompts/agent1.md` | Ekstraksi atom dari FR tanpa diagram |
| Mermaid Parser | `mermaid.py` | Participant, pesan, arrow, nested alt/opt/loop, source span |
| IR Validator | `validation.py` | Schema, ID, referensi, scope, exact evidence, reparse SD |
| Agent 2 | `prompts/agent2.md` | Role/behavior/guard mapping, termasuk many-to-many |
| Agent 3 | `prompts/agent3.md` | Keputusan per kandidat dengan kedua sumber asli |
| Rule Checker | `rules.py` | R1-R7 tanpa pemanggilan LLM |
| Aggregator | `reporting.py` | Deduplikasi identik, coverage, status, traceability dua arah |
| Agent 4 | `prompts/agent4.md` | Narasi advisory terikat ke finding ID |
| Orchestrator | `pipeline.py` | Urutan eksplisit, checkpoint, stop/resume, kegagalan |
| Observability | `logging_utils.py`, `storage.py` | JSONL events, provenance, durasi, token usage |

Empat agent memakai instans Agents SDK dengan instruksi/structured output berbeda.
Tidak ada handoff bebas, akses web/shell, atau conversation state bersama. Agent 4
tidak memiliki akses menulis dokumen sumber. Parsing berjalan sebelum Agent 1 agar
input rusak tidak membuang biaya API.

## Instalasi dan kredensial

Gunakan Python >=3.11. Dari root repository pada Windows/PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
Copy-Item .env.example .env
notepad .env
```

Isi `.env` lokal:

```dotenv
OPENAI_API_KEY=isi_key_Anda_hanya_di_file_lokal
OPENAI_MODEL=gpt-4.1-mini
OPENAI_AGENTS_DISABLE_TRACING=1
OPENAI_AGENTS_TRACE_INCLUDE_SENSITIVE_DATA=0
```

Linux/macOS: `python3 -m venv .venv`, lalu gunakan `.venv/bin/python`.
Environment yang sudah ada diprioritaskan atas `.env` (`override=False`).
`OPENAI_MODEL` mengalahkan `llm.model`; `llm.models.agentN` mengalahkan keduanya.
Model harus mendukung Structured Outputs dan tersedia di project API Anda.
Tidak ada klaim model default terbaik. Pin model snapshot dan dependencies ketika
memulai eksperimen formal; versi environment aktual dicatat pada setiap run.

FR/SD dikirim ke OpenAI ketika tahap LLM dijalankan. Pastikan izin penggunaan dan
anonimisasi data. `store=False` dan tracing nonaktif bukan jaminan zero-retention
seluruh layanan API. Checkpoint lokal mengandung kutipan sumber: lindungi folder
output meskipun diabaikan Git. Tidak perlu membagikan key untuk debugging.

## Menjalankan sistem

```powershell
# Tanpa API: parser.
.\.venv\Scripts\python.exe -m thesis_agents.cli run --case examples/case.json --until parse

# Ekstraksi saja.
.\.venv\Scripts\python.exe -m thesis_agents.cli run --until agent1

# Pipeline lengkap, menggunakan pasangan REQ-PD-003 / SD-PD-02.
.\.venv\Scripts\python.exe -m thesis_agents.cli run --case config/case-pd-02.json

# Hasil tetap tersedia tanpa Agent 4.
.\.venv\Scripts\python.exe -m thesis_agents.cli run --disable agent4
```

Semua relative path mengacu ke `--root`, default current working directory, bukan
folder config. `examples/` adalah data sintetis. Case dataset default tidak mengasumsikan
cakupan lengkap dan tidak memuat jawaban injeksi. Exit 0 berarti proses selesai atau
berhenti sesuai `--until`, bukan berarti diagram konsisten. Exit 1 adalah kegagalan
pipeline; exit 2 adalah kesalahan konfigurasi/dataset. Baca `report.json` untuk verdict.

## Kontrol on/off

| Kontrol | Efek |
| --- | --- |
| `stages.<nama>.enabled` | Jalankan tahap; bila false, wajib reuse checkpoint |
| `stages.<nama>.log_enabled` | Kontrol logging saja, tidak mengubah komputasi |
| `stages.<nama>.log_level` | Override global; tanpa nilai mewarisi `logging.level` |
| `logging.disabled_steps` | Matikan log tahap tertentu, termasuk load/pipeline |
| `rules.Rn` | Rule false dilaporkan sebagai abstention, bukan pass |

Tahap: parse, agent1, validate, agent2, agent3, check, aggregate, agent4.
Validasi path/allowlist/size input selalu aktif karena merupakan batas keselamatan.
Agent 4 satu-satunya tahap yang boleh off tanpa checkpoint: renderer deterministik
menghasilkan laporan dari temuan Python.

Contoh konfigurasi:

```toml
[stages.agent2]
enabled = true
log_enabled = true
log_level = "DEBUG"

[stages.agent3]
enabled = false
log_enabled = true

[stages.agent4]
enabled = false

[rules]
R6 = false
```

Agent 3 di atas membutuhkan checkpoint kompatibel:

```powershell
.\.venv\Scripts\python.exe -m thesis_agents.cli run --resume outputs/RUN_ID
.\.venv\Scripts\python.exe -m thesis_agents.cli run --disable agent1 --resume outputs/RUN_ID
.\.venv\Scripts\python.exe -m thesis_agents.cli run --quiet-step agent2 --quiet-step load
.\.venv\Scripts\python.exe -m thesis_agents.cli run --disable-rule R7
```

**Tidak ada bypass diam-diam.** Tahap wajib off tanpa cache valid menghentikan run.
Reuse Agent 3 bukan ablation "tanpa Agent 3"; ablation sungguhan memerlukan metode
pembanding dan protokol eksperimen tersendiri. `--until agent3` menyimpan output
sampai Agent 3, bukan mengklaim checker telah dijalankan.

## Logging dan debugging

`events.jsonl` menyimpan satu event JSON per baris dengan UTC timestamp, run ID,
step, event, level dan metadata. Event meliputi source load, line parser (DEBUG),
start/end, durasi, checkpoint, request/response API, token usage, retry, error type,
rule start/result/end, dan fallback report. Console log memakai stderr.

```toml
[logging]
enabled = true
console = true
jsonl = true
level = "INFO"
disabled_steps = ["load", "agent2"]

[stages.check]
enabled = true
log_enabled = true
log_level = "DEBUG"
```

`logging.enabled=false` mematikan seluruh application events, tetapi checkpoint dan
run metadata tetap disimpan sebagai artefak reproduksi. Log tidak memuat prompt utuh,
output LLM mentah, API key atau string error SDK mentah. Pola key/Bearer disamarkan.
Checkpoint berisi output terstruktur; jangan memublikasikannya tanpa tinjauan privasi.

Retries koneksi, timeout, 429, 5xx dan model-output invalid dibatasi `llm.attempts`.
SDK retries dimatikan agar tidak ada retry berlapis. Error autentikasi/model salah
bukan retry tanpa akhir. Error evidence/reference tidak dianggap sukses dan tidak
mengubah dokumen sumber: run berhenti dengan catatan tahap gagal.

Tracing SDK default nonaktif. Untuk mengaktifkannya, gunakan `llm.tracing=true` dan
hapus/ubah global `OPENAI_AGENTS_DISABLE_TRACING=1`; sensitive trace data tetap tidak
diikutkan. Pertimbangkan kebijakan privasi sebelum mengaktifkan tracing eksternal.

## Output dan checkpoint

```text
outputs/<run-id>/
  run.json          # status, config, source/code hashes, git revision, dependencies,
                    # stage durations dan token usage
  events.jsonl
  parse.json
  agent1.json
  validate.json
  agent2.json
  agent3.json
  traceability.json # indeks dua arah accepted realizations + unmatched
  check.json
  aggregate.json
  report.json       # kanonis Python, disimpan SEBELUM Agent 4
  agent4.json       # kandidat narasi bila dipanggil
  narrative.json    # narasi lolos validasi ID/schema
  report.md
```

Checkpoint memiliki schema version, input signature, output SHA-256 dan data.
Reuse memeriksa sumber, dependency upstream, kode/prompt, schema, model/parameter
agent terkait dan versi dependency. Perubahan logging/API key tidak membatalkan
hasil. Hash integritas lokal bukan tanda tangan keamanan: gunakan checkpoint lokal
tepercaya. Run berhenti tidak selalu mempunyai seluruh file di atas.

Canonical `report.json` tidak pernah ditulis ulang Agent 4. Schema narasi tidak
memiliki field status/evidence, dan ID harus cocok dengan temuan kanonis. Pemeriksaan
ini tidak membuktikan kebenaran semua kalimat narasi; narasi tetap diberi label advisory.
Kegagalan Agent 4 memakai `completed_with_report_fallback`, tanpa kehilangan laporan.

## Kontrak semantik dan cakupan R1-R7

IR memakai Boolean predicate facts: activation = kapan obligation berlaku;
preconditions = syarat sebelum aksi; effects = perubahan fakta sesudah aksi.
Exact quote/Pydantic validation memeriksa bentuk dan keterlacakan, bukan menjamin
seluruh makna FR telah diekstraksi. Ketepatan interpretasi LLM tetap dievaluasi terpisah.

| Rule | Implementasi | Batas konservatif |
| --- | --- | --- |
| R1 | Kelompok realisasi pada jalur model | Absence perlu scope lengkap + pencarian; activation bersyarat abstain |
| R2 | Larangan terpetakan, tambahan pada closed-world contract | Pesan teknis/unmatched tidak otomatis salah; larangan bersyarat abstain |
| R3 | Tanggung jawab endpoint terhadap role mapping | Pelanggaran perlu incompatible yang diterima; alias tidak ada bukan bukti salah |
| R4 | Relasi realizes/contradicts yang diverifikasi | Bergantung pada interpretasi semantik Agent 3 |
| R5 | Pembalikan sender/receiver interaksi | Receiver unspecified, anchor multi-atom atau mapping kurang abstain |
| R6 | Precedence per jalur, bukan nomor baris global | Loop, lifeline tak terkait, scope kurang atau group overlap abstain |
| R7 | Guard entailment + efek eksplisit terdahulu terhadap precondition | Fakta unknown abstain; belum ada numeric/SMT solver |

Default `shared_lifeline` memakai closure precedence konservatif pesan yang berbagi
participant di satu jalur. Ini abstraksi interaksi bisnis, bukan semantik occurrence/
weak-sequencing UML lengkap. Arrow asynchronous tidak menjadi bukti precedence.
`explicit_message_order` hanya digunakan bila kontrak penelitian menetapkan urutan
total pada setiap jalur. Semua batas ini perlu dinyatakan dalam metode eksperimen.

Parser mempertahankan loop, tetapi checker tidak mengklaim analisis lintas iterasi.
`max_paths` membatasi eksplorasi; truncation menjadi incomplete, bukan sukses.
Semantik `par` dan konstruk struktural lain belum didukung dan ditolak. Path analysis
bersifat struktural: belum ada pembuktian satisfiability seluruh kombinasi guard.
Gunakan hasil sebagai prototype relatif terhadap IR/kontrak, bukan formal verification.

Satu pasangan bisa memiliki violation dan abstention. Status agregat memprioritaskan
violation yang ditemukan, tanpa menyembunyikan coverage/uncertainty. Coverage adalah
proporsi hasil pemeriksaan yang diputuskan, bukan semantic recall. Deduplikasi hanya
hasil identik; pengelompokan akar masalah lintas kategori belum dilakukan otomatis.
Jangan menghitung setiap kategori sebagai ground-truth issue independen tanpa matching.

## Pemisahan inferensi dan evaluasi

Inference hanya membaca case, source allowlisted, prompt dan checkpoint yang dipilih.
Tidak membaca `ground_truth.csv` atau manifest asli. Preparasi offline:

```powershell
.\.venv\Scripts\python.exe -m thesis_agents.cli prepare
.\.venv\Scripts\python.exe -m thesis_agents.cli run --case config/cases/SD-PD-02.json
```

`prepare` memproyeksikan hanya ID/pasangan/path ke `config/cases/*.json`; label injeksi
dan penjelasannya tidak disalin. Case yang telah dikurasi tidak ditimpa. Contract awal
scope_complete=false, closed_world=false, technical refinement diperbolehkan.
Contract tidak boleh dipakai untuk menyelundupkan jawaban gold.

Baseline, ablation, gold-standard annotation, issue-level matching dan precision/recall
merupakan eksperimen terpisah, belum digantikan oleh unit test atau label injeksi.

## Pengujian dan maintenance

```powershell
.\.venv\Scripts\python.exe -m pytest -q
.\.venv\Scripts\python.exe -m compileall -q src
```

FixtureBackend hanya ada pada test suite dan ditandai di metadata. Tidak ada fallback
production yang mengganti LLM dengan fixture. Test SDK offline mengecek strict schema
ketika SDK terpasang. Pengujian API langsung tetap perlu setelah setup lokal.

Perubahan kontrak IR harus memperbarui schema version di `storage.py`, prompt dan
unit test. Perubahan kode otomatis membatalkan cache. Simpan versi dependency atau
lockfile environment eksperimen setelah instalasi berhasil pada mesin penelitian.

## Acuan integrasi

- [Agents SDK orchestration](https://openai.github.io/openai-agents-python/multi_agent/)
- [Agents SDK runner](https://openai.github.io/openai-agents-python/ref/run/)
- [Agents SDK model settings](https://openai.github.io/openai-agents-python/ref/model_settings/)
- [Agents SDK tracing](https://openai.github.io/openai-agents-python/tracing/)
- [Mermaid sequence syntax](https://mermaid.js.org/syntax/sequenceDiagram.html)

Acuan ini untuk integrasi software, bukan bukti peningkatan akurasi penelitian.
