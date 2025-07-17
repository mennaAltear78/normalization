#  DCG & nDCG Evaluation in Python

This Python script demonstrates how to calculate **Discounted Cumulative Gain (DCG)** and **Normalized Discounted Cumulative Gain (nDCG)** — two fundamental metrics used to evaluate the quality of ranking systems in search engines, recommender systems, and information retrieval.

---

##  What It Does

- Calculates **DCG@k**: Evaluates the usefulness of a ranked list by reducing the score for items that appear lower in the list.
- Calculates **iDCG@k**: Computes the ideal DCG with items sorted in perfect order (highest relevance first).
- Computes **nDCG@k**: Normalizes DCG by the ideal DCG to produce a score between 0 and 1.

---

##  Example Output

<img width="815" height="489" alt="image" src="https://github.com/user-attachments/assets/c770f885-3a95-4717-ba8f-49b4cae651c4" />
