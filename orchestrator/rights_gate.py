from dataclasses import dataclass
@dataclass
class Decision:
    approved: bool
    reason: str
    attribution_required: bool=False
ALLOW={"CC0","PUBLIC_DOMAIN","CC-BY","CC-BY-SA","EXPLICIT_COMMERCIAL_PERMISSION","OWNED_BY_UPLOADER"}
def evaluate(license_name, evidence_url):
    name=(license_name or "").strip().upper().replace(" ","-")
    if not evidence_url or not evidence_url.startswith("https://"):
        return Decision(False,"Missing HTTPS evidence for license/permission.")
    if name not in ALLOW:
        return Decision(False,f"License not on conservative allowlist: {name or 'UNKNOWN'}")
    return Decision(True,f"Evidence supplied for allowlisted license {name}", name in {"CC-BY","CC-BY-SA"})
