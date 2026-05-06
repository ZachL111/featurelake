# featurelake

`featurelake` explores data engineering with a small Python codebase and local fixtures. The technical goal is to maintain typed feature schemas and train-serving parity checks.

## Use Case

The point is to make a small domain rule concrete enough that a reader can change it and immediately see what broke.

## Featurelake Review Notes

`stale` and `baseline` are the cases worth reading first. They show the optimistic and cautious ends of the fixture.

## Highlights

- `fixtures/domain_review.csv` adds cases for schema drift and lineage depth.
- `metadata/domain-review.json` records the same cases in structured form.
- `config/review-profile.json` captures the read order and the two review questions.
- `examples/featurelake-walkthrough.md` walks through the case spread.
- The Python code includes a review path for `schema drift` and `schema drift`.
- `docs/field-notes.md` explains the strongest and weakest cases.

## Code Layout

The core code exposes a scoring path and the added review layer uses `signal`, `slack`, `drag`, and `confidence`. The domain terms are `schema drift`, `lineage depth`, `partition skew`, and `quality gap`.

The Python implementation avoids hidden state so fixture changes are easy to reason about.

## Run The Check

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify.ps1
```

## Regression Path

The check exercises the source code and the review fixture. `stale` is the high score at 198; `baseline` is the low score at 154.

## Future Work

The fixture set is small enough to audit by hand. The next useful expansion is malformed input coverage, not extra surface area.
