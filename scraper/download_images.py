import argparse
import json
import time
import os

import requests
from PIL import Image


def parse_jsonl(file_path: str) -> list[dict]:
    """
    Parse a jsonl file into a list of dictionaries

    Args:
        file_path (str): Path to file containing jsonl

    Returns:
        jsonl (list): List of dictionaries
    """
    with open(file_path, 'r') as f:
        jsonl = [json.loads(line) for line in f]

    return jsonl

def download_image_from_url(url: str) -> Image:
    """
    Download image from url

    Args:
        url (str): Url to image
    
    Returns:
        image (Image): Image object
    """
    img_data = requests.get(url, stream=True)
    image = Image.open(img_data.raw)
    return image

def parse_args() -> argparse.Namespace:
    """
    Parse command line arguments

    Returns:
        args (argparse.Namespace): Parsed command line arguments
    """
    parser = argparse.ArgumentParser(description='Download images from jsonl file')
    parser.add_argument('jsonl_file', type=str, help='Path to jsonl file')
    parser.add_argument('output_dir', type=str, help='Path to output directory')
    parser.add_argument('--delay', type=float, default=0., help='Delay between requests')
    parser.add_argument('--overwrite', action='store_true', help='Overwrite existing files')

    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    jsonl = parse_jsonl(args.jsonl_file)

    for item in jsonl:
        image_urls = item['images']
        for image_url in image_urls:
            # Get image name and output path
            image_name = image_url.split('/')[-1]
            image_path = f'{args.output_dir}/{image_name}'
            if not args.overwrite and os.path.exists(image_path):
                print(f"Skipping {image_url} as {image_path} already exists")
                continue

            # Download image
            image = download_image_from_url(image_url)

            # Save image
            image.save(image_path)
            print(f"Saved {image_url} to {image_path}")

            # Delay between requests
            time.sleep(args.delay)


if __name__ == '__main__':
    main()
