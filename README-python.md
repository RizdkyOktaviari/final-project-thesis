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

### AgentRouter (401 Unauthorized)

AgentRouter adalah gateway pihak ketiga, bukan API OpenAI langsung. Jika key berasal
AgentRouter, set **ketiganya** di `.env`:

```dotenv
OPENAI_API_KEY=key_agentrouter_anda
OPENAI_BASE_URL=https://co.agentrouter.org/v1
OPENAI_API_MODE=chat_completions
OPENAI_MODEL=gpt-5.5
```

Pilih model ID yang tersedia di akun Anda. Model `gpt-5.5` hanya contoh dari
panduan AgentRouter. Bila memakai key OpenAI resmi, hilangkan `OPENAI_BASE_URL`
dan `OPENAI_API_MODE` agar menggunakan Responses API. `OPENAI_API_MODE` mengatasi
gateway yang tidak menyediakan endpoint `/responses`; jangan mencampur protokol
Anthropic tanpa `/v1` dengan OpenAI-compatible `/v1`.

PowerShell dapat mewarisi environment variable lama yang mengalahkan `.env`.
Pastikan `OPENAI_API_KEY` aktif sesuai provider, tanpa mencetak key ke terminal.
Lihat [diagnostik dan tes koneksi](docs/implementation/README.md#agentrouter-dan-error-401).
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


## AgentRouter via Claude Code CLI (tested connection path)

The previous Python OpenAI Agents SDK integration can be rejected by AgentRouter as an
unsupported client (HTTP 401). A new optional `claude_cli` backend uses the installed
Claude Code CLI as a supported client. Python still controls all four agent stages,
Mermaid parsing, IR validation, R1–R7 rules, checkpointing and reporting.

1. Install Claude Code CLI, verify `claude --version`, and first verify your
   AgentRouter account supports the selected model. Do not commit credentials.
2. In your local `.env` set:

```dotenv
THESIS_LLM_BACKEND=claude_cli
AGENT_ROUTER_TOKEN=your_private_token
AGENT_ROUTER_BASE_URL=https://agentrouter.org
AGENT_ROUTER_MODEL=gpt-5.6-sol
```

3. Run the existing orchestration with the new backend:

```powershell
.\.venv\Scripts\python.exe -m pytest -q
.\.venv\Scripts\python.exe -m thesis_agents.cli run --case examples/case.json --until agent1
.\.venv\Scripts\python.exe -m thesis_agents.cli run --case config/case-pd-02.json
```

Each agent is a separate CLI call with `--tools ""`, a stage-specific system
prompt, input JSON sent through stdin and JSON/Pydantic validation. The adapter
keeps the input out of command-line arguments and does not log API keys or raw
provider output. Stage retries are bounded; authorization failures fail fast.

**Important:** The previously successful `Reply with exactly OK` check proves
connectivity only. It does not verify that all models support schema-sized outputs
or that the full four-agent thesis pipeline has succeeded. Run an Agent 1 case
first and inspect `outputs/<run-id>/` before running the full pipeline. This is
Claude Code CLI orchestration, not native OpenAI Agents SDK compatibility.
