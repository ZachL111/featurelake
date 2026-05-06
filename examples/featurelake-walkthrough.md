# Featurelake Walkthrough

This note is the quickest way to read the extra review model in `featurelake`.

| Case | Focus | Score | Lane |
| --- | --- | ---: | --- |
| baseline | schema drift | 154 | ship |
| stress | lineage depth | 161 | ship |
| edge | partition skew | 196 | ship |
| recovery | quality gap | 186 | ship |
| stale | schema drift | 198 | ship |

Start with `stale` and `baseline`. They create the widest contrast in this repository's fixture set, which makes them better review anchors than the middle cases.

`stale` is the optimistic case; use it to make sure the scoring path still rewards strong signal.
