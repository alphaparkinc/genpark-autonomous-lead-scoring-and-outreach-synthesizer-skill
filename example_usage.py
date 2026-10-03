"""Example usage for Autonomous Lead Scoring & Outreach Synthesizer."""
from client import LeadScoringOutreachSynthesizer

if __name__ == "__main__":
    profile = {
        "name": "Sarah Connor",
        "company": "Cyberdyne Solutions",
        "company_size": 250,
        "title": "VP of Engineering",
        "target_need": "automating continuous agent evaluation",
        "intent_signals": ["viewed_pricing", "hiring_in_domain"]
    }
    result = LeadScoringOutreachSynthesizer.evaluate_and_synthesize(profile)
    print("Lead Score:", result["score"])
    print("Tier:", result["tier"])
    print("Outreach Message:\n", result["personalized_outreach"])
