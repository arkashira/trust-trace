from audit_trail import AuditTrail, Asset
import json
import datetime
import hashlib
import pytest

def test_add_log():
    audit_trail = AuditTrail()
    asset = Asset("image", "tool1", "high")
    audit_trail.add_log(asset)
    assert len(audit_trail.audit_logs) == 1
    log = audit_trail.audit_logs[0]
    assert log["timestamp"] is not None
    assert log["asset_type"] == "image"
    assert log["ai_tool"] == "tool1"
    assert log["human_oversight_level"] == "high"
    assert log["hash"] is not None

def test_calculate_hash():
    asset = Asset("image", "tool1", "high")
    audit_trail = AuditTrail()
    hash = audit_trail.calculate_hash(asset)
    data = json.dumps({
        "asset_type": asset.asset_type,
        "ai_tool": asset.ai_tool,
        "human_oversight_level": asset.human_oversight_level
    }, sort_keys=True)
    expected_hash = hashlib.sha256(data.encode()).hexdigest()
    assert hash == expected_hash

def test_export_to_csv():
    audit_trail = AuditTrail()
    asset = Asset("image", "tool1", "high")
    audit_trail.add_log(asset)
    audit_trail.export_to_csv("test.csv")
    with open("test.csv", "r") as f:
        lines = f.readlines()
        assert len(lines) == 2
        assert lines[0].strip() == "Timestamp,Asset Type,AI Tool,Human Oversight Level,Hash"
        log = lines[1].strip().split(",")
        assert log[0] is not None
        assert log[1] == "image"
        assert log[2] == "tool1"
        assert log[3] == "high"
        assert log[4] is not None

def test_export_to_pdf():
    audit_trail = AuditTrail()
    asset = Asset("image", "tool1", "high")
    audit_trail.add_log(asset)
    audit_trail.export_to_pdf("test.pdf")
    with open("test.pdf", "r") as f:
        lines = f.readlines()
        assert len(lines) > 0
        assert lines[0].strip() == "Audit Trail Report"
