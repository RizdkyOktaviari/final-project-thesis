# Catatan validasi implementasi awal

Validasi lokal pada 31 Oktober 2026:

- Python 3.13.5.
- `python -m pytest -q`: **55 passed, 1 skipped**.
- `python -m compileall -q src`: berhasil.
- CLI `run --case examples/case.json --until parse`: berhasil tanpa API.

Test mencakup nested branch, implicit participant, malformed/unsupported syntax,
path limit, evidence palsu, scope/ID invalid, rejected mapping, ketujuh rule,
ketidakpastian, checkpoint reuse/invalidation/integrity, logging on/off/redaction,
input allowlist, proyeksi manifest tanpa label, dan fallback Agent 4.

Satu test dilewati karena `openai-agents` tidak terpasang di lingkungan offline.
Instalasi dependency tidak dapat diselesaikan karena lingkungan tidak memiliki
akses jaringan paket. API OpenAI langsung belum diuji dan API key pengguna tidak
tersedia/digunakan. Jalankan kembali `pip install -e ".[dev]"`, `pytest`, lalu satu
case setelah menyiapkan `.env` di mesin penelitian.

Hasil ini merupakan validasi software dengan fixture, BUKAN hasil eksperimen
precision/recall atau klaim bahwa interpretasi LLM sudah benar.
