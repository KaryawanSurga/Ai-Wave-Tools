# Execution Readiness Score — Rubrik v1

Rubrik ini adalah kontrak evaluasi untuk BikinPRD. Sumber canonical bobot dan hard gate adalah `PRD.md` §5; perubahan harus menaikkan `rubric_version` dan menjalankan regression evaluation.

## Skala dan dimensi

| Kode | Dimensi | Bobot |
|---|---|---:|
| ER-01 | Problem, user, dan desired outcome | 10 |
| ER-02 | Scope dan non-goals | 10 |
| ER-03 | Functional requirements | 15 |
| ER-04 | Testable acceptance criteria | 20 |
| ER-05 | Context dan likely affected areas | 10 |
| ER-06 | Dependencies dan sequencing | 10 |
| ER-07 | Constraints dan non-functional requirements | 10 |
| ER-08 | Edge cases dan failure states | 10 |
| ER-09 | Risks, assumptions, dan open decisions | 5 |

Setiap dimensi dinilai 0–4 lalu dinormalisasi terhadap bobot: `dimension_score = rating / 4 × weight`. Total adalah jumlah sembilan dimension score, dibulatkan ke integer terdekat. Evaluator wajib menyimpan rating, evidence, missing items, recommendations, rubric version, prompt version, model/provider, revision, dan timestamp.

## Anchor penilaian

| Rating | Makna |
|---:|---|
| 0 | Tidak ada atau bertentangan |
| 1 | Disebut tetapi generik/tidak dapat digunakan |
| 2 | Sebagian usable; gap material masih ada |
| 3 | Lengkap dan actionable dengan perbaikan minor |
| 4 | Spesifik, konsisten, traceable, dan dapat diverifikasi |

Evaluator tidak boleh memberi nilai berdasarkan panjang, jumlah heading semata, atau jumlah task. Evidence harus menunjuk elemen aktual dalam revision.

## Hard gates

Skor final dibatasi maksimum 79 jika salah satu kondisi berikut benar:

- ada requirement P0 tanpa acceptance criteria yang dapat diuji;
- scope atau non-goals kosong;
- ada open decision blocking yang belum diselesaikan tetapi output menyatakan siap dibangun;
- requirement penting saling bertentangan;
- output mengarang stack, budget, deadline, file, atau keputusan bisnis yang tidak diberikan user.

## Status

- 90–100: **Ready** — review singkat tetap wajib.
- 80–89: **Ready with minor edits** — memenuhi promise produk.
- 60–79: **Needs review** — export boleh dengan warning.
- 0–59: **Incomplete** — minta input/perbaikan sebelum menyebut siap eksekusi.

## Minimum requirement anatomy

Setiap requirement P0/P1 wajib memiliki ID stabil, tujuan/deskripsi, priority + milestone, aturan bisnis, minimal satu success dan satu failure acceptance criterion, dependency, edge case relevan, dan likely affected area tanpa mengarang nama file.

## Kalibrasi dan regression

1. Evaluation set awal minimal 20 brief ICP: lengkap, ambigu, kontradiktif, dan adversarial.
2. Dua reviewer manusia menilai secara blind dengan anchor yang sama.
3. M0 gate membutuhkan agreement ≥0,7 dan penyelesaian disagreement terdokumentasi.
4. Setiap perubahan prompt/model/rubric dibandingkan dengan baseline; penurunan quality, hard-gate detection, latency, atau cost di luar guardrail memblokir rollout.
5. Simpan score AI dan human secara terpisah. Score historis immutable; recalculation membuat evaluation baru.

## Output evaluator

```json
{
  "rubricVersion": "ers-v1",
  "totalScore": 84,
  "status": "ready_with_minor_edits",
  "hardGates": [],
  "dimensions": [
    {
      "code": "ER-04",
      "rating": 3,
      "weightedScore": 15,
      "evidence": ["F-05 lists success and timeout/retry acceptance"],
      "missingItems": ["Cancellation race outcome is not explicit"],
      "recommendations": ["Add an acceptance criterion for cancel after provider completion"]
    }
  ]
}
```

Schema production wajib menolak kode dimensi tak dikenal, score di luar rentang, duplicate dimension, total yang tidak cocok dengan formula, dan evidence/recommendation kosong ketika rating <4.
