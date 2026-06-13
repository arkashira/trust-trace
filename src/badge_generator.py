import json
import hashlib
import hmac
import base64
import argparse
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Studio:
    name: str
    logo: str
    policy_summary: str

@dataclass
class Badge:
    studio: Studio
    timestamp: str
    policy_hash: str
    signature: str

def generate_badge(studio: Studio, secret_key: str) -> Badge:
    timestamp = datetime.now().isoformat()
    policy_hash = hashlib.sha256(studio.policy_summary.encode()).hexdigest()
    signature = hmac.new(secret_key.encode(), (timestamp + policy_hash).encode(), hashlib.sha256).hexdigest()
    return Badge(studio, timestamp, policy_hash, signature)

def generate_svg_badge(badge: Badge) -> str:
    svg = f"""
    <svg width="200" height="150">
        <rect x="0" y="0" width="200" height="150" fill="#ffffff" rx="10"/>
        <image x="10" y="10" width="50" height="50" href="{badge.studio.logo}"/>
        <text x="70" y="30" font-size="20" fill="#000000">{badge.studio.name}</text>
        <text x="10" y="70" font-size="15" fill="#000000">{badge.studio.policy_summary}</text>
        <text x="10" y="90" font-size="10" fill="#000000">Timestamp: {badge.timestamp}</text>
        <text x="10" y="110" font-size="10" fill="#000000">Policy Hash: {badge.policy_hash}</text>
        <text x="10" y="130" font-size="10" fill="#000000">Signature: {badge.signature}</text>
    </svg>
    """
    return svg

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--studio-name", required=True)
    parser.add_argument("--studio-logo", required=True)
    parser.add_argument("--policy-summary", required=True)
    parser.add_argument("--secret-key", required=True)
    args = parser.parse_args()
    studio = Studio(args.studio_name, args.studio_logo, args.policy_summary)
    badge = generate_badge(studio, args.secret_key)
    svg_badge = generate_svg_badge(badge)
    print(svg_badge)

if __name__ == "__main__":
    main()
