import json
import os

# Define the list of entities with their names and image links
entities = [
    {
        "name": "Chona's Toys and Lovelivious (BCC2024)",
        "image": "https://i.imgur.com/tI15nZs.jpeg"
    },
    {
        "name": "Apple's Toy Crib and Sundries 3D (BCC2024)",
        "image": "https://i.imgur.com/nNtx44C.jpeg"
    },
    {
        "name": "Oshi Toy Shop (BCC2024)",
        "image": "https://i.imgur.com/gGHz4Jq.jpeg"
    },
    {
        "name": "Sunny Side Up Senpai (BCC2024)",
        "image": "https://i.imgur.com/pDCUY5j.jpeg"
    },
    {
        "name": "The Bloom (BCC2024)",
        "image": "https://i.imgur.com/mpworBi.jpeg"
    },
    {
        "name": "Toys4Juan (BCC2024)",
        "image": "https://i.imgur.com/gEZw6ci.jpeg"
    },
    # Add more entities as needed
]

# Directory to save the JSON files
output_dir = "metadata"

# Ensure the directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Loop through each entity and create a JSON file
for entity in entities:
    # Use the constant symbol "BCC2024"
    symbol = "BCC2024"

    # Remove "(BCC2024)" or other tags from the name for the description
    clean_name = entity["name"].replace(" (BCC2024)", "").replace(" (TEX2024)", "")

    # Create the description by replacing the placeholder [name]
    description = f"Visited {clean_name} booth during BCC2024 Mindanao"
    
    # Create the metadata structure
    metadata = {
        "name": entity["name"],
        "description": description,
        "symbol": symbol,  # Constant symbol
        "image": entity["image"],
        "attributes": [
            {
                "trait_type": "event",
                "value": "Blockchain Campus Conference"
            },
            {
                "trait_type": "year",
                "value": "2024"
            },
            {
                "trait_type": "region",
                "value": "Mindanao"
            },
            {
                "trait_type": "website",
                "value": "https://blockchaincampusconference.com/"
            }
        ]
    }

    # Define the output filename using the lowercase name without spaces
    output_filename = f"{output_dir}/{clean_name.lower().replace(' ', '')}.json"

    # Write the metadata to a JSON file
    with open(output_filename, "w") as json_file:
        json.dump(metadata, json_file, indent=4)

    print(f"Metadata for {entity['name']} saved to {output_filename}")
