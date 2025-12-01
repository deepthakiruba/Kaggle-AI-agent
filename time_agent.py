# time_agent.py
CATEGORY = {"food":["18:30 IST","20:30 IST","10:00 IST"], "product":["10:00 IST","16:00 IST","19:00 IST"]}
def recommend_times(category="food", user_history=None):
    slots = CATEGORY.get(category, CATEGORY["food"])
    res = [{"time":s, "rationale":"optimal for "+category, "confidence":0.7} for s in slots]
    return res
if __name__ == "__main__":
    print(recommend_times("food"))