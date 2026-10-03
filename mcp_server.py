"""MCP server for Autonomous Lead Scoring & Outreach Synthesizer."""
import sys
import json
from client import LeadScoringOutreachSynthesizer

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "score_and_synthesize_outreach",
                "description": "Scores a lead profile and drafts personalized outreach copy",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "lead_profile": {"type": "object", "description": "Candidate profile details"}
                    },
                    "required": ["lead_profile"]
                }
            }]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        if params.get("name") == "score_and_synthesize_outreach":
            profile = params.get("arguments", {}).get("lead_profile", {})
            res = LeadScoringOutreachSynthesizer.evaluate_and_synthesize(profile)
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()
