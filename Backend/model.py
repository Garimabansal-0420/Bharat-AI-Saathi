import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "schemes.json")

def load_schemes():
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def calculate_score(user, scheme):
    score = 0

    age_min = scheme.get("age_min", 0)
    age_max = scheme.get("age_max", 100)

    if age_min <= user["age"] <= age_max:
        score += 20

    if scheme.get("gender", "any") in ["any", user["gender"]]:
        score += 15

    if user["income"] <= scheme.get("income_max", 9999999):
        score += 25

    if scheme.get("state", "all") in ["all", user["state"]]:
        score += 20

    if scheme.get("category", "all") in ["all", user["category"]]:
        score += 20

    return score

def recommend_schemes(user):
    schemes = load_schemes()
    results = []

    for scheme in schemes:
        score = calculate_score(user, scheme)

        if score > 40:
            scheme_copy = scheme.copy()
            scheme_copy["eligibility_score"] = score
            results.append(scheme_copy)

    return sorted(results, key=lambda x: x["eligibility_score"], reverse=True)
