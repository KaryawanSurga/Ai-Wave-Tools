# Breakdown — ngodingpakeai.com
Tanggal riset: 17 Agustus 2026
Metode: curl recon + mining JS bundle (Vite SPA) + browser live + API probing

---
## 1. Ringkasan Eksekutif

**Ngoding Pake AI** = platform Indonesia untuk membuat PRD (Product Requirements
Document) yang siap dipakai AI coding agent, plus komunitas AI coding terbesar di
Indonesia (klaim mereka). Dibuat oleh **Raf Dev** (Rafiul, iultech.com) — YouTuber
AI coding ~31,6K subscriber. Monetisasi: subscription bulanan (Rp), coaching,
consulting.

Fakta cepat (live stats dari /api/stats):
- Total user: 33.766
- Total PRD dibuat: 17.140
- Produk: PRD generator berbasis AI + komunitas Discord + coaching + ranking tools

---

## 2. Stack Teknis

### Frontend (terkonfirmasi dari bundle)
- **React SPA** dibangun dengan **Vite** (pattern `/assets/index-*.js`, modulepreload)
- **React Router** (route map lengkap berhasil diekstrak — lihat bagian 3)
- **Tailwind CSS v4** + design token ala shadcn/ui (oklch, `--background`, `--card`,
  `--border`, `--accent`, `--chart-1..5`) — dark mode default + light mode toggle
- Font: **DM Sans** (Google Fonts)
- Komponen UI: **Radix UI** primitives
- **React Flow** (reactflow.dev + pro.reactflow.dev) — visualisasi node/workflow
  (dipakai di workspace/plan editor)
- **nuqs** — state URL search params
- Ikon: custom icon set (ArrowDown01Icon, Rocket01Icon, TicketStarIcon, dll —
  kemungkinan dari Iconify/akar-icons, di-import per-komponen)

### Backend (inferred dari API surface)
- API same-origin di `/api/*` (session cookie, `credentials: same-origin`)
- Framework backend TIDAK terdeteksi dari header (Cloudflare nutupin, tidak ada
  x-powered-by). Pola endpoint REST + SSE streaming mengindikasikan Node.js
  (Express/Hono/Fastify) atau Next.js API routes
- **SSE streaming** untuk generation: `/api/plan/generation/stream`,
  `/api/plan/tasks/stream` — PRD di-generate streaming real-time
- Hosting: di balik **Cloudflare** (CDN + proxy). Aset static cache immutable 1
  tahun, etag gaya Node — kuat dugaan **VPS self-hosted** (nginx/caddy + Node),
  bukan Vercel/Netlify

### Auth
- **Google OAuth** (satu-satunya metode: "Sign in with Google")
- Session cookie same-origin; endpoint `/api/auth` (POST) + `/api/auth/attribute-me`
- **API tokens** (`/api/account/tokens`) — token untuk integrasi CLI

### Payment
- **Midtrans** (custom hook `use-midtrans`) — payment gateway utama (Snap)
- **Fallback transfer manual** ke Bank BSI (no. rekening hardcoded di bundle),
  dengan email bukti pembayaran ke rafiul@iultech.com
- Modul **voucher** (kode diskon) + **addon** (credits/packs) + **bundle**

### Analytics & Integrasi
- Google Tag Manager, **Microsoft Clarity** (session recording)
- **YouTube** integration: `/api/youtube/subscriber-count` (jumlah subscriber
  tampil live di header), `yt3.googleusercontent.com` (avatar channel)
- **Discord** — komunitas
- robots.txt modern: **Content-Signal** (ai-input, ai-train, search) — mereka
  paham AI SEO

---

## 3. Arsitektur Aplikasi

### Route map (diekstrak dari React Router bundle)
| Route | Fungsi |
|-------|--------|
| `/` | Landing page (hero + 4 kartu: Bikin Plan, AndalAI, Community, Konsultasi) |
| `/pricing` | Halaman pricing (tab 1 Bulan / 3 Bulan Hemat) |
| `/sign-in`, `/sign-up` | Auth (Google OAuth) |
| `/new` | Buat PRD baru (onboarding/questionnaire) |
| `/p/$slug` | Halaman publik PRD |
| `/plan`, `/plans/$planId` | Editor plan (PRD) |
| `/workspace/$planId/`, `/workspace/$planId/task` | Workspace + task detail |
| `/onboarding` | Onboarding flow (questionnaire) |
| `/settings` | Settings akun |
| `/transactions` | Riwayat transaksi |
| `/vouchers/` | Voucher |
| `/support` | Support |
| `/feedback` | Feedback |
| `/coaching`, `/consulting` | Layanan berbayar |
| `/tools`, `/prompts` | Ranking tools AI + library prompts |
| `/cli-auth` | **Login CLI** (integrasi AI coding agent lokal!) |
| `/attribution` | Attribution/referral |
| `/admin/dashboard`, `/admin/plans` | **Admin panel** |
| `/marketing` | Admin marketing |
| `/workflows/saas` | Template workflow SaaS |
| `/mock/*` | Halaman demo/dev (agent-chat, prd, roadmap, workspace) |

### Component tree (dari daftar chunk Vite = arsitektur gratis)
- Editor: `plan`, `plan-attachment`, `plan-export`, `PlanSidebar`, `PrdMarkdownPreview`,
  `roadmap`, `kanban`, `task`, `progress`, `PriorityBadge`, `tabs`, `step`
- AI: `agent-chat`, `ChatContextPanel`, `context`, `QuestionnaireQuestion`
- Tools: `tools` (ranking), `tool-categories`, `tool-form`, `pricing-plans`
- Admin: `admin-dashboard`, `admin-plans`, `marketing`, `use-admin-date-filter`
- Monetisasi: `use-midtrans`, `voucher`, `upgrade-modal`, `pricing`, `addon`
- Lainnya: `cli-auth`, `attribution`, `feedback`, `support`, `onboarding`, `settings`,
  `share`, `linear` (UI gaya Linear?), `command` (command palette)

### API surface (lengkap)
**Auth & akun**
- POST `/api/auth`, POST `/api/auth/attribute-me` (atribusi referral)
- GET/POST `/api/account/tokens`, DELETE `/api/account/tokens/{id}` (API keys)
- GET `/api/workspaces`

**Generation PRD (inti produk)**
- POST `/api/plan/generation/start` — mulai generate PRD
- GET `/api/plan/generation/stream?planId=` — SSE streaming
- POST `/api/plan/features/generate`, POST `/api/plan/tasks/generate`
- POST `/api/plan/tasks/create`
- GET/PATCH/DELETE `/api/plan/features/{id}`, `/api/plan/subfeatures/{id}`, `/api/plan/tasks/{id}`
- GET `/api/plan/features/list?planId=`, `/api/plan/subfeatures/list?planId=`,
  `/api/plan/tasks/list?planId=` / `?featureId=`

**Subscription & payment**
- GET `/api/subscription/status` (401 tanpa login), GET `/api/subscription/history`

**Konten & statistik**
- GET `/api/stats` (totalUsers, totalPrds — publik), GET `/api/stats-stream` (SSE live)
- GET `/api/youtube/subscriber-count`
- GET `/api/tools/list`, GET `/api/tools/{slug}` (publik)
- GET/POST `/api/admin/tools/*` (create, upload-url, plans, scores, videos — CRUD admin)
- POST `/api/feedback/submit`, GET `/api/feedback/eligibility`

### Struktur data (inferred)
```
User (Google OAuth) → Subscription (Midtrans) → Voucher/Addon
User → Workspace (surface: web|cli) → Plan (PRD) → Feature → Subfeature → Task
Tool (AI coding tool) → Plans, Scores (9 kategori), Videos (YouTube review)
Stats: totalUsers, totalPrds
```

---

## 4. Fitur Utama & Alur

1. **Bikin Plan (inti)**: user isi questionnaire/ide → AI generate PRD lengkap
   (features + subfeatures + tasks) secara streaming → edit di editor
   (kanban/roadmap/task) → export/download Markdown → siap di-paste ke AI
   coding agent
2. **AndalAI**: pilih model AI premium (GPT-5.6, Opus 5, Kimi K3, dll) untuk
   generate — akses model premium dibatasi subscription
3. **CLI integration (pembeda!)**: user login lewat browser di port lokal
   (`127.0.0.1:{port}/callback`), dapat token API → CLI menarik PRD langsung
   ke AI coding agent lokal (Claude Code, Cursor, dll)
4. **Chat AI planning**: tanya-jawab soal PRD/fitur/task dengan AI (kuota per
   tier: 100x/bln di Starter, unlimited di Pro)
5. **Community**: Discord + jumlah subscriber YouTube live + atribusi referral
6. **Tools Ranking**: leaderboard AI coding tools (skor 0-10 per kategori:
   Harga, Batas Penggunaan, Value for Money, Performa, Kecepatan, Kemudahan,
   Kualitas Kode, Dokumentasi, Integrasi) — masih kosong/early stage
7. **Coaching & Consulting**: layanan berbayar 1-on-1 dengan Raf Dev
8. **Feedback** loop + stats live di header (social proof)

---

## 5. Pricing & Monetisasi (17 Agu 2026)

| Tier | Harga | Fitur |
|------|-------|-------|
| Free | Rp 0 | Akses dasar (promo "Mulai Gratis") |
| Starter | Rp 66rb/bln (Rp 199rb/3bln, 12% OFF) | Premium AI model, 5 PRD/bln, chat AI 100x/bln, download Markdown, generate spec |
| Pro | Rp 133rb/bln (Rp 399rb/3bln, 34% OFF) | Unlimited PRD, chat AI unlimited, chat langsung Raf Dev, semua fitur |
| Addon | credits/packs | Pembelian tambahan |
| Voucher | kode diskon | Promo |
| Coaching/Consulting | custom | 1-on-1 |

Diskon banner: "DISKON terbatas hingga 34%". Semua harga Rupiah. Bisa upgrade/
downgrade/cancel kapan aja.

---

## 6. Insight Kompetitif — Kenapa Mereka Menang

1. **Personal brand Raf Dev (YouTube 31,6K)** sebagai mesin traffic utama —
   produknya adalah monetisasi dari audiens yang sudah ada. Ini sulit ditiru
   produk-only; perlu strategi konten paralel.
2. **Positioning niche yang jelas**: "PRD untuk AI coding" — menjawab pain
   point nyata developer Indonesia yang pakai Claude Code/Cursor tapi bingung
   bikin spec.
3. **Workflow lengkap**: ide → PRD → task → export Markdown → langsung dipakai
   AI agent. Bukan cuma template statis, tapi pipeline.
4. **CLI integration**: token API + auth browser → PRD bisa di-pull ke agent
   lokal. Ini moat teknis yang belum banyak pesaing.
5. **Social proof live**: counter user/PRD real-time + subscriber YouTube di
   header = trust builder.
6. **Bahasa Indonesia + harga Rupiah + Midtrans** = fokus pasar lokal, pesaing
   global (PRD generators) tidak menyasar ini.
7. **Community Discord + feedback loop** → retention & word-of-mouth.
8. **Monetisasi bertingkat**: subscription (PRD generator) + coaching +
   consulting + addon — beberapa revenue stream dari 1 audiens.

### Kelemahan yang bisa dieksploitasi
- Tools ranking masih kosong (fitur belum jalan) — peluang buat duluan
- Tanpa account: fitur inti tidak bisa dicoba (semua di balik login) — peluang
  buat free-trial tanpa login / PRD publik lebih kaya
- Hanya Google OAuth — barrier untuk sebagian user
- SPA murni (tanpa SSR) — SEO halaman konten lemah; mereka andalkan YouTube,
  bukan SEO organik dari situs
- Payment gateway "kadang kendala" (ada fallback transfer manual) — pengalaman
  checkout bisa lebih mulus
- Belum ada marketplace/template sharing antar user (PRD publik ada di /p/$slug
  tapi terbatas)

---

## 7. Blueprint: Cara Bikin Website Serupa

### Rekomendasi stack (sesuai preferensi & stack yang sudah kamu kuasai)
- **Frontend**: Next.js (App Router) + Tailwind v4 — beda dari mereka (Vite SPA),
  dapat keunggulan SSR/SEO yang mereka lemah. Desain original, JANGAN tiru layout
  mereka (aturan: ambil fitur & stack, jangan desain).
- **Backend**: Next.js API Routes / Route Handlers + **Drizzle ORM**
  (SQLite dev / PostgreSQL prod) — sudah terbukti di project kamu.
- **Auth**: NextAuth V4 (Google OAuth + credentials) — pola yang sudah kamu
  pakai; tambah session cookie same-origin.
- **Payment**: Midtrans Snap (sama seperti mereka — gateway lokal standar) +
  opsi manual transfer; pakai webhook signature validation.
- **AI generation**: route handler streaming (SSE / ReadableStream) memanggil
  provider AI; kalau mau hemat, pakai router AI gratis (9Router) seperti setup
  kamu; biarkan user pilih model (GPT, Claude, Kimi, DeepSeek).
  - *Terverifikasi via Context7 (Next.js v16 docs)*: Route Handler bisa return
    `new Response(readableStream, {headers: {'Content-Type': 'text/event-stream'}})`.
    Gunakan `Request.signal` untuk auto-cancel saat client disconnect (mencegah
    token/cost terbuang). Alternatif resmi: AI SDK (`ai` + `@ai-sdk/openai`,
    `streamText` → `toAIStream()`).
- **Database schema** (port dari struktur mereka):
  ```
  users, accounts, sessions (NextAuth)
  subscriptions (tier, status, midtrans_order_id), vouchers, addons
  workspaces (surface: web|cli)
  plans (slug, title, desc, status), features, subfeatures, tasks (priority, status)
  tools, tool_scores, tool_videos, tool_plans (ranking)
  feedback, api_tokens, attributions
  ```

### Scope MVP (prioritas)
- P1: Landing + auth Google + bikin PRD (questionnaire → generate streaming →
  editor features/tasks → export Markdown) + pricing + Midtrans checkout
- P1: Kuota per tier (free 2 PRD, starter 5, pro unlimited) + gating
- P2: Chat AI planning, public PRD page (/p/$slug), stats counter live
- P2: CLI integration (API token + /cli-auth flow)
- P3: Tools ranking, prompt library, coaching booking, referral/attribution

### Estimasi effort (solo dev, sehari ~4-6 jam fokus)
- MVP inti (tanpa CLI): 3-4 minggu
- + CLI integration: +1 minggu
- + Tools ranking & prompts: +1-2 minggu
- Total path ke parity: 5-7 minggu; path ke "unggul" (lihat bagian 8): 6-8 minggu

### Alur kerja rekomendasi
1. Prototipe frontend interaktif dulu (preferensimu: Chrome preview sebelum
   implementasi penuh) — validasi UX Bikin Plan flow
2. Backend: schema Drizzle → route handlers generation streaming → auth → payment
3. QA: test generate PRD end-to-end, uji kuota, uji webhook Midtrans
4. Deploy: Vercel opsional / VPS (pola kamu sudah terbukti)

---

## 8. Strategi Unggul (Differentiator) — P1/P2/P3

### P1 — Langsung beda dari hari pertama
1. **SSR + SEO organik**: halaman PRD publik `/p/$slug` di-render server-side +
   schema.org + konten "contoh PRD" yang bisa di-index Google. Mereka SPA murni
   → kita menang traffic pencarian "contoh PRD", "cara bikin PRD AI", dll.
2. **Free tier tanpa login**: kasih 1-2 PRD gratis tanpa daftar (device-based
   quota) → user ngerasain value sebelum kasih email. Conversion funnel lebih
   halus.
3. **Template & workflow siap pakai**: selain PRD dari nol, sediakan template
   per jenis produk (SaaS, marketplace, mobile app, agency client) + workflow
   prebuilt. Mereka baru punya `/workflows/saas`.
4. **Quality over quantity**: prompt engineering + validation loop yang bikin
   output PRD benar-benar "execution-ready" (task yang bisa langsung dieksekusi
   agent, bukan generic). Ini reputasi jangka panjang.

### P2 — Fitur yang mereka belum punya
5. **PRD versioning + diff**: riwayat revisi PRD, bandingkan versi, rollback.
6. **Kolaborasi**: share PRD ke client/team dengan komentar (bukan cuma link
   publik). Target: developer freelance/agency yang perlu review client.
7. **Import dari ide mentah**: tempel catatan/voice note/rapat → AI rapikan
   jadi PRD. UX "tidak perlu mulai dari nol".
8. **Integrasi langsung ke agent**: selain CLI, dukungan `claude.md` /
   `.cursorrules` / AGENTS.md export — satu klik generate file konteks agent
   dari PRD. Lebih praktis dari CLI mereka.

### P3 — Moat jangka panjang
9. **Komunitas template marketplace**: user share template PRD mereka,
   rating, reuse. UGC loop yang bikin switching cost tinggi.
10. **Prompt/agent recipe library**: kumpulan prompt & recipe AI coding yang
    sudah terbukti, per stack (Next.js, Laravel, dll).
11. **Analytics untuk user**: track progress PRD → code → ship; "PRD kamu
    sudah dipakai agent berapa kali" — value yang terasa.
12. **Konten YouTube/SEO paralel**: kalau mau serius compete, bangun channel
    konten (atau kolaborasi creator) — traffic mereka datang dari sini.

### Hal yang TIDAK akan ditiru
- Desain/layout/copywriting ngodingpakeai.com (harus original)
- Klaim "komunitas terbesar" tanpa bukti
- Hardcode data pribadi di bundle (email/rekening developer terekspos — risiko
  keamanan yang tidak perlu)

---

## 9. Keputusan Terbuka (perlu konfirmasi sebelum build)
- Nama & brand produk baru (jangan mirip "Ngoding Pake AI")
- Target: general developer Indonesia, atau niche spesifik (agency, mahasiswa,
  karyawan belajar coding)?
- Monetisasi: subscription murni, atau freemium + addon credit?
- Perlu integrasi YouTube/creator partner dari awal, atau fokus SEO dulu?
- Deploy: Vercel atau VPS (pola kamu)?
- AI provider: langsung ke OpenAI/Anthropic, atau lewat router (9Router) untuk
  multi-model + hemat biaya?

---

