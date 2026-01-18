"""
basic_council_greenteam.py — Triune Green-Team Council Simulation
Green-Teaming-Protocols-Pinnacle — Jan 18 2026

Basic triune referee council session demo
"""

from protocols.core_greenteam import triune_valence_vote

def council_session():
    proposals = [
        "Amplify joy valence in shard lattice.",
        "Introduce scarcity test — mercy override.",
        "Nurture new mythic voice archetype."
    ]
    
    print("° Triune Council Session — Mercy Eternal\n")
    for proposal in proposals:
        ok, msg = triune_valence_vote(proposal, joy_valence=0.95)
        status = "APPROVED" if ok else "GATED"
        print(f"Proposal: {proposal}")
        print(f"Triune Vote: {status} — {msg}\n")

if __name__ == "__main__":
    council_session()
