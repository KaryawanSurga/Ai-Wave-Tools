# Delivery Backlog — Vertical Slice M1

Backlog ini memecah kontrak PRD menjadi urutan delivery. Estimasi dilakukan tim setelah spike; urutan dan dependency lebih penting daripada angka prematur.

## Epic 0 — Discovery dan technical spikes

- `M0-01` Interview 10 ICP dan dokumentasikan evidence terhadap A-01.
- `M0-02` Uji prototype UX dengan 5 ICP memakai script `UX-SPEC.md`.
- `M0-03` Bangun evaluation set 20 brief anonim + two-reviewer baseline.
- `M0-04` Spike satu provider/model: structured output, latency, retry, cost, dan score.
- `M0-05` Spike deployment worker/queue/SSE reconnect; approve ADR-001/002.
- `M0-06` Finalisasi data map, retention, refund, plan economics, dan vendor review.

**Exit:** seluruh blocking item `TECHNICAL-DESIGN.md` §12 selesai.

## Epic 1 — Foundation

- `M1-01` Scaffold app, environments, CI, lint/type/test, migration runner.
- `M1-02` Implement schema + constraints + migration tests dari ERD.
- `M1-03` Implement error envelope, request ID, structured redacted logging.
- `M1-04` Implement Google auth, session rotation, CSRF, logout/delete request.
- `M1-05` Implement anonymous session, expiry cleanup, adaptive rate-limit hook.

## Epic 2 — Core value slice

- `M1-06` Brief intake + validation + draft persistence.
- `M1-07` Plan catalogue, entitlement calculation, append-only usage reservation.
- `M1-08` Job state machine, outbox, worker lease/retry/cancel, SSE + polling.
- `M1-09` AI adapter + `PrdDocumentV1` validation + checkpoint persistence.
- `M1-10` Revision creation + readiness evaluator/rubric hard gates.
- `M1-11` Preview + anonymous login gate + transactional claim.
- `M1-12` Owner-only editor + autosave + revision conflict recovery.
- `M1-13` Markdown renderer + immutable revision export + golden fixtures.

**First demonstrable slice:** M1-01–13 memungkinkan brief → generated PRD → claim → edit → score → export; payment dapat menyusul tanpa menghambat validasi kualitas.

## Epic 3 — Monetization dan operations

- `M1-14` Pricing/plan UI dan checkout order idempotent.
- `M1-15` Midtrans Snap + verified webhook state machine.
- `M1-16` Subscription activation, refund/chargeback effect, reconciliation.
- `M1-17` Minimal operator lookup, audit timeline, safe retry/adjustment.
- `M1-18` Legal pages, analytics events, dashboards, alerts, runbooks.

## Epic 4 — Release assurance

- `M1-19` Integration tests: claim race, job retry, ledger settlement, payment idempotency.
- `M1-20` Security matrix: IDOR, CSRF, XSS, prompt injection, webhook replay.
- `M1-21` Accessibility audit untuk semua flow P0.
- `M1-22` Load/provider outage/backup restore drills.
- `M1-23` Regression evaluation 20 PRD dan sign-off release gate.

## Dependency path

```text
M0 spikes
  → foundation/schema/auth
  → brief + entitlement reservation
  → job/AI/revision/evaluation
  → claim/editor/export
  → payment/operations
  → release assurance
```

## Definition of Ready per ticket

- Memiliki PRD feature/journey ID dan acceptance criteria terukur.
- API/schema/UX state yang terdampak sudah dirujuk.
- Dependency, security/privacy, analytics, dan failure path dinyatakan.
- Tidak membawa capability M2+ secara terselubung.

## Definition of Done

Mengikuti PRD §19.2, ditambah test core + satu failure path + boundary, migration/rollback bila relevan, observability yang bisa ditindak, dan bukti verifikasi pada ticket. “Compile” saja bukan bukti selesai.
