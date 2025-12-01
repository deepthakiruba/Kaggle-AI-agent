# hashtag_agent.py
import re
POP = {"chocolatecake":0.9,"dessertlover":0.85,"jarcake":0.6,"homebaker":0.5,"coimbatoreeats":0.4}
def normalize(t): return re.sub(r'[^A-Za-z0-9]','',t).lower()
def generate_hashtags(caption, vision_labels, top_n=12):
    import re
    words = re.findall(r'\w+', caption)
    candidates = set([w.lower() for w in words if len(w)>2] + [normalize(x) for x in vision_labels])
    scored = []
    for c in candidates:
        score = POP.get(c, 0.1)
        scored.append((c, score))
    scored.sort(key=lambda x:x[1], reverse=True)
    selected = [t for t,s in scored[:top_n]]
    final = ["#"+t for t in selected]
    return {"final": " ".join(final), "list": final}

if __name__ == "__main__":
    print(generate_hashtags("Baked with love — chocolate dreams come true", ["jar","cake","sprinkles"]))