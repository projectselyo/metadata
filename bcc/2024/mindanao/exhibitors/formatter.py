# List of names and image links
names = [
    "Chona's Toys and Lovelivious",
    "Apple's Toy Crib and Sundries 3D",
    "Oshi Toy Shop",
    "Sunny Side Up Senpai",
    "The Bloom",
    "Toys4Juan"
]

image_links = [
    "https://i.imgur.com/tI15nZs.jpeg",
    "https://i.imgur.com/nNtx44C.jpeg",
    "https://i.imgur.com/gGHz4Jq.jpeg",
    "https://i.imgur.com/pDCUY5j.jpeg",
    "https://i.imgur.com/mpworBi.jpeg",
    "https://i.imgur.com/gEZw6ci.jpeg"
]

# Create the entities list
entities = []

for name, image in zip(names, image_links):
    # Add " (BCC2024)" to the name
    full_name = f"{name} (BCC2024)"
    
    entity = {
        "name": full_name,
        "image": image
    }
    entities.append(entity)

# Output the result as formatted text
print("entities = [")
for entity in entities:
    print(f"    {{")
    print(f"        \"name\": \"{entity['name']}\",")
    print(f"        \"image\": \"{entity['image']}\"")
    print(f"    }},")
print("    # Add more entities as needed")
print("]")


