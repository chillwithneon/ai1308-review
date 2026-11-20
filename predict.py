THRESHOLD = 0.5

def predict(scores):
    """Nhãn có di?m cao nh?t trong dict {nhãn: di?m}."""
    return max(scores, key=scores.get)
