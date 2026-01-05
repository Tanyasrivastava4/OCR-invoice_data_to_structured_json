def clean_ocr_text(text: str) -> str:
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    return "\n".join(lines)
