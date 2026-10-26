from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"
)

MODEL_NAME = "qwen3.5-9b"


def generate_feedback(summary):
    average_time = summary["average_time"]
    best_time = summary["best_time"]
    rpe_relationship = summary["rpe_time_relationship"]
    prompt = f"""
あなたは競泳データ分析を補助するAIです。

以下の記録だけを根拠にしてください。

記録数: {summary["count"]}
平均タイム: {f'{average_time:.2f} 秒' if average_time is not None else 'データなし'}
ベストタイム: {f'{best_time:.2f} 秒' if best_time is not None else 'データなし'}
直近5回の記録: {summary["recent_records"]}
直近の同一泳法・距離でのタイム変化（最新 - 直近5回の最初）: {summary["recent_time_change"]}
前回の同一泳法・距離の記録との差（最新 - 前回）: {summary["previous_time_difference"]}
平均ストローク数: {summary["average_stroke_count"]}
直近5回の同一泳法・距離でのストローク数傾向: {summary["stroke_count_trend"]}
RPEとタイムの相関（対象件数 {rpe_relationship["sample_count"]}）: {rpe_relationship["correlation"]}

以下の点を日本語で簡潔に説明してください。

1. 現在の状態
2. 直近のタイム・ストローク数の推移と前回との差
3. RPEとタイムの関係（相関は因果関係ではない点に注意）
4. 次に集めるべきデータ

比較は同じ泳法・距離の記録に限り、データがない場合や件数が少ない場合はその旨を伝えてください。分からないことは推測で断定しないでください。
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content