"""Autonomous Lead Scoring & Outreach Synthesizer.
100% Python Standard Library.
"""

import json

class LeadScoringOutreachSynthesizer:
    """Scores outbound lead profiles, evaluates purchase intent, and synthesizes personalized messages."""
    
    @staticmethod
    def evaluate_and_synthesize(lead_profile: dict) -> dict:
        score = 0
        factors = []
        
        size = lead_profile.get("company_size", 0)
        if size > 500:
            score += 35
            factors.append("Enterprise scale (+35)")
        elif size > 50:
            score += 25
            factors.append("Mid-market scale (+25)")
        else:
            score += 15
            factors.append("Early-stage/SMB scale (+15)")
            
        role = lead_profile.get("title", "").lower()
        if any(kw in role for kw in ["founder", "ceo", "cto", "vp", "head of"]):
            score += 35
            factors.append("High decision-maker authority (+35)")
        elif any(kw in role for kw in ["lead", "manager", "director", "engineer"]):
            score += 20
            factors.append("Operational influencer (+20)")
            
        signals = lead_profile.get("intent_signals", [])
        if "viewed_pricing" in signals:
            score += 15
            factors.append("High intent: viewed pricing (+15)")
        if "hiring_in_domain" in signals:
            score += 15
            factors.append("Growth signal: hiring in domain (+15)")
            
        score = min(score, 100)
        tier = "Tier A (High Intent)" if score >= 75 else ("Tier B (Warm)" if score >= 50 else "Tier C (Nurture)")
        
        lead_name = lead_profile.get("name", "there")
        company = lead_profile.get("company", "your team")
        domain_need = lead_profile.get("target_need", "accelerating workflows")
        
        message = (
            f"Hi {lead_name},\n\n"
            f"Noticed {company}'s recent momentum and focus on {domain_need}. "
            f"We've helped teams in similar stages streamline operations by up to 60% without engineering overhead. "
            f"Would you be open to a quick 5-minute walkthrough this Thursday?\n\nBest,\nGenPark Growth Team"
        )
        
        return {
            "score": score,
            "tier": tier,
            "evaluated_factors": factors,
            "recommended_channel": "Email & LinkedIn" if score >= 70 else "Nurture Newsletter",
            "personalized_outreach": message
        }
