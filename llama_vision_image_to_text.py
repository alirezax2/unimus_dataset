# -*- coding: utf-8 -*-
"""Llama vision image to text.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cWGuZ26j4tWLfkR7tUmiLiOLohUM5U78
"""

!pip install -q huggingface_hub

import os

myHF = "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"
os.environ["HF_TOKEN"] = myHF

image_url = fr"https://c8.alamy.com/comp/2AJD2ET/gean-archeology-an-introduction-to-the-archeology-of-prehistoric-greece-fig-90-carnelian-seal-stone-with-pictographs-j-crete-enlarged-2AJD2ET.jpg"

from huggingface_hub import InferenceClient

# Initialize the client
client = InferenceClient("meta-llama/Llama-3.2-11B-Vision-Instruct")
# Send image queries through remote URL or base64 encoded URL
output = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {"url": image_url},
                },
                {
                    "type": "text",
                    "text": "generate a headline for this image.",
                },
            ],
        },
    ],
)

print(output.choices[0].message.content)
# Expected output: A determined figure of Lady Liberty stands tall, holding a torch aloft, atop a pedestal on an island.




