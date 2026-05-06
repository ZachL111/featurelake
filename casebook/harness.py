"""Executable checks for the featurelake casebook."""

from __future__ import annotations

from collections import Counter

from . import featurelake_segment_00
from . import featurelake_segment_01
from . import featurelake_segment_02
from . import featurelake_segment_03
from . import featurelake_segment_04
from . import featurelake_segment_05
from . import featurelake_segment_06
from . import featurelake_segment_07
from . import featurelake_segment_08
from . import featurelake_segment_09
from .expected import EXPECTED
from .model import validate_case


def iter_cases():
    yield from featurelake_segment_00.iter_featurelake_00()
    yield from featurelake_segment_01.iter_featurelake_01()
    yield from featurelake_segment_02.iter_featurelake_02()
    yield from featurelake_segment_03.iter_featurelake_03()
    yield from featurelake_segment_04.iter_featurelake_04()
    yield from featurelake_segment_05.iter_featurelake_05()
    yield from featurelake_segment_06.iter_featurelake_06()
    yield from featurelake_segment_07.iter_featurelake_07()
    yield from featurelake_segment_08.iter_featurelake_08()
    yield from featurelake_segment_09.iter_featurelake_09()


def summarize_cases() -> dict:
    rows = list(iter_cases())
    for row in rows:
        validate_case(row)
    lanes = Counter(row.expected_lane for row in rows)
    focus = Counter(row.focus for row in rows)
    return {
        "case_count": len(rows),
        "score_min": min(row.expected_score for row in rows),
        "score_max": max(row.expected_score for row in rows),
        "lane_counts": dict(sorted(lanes.items())),
        "focus_counts": dict(sorted(focus.items())),
        "score_checksum": sum((index + 1) * row.expected_score for index, row in enumerate(rows)),
        "pressure_checksum": sum((index % 17 + 1) * row.pressure for index, row in enumerate(rows)),
    }


def assert_expected() -> dict:
    summary = summarize_cases()
    if summary != EXPECTED:
        raise AssertionError(f"casebook summary mismatch: {summary!r} != {EXPECTED!r}")
    return summary


def featurelake_summary() -> dict:
    return assert_expected()
