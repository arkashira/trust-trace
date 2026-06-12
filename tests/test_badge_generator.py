from src.badge_generator import generate_badge, create_svg_badge, verify_badge
import pytest

def test_generate_badge():
    studio_logo = "Test Studio"
    policy_summary = "This is a test policy summary"
    badge = generate_badge(studio_logo, policy_summary)
    assert badge.studio_logo == studio_logo
    assert badge.policy_summary == policy_summary
    assert badge.timestamp is not None
    assert badge.policy_hash is not None

def test_create_svg_badge():
    studio_logo = "Test Studio"
    policy_summary = "This is a test policy summary"
    badge = generate_badge(studio_logo, policy_summary)
    svg_badge = create_svg_badge(badge)
    assert svg_badge is not None
    assert studio_logo in svg_badge
    assert policy_summary in svg_badge

def test_verify_badge():
    studio_logo = "Test Studio"
    policy_summary = "This is a test policy summary"
    badge = generate_badge(studio_logo, policy_summary)
    assert verify_badge(badge) == True

def test_verify_badge_invalid_policy_hash():
    studio_logo = "Test Studio"
    policy_summary = "This is a test policy summary"
    badge = generate_badge(studio_logo, policy_summary)
    badge.policy_hash = "invalid_policy_hash"
    assert verify_badge(badge) == False
