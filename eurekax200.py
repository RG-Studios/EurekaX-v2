import random
import json
import os
import uuid
from datetime import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Sample domains with real topics
knowledge_base = {
    "AI": [
        "reinforcement learning for robotics",
        "transformers in natural language processing",
        "graph neural networks for chemistry"
    ],
    "Aerospace": [
        "aerodynamic modeling using CFD",
        "rocket trajectory optimization",
        "satellite orbit estimation"
    ],
    "Neuroscience": [
        "synaptic plasticity in learning",
        "neural circuits for decision making",
        "brain-inspired computing"
    ],
    "Quantum Computing": [
        "superposition for parallel computation",
        "qubit error correction",
        "quantum annealing for optimization"
    ],
    "Biotech": [
        "CRISPR gene editing systems",
        "synthetic biology circuits",
        "protein folding prediction with AI"
    ]
}

INSIGHT_FILE = "eurekax_insights.json"

def extract_vectorizer():
    texts = [text for domain in knowledge_base.values() for text in domain]
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(texts)
    return vectorizer, texts, X

def generate_hypothesis():
    d1, d2 = random.sample(list(knowledge_base.keys()), 2)
    topic1 = random.choice(knowledge_base[d1])
    topic2 = random.choice(knowledge_base[d2])
    hypothesis = f"Can we apply '{topic1}' from {d1} to solve '{topic2}' in {d2}?"
    return d1, d2, topic1, topic2, hypothesis

def calculate_novelty(t1, t2, vectorizer):
    v = vectorizer.transform([t1, t2])
    score = 1 - cosine_similarity(v[0], v[1])[0][0]  # 1 - similarity = novelty
    return round(score, 3)

# Simulated feasibility score (random + keyword based)
def simulate_feasibility(t1, t2):
    synergy_keywords = ["optimization", "prediction", "learning", "circuit"]
    match = sum(word in t1.lower() + t2.lower() for word in synergy_keywords)
    base = 0.4 + 0.1 * match
    return round(min(1.0, base + random.uniform(0.0, 0.4)), 3)

def compute_insight_score(novelty, feasibility):
    return round((novelty * 0.6 + feasibility * 0.4), 3)

def classify_score(score):
    if score >= 0.75:
        return "Breakthrough"
    elif score >= 0.6:
        return "Promising"
    elif score >= 0.4:
        return "Uncertain"
    else:
        return "Rejected"

# Save to local memory file
def save_insight(hypothesis, topic1, topic2, novelty, feasibility, score, verdict):
    insight = {
        "id": str(uuid.uuid4()),
        "timestamp": datetime.now().isoformat(),
        "hypothesis": hypothesis,
        "domain_1": topic1,
        "domain_2": topic2,
        "novelty": novelty,
        "feasibility": feasibility,
        "score": score,
        "verdict": verdict
    }

    if not os.path.exists(INSIGHT_FILE):
        with open(INSIGHT_FILE, "w") as f:
            json.dump([insight], f, indent=2)
    else:
        with open(INSIGHT_FILE, "r+") as f:
            data = json.load(f)
            data.append(insight)
            f.seek(0)
            json.dump(data, f, indent=2)

def print_insight(hypothesis, novelty, feasibility, score, verdict):
    print(f"\n🧠 Hypothesis: {hypothesis}")
    print(f"📈 Novelty Score     : {novelty}")
    print(f"🔬 Feasibility Score : {feasibility}")
    print(f"💡 Final Insight Score: {score}")
    print(f"🏆 Verdict: {verdict}")

def run_discovery(n=5, min_score=0.5):
    print("🚀 EurekaX Autonomous Discovery Engine v2.0\n")
    vectorizer, _, _ = extract_vectorizer()

    for _ in range(n):
        d1, d2, t1, t2, hypothesis = generate_hypothesis()
        novelty = calculate_novelty(t1, t2, vectorizer)
        feasibility = simulate_feasibility(t1, t2)
        score = compute_insight_score(novelty, feasibility)
        verdict = classify_score(score)

        if score >= min_score:
            save_insight(hypothesis, t1, t2, novelty, feasibility, score, verdict)
        print_insight(hypothesis, novelty, feasibility, score, verdict)

if __name__ == "__main__":
    run_discovery(n=5)
