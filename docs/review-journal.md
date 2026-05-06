# Review Journal

I treated `featurelake` as a project where the smallest useful behavior should still be inspectable.

The local checks classify each case as `ship`, `watch`, or `hold`. That gives the project a small review vocabulary that matches its data engineering focus without claiming live deployment or external usage.

## Cases

- `baseline`: `schema drift`, score 154, lane `ship`
- `stress`: `lineage depth`, score 161, lane `ship`
- `edge`: `partition skew`, score 196, lane `ship`
- `recovery`: `quality gap`, score 186, lane `ship`
- `stale`: `schema drift`, score 198, lane `ship`

## Note

This file is intentionally plain so the fixture remains the source of truth.
