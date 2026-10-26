from collections import Counter
SHORT = "short"
STANDARD = "standard"

def choose_format(recent_formats, target_shorts_ratio=0.5):
    valid = [f for f in recent_formats if f in (SHORT, STANDARD)]
    if not valid:
        return SHORT if target_shorts_ratio >= 0.5 else STANDARD
    c = Counter(valid)
    ratio = c[SHORT] / len(valid)
    if ratio < target_shorts_ratio: return SHORT
    if ratio > target_shorts_ratio: return STANDARD
    return STANDARD if valid[-1] == SHORT else SHORT

def output_profile(fmt, short_seconds=60, standard_seconds=60):
    if fmt == SHORT:
        return {"format": SHORT, "width": 1080, "height": 1920, "max_seconds": short_seconds, "aspect": "9:16"}
    if fmt == STANDARD:
        return {"format": STANDARD, "width": 1920, "height": 1080, "max_seconds": standard_seconds, "aspect": "16:9"}
    raise ValueError(f"Unknown format: {fmt}")
