import json
from dataclasses import dataclass
from datetime import datetime
import hashlib
import argparse

@dataclass
class Asset:
    asset_type: str
    ai_tool: str
    human_oversight_level: str

class AuditTrail:
    def __init__(self):
        self.audit_logs = []

    def add_log(self, asset):
        log = {
            "timestamp": datetime.now().isoformat(),
            "asset_type": asset.asset_type,
            "ai_tool": asset.ai_tool,
            "human_oversight_level": asset.human_oversight_level,
            "hash": self.calculate_hash(asset)
        }
        self.audit_logs.append(log)

    def calculate_hash(self, asset):
        data = json.dumps({
            "asset_type": asset.asset_type,
            "ai_tool": asset.ai_tool,
            "human_oversight_level": asset.human_oversight_level
        }, sort_keys=True)
        return hashlib.sha256(data.encode()).hexdigest()

    def export_to_csv(self, filename):
        with open(filename, "w") as f:
            f.write("Timestamp,Asset Type,AI Tool,Human Oversight Level,Hash\n")
            for log in self.audit_logs:
                f.write(f"{log['timestamp']},{log['asset_type']},{log['ai_tool']},{log['human_oversight_level']},{log['hash']}\n")

    def export_to_pdf(self, filename):
        # This is a simplified example and does not actually generate a PDF
        with open(filename, "w") as f:
            f.write("Audit Trail Report\n")
            for log in self.audit_logs:
                f.write(f"Timestamp: {log['timestamp']}\n")
                f.write(f"Asset Type: {log['asset_type']}\n")
                f.write(f"AI Tool: {log['ai_tool']}\n")
                f.write(f"Human Oversight Level: {log['human_oversight_level']}\n")
                f.write(f"Hash: {log['hash']}\n\n")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--asset-type", help="Asset type")
    parser.add_argument("--ai-tool", help="AI tool used")
    parser.add_argument("--human-oversight-level", help="Human oversight level")
    parser.add_argument("--export-csv", help="Export to CSV file")
    parser.add_argument("--export-pdf", help="Export to PDF file")
    args = parser.parse_args()

    audit_trail = AuditTrail()
    asset = Asset(args.asset_type, args.ai_tool, args.human_oversight_level)
    audit_trail.add_log(asset)

    if args.export_csv:
        audit_trail.export_to_csv(args.export_csv)
    if args.export_pdf:
        audit_trail.export_to_pdf(args.export_pdf)

if __name__ == "__main__":
    main()
