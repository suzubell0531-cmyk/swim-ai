def summarize_records(records):
    if not records:
        return {
            "count": 0,
            "average_time": None,
            "best_time": None
        }

    times = [record[4] for record in records]

    return {
        "count": len(records),
        "average_time": sum(times) / len(times),
        "best_time": min(times)
    }