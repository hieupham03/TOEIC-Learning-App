# Listening offline manifest and dry-run contract V0.1

The acquisition adapter records what a named source exposes. The offline validator rechecks the local bytes and binding metadata from a website-independent version 1 manifest. The Android app only consumes its existing synthetic fixtures under current authority.

| Stage | Command from `android-app/` | Output |
| --- | --- | --- |
| Normalize the recorded Zenlish batch | `python -B scripts/normalize_zenlish_batch.py` | `.tooling/listening-overnight/normalized_manifest.json`. The adapter re-reads the retained HTML, checks its receipt hash and resolves only the four observed targets. |
| Validate a manifest | `python -B scripts/listening_manifest.py .tooling/listening-overnight/normalized_manifest.json` | A JSON summary of per-group retrieval, mapping, declared QA, errors and holds. |
| Use another adapter later | Emit the [manifest schema](../android-app/scripts/listening_manifest.schema.json) and supply relative file paths under the manifest directory | Identified groups and ordered items, pinned source snapshot, explicit audio/file binding and independent answer, QA and rights evidence. |

## Exit codes and evidence

- `1 INVALID` means the document or a structural/media check failed. This includes missing essential audio or Part 1 image, malformed files, duplicate IDs or audio, wrong group/media/order, missing required question content, incorrect MIME and mismatched checksums or byte counts.
- `2 HOLD` means the manifest has no structural errors but at least one explicit gap, such as a partial acquisition, a labels-only item, an unverified answer, an unrun compressed decode or pending QA and rights evidence.
- `0 REVIEW_REQUIRED` means the structural check passed and required review declarations are present in the input. It comes with `eligible_for_app: false`. The validator checks declarations and references. A later authorized reviewer may inspect the evidence and verify content.

`FETCHED` describes acquisition and `MAPPED` describes relationships and verified local file structure. The validator reads external QA declarations as metadata and preserves the import hold. A source that repeats a parent ID on every question, or exposes only displayed numbering, can use a documented local composite key and a null `source_item_id`. Part 1 and Part 2 may have source labels only. The adapter keeps that absence visible and never writes a guessed transcript or key.

## Later CX-04 dry run

With a separate PO authorization, a dry-run adapter could resolve `group.id`, ordered item IDs, expected indices, `audio_binding`, and local audio SHA-256 into candidate inputs to the same CX-04 playback boundary. It would first require reviewed rights and answers, content QA evidence and an explicitly authorized group. The runtime group and item association and the actual file bytes must both be verified. A corrupt file, missing mandatory image or audio, failed decode, source mismatch or missing approval stays on hold. This contract creates no importer, APK asset or Android data store.

Container inspection establishes only what can be measured from local bytes. MPEG frame lengths and sampling rate provide an estimated duration. Full compressed decoding uses installed local tools when available, and semantic audio-to-item alignment needs later review. The local adapters and validator output contain provenance and metadata derived from the source. The full manifests, source page, questions, media, and diagnostic logs stay in Git-ignored storage.
