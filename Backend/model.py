# import pandas as pd

# try:
#     df = pd.read_csv("updated_data.csv")
#     df.columns = df.columns.str.strip()
#     print("Dataset loaded ✅")
# except Exception as e:
#     print("Dataset error:", e)
#     df = pd.DataFrame()

# def recommend_schemes(user):

#     if df.empty:
#         return ["Dataset not loaded"]

#     results = []

#     for _, row in df.iterrows():

#         text = " ".join(row.fillna("").astype(str)).lower()

#         score = 0
#         reasons = []

#         # ⭐ STATE MATCH
#         if user["state"].lower() in text:
#             score += 30
#             reasons.append("State match")

#         # ⭐ CATEGORY MATCH
#         if user["category"].lower() in text:
#             score += 25
#             reasons.append("Category eligible")

#         # ⭐ LOW INCOME SCHEMES
#         if "scholarship" in text or "assistance" in text:
#             if user["income"] < 300000:
#                 score += 20
#                 reasons.append("Low income eligible")

#         # ⭐ WOMEN SCHEMES
#         if "women" in text or "girl" in text:
#             if user["gender"].lower() == "female":
#                 score += 15
#                 reasons.append("Women specific scheme")

#         # ⭐ AGE-BASED SCHEMES
#         if "student" in text or "youth" in text:
#             if user["age"] <= 25:
#                 score += 10
#                 reasons.append("Youth eligible")

#         # Only include if some eligibility matched
#         if score > 0:
#             results.append({
#                 "scheme": row.iloc[0],
#                 "match_score": score,
#                 "reason": ", ".join(reasons)
#             })

#     if not results:
#         return ["No matching schemes found"]

#     # Sort by best match
#     results = sorted(results, key=lambda x: x["match_score"], reverse=True)

#     return results[:5]


import pandas as pd

try:
    df = pd.read_csv("updated_data.csv")
    df.columns = df.columns.str.strip()
    print("Dataset loaded ✅")
except Exception as e:
    print("Dataset error:", e)
    df = pd.DataFrame()

def recommend_schemes(user):

    if df.empty:
        return ["Dataset not loaded"]

    results = []

    for _, row in df.iterrows():

        text = " ".join(row.fillna("").astype(str)).lower()

        score = 0
        reasons = []

        # ⭐ SCHEME LEVEL LOGIC
        level = str(row.get("Level", "")).lower()

        if level == "central":
            score += 40
            reasons.append("Central scheme (nationwide eligible)")

        elif level == "state":
            if user["state"].lower() in text:
                score += 40
                reasons.append("State scheme eligible")

        elif level == "local":
            if user["state"].lower() in text:
                score += 30
                reasons.append("Local scheme eligible")

        # ⭐ CATEGORY MATCH
        if user["category"].lower() in text:
            score += 25
            reasons.append("Category eligible")

        # ⭐ LOW INCOME
        if user["income"] < 300000 and ("scholarship" in text or "assistance" in text):
            score += 20
            reasons.append("Low income eligible")

        # ⭐ WOMEN SCHEMES
        if "women" in text or "girl" in text:
            if user["gender"].lower() == "female":
                score += 15
                reasons.append("Women specific scheme")

        # ⭐ AGE-BASED
        if "student" in text or "youth" in text:
            if user["age"] <= 25:
                score += 10
                reasons.append("Youth eligible")

        if score > 0:
            results.append({
                "scheme": row.iloc[0],
                "match_score": score,
                "reason": ", ".join(reasons)
            })

    if not results:
        return ["No matching schemes found"]

    results = sorted(results, key=lambda x: x["match_score"], reverse=True)

    return results[:5]
