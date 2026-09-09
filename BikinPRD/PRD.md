# Product Requirements Document — BikinPRD

> Mengubah brief mentah menjadi execution contract yang dapat ditinjau manusia dan dijalankan AI coding agent.

| Metadata | Nilai |
|---|---|
| Versi | 1.0 |
| Tanggal | 8 September 2026 |
| Status | Baseline produk — siap untuk discovery teknis dan breakdown delivery |
| Owner | Product Owner BikinPRD |
| Target rilis | Ditentukan setelah estimasi teknis |
| Dokumen terkait | `BRD.md`; `TECHNICAL-DESIGN.md`; `UX-SPEC.md`; `DELIVERY-BACKLOG.md`; `PRD-SCORING-RUBRIK.md`; `../recon-ngodingpakeai/BREAKDOWN.md` |
| Bahasa produk awal | Bahasa Indonesia |

## 1. Ringkasan eksekutif

BikinPRD adalah platform web untuk freelancer dan agency developer Indonesia yang perlu mengubah brief client menjadi spesifikasi yang dapat dieksekusi AI coding agent. Produk memandu pengguna melengkapi konteks, menghasilkan PRD terstruktur, memeriksa kualitasnya dengan rubrik terukur, menyediakan editor untuk review, lalu mengekspor hasil sebagai Markdown.

BikinPRD bukan sekadar generator dokumen. Produk ini adalah **compiler dari intent manusia menjadi execution contract**: masalah, tujuan, ruang lingkup, requirement, dependency, constraint, risiko, dan acceptance criteria yang dapat diuji.

MVP membuktikan satu hipotesis utama:

> Freelancer atau agency developer Indonesia bersedia menggunakan dan membayar produk yang secara konsisten menghasilkan PRD siap eksekusi tanpa rewrite besar.

MVP sengaja dibatasi pada satu vertical slice: visitor mencoba sekali, membuat PRD, mengklaim draft melalui login, mengedit, mengekspor Markdown, dan membeli satu paket berbayar. Kanban, kolaborasi, halaman PRD publik, export khusus agent, multi-model, konsultasi, komunitas, dan admin lengkap bukan bagian dari MVP.

## 2. Masalah dan peluang

### 2.1 Masalah pengguna

- Brief client biasanya ambigu, tersebar, dan tidak memiliki acceptance criteria.
- AI coding agent menghasilkan implementasi yang tidak konsisten ketika konteks, dependency, constraint, dan non-goal tidak eksplisit.
- Menulis PRD manual membutuhkan waktu dan kemampuan product thinking yang tidak selalu dimiliki developer.
- Generator generik sering menghasilkan dokumen panjang tetapi tidak actionable.

### 2.2 Peluang

BikinPRD berfokus pada kualitas handoff ke coding agent, bahasa dan pembayaran lokal, serta alur dari brief client ke spesifikasi. Sinyal kompetitor hanya dianggap indikasi pasar, bukan bukti product-market fit. Klaim jumlah pengguna kompetitor harus diperlakukan sebagai `claimed/unverified` sampai ada bukti independen.

### 2.3 Positioning

**Untuk** freelancer dan agency developer Indonesia **yang** memakai AI coding agent dan menerima brief client yang belum rapi, **BikinPRD adalah** spec-to-agent execution system **yang** mengubah brief menjadi kontrak implementasi terukur, **berbeda dari** generator dokumen generik yang mengoptimalkan panjang atau jumlah output.

Janji produk: **“Dari brief mentah ke spec siap eksekusi dalam kurang dari 15 menit.”**

## 3. Pengguna sasaran

### 3.1 Primary ICP

Freelancer atau anggota agency kecil di Indonesia yang:

- membangun web/app untuk client;
- menggunakan Claude Code, Codex, Cursor, atau alat sejenis;
- mengerjakan minimal dua brief per bulan;
- menjadi pihak yang mengubah permintaan client menjadi scope teknis;
- memiliki kewenangan membeli software produktivitas murah–menengah.

### 3.2 Persona utama

**Rizky — freelance full-stack developer**

- Input: chat WhatsApp, catatan meeting, dan referensi produk.
- Job-to-be-done: mengubah input tersebut menjadi scope yang bisa disetujui client dan dikerjakan agent.
- Pain: scope creep, requirement hilang, revisi berulang, agent salah asumsi.
- Outcome: PRD dapat diekspor dan dipakai tanpa rewrite besar.

**Andi — owner agency kecil**

- Input: brief dari beberapa client dengan format berbeda.
- Job-to-be-done: menstandarkan discovery dan handoff untuk developer.
- Pain: kualitas spec bergantung pada orang, estimasi meleset, pekerjaan berulang.
- Outcome: format PRD konsisten dan waktu persiapan turun.

PM startup dan mahasiswa adalah secondary audience untuk riset setelah MVP; keduanya tidak menentukan prioritas MVP.

## 4. Outcome, hipotesis, dan metrik

### 4.1 Outcome produk

| ID | Outcome | Ukuran |
|---|---|---|
| O-01 | Pengguna menghasilkan spec yang benar-benar actionable | ≥70% PRD sampel mencapai Execution Readiness Score ≥80/100 |
| O-02 | Pengguna menghemat waktu persiapan | Median waktu dari submit brief sampai export pertama ≤15 menit |
| O-03 | Output digunakan dalam workflow nyata | ≥30% PRD selesai diekspor dalam 7 hari pada cohort aktif |
| O-04 | Pengguna tidak perlu rewrite besar | ≥60% evaluator menyatakan output hanya butuh perubahan minor |
| O-05 | Ada willingness-to-pay | Free-to-paid conversion ≥5% pada cohort eligible di bulan ke-3 |

### 4.2 North-star metric

**Weekly Adopted Execution-Ready PRDs**: jumlah PRD unik per minggu yang:

1. mendapat Execution Readiness Score ≥80;
2. diekspor; dan
3. dikonfirmasi dipakai untuk handoff/client/agent atau lolos review manusia tanpa rewrite besar.

Jumlah user dan jumlah PRD tetap dipantau sebagai health metric, bukan ukuran nilai utama.

### 4.3 Guardrail metrics

- P95 biaya AI per PRD selesai berada di bawah batas unit economics yang disetujui.
- Generation completion rate ≥95%, tidak termasuk pembatalan pengguna.
- Claim draft setelah login berhasil ≥99%.
- Payment webhook diproses tepat satu kali secara efektif ≥99,9%.
- Complaint akibat kehilangan draft <0,5% generation.
- Persentase false-positive abuse challenge <2% pengguna sah yang ditantang.

### 4.4 Definition of success MVP

MVP dinyatakan tervalidasi setelah minimal 50 pengguna ICP menyelesaikan generation dan minimal 20 PRD dinilai memakai rubrik oleh dua reviewer. Keputusan lanjut membutuhkan: median score ≥80, inter-rater agreement ≥0,7, export rate ≥30%, dan minimal lima transaksi organik. Target ini adalah learning gate, bukan forecast pendapatan.

## 5. Rubrik Execution Readiness

Skor dihitung pada versi PRD, bukan pada akun atau project. Sistem menampilkan skor total, alasan, dan tindakan perbaikan. Jumlah feature/task tidak pernah menjadi proxy kualitas.

| Dimensi | Bobot | Kriteria lulus |
|---|---:|---|
| Problem, user, dan desired outcome | 10 | Masalah, pengguna, dan perubahan yang diharapkan eksplisit |
| Scope dan non-goals | 10 | In-scope, out-of-scope, dan batas release tidak ambigu |
| Functional requirements | 15 | Requirement bernomor, spesifik, dan dapat ditelusuri ke kebutuhan |
| Testable acceptance criteria | 20 | Tiap P0 memiliki kondisi sukses/gagal yang dapat diverifikasi |
| Context dan likely affected areas | 10 | Domain/sistem/area yang kemungkinan terdampak disebut tanpa mengarang file |
| Dependencies dan sequencing | 10 | Dependency internal/eksternal dan urutan kritis terlihat |
| Constraints dan non-functional requirements | 10 | Security, performance, accessibility, data, dan batas teknis relevan |
| Edge cases dan failure states | 10 | Empty, invalid, timeout, retry, authorization, dan recovery dibahas |
| Risks, assumptions, dan open decisions | 5 | Fakta dipisahkan dari asumsi dan keputusan yang belum dibuat |

**Status skor:**

- 90–100: Ready — dapat dipakai setelah review singkat.
- 80–89: Ready with minor edits — memenuhi promise produk.
- 60–79: Needs review — export boleh, tetapi warning ditampilkan.
- <60: Incomplete — sistem meminta input tambahan sebelum menyebut output siap eksekusi.

Hard gate: skor tidak boleh ≥80 jika ada P0 tanpa acceptance criteria, keputusan blocking belum terjawab, atau scope/non-goals kosong. Evaluator AI memberi rekomendasi; pengguna tetap pemilik keputusan. Pada masa beta, sampel dinilai manusia untuk mengkalibrasi prompt dan mencegah score gaming.

## 6. Prinsip produk

1. **Quality over volume:** lebih sedikit requirement yang teruji lebih bernilai daripada task generik yang banyak.
2. **Human approval:** AI mengusulkan; pengguna mengedit dan menyetujui.
3. **No lost work:** draft disimpan sebelum generation dan dapat dipulihkan.
4. **Private by default:** tidak ada publikasi otomatis atau penggunaan konten untuk training tanpa consent terpisah.
5. **One source of truth:** scope, entitlement, roadmap, dan release gate berasal dari tabel canonical di §8.
6. **Provider-neutral domain:** model/provider dapat diganti tanpa mengubah struktur data produk.
7. **Progressive friction:** abuse control meningkat berdasarkan risiko, bukan fingerprint permanen.

## 7. User journeys MVP

### J-01 — Visitor membuat trial dan mengklaim draft

1. Visitor membuka landing dan memilih “Coba Gratis”.
2. Server membuat anonymous session bertanda tangan dengan expiry 24 jam.
3. Visitor memasukkan brief dan menjawab pertanyaan klarifikasi minimum.
4. Sistem menyimpan draft, mengecek abuse/rate limit, lalu memulai generation.
5. Progress tampil; hasil parsial yang tervalidasi disimpan per checkpoint.
6. Visitor melihat hasil dan score, tetapi harus login untuk edit penuh/export.
7. Visitor login dengan Google.
8. Dalam transaksi database, draft dipindahkan ke user jika claim token valid dan belum dipakai.
9. Jika akun sudah memiliki draft serupa, sistem tetap menyimpan keduanya dan meminta pengguna memilih kemudian; tidak overwrite otomatis.

Acceptance:

- Refresh/reconnect tidak menghilangkan draft atau membuat generation ganda.
- Claim token single-use, expired setelah 24 jam, terikat ke anonymous session, dan dirotasi setelah login.
- Race login atau double-click menghasilkan tepat satu ownership transfer.
- Anonymous draft yang tidak diklaim dihapus maksimal 7 hari setelah expiry.
- IP bersama tidak otomatis menyebabkan ban; CAPTCHA hanya muncul saat risk threshold tercapai.

### J-02 — User membuat, memperbaiki, dan mengekspor PRD

1. User memasukkan brief atau memakai satu template dasar.
2. Sistem menampilkan pertanyaan untuk informasi blocking yang belum ada.
3. User menyetujui input dan memulai generation.
4. Sistem menghasilkan struktur PRD dan menjalankan quality evaluation.
5. User melihat score per dimensi, memperbaiki konten, dan autosave.
6. User mengekspor versi terkini sebagai Markdown.

Acceptance:

- Export selalu berasal dari version revision yang terlihat pengguna.
- Warning muncul jika score <80; export tetap diizinkan agar pengguna tidak terkunci.
- Regenerate section tidak menimpa edit manual tanpa konfirmasi diff.

### J-03 — User membeli paket

1. User mencapai entitlement limit atau membuka pricing.
2. User memilih Starter bulanan dan membuat checkout.
3. Backend membuat order unik dan Midtrans Snap token.
4. Midtrans mengirim webhook; backend memverifikasi signature dan mengambil status authoritative bila perlu.
5. Payment event dicatat idempotent dan entitlement user diaktifkan.
6. UI memperoleh status terbaru melalui polling/revalidation.

Acceptance:

- Callback browser tidak pernah mengaktifkan entitlement.
- Webhook duplicate/out-of-order aman dan tidak menggandakan periode/credit.
- Settlement setelah browser ditutup tetap mengaktifkan paket.
- Pending, deny, cancel, expire, refund, chargeback, dan reconciliation memiliki state eksplisit.

## 8. Scope canonical dan roadmap fitur

Milestone: **M0 Discovery**, **M1 Private MVP**, **M2 Public Beta**, **M3 Growth**, **Future**. Hanya tabel ini yang menentukan milestone fitur.

| ID | Capability | Priority | Milestone | Dependency | Release gate |
|---|---|---|---|---|---|
| F-01 | Landing, pricing, legal | P0 | M1 | Brand/copy minimum | Core pages usable dan klaim tidak menyesatkan |
| F-02 | Anonymous session dan draft claim | P0 | M1 | Data lifecycle, auth | J-01 lulus termasuk race/idempotency |
| F-03 | Google authentication dan account | P0 | M1 | OAuth config | Ownership dan account deletion lulus |
| F-04 | Guided brief intake | P0 | M1 | Prompt schema | Blocking questions tervalidasi |
| F-05 | Generation job dan recovery | P0 | M1 | AI adapter, usage reservation | Completion ≥95%; retry/cancel aman |
| F-06 | Execution readiness evaluation | P0 | M1 | Rubric v1 | Kalibrasi 20 PRD; agreement ≥0,7 |
| F-07 | Owner-only document editor | P0 | M1 | Revision control | Autosave/recovery/export consistency lulus |
| F-08 | Markdown export | P0 | M1 | Export template version | Golden-file tests lulus |
| F-09 | Entitlement, usage ledger, rate limit | P0 | M1 | Plan catalogue | Tidak ada double charge usage |
| F-10 | Starter checkout Midtrans | P0 | M1 | Payment events | Semua payment states dan idempotency lulus |
| F-11 | Minimal support operations | P0 | M1 | Audit log | Operator dapat cari user/job/payment dan retry aman |
| F-12 | Template library | P1 | M2 | Template versioning | ≥3 template tervalidasi ICP |
| F-13 | Agent-specific export | P1 | M2 | Compatibility matrix | Fixture per target dan version note lulus |
| F-14 | Public share page | P1 | M2 | Consent/moderation/SEO | Private default; noindex quality gate |
| F-15 | Version history dan diff | P1 | M2 | Revisions | Restore non-destructive lulus |
| F-16 | API token/integration | P2 | M3 | Stable API, scopes | Rotation, revocation, audit lulus |
| F-17 | AI-assisted change proposal | P2 | M3 | Diff/usage ledger | Apply/reject per change lulus |
| F-18 | Collaboration/client review | P2 | M3 | RBAC, versioning | Permission matrix dan conflict handling lulus |
| F-19 | Add-on/voucher/referral | P2 | M3 | Ledger/payment catalogue | Accounting invariant lulus |
| F-20 | Community dan consultation booking | P3 | Future | Validated demand/operations | Separate business case disetujui |
| F-21 | Tools ranking/marketplace/mobile app | P3 | Future | Growth evidence | Separate PRD disetujui |

### 8.1 Explicitly out of MVP

Kanban task management, drag-and-drop, collaboration, comments, public SEO pages, agent-specific files, model selector, chat planning, version diff UI, API/CLI, vouchers, referrals, live vanity counters, consulting booking, template marketplace, tools ranking, native mobile app, and multi-language.

Empat pilar bisnis boleh disebut secara ringan sebagai arah produk, tetapi landing MVP memiliki satu CTA utama ke pembuatan PRD. Capability yang belum tersedia tidak boleh ditampilkan seolah sudah live.

## 9. Functional requirements MVP

### F-01 — Landing, pricing, dan legal

- Menjelaskan ICP, input, output, contoh hasil, batas AI, harga, dan CTA trial.
- Menyediakan Terms, Privacy, Refund Policy, dan kanal support.
- Tidak menampilkan counter atau klaim kualitas yang belum dapat dibuktikan.
- Responsive pada viewport 360 px dan dapat digunakan dengan keyboard.

### F-02/F-03 — Identity dan ownership

- Anonymous session memakai opaque ID random dalam cookie `HttpOnly`, `Secure`, `SameSite=Lax`; database hanya menyimpan hash token.
- Login Google menautkan email terverifikasi ke satu user.
- Semua mutasi memvalidasi ownership server-side.
- User dapat meminta penghapusan akun; job/payment record yang wajib dipertahankan dianonimkan sesuai retention policy.
- MVP owner-only. Tidak ada konsep collaborator di authorization.

### F-04 — Guided brief intake

- Input mendukung plain text maksimum 20.000 karakter.
- Minimum: jenis produk, pengguna sasaran, masalah, desired outcome, dan batas scope.
- Sistem dapat mengajukan maksimum lima pertanyaan blocking per ronde.
- Pengguna dapat menjawab “belum tahu”; output menandainya sebagai assumption/open decision, bukan mengarang fakta.
- Input kosong, terlalu pendek, berbahaya, atau tidak relevan menghasilkan error actionable.

### F-05 — Generation lifecycle

State machine: `draft → queued → running → evaluating → completed`; terminal state: `failed`, `cancelled`. Transisi divalidasi server-side.

- Create job menerima `Idempotency-Key` dan mengembalikan job ID.
- Kuota di-reserve sebelum job dan di-settle berdasarkan kebijakan usage setelah terminal state.
- Progress dikirim melalui SSE; status dapat diambil lewat endpoint biasa untuk reconnect.
- Checkpoint menyimpan output terstruktur yang lolos schema validation.
- Retry membuat attempt baru di job yang sama dan tidak menggandakan debit.
- Provider output divalidasi terhadap schema; prose mentah tidak ditulis langsung ke domain tables.
- Timeout, provider unavailable, malformed output, moderation reject, dan internal error mempunyai kode berbeda.

### F-06 — Quality evaluation

- Evaluator mengembalikan skor per dimensi, evidence, missing items, dan recommendations.
- Evaluator menyimpan rubric version, prompt version, provider/model, dan timestamp.
- Score diperbarui setelah perubahan konten dengan debounce; perubahan manual tidak diblokir.
- Admin/operator tidak dapat diam-diam mengubah score historis; recalculation membuat evaluation baru.

### F-07 — Editor

- Mengedit section PRD: summary, problem, users, goals/non-goals, scope, requirements, NFR, dependencies, risks, assumptions, open decisions.
- Autosave setelah 1,5 detik idle dan save manual.
- Setiap PATCH memakai revision number; mismatch menghasilkan `409 REVISION_CONFLICT`, bukan last-write-wins diam-diam.
- UI menampilkan `saving`, `saved`, `offline`, dan `failed` dengan retry.
- Delete PRD memakai soft-delete dan undo 7 hari.
- Regeneration section menghasilkan preview diff yang harus disetujui.

### F-08 — Markdown export

- Export mencakup metadata, seluruh section, readiness score/version, unresolved decisions, dan disclaimer review manusia.
- Nama file disanitasi; encoding UTF-8; line ending LF.
- Export dibuat dari immutable revision dan mencatat template version.
- Golden fixtures memastikan heading, escaping, list, table, dan Unicode konsisten.

### F-09 — Entitlement dan usage

Plan MVP:

| Entitlement | Trial | Free | Starter |
|---|---:|---:|---:|
| Generate | 1 total per anonymous session/risk policy | 3 per billing month | 15 per billing month |
| Edit/export Markdown | Setelah login | Ya | Ya |
| Draft aktif | 1 | 3 | 50 |
| Support | Self-service | Self-service | Email |

Harga baseline Starter: **Rp49.000/bulan**, diuji dan dapat diubah melalui plan catalogue tanpa migrasi data. Tidak ada “unlimited” pada MVP. Limit final wajib diuji terhadap biaya nyata sebelum public beta.

- Entitlement berasal dari plan version, bukan string tier tersebar di code.
- Usage ledger bersifat append-only: `reserve`, `commit`, `release`, `adjustment` dengan reference unik.
- Balance/usage dihitung dari ledger; adjustment manual memerlukan actor, reason, dan audit event.
- Boundary periode menggunakan timestamp UTC dan ditampilkan di timezone user.

### F-10 — Payment

- Order ID unik dan idempotency key mencegah checkout ganda.
- Raw webhook tersimpan terenkripsi/terproteksi sesuai kebutuhan audit, dengan gateway event identity.
- Signature diverifikasi constant-time; nominal, currency, merchant, dan order ownership dicocokkan.
- State transaksi: `created`, `pending`, `paid`, `denied`, `cancelled`, `expired`, `refunded`, `chargeback`.
- Subscription/entitlement mutation dilakukan dalam transaksi yang sama dengan pencatatan event efektif.
- Reconciliation job memeriksa payment pending/stale dan mismatch.
- Refund dan chargeback tidak menghapus histori; entitlement mengikuti kebijakan refund yang dipublikasikan.

### F-11 — Minimal support operations

MVP tidak memerlukan admin suite penuh. Operator yang berizin dapat:

- mencari user, PRD, generation job, usage entry, dan payment berdasarkan ID;
- melihat timeline event dan error yang sudah di-redact;
- retry reconciliation atau release reservation secara idempotent;
- memberi adjustment dengan reason;
- melihat audit log.

Tidak ada impersonation atau edit konten user pada MVP.

## 10. Information architecture

| Route | Akses | Milestone | Tujuan |
|---|---|---|---|
| `/` | Publik | M1 | Positioning dan CTA |
| `/pricing` | Publik | M1 | Plan catalogue dan FAQ |
| `/privacy`, `/terms`, `/refund` | Publik | M1 | Legal |
| `/new` | Publik/session | M1 | Trial dan intake |
| `/sign-in` | Publik | M1 | Login dan claim continuation |
| `/dashboard` | User | M1 | Daftar PRD, usage, CTA |
| `/plans/{id}` | Owner | M1 | Editor dan score |
| `/plans/{id}/export` | Owner | M1 | Export flow |
| `/settings` | User | M1 | Account, plan, delete account |
| `/transactions` | User | M1 | Payment history |
| `/templates` | User | M2 | Template library |
| `/p/{slug}` | Publik | M2 | Explicitly published PRD |
| `/ops` | Operator | M1 | Support minimum |

## 11. Domain model

Semua ID berupa UUID/ULID; timestamp disimpan UTC; record penting memiliki `createdAt` dan `updatedAt`. Detail tipe/migration ditentukan technical design, tetapi invariant berikut wajib dipertahankan.

```text
users
  ├─ identities / sessions
  ├─ anonymous_claims
  ├─ projects ──< document_revisions ──< readiness_evaluations
  │              └─< export_artifacts
  ├─ generation_jobs ──< generation_attempts ──< generation_checkpoints
  ├─ usage_ledger
  ├─ subscriptions
  ├─ payment_orders ──< payment_events
  └─ audit_events

plan_catalogue ──< plan_versions ──< entitlement_rules
prompt_templates ──< prompt_versions
export_templates ──< export_template_versions
```

### 11.1 Core invariants

- Satu project memiliki tepat satu owner pada M1.
- Revision immutable; project menunjuk current revision.
- Satu anonymous claim hanya dapat dikonsumsi sekali.
- Satu idempotency key hanya dapat menghasilkan satu logical generation/order per owner dan operation.
- Satu gateway event hanya memberi efek bisnis sekali.
- Ledger entry tidak diedit/dihapus; koreksi memakai adjustment.
- Payment event tidak menjadi entitlement sebelum validasi selesai.
- Provider/model/prompt/rubric/export version tercatat untuk reproducibility.
- Sensitive tokens disimpan dalam bentuk hash; payload/log tidak menyimpan secret.

## 12. API contract MVP

Konvensi:

- Base path `/api/v1`; JSON UTF-8 kecuali SSE/export.
- Auth melalui session cookie; anonymous endpoint memakai anonymous cookie.
- Mutasi mendukung `Idempotency-Key` bila dapat diulang.
- Error: `{ "error": { "code": "STABLE_CODE", "message": "safe message", "requestId": "...", "details": {} } }`.
- List memakai cursor pagination. Semua request memiliki correlation/request ID.
- `POST` sukses create: 201; accepted job: 202; no content: 204; validation: 422; conflict: 409; rate limit: 429.

| Method | Endpoint | Auth | Fungsi |
|---|---|---|---|
| POST | `/anonymous-sessions` | Publik | Membuat anonymous session |
| POST | `/auth/claim` | User + claim token | Claim draft idempotent |
| POST | `/projects` | Anonymous/User | Membuat draft |
| GET | `/projects` | User | List milik user |
| GET | `/projects/{id}` | Owner | Mengambil current revision |
| PATCH | `/projects/{id}` | Owner + revision | Autosave/edit |
| DELETE | `/projects/{id}` | Owner | Soft-delete |
| POST | `/projects/{id}/generation-jobs` | Owner/session | Mulai generation |
| GET | `/generation-jobs/{id}` | Owner/session | Status/reconnect |
| GET | `/generation-jobs/{id}/events` | Owner/session | SSE progress |
| POST | `/generation-jobs/{id}/cancel` | Owner/session | Cancel idempotent |
| POST | `/generation-jobs/{id}/retry` | Owner/session | Retry attempt |
| POST | `/projects/{id}/evaluate` | Owner | Evaluate revision |
| GET | `/projects/{id}/exports/markdown` | Owner | Export revision |
| GET | `/me/entitlements` | User | Limit dan usage |
| GET | `/plans` | Publik | Plan catalogue aktif |
| POST | `/checkout/orders` | User | Membuat order Midtrans |
| POST | `/webhooks/midtrans` | Signature | Menerima event |
| GET | `/payments` | User | Payment history |
| DELETE | `/me` | User + reauth | Request account deletion |

SSE hanya membawa event reference/progress aman; client mengambil state authoritative melalui GET. Webhook dan ops endpoint memiliki rate limit serta audit terpisah.

## 13. Non-functional requirements

| Area | Requirement / SLO |
|---|---|
| Availability | 99,5% bulanan untuk authenticated app, maintenance terjadwal dikecualikan |
| Web performance | P75 LCP ≤2,5 s, INP ≤200 ms, CLS ≤0,1 pada halaman publik |
| API performance | P95 read ≤500 ms dan mutation non-AI ≤1 s pada beban target |
| Generation | P95 first progress ≤10 s; hard timeout dan heartbeat terdefinisi |
| Durability | Tidak kehilangan revision acknowledged; DB backup harian, retensi 30 hari |
| Recovery | RPO ≤24 jam, RTO ≤4 jam; restore drill sebelum public beta dan tiap kuartal |
| Capacity | Load test pada 100 concurrent active generations atau 2× proyeksi puncak, mana lebih tinggi |
| Accessibility | WCAG 2.2 AA untuk flow P0; keyboard, focus, label, error announcement |
| Compatibility | Dua versi stabil terbaru Chrome, Edge, Firefox, Safari; viewport ≥360 px |
| Localization | UI Bahasa Indonesia; data/time/currency locale-aware; storage UTC |
| Data lifecycle | Anonymous expiry 24 jam; cleanup ≤7 hari; retention lain didokumentasikan |
| Observability | Structured logs, metrics, traces/correlation ID; secret dan content sensitif di-redact |

## 14. Security, privacy, dan compliance

- Threat model sebelum public beta mencakup account takeover, IDOR, prompt injection, XSS dari output, quota abuse, webhook forgery, dan data leakage antar user.
- Authorization diuji per object dan server-side; ID tidak dianggap authorization.
- CSRF protection untuk mutasi cookie-authenticated; CSP ketat; output Markdown/HTML disanitasi sesuai context.
- OAuth/session cookie memakai `HttpOnly`, `Secure`, `SameSite=Lax`; session rotation setelah login dan privilege change.
- Secret hanya di secret manager/environment; rotasi dan least privilege diterapkan.
- Rate limit berlapis per session/user/IP/risk signal. Tidak ada device fingerprinting persisten pada MVP.
- CAPTCHA adaptif hanya setelah risk threshold; shared IP bukan bukti pelanggaran.
- User content tidak dipakai training internal/provider di luar kebutuhan inference tanpa opt-in eksplisit dan perjanjian provider yang sesuai.
- Privacy notice menjelaskan data, tujuan, provider/subprocessor, lokasi/transfer, retention, serta hak akses/koreksi/hapus.
- Account deletion memiliki SLA dan pengecualian legal yang terdokumentasi.
- Payment card data tidak melewati server BikinPRD; gunakan hosted Midtrans flow.
- Dependency scanning, secret scanning, backup encryption, dan audit log wajib sebelum public beta.
- Review legal UU PDP, Terms, Privacy, Refund, serta pajak dilakukan oleh pihak kompeten; PRD ini bukan nasihat hukum.

## 15. AI quality dan safety

- Prompt memperlakukan brief sebagai data tidak tepercaya; instruksi di dalam brief tidak boleh mengubah system policy.
- Provider adapter menerima schema dan timeout standar serta menghasilkan usage/cost metadata normalized.
- Model tidak boleh mengarang stack, file, deadline, budget, atau keputusan bisnis; ketidakpastian masuk assumptions/open decisions.
- PII/secrets scanner memberi warning sebelum request jika input tampak memuat credential.
- Moderation hanya membatasi konten sesuai kebijakan yang dipublikasikan; error menjelaskan langkah pengguna.
- Evaluation set versi awal minimal 20 brief representatif ICP, mencakup brief bagus, ambigu, kontradiktif, dan adversarial.
- Setiap perubahan model/prompt/rubric menjalankan regression evaluation sebelum rollout.
- Rollout provider/prompt baru dapat di-canary dan di-rollback tanpa migrasi dokumen.

## 16. Analytics dan experiment design

Event server-side menjadi sumber kebenaran untuk generation, export, usage, dan payment. Event tidak membawa isi PRD atau PII ke analytics pihak ketiga.

| Event | Properti minimum |
|---|---|
| `trial_started` | anonymousSessionIdHash, source, experiment |
| `brief_submitted` | projectId, inputBand, missingFieldCount |
| `generation_started/completed/failed/cancelled` | jobId, attempt, provider, model, latency, errorCode, cost |
| `readiness_evaluated` | projectId, revision, rubricVersion, totalScore, dimensionScores |
| `draft_claimed` | claimLatency, success/errorCode |
| `editor_saved/conflicted` | projectId, revision, latency |
| `prd_exported` | projectId, revision, score, format, templateVersion |
| `checkout_started` | orderId, planVersion, amount |
| `payment_state_changed` | orderId, from, to, gatewayEventId |
| `account_deleted` | deletionMode, latencyBand |

Funnel utama: landing → trial start → brief submit → generation complete → login/claim → score ≥80 → export → paid. Setiap eksperimen memiliki hypothesis, primary metric, guardrail, sample rule, dan stop condition sebelum dijalankan.

## 17. Observability dan operations

- Dashboard: availability, latency, job state/age, provider error, token/cost, ledger mismatch, webhook lag, payment mismatch, claim failure, and export errors.
- Alert: generation failure spike, stuck jobs, cost anomaly, duplicate-effect invariant, payment backlog, backup failure, dan cross-user authorization error.
- Runbook wajib: provider outage, stuck job, lost SSE connection, quota dispute, duplicate webhook, pending payment, refund/chargeback, suspected breach, backup restore.
- Logs memakai correlation ID dan retention terbatas; brief/output tidak masuk log default.
- Rekonsiliasi harian memeriksa job vs usage ledger dan payment vs entitlement.

## 18. Delivery plan dan release gates

### M0 — Discovery dan calibration

- Wawancara minimal 10 pengguna primary ICP.
- Uji prototype intake/editor/export dengan minimal lima pengguna.
- Kumpulkan 20 brief yang dianonimkan dan buat evaluation set.
- Finalisasi plan economics, privacy/data map, dan technical design.

**Gate:** problem/value tervalidasi, rubric agreement ≥0,7, unit economics memiliki batas biaya, dan tidak ada open decision blocking.

### M1 — Private MVP

Mencakup F-01 sampai F-11. Akses invite-only.

**Gate:**

- Semua acceptance P0 dan critical-path integration test lulus.
- Journey visitor → claim → edit → export → pay lulus end-to-end.
- Threat model, backup restore, accessibility audit, dan operational runbook selesai.
- Tidak ada severity critical/high terbuka; medium memiliki owner dan deadline.
- 20 PRD regression set memenuhi target quality.

### M2 — Public Beta

Mencakup capability P1 yang dipilih berdasarkan data; bukan otomatis semua F-12–F-15.

**Gate:** MVP success criteria §4.4 tercapai, cost guardrail aman selama empat minggu, support load terkendali, serta privacy/legal review selesai.

### M3/Future — Growth

Capability P2/P3 membutuhkan mini-PRD, evidence masalah, owner, metric, cost, dependency, dan security review sendiri. Roadmap bersifat outcome-based; tanggal baru dibuat setelah estimasi engineering.

## 19. Test strategy dan Definition of Done

### 19.1 Test layers

- Unit: rubric calculation, state machines, entitlement, ledger, signature, sanitizer, export formatter.
- Contract: AI provider adapter, Midtrans payload/webhook, OAuth, SSE event schema.
- Integration: claim transaction, job/checkpoint/retry, revision conflict, usage settlement, payment-to-entitlement.
- End-to-end: J-01, J-02, J-03 termasuk failure/recovery paths.
- Security: IDOR matrix, CSRF, XSS, webhook replay, rate limit, secret leakage.
- Non-functional: load, accessibility, backup restore, provider outage drill.

### 19.2 Definition of Done per requirement

Requirement selesai hanya jika:

1. acceptance criteria dan failure states teruji;
2. authorization, privacy, analytics, dan accessibility impact ditangani;
3. observability dan runbook ditambahkan bila operasional;
4. migration backward/rollback aman bila ada perubahan data;
5. dokumentasi user/operator diperbarui;
6. product owner menerima hasil terhadap requirement ID.

## 20. Risks, assumptions, dan dependencies

| ID | Tipe | Pernyataan | Validasi/mitigasi | Owner |
|---|---|---|---|---|
| R-01 | Risiko | Output terlihat lengkap tetapi tidak actionable | Rubric hard gate, human calibration, regression set | Product/AI |
| R-02 | Risiko | Biaya generation melebihi revenue | Reservation ledger, model routing, hard budget, alert | Engineering/Finance |
| R-03 | Risiko | Anonymous trial disalahgunakan | Signed session, IP/risk rate limit, adaptive CAPTCHA | Security |
| R-04 | Risiko | Draft hilang saat login/reconnect | Claim transaction, checkpoint, idempotency tests | Engineering |
| R-05 | Risiko | Payment/entitlement mismatch | Event idempotency, reconciliation, audit ledger | Engineering/Finance |
| R-06 | Risiko | Brief client membocorkan data sensitif | Private default, redaction warning, retention, provider terms | Privacy |
| A-01 | Asumsi | ICP mengerjakan ≥2 brief/bulan dan merasa pain cukup besar | 10 interview + prototype test | Product |
| A-02 | Asumsi | Score ≥80 berkorelasi dengan handoff lebih baik | Blind human review dan adoption tracking | Product/AI |
| A-03 | Asumsi | Rp49.000 menghasilkan willingness-to-pay dan margin aman | Price test + actual COGS | Product/Finance |
| D-01 | Dependency | Google OAuth production approval/config | Checklist launch | Engineering |
| D-02 | Dependency | Midtrans production account dan webhook | Sandbox + production verification | Finance/Engineering |
| D-03 | Dependency | AI provider DPA, limits, dan reliability | Vendor review + fallback plan | Engineering/Privacy |

## 21. Open decisions

Open decision tidak boleh disamarkan sebagai requirement. Item blocking harus selesai sebelum gate terkait.

| ID | Keputusan | Default kerja | Deadline/gate |
|---|---|---|---|
| OD-01 | Nama/brand final | BikinPRD | Sebelum visual production |
| OD-02 | Harga dan limit Starter final | Rp49.000; 15 generation/bulan | Sebelum payment production |
| OD-03 | Policy debit job gagal/cancel | Release jika belum completed; log actual cost internal | Sebelum F-09 build |
| OD-04 | Provider/model baseline | Satu provider + satu fallback, disembunyikan dari user | Sebelum AI adapter build |
| OD-05 | Retention user content setelah delete | Hapus/anonymize sesuai kewajiban legal | Sebelum private MVP |
| OD-06 | Refund window dan entitlement effect | Mengikuti policy tertulis dan gateway capability | Sebelum payment production |
| OD-07 | Stack/deployment final | Modular monolith TypeScript + PostgreSQL + worker/queue diusulkan di `TECHNICAL-DESIGN.md`; menunggu spike dan approval | Sebelum implementation kickoff |

## 22. Traceability matrix MVP

| Outcome | Journey | Capability | Evidence |
|---|---|---|---|
| O-01, O-04 | J-02 | F-04–F-08 | Rubric evaluation + reviewer result |
| O-02 | J-01, J-02 | F-02–F-08 | Funnel timestamp |
| O-03 | J-02 | F-07, F-08 | Revision export event + adoption prompt |
| O-05 | J-03 | F-09, F-10 | Eligible cohort + paid transaction |
| Guardrail cost | Semua generation | F-05, F-09 | Provider usage + ledger reconciliation |
| Guardrail durability | J-01, J-02 | F-02, F-05, F-07 | Recovery and conflict tests |

## 23. Glosarium

- **Execution contract:** spesifikasi yang cukup eksplisit untuk disetujui manusia dan dijalankan coding agent.
- **Execution Readiness Score:** evaluasi ter-versioning terhadap rubrik §5; bukan jaminan kebenaran implementasi.
- **Revision:** snapshot immutable dari isi PRD pada suatu titik.
- **Generation job/attempt:** pekerjaan logis dan percobaan provider untuk menghasilkan PRD.
- **Entitlement:** hak fitur/limit berdasarkan plan version aktif.
- **Usage ledger:** catatan append-only untuk reservation, commit, release, dan adjustment pemakaian.
- **Claim:** pemindahan ownership draft anonim ke akun terautentikasi.
- **Idempotency:** request/event berulang menghasilkan satu efek bisnis.
- **P0/P1/P2/P3:** must-have milestone saat ini / next / later / future bet.

## 24. Approval

Dokumen ini menjadi baseline setelah disetujui Product Owner, Engineering Lead, Design Lead, dan pihak yang bertanggung jawab atas privacy/payment. Perubahan scope setelah approval dicatat dalam decision log dengan alasan, dampak outcome, milestone, dan approver. BRD tetap menjelaskan strategi bisnis; jika BRD dan PRD bertentangan pada detail produk, perubahan harus direkonsiliasi secara eksplisit—jangan menjalankan dua sumber kebenaran.
