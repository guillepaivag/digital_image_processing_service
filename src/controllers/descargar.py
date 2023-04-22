import os
import random
from fastapi import FastAPI
from google.cloud import storage

# Create a FastAPI app
app = FastAPI()

# Create a cloud storage client
client = storage.Client()

# Define the bucket name
bucket_name = "vilab-dev.appspot.com"

# Define the directory where to save the images
download_dir = "/tmp/images"

async def download_images():
  # Get the bucket
  bucket = client.get_bucket(bucket_name)

  # Get all the blobs in the bucket
  blobs = bucket.list_blobs()

  # Create a list to store the names of the downloaded images
  images = []

  # Loop through the blobs and download them to the directory
  for blob in blobs:
    # Get the file name
    filename = blob.name.split('/')[-1]
    print("filename",filename.split('/')[-1])

    if not filename:
      continue

    # Create the full file path
    filepath = f"temp/{filename}"

    # Download the blob to the file
    blob.download_to_filename(filepath)

    # Add the file name to the list of images
    images.append(filename)

  # Return the list of downloaded images'
  print("images",images)
  return {"images": images}