import pytest
import sys
from badge_generator import Studio, Badge, generate_badge, generate_svg_badge

def test_generate_badge():
    studio = Studio("Test Studio", "https://example.com/logo.png", "This is a test policy summary.")
    secret_key = "secret_key"
    badge = generate_badge(studio, secret_key)
    assert badge.studio == studio
    assert badge.timestamp is not None
    assert badge.policy_hash is not None
    assert badge.signature is not None

def test_generate_svg_badge():
    studio = Studio("Test Studio", "https://example.com/logo.png", "This is a test policy summary.")
    secret_key = "secret_key"
    badge = generate_badge(studio, secret_key)
    svg_badge = generate_svg_badge(badge)
    assert svg_badge is not None
    assert "<svg" in svg_badge
    assert "</svg>" in svg_badge

def test_main(capsys):
    sys.argv = ["badge_generator.py", "--studio-name", "Test Studio", "--studio-logo", "https://example.com/logo.png", "--policy-summary", "This is a test policy summary.", "--secret-key", "secret_key"]
    import badge_generator
    badge_generator.main()
    captured = capsys.readouterr()
    assert captured.out is not None
