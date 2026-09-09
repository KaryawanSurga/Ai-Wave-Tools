# BRD - BikinPRD (Business Requirements Document)

Versi: 0.1 (draf pertama)
Tanggal: 2 September 2026
Status: Draft untuk review owner
Hubungan dokumen: *Business layer* dari `PRD.md` (produk). PRD memakai BRD ini
sebagai acuan "kenapa & untuk siapa"; PRD menjelaskan "apa & bagaimana".
Basis riset: `recon-ngodingpakeai/BREAKDOWN.md` + `PRD.md` + wawancara owner.

---

## 1. Ringkasan Eksekutif

**BikinPRD** adalah platform Indonesia yang mengubah ide mentah menjadi dokumen
project siap eksekusi (PRD, roadmap, spec) untuk AI coding agent. Bisnis ini
dibangun di atas **empat pilar** yang sekaligus menjadi empat kartu utama di
landing page:

| # | Pilar | Kartu landing | Fungsi bisnis |
|---|-------|---------------|---------------|
| 1 | **Dokumentasi & Project Document** | Dokumentasi / Project Document | Penawaran inti: generate PRD & dokumen project lengkap dari ide |
| 2 | **Model AI Premium** | Dokumen dengan model AI yang lebih tinggi | Upsell margin tinggi: akses model AI canggih untuk kualitas dokumen lebih baik |
| 3 | **Komunitas Discord** | Komunitas Discord | Retention, word-of-mouth, feedback loop, calon konversi |
| 4 | **Konsultasi Project** | Konsultasi terkait project | Revenue stream kedua: layanan 1-on-1 konsultasi project |

**Tujuan bisnis inti:**
- TB-1: Validasi pasar PRD-generator lokal (bukti konversi free→paid)
- TB-2: Bangun aset SEO (PRD publik + konten) untuk traffic organik
- TB-3: MRR positif dalam 6 bulan
- TB-4: Diversifikasi revenue (subscription + konsultasi) supaya tidak
  bergantung pada satu stream

---

## 2. Konteks Bisnis & Masalah

### 2.1 Masalah yang dipecahkan
Developer & freelance Indonesia yang memakai AI coding agent (Claude Code,
Cursor, Codex) kesulitan menyusun spec yang rapi. Akibatnya:
- Agent AI "ngaco" karena tidak ada dokumen acuan yang jelas
- Client minta "PRD dulu" tapi developer benci menulis dokumen
- PRD yang disusun manual memakan 1-2 hari padahal isinya bisa distrukturkan
  dalam hitungan menit

### 2.2 Bukti pasar
- Kompetitor (ngodingpakeai.com) punya ~33.766 user dan 17.140 PRD dibuat
  (live stats, 17 Agu 2026) - sinyal permintaan nyata
- Kompetitor sudah memonetisasi: subscription (66rb/133rb), coaching,
  consulting
- Pasar lokal berbahasa Indonesia + harga Rupiah belum dilayani dengan baik
  oleh generator PRD global

### 2.3 Kenapa empat pilar
Struktur empat pilar meniru pola yang sudah terbukti kompetitor (hero + 4
kartu: Bikin Plan, AndalAI, Community, Konsultasi) TAPI dengan penamaan dan
eksekusi original. Alasannya:
- **Satu produk inti** (dokumentasi) untuk menarik user
- **Upsell model premium** untuk menaikkan ARPU tanpa menambah beban operasional
- **Komunitas** untuk retention & akusisi murah (word-of-mouth)
- **Konsultasi** untuk menangkap user yang butuh bantuan manusia, bukan cuma
  dokumen

---

## 3. Tujuan Bisnis (Objective)

### 3.1 Tujuan jangka pendek (0-6 bulan)
- Validasi willingness-to-pay user Indonesia untuk tools dokumentasi AI
- Capai konversi free→paid ≥ 5% di M6
- Bangun 500+ PRD publik ter-index Google (aset SEO)
- Buktikan konsultasi sebagai revenue stream kedua yang viable

### 3.2 Tujuan jangka panjang (6-24 bulan)
- Menjadi standar "dokumen project untuk AI coding" di Indonesia
- Marketplace template komunitas (UGC loop)
- Ekosistem: dokumentasi → ekspor ke agent → komunitas → konsultasi

### 3.3 KPI Bisnis (diadopsi dari PRD, ditambah dimensi 4 pilar)

| KPI | Target M1 | Target M3 | Target M6 |
|-----|-----------|-----------|-----------|
| User terdaftar | 300 | 1.500 | 5.000 |
| PRD dibuat | 600 | 3.000 | 12.000 |
| Trial tanpa login → daftar | 15% | 20% | 25% |
| Konversi free→paid | 3% | 5% | 7% |
| Paid subscribers | 10 | 75 | 350 |
| MRR (subscription) | Rp 1jt | Rp 7jt | Rp 35jt |
| Revenue konsultasi | 0 | Rp 1jt | Rp 5jt |
| Anggota Discord aktif | 0 | 200 | 1.000 |
| PRD publik ter-index | - | 500 | 3.000 |
| P95 waktu generate | < 3 mnt | < 2 mnt | < 1,5 mnt |

---

## 4. Target Pasar & Segmentasi

### 4.1 Segmen utama
| Segmen | Kebutuhan inti | Kecenderungan bayar | Prioritas |
|--------|---------------|---------------------|-----------|
| Developer freelance (web dev, 25-35) | Spec client rapi & cepat | Tinggi (investasi tools) | **P0** |
| Product manager startup | PRD terstruktur untuk review tim | Sedang-tinggi | **P0** |
| Mahasiswa belajar coding + AI | Struktur project agar agent tidak ngaco | Rendah-sedang | **P1** |
| Agency kecil (3-5 dev) | Proposal + spec per client, reuse template | Tinggi (volume) | **P1** |

### 4.2 Segmen yang TIDAK disasar
- Korporat besar (butuh enterprise procurement, onboarding panjang)
- Non-developer murni (tidak paham AI coding agent)
- Pasar global (fokus Indonesia dulu, Rupiah, bahasa Indonesia)

### 4.3 Persona (dari PRD)
- **P-01 Rizky** - freelance web dev, 27, pakai Claude Code; benci nulis dokumen
- **P-02 Sari** - PM startup, 30, manage 2 developer; sering revisi berulang
- **P-03 Dimas** - mahasiswa, 22, belajar coding + AI; bingung mulai dari mana
- **P-04 Andi** - agency kecil, 34, 3 dev, 5 client; bikin spec dari nol tiap project

---

## 5. Empat Pilar Penawaran (Kartu Landing) - Detail

Struktur ini WAJIB tercermin di landing page sebagai empat kartu utama
(hero → 4 kartu). Deskripsi produk teknis masing-masing di PRD (F-01, F-03,
F-12, F-16, dsb).

### PILAR 1 - Dokumentasi & Project Document (kartu #1)

**Posisi:** Penawaran inti / entry point.

**Value proposition:** "Tempel ide mentah, dapat PRD lengkap dengan fitur,
subfitur, dan task, siap dieksekusi AI coding agent."

**Scope layanan:**
- Generate PRD dari ide bebas / template / questionnaire (F-03)
- Editor PRD: features, subfeatures, tasks, prioritas P0-P2, status (F-04)
- Export Markdown + file konteks agent: `claude.md`, `.cursorrules`,
  `AGENTS.md` (F-05)
- Halaman PRD publik `/p/$slug` (SSR, SEO) (F-07)
- Template per jenis produk: SaaS, marketplace, mobile, agency, internal (F-08)

**Ukuran sukses pilar ini:**
- Waktu ide→PRD < 15 menit (TP-2)
- Output "execution-ready" tanpa rewrite besar (TP-1, rubrik skor ≥ 70)
- Trial tanpa login berfungsi sebagai pintu masuk (zero-friction)

### PILAR 2 - Dokumen dengan Model AI yang Lebih Tinggi (kartu #2)

**Posisi:** Upsell margin tinggi.

**Value proposition:** "Butuh kualitas dokumen di atas rata-rata? Pilih model AI
premium untuk output yang lebih dalam, lebih detail, lebih akurat."

**Scope layanan:**
- Pilihan model AI per generate: model dasar (hemat) vs model premium
  (GPT/Claude terbaru, Kimi, DeepSeek) (F-03, F-06)
- Akses model premium sebagai pembeda tier (Pro dapat semua model)
- Kualitas output diukur dengan PRD Completeness Score (rubrik internal)
  sebagai bukti nilai - bukan sekadar klaim

**Aturan bisnis:**
- Model premium = fitur berbayar (gating per tier)
- Cost protection: rate limit, cancel stream, model routing hemat (9Router)
- User bisa melihat perbandingan skor output antar model sebagai social proof

**Ukuran sukses pilar ini:**
- % user Starter+ yang memakai model premium ≥ 50%
- Perbedaan skor completeness model premium > model dasar (≥ 5 poin)
- Uptime provider AI tinggi (fallback multi-provider)

### PILAR 3 - Komunitas Discord (kartu #3)

**Posisi:** Retention & akusisi murah.

**Value proposition:** "Gak sendirian: gabung komunitas developer yang
membangun dengan AI, tukar template, dan dapat bantuan."

**Scope layanan:**
- Server Discord resmi (invite dari landing & dashboard) (F-16 referal sinergi)
- Channel: #tanya-jawab, #template-sharing, #showcase-PRD, #feedback
- Feedback loop: user report/bug/idea masuk ke product backlog (F-10)
- Referral: undang member Discord → reward kuota (F-16)

**Aturan bisnis:**
- Komunitas gratis tapi TERKURASI (tidak bisa dibeli dengan uang)
- Aktivitas komunitas dihubungkan ke akun (attribution, F-16)
- Moderasi aktif (anti-spam, anti-promosi kompetitor)

**Ukuran sukses pilar ini:**
- Anggota Discord aktif M6 ≥ 1.000 (dari KPI)
- % signup yang berasal dari Discord ≥ 20% di M6
- Feedback yang masuk → feature shipped (loop tertutup)

### PILAR 4 - Konsultasi Project (kartu #4)

**Posisi:** Revenue stream kedua, menangkap kebutuhan "butuh manusia".

**Value proposition:** "PRD sudah, tapi masih ragu? Konsultasi 1-on-1 untuk
review project, scope, atau roadmap dengan praktisi."

**Scope layanan:**
- Sesi konsultasi berbayar: review PRD, bantu scope, arsitektur, rencana
  implementasi
- Booking via halaman/flow khusus (sinergi PRD: `/consulting`)
- Paket: single session / bundle sesi
- Output sesi bisa berupa catatan actionable yang masuk ke editor PRD user

**Aturan bisnis:**
- Harga custom/fixed per paket (keputusan owner, lihat §12)
- Kuota terbatas per minggu (quality > quantity, personal brand)
- Konsultasi TIDAK termasuk jaminan hasil coding - scope-nya dokumen &
  perencanaan

**Ukuran sukses pilar ini:**
- Revenue konsultasi ≥ Rp 5jt di M6 (dari KPI)
- Kepuasan sesi (rating) ≥ 4.5/5
- Cross-sell: ≥ 30% peserta konsultasi upgrade ke tier berbayar

---

## 6. Value Proposition & Positioning

### 6.1 Kalimat jual (per persona)
- **User:** "PRD yang biasanya 1-2 hari disusun, jadi 10 menit + langsung bisa
  dipakai agent AI lo."
- **Freelancer:** "Kirim PRD yang rapi ke client, bukan sekadar 'ini spec-nya'."
- **Tim:** "Satu sumber kebenaran PRD, bisa di-share & direvisi."
- **Yang butuh manusia:** "Butuh pendamping? Ada konsultasi project dari
  praktisi."

### 6.2 Positioning vs kompetitor

| Aspek | BikinPRD | ngodingpakeai.com |
|-------|----------|-------------------|
| Target | Developer, freelancer, PM, mahasiswa ID | Audiens YouTube Raf Dev |
| Akses | Free trial tanpa login + free tier | Semua fitur di balik login |
| SEO | SSR, PRD publik ter-index | SPA murni, andalkan YouTube |
| Export | Markdown + claude.md/.cursorrules/AGENTS.md | Markdown |
| Harga | Starter 49rb / Pro 99rb | 66rb / 133rb |
| Template | Per jenis produk + workflow | Terbatas |
| Komunitas | Discord + marketplace template | Discord |

### 6.3 Pembeda (differentiator)
1. **Free trial tanpa login** - user merasakan value sebelum kasih email
2. **SSR + SEO organik** - traffic pencarian "contoh PRD", "cara bikin PRD AI"
3. **Agent file export** - satu klik jadi file konteks agent (lebih praktis
   dari CLI kompetitor untuk sebagian besar user)
4. **Completeness Score** - bukti kualitas output, bukan klaim
5. **Harga value-for-money** - 49rb vs 66rb di tier yang sebanding

### 6.4 Positioning statement
*Untuk developer & freelancer Indonesia yang memakai AI coding agent, BikinPRD
adalah cara tercepat mengubah ide menjadi dokumen project eksekusi-ready -
plus akses model AI premium, komunitas, dan konsultasi, dalam satu platform.*

---

## 7. Model Bisnis & Monetisasi

### 7.1 Prinsip
- **Freemium:** free tier nyata (3 PRD/bln) + trial tanpa login (1 PRD,
  device-based) - user merasakan value sebelum bayar
- **Harga Rupiah** kompetitif di bawah kompetitor, diskon 3 bulan untuk
  commitment tanpa lock-in panjang
- **Dua revenue stream utama:** subscription (pilar 1+2) + konsultasi (pilar 4)
- **Anti-abuse:** kuota akun + device, rate limit AI, voucher 1x/akun

### 7.2 Struktur harga subscription (dari PRD)

| Tier | Harga | PRD/bln | Chat AI | Export agent | Model premium |
|------|-------|---------|---------|--------------|---------------|
| Trial (tanpa login) | Rp 0 | 1 (total) | - | Markdown | dasar |
| Free | Rp 0 | 3 | 20x | Markdown | dasar |
| Starter | Rp 49rb (129rb/3bln) | 10 | 150x | Markdown + agent file | ✅ |
| Pro | Rp 99rb (249rb/3bln) | Unlimited | Unlimited | Semua + prioritas | ✅ semua |

*(Harga final menunggu keputusan owner - §12.)*

### 7.3 Revenue stream konsultasi (pilar 4)
- Model harga: fixed package (contoh arah: sesi 30-60 menit, bundle 3 sesi
  dengan diskon) - angka final menunggu owner
- Billing: prepaid via Midtrans (sama infrastruktur payment)
- Kuota sesi per minggu dibatasi (supply constraint → harga premium tersupport)

### 7.4 Alur pembelian (dari PRD)
1. Klik "Upgrade" → pilih paket (bulanan / 3 bulan) → kode voucher opsional
2. Midtrans Snap (VA, QRIS, e-wallet) → bayar
3. Webhook Midtrans (verifikasi signature) → subscription aktif
4. Kuota tier langsung aktif; prorata upgrade; downgrade akhir periode

---

## 8. Analisis Kompetitif

### 8.1 Peta kompetitor
| Kompetitor | Model | Kekuatan | Kelemahan yang kita exploit |
|------------|-------|----------|-----------------------------|
| ngodingpakeai.com | Freemium + coaching | Personal brand Raf Dev, komunitas, CLI | SPA tanpa SEO, semua di balik login, harga lebih tinggi |
| Generator PRD global (AI PRD builders) | SaaS $ | Brand global, kualitas | Bukan bahasa Indonesia, bukan Rupiah, tidak paham lokal |
| Nulis PRD manual / template | DIY | Gratis | Lama, tidak terstruktur, agent tetap "ngaco" |

### 8.2 Insight kunci dari riset kompetitor
- Traffic mereka datang dari YouTube + personal brand, BUKAN SEO - kita bisa
  menang di SEO dengan SSR
- Tools ranking mereka masih kosong - peluang konten, tapi PRIORITAS RENDAH
  (jangan digarap sebelum pilar inti jalan)
- Tanpa akun = tidak bisa coba → kita pecahkan dengan trial tanpa login
- Monetisasi bertingkat (subs + coaching + consulting) terbukti viable - kita
  ikuti dengan 4 pilar

### 8.3 Yang TIDAK akan ditiru
- Desain/layout/copywriting kompetitor (harus original)
- Klaim "komunitas terbesar" tanpa bukti
- Hardcode data pribadi (email/rekening) di JS bundle

---

## 9. Alur Bisnis (Business Flows)

### BF-01 - Pengunjung → Trial → User (pilar 1)
1. Landing (hero + 4 kartu) → klik "Coba Gratis"
2. `/new` tanpa login → generate trial (1 PRD/device) → lihat hasil
3. Export lanjutan / kuota habis → upsell daftar akun
4. Daftar Google → data trial tersimpan → kuota Free

### BF-02 - User → Paid subscription (pilar 1 + 2)
1. Kuota habis / butuh model premium / export agent file → klik Upgrade
2. Pilih Starter/Pro → checkout Midtrans → tier aktif < 60 detik
3. Kuota & fitur premium terbuka

### BF-03 - User → Komunitas (pilar 3)
1. Landing kartu "Komunitas" / dashboard → join Discord
2. Interaksi (tanya-jawab, share template, feedback)
3. Referral: undang member → reward kuota (F-16)

### BF-04 - User → Konsultasi (pilar 4)
1. Landing kartu "Konsultasi" / setelah generate PRD → lihat paket
2. Booking sesi → bayar Midtrans → jadwal sesi
3. Sesi → catatan actionable → masuk ke editor PRD user

### BF-05 - Free → Paid → Churn loop
- Upgrade, downgrade (akhir periode), cancel - semua tercatat di
  `/transactions`
- Churn risk → komunitas + konten SEO + referral sebagai re-engagement

---

## 10. Regulasi & Kepatuhan (Bisnis)

- **UU PDP**: privacy policy jelas, consent Google data, hak hapus akun & data,
  batasi pengumpulan data (pendampingan hukum sebelum launch luas)
- **Pembayaran**: verifikasi signature webhook Midtrans; jangan percaya
  client-side status; rekam gatewayOrderId
- **Disclaimer**: output AI wajib direview manusia (tampil di footer & halaman
  PRD publik)
- **Refund/kebijakan**: kebijakan refund transparan (terutama untuk konsultasi)
- **Konten**: moderasi PRD publik + tombol report (anti konten tidak pantas)

---

## 11. Risiko Bisnis & Mitigasi

| Risiko | Dampak | Mitigasi |
|--------|--------|----------|
| Biaya AI tinggi / abuse | Rugi operasional | Rate limit, cancel stream, model routing hemat, kuota ketat, alert cost |
| Output AI generik/kualitas rendah | Churn, reputasi | Prompt engineering + validation loop (Completeness Score), contoh berkualitas, feedback, iterasi model |
| Kompetitor menjauh (ngodingpakeai) | Kehilangan pangsa | SEO organik + pembeda (free trial, agent export, template); jalankan cepat |
| Payment gateway kendala | Gagal checkout | Webhook robust, fallback transfer manual, retry, monitoring |
| Compliance UU PDP | Denda/legal | Privacy policy, consent, hak hapus; pendampingan hukum |
| Ketergantungan provider AI | Downtime/cost | Multi-model via 9Router + fallback provider |
| Adopsi lambat | MRR rendah | Konten SEO, komunitas Discord, gratis coba, referral |
| Konsultasi tidak terjual | Revenue stream kedua gagal | Bundle dengan cross-sell dari user paid; harga diuji |
| Founder bandwidth (konsultasi) | Kapasitas terbatas | Batasi kuota sesi; dokumentasikan insight jadi konten |

---

## 12. Keputusan Terbuka & Asumsi

**Keputusan yang perlu konfirmasi owner:**

| # | Keputusan | Default diusulkan | Alternatif |
|---|-----------|-------------------|------------|
| KB-1 | Nama produk | "BikinPRD" (working) | PRDit, SpecID, dll |
| KB-2 | Harga Starter/Pro | Rp 49rb / Rp 99rb | Rp 39rb / Rp 79rb |
| KB-3 | Harga & paket konsultasi | Fixed package (mis. 1 sesi / bundle 3) | Per-jam, custom quote |
| KB-4 | Model premium mana yang di-upsell | GPT/Claude terbaru + Kimi + DeepSeek (via 9Router) | Batasi ke 1-2 model dulu |
| KB-5 | Referral reward | +1 PRD/bln per member aktif | Cash/kredit |
| KB-6 | Kapan konsultasi diluncurkan | Setelah MVP live (Fase 2) | Sejak Fase 1 (landing card dulu, booking menyusul) |
| KB-7 | Tools ranking (pilar konten) | Fase 3, prioritas rendah | Tarik ke fase 2 |
| KB-8 | Deploy | VPS + Cloudflare | Vercel |

**Asumsi yang perlu divalidasi:**
- Pasar PRD-generator lokal memang ada permintaan (sinyal 33k user pesaing) -
  uji di Fase 0
- User mau bayar untuk "hemat waktu bikin spec" - uji via price page test
- Output AI perlu cukup baik agar terasa "execution-ready" - validasi dengan
  sample PRD berkualitas
- Empat pilar tidak saling mengaburkan fokus - landing harus jelas memimpin ke
  pilar 1 sebagai entry point

---

## 13. Roadmap Bisnis (diadopsi dari PRD)

| Fase | Fokus | Kriteria selesai |
|------|-------|------------------|
| Fase 0 (1 minggu) | Prototipe frontend interaktif (Chrome) flow utama: landing (4 kartu), /new, editor, pricing | Review desain & flow; validasi sebelum build penuh |
| Fase 1 (3-4 minggu) | MVP: F-01..F-06, F-18; auth, generate streaming, editor, export Markdown, Midtrans, kuota | Semua AC P0 lulus; daftar→bikin PRD→bayar end-to-end |
| Fase 2 (2 minggu) | F-07, F-08, F-09, F-10, F-11, F-13 (sebagian) + **kartu komunitas live + konsultasi booking** | PRD publik SSR + template + export agent + API token + komunitas + konsultasi terjual |
| Fase 3 (ongoing) | F-12, F-14, F-15, F-16, F-17 | Fitur fase 2/3 live; komunitas & marketplace |

---

## 14. Prinsip Brand & Komunikasi

- Tone bahasa: Indonesia santai-profesional ("Dari ide jadi PRD")
- Desain original, dark-first + light mode (TIDAK meniru kompetitor)
- Empat kartu landing sebagai "menu penawaran" - wajib ada sejak Fase 0
- Copy landing memimpin ke pilar 1 (dokumentasi) sebagai entry point; pilar
  2-4 sebagai ekspansi
- Semua klaim kualitas didukung data (Completeness Score, stats live), bukan
  klaim kosong

---

## 15. Ukuran Keberhasilan BRD Ini

BRD dianggap matang dan selesai ketika:
- [ ] Owner menyetujui empat pilar sebagai struktur penawaran
- [ ] Harga final (subscription + konsultasi) diputuskan (§12)
- [ ] Nama & logo final diputuskan
- [ ] PRD.md konsisten dengan BRD ini (tidak ada kontradiksi scope)
- [ ] Landing page Fase 0 menampilkan empat kartu sesuai §5