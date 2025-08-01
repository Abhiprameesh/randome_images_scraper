from icrawler.builtin import GoogleImageCrawler
import os

# Set the folder where images will be saved
save_dir = "satellite_cloud_images1"
os.makedirs(save_dir, exist_ok=True)

# Create crawler instance
google_crawler = GoogleImageCrawler(storage={"root_dir": save_dir})

# Define your search term (tweak this to get better results)
search_query = "satellite cloud images from satellites near Earth"

# Start crawling (increase max_num as needed)
google_crawler.crawl(keyword=search_query, max_num=1000, min_size=(256, 256))

print(f"\n✅ Done. Images saved to: {save_dir}")
