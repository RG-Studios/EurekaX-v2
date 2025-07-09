<h1 align="center">🚀 EurekaX-v2</h1>
<p align="center">
  <b>Autonomous Cross-Domain Discovery Engine</b><br>
  An intelligent AI algorithm that generates groundbreaking ideas by fusing knowledge across multiple domains like AI, Quantum Computing, Neuroscience, Aerospace, and Biotech.
</p>

---

## 📘 Overview

**EurekaX** is a powerful, lightweight, and extendable AI research engine that simulates the role of a human researcher — autonomously generating, scoring, classifying, and storing new research hypotheses.

> Designed to serve as the foundation for innovation at organizations like **Meta, Google, SpaceX, NASA, ISRO**, and research labs.

---

## 🎯 Core Features

| Feature | Description |
|--------|-------------|
| 🔍 **Cross-Domain Hypothesis Generation** | Randomly pairs concepts from two fields to ask scientific "What if?" questions |
| 📈 **Novelty Estimation** | Uses TF-IDF + cosine similarity to determine how unique the idea is |
| 🧠 **Feasibility Scoring** | Simulates whether an idea is realistic based on topic overlap |
| 💡 **Insight Scoring System** | Combines novelty & feasibility to compute a score (0.0–1.0) |
| 🏆 **Verdict Classification** | Classifies ideas as `Breakthrough`, `Promising`, `Uncertain`, or `Rejected` |
| 💾 **Memory Storage** | Logs all accepted insights to a persistent JSON knowledge base |

---

## 🛠 How It Works

1. **Select Two Domains**: Randomly selects two distinct scientific fields from the knowledge base.
2. **Pick Topics**: Chooses one topic from each domain.
3. **Form Hypothesis**: Constructs a sentence like:  
   _"Can we apply 'X' from AI to solve 'Y' in Aerospace?"_
4. **Calculate Novelty**: TF-IDF vectorizes both topics and calculates 1 - cosine similarity.
5. **Estimate Feasibility**: Uses keyword matching and heuristic scoring to simulate feasibility.
6. **Compute Insight Score**: Weighted sum of novelty and feasibility.
7. **Classify & Store**: Saves high-scoring ideas to `eurekax_insights.json`.

---

## 🧠 Example Output

```text
🚀 EurekaX Autonomous Discovery Engine v2.0

🧠 Hypothesis: Can we apply 'transformers in natural language processing' from AI to solve 'protein folding prediction with AI' in Biotech?
📈 Novelty Score     : 0.812
🔬 Feasibility Score : 0.667
💡 Final Insight Score: 0.754
🏆 Verdict: Breakthrough
