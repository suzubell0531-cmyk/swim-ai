from database import init_db, add_record, get_all_records
from analysis import summarize_records

init_db()

add_record(
    date="2026-09-26",
    stroke="Freestyle",
    distance=50,
    time_seconds=24.70,
    stroke_count=32,
    rpe=9,
    note="テスト1"
)

add_record(
    date="2026-09-27",
    stroke="Freestyle",
    distance=50,
    time_seconds=24.55,
    stroke_count=31,
    rpe=8,
    note="テスト2"
)

add_record(
    date="2026-09-28",
    stroke="Freestyle",
    distance=50,
    time_seconds=24.40,
    stroke_count=30,
    rpe=9,
    note="テスト3"
)

records = get_all_records()
summary = summarize_records(records)

print("記録数:", summary["count"])
print("平均タイム:", summary["average_time"])
print("ベストタイム:", summary["best_time"])