from database import init_db, get_all_records
from analysis import summarize_records
from llm import generate_feedback

init_db()

records = get_all_records()
summary = summarize_records(records)

print("記録数:", summary["count"])
print("平均タイム:", summary["average_time"])
print("ベストタイム:", summary["best_time"])
print("直近5回:", summary["recent_records"])
print("直近5回のタイム変化:", summary["recent_time_change"])
print("前回記録との差:", summary["previous_time_difference"])
print("平均ストローク数:", summary["average_stroke_count"])
print("ストローク数の傾向:", summary["stroke_count_trend"])
print("RPEとタイムの相関:", summary["rpe_time_relationship"])

print("\n--- AIフィードバック ---")

feedback = generate_feedback(summary)

print(feedback)