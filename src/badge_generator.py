import json
from dataclasses import dataclass
from datetime import datetime
import hashlib
import argparse

@dataclass
class Badge:
    studio_logo: str
    policy_summary: str
    timestamp: str
    policy_hash: str

def generate_badge(studio_logo: str, policy_summary: str) -> Badge:
    timestamp = datetime.now().isoformat()
    policy_hash = hashlib.sha256(policy_summary.encode()).hexdigest()
    return Badge(studio_logo, policy_summary, timestamp, policy_hash)

def create_svg_badge(badge: Badge) -> str:
    svg_template = """
    <svg width="200" height="50">
        <rect x="0" y="0" width="200" height="50" fill="#ffffff" rx="10"/>
        <text x="10" y="30" font-size="20" fill="#000000">{studio_logo}</text>
        <text x="10" y="50" font-size="15" fill="#000000">{policy_summary}</text>
        <text x="10" y="70" font-size="10" fill="#000000">Timestamp: {timestamp}</text>
        <text x="10" y="90" font-size="10" fill="#000000">Policy Hash: {policy_hash}</text>
    </svg>
    """
    return svg_template.format(
        studio_logo=badge.studio_logo,
        policy_summary=badge.policy_summary,
        timestamp=badge.timestamp,
        policy_hash=badge.policy_hash
    )

def verify_badge(badge: Badge) -> bool:
    expected_policy_hash = hashlib.sha256(badge.policy_summary.encode()).hexdigest()
    return badge.policy_hash == expected_policy_hash

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a GenAI-Ethics badge")
    parser.add_argument("--studio-logo", required=True, help="Studio logo")
    parser.add_argument("--policy-summary", required=True, help="Policy summary")
    args = parser.parse_args()
    badge = generate_badge(args.studio_logo, args.policy_summary)
    svg_badge = create_svg_badge(badge)
    print(svg_badge)
