from icrawler.builtin import BingImageCrawler
import os

# Create directory to save images
save_dir = "satellite_cloud_images1"
os.makedirs(save_dir, exist_ok=True)

# Set up the crawler
crawler = BingImageCrawler(storage={"root_dir": save_dir})

# Define the search query
search_query = "Cloud images patterns from space"

# Start crawling
crawler.crawl(keyword=search_query, max_num=800, min_size=(256, 256), file_idx_offset=0)

print(f"\n✅ Download complete. Images saved in '{save_dir}' folder.")
