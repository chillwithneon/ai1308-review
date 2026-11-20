THRESHOLD = 0.5

def predict(scores):
    """Nhãn có di?m cao nh?t trong dict {nhãn: di?m}."""
    best = max(scores, key=scores.get)
    if scores[best] < THRESHOLD:
        return "unknown"
    return best
