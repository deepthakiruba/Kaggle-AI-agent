# clip_integration.py
# Example CLIP usage using transformers
from PIL import Image
from transformers import CLIPProcessor, CLIPModel

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

def get_clip_labels(image_path, candidate_labels):
    image = Image.open(image_path).convert("RGB")
    inputs = processor(text=candidate_labels, images=image, return_tensors="pt", padding=True)
    outputs = model(**inputs)
    image_emb = outputs.image_embeds
    text_emb = outputs.text_embeds
    # normalize and compute similarities
    import torch
    image_emb = image_emb / image_emb.norm(p=2, dim=-1, keepdim=True)
    text_emb = text_emb / text_emb.norm(p=2, dim=-1, keepdim=True)
    sims = (image_emb @ text_emb.T).squeeze(0).tolist()
    ranked = sorted(zip(candidate_labels, sims), key=lambda x: x[1], reverse=True)
    return ranked[:5]

if __name__ == "__main__":
    labels = ["chocolate cake","jar","sprinkles","baker","kitchen"]
    print(get_clip_labels("path_to_image.jpg", labels))
