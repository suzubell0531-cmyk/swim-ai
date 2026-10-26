def summarize_records(records):
    if not records:
        return {
            "count": 0,
            "average_time": None,
            "best_time": None,
            "recent_records": [],
            "recent_time_change": None,
            "previous_time_difference": None,
            "average_stroke_count": None,
            "stroke_count_trend": None,
            "rpe_time_relationship": {
                "sample_count": 0,
                "correlation": None
            }
        }

    times = [record[4] for record in records]
    recent_records = records[-5:]
    latest_record = records[-1]

    def same_event(record):
        return record[2] == latest_record[2] and record[3] == latest_record[3]

    comparable_records = [record for record in records if same_event(record)]
    comparable_recent = [record for record in recent_records if same_event(record)]
    previous_time_difference = None
    recent_time_change = None

    if len(comparable_records) >= 2:
        previous_time_difference = round(
            latest_record[4] - comparable_records[-2][4], 2
        )
    if len(comparable_recent) >= 2:
        recent_time_change = round(
            comparable_recent[-1][4] - comparable_recent[0][4], 2
        )

    stroke_counts = [
        record[5] for record in comparable_records if record[5] is not None
    ]
    recent_stroke_records = [
        record for record in recent_records
        if same_event(record) and record[5] is not None
    ]
    stroke_count_trend = None
    if len(recent_stroke_records) >= 2:
        stroke_change = recent_stroke_records[-1][5] - recent_stroke_records[0][5]
        stroke_count_trend = {
            "change": stroke_change,
            "direction": "増加" if stroke_change > 0 else "減少" if stroke_change < 0 else "横ばい"
        }

    rpe_time_pairs = [
        (record[6], record[4])
        for record in comparable_records
        if record[6] is not None
    ]
    correlation = None
    if len(rpe_time_pairs) >= 2:
        rpes, paired_times = zip(*rpe_time_pairs)
        mean_rpe = sum(rpes) / len(rpes)
        mean_time = sum(paired_times) / len(paired_times)
        covariance = sum(
            (rpe - mean_rpe) * (time - mean_time)
            for rpe, time in rpe_time_pairs
        )
        rpe_variance = sum((rpe - mean_rpe) ** 2 for rpe in rpes)
        time_variance = sum((time - mean_time) ** 2 for time in paired_times)
        if rpe_variance and time_variance:
            correlation = covariance / (rpe_variance * time_variance) ** 0.5

    return {
        "count": len(records),
        "average_time": sum(times) / len(times),
        "best_time": min(times),
        "recent_records": [
            {
                "date": record[1],
                "stroke": record[2],
                "distance": record[3],
                "time_seconds": record[4],
                "stroke_count": record[5],
                "rpe": record[6]
            }
            for record in recent_records
        ],
        "recent_time_change": recent_time_change,
        "previous_time_difference": previous_time_difference,
        "average_stroke_count": (
            round(sum(stroke_counts) / len(stroke_counts), 2)
            if stroke_counts else None
        ),
        "stroke_count_trend": stroke_count_trend,
        "rpe_time_relationship": {
            "sample_count": len(rpe_time_pairs),
            "correlation": round(correlation, 3) if correlation is not None else None
        }
    }