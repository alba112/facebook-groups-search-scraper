thonimport time

def wait_for_page_load():
    time.sleep(3)  # Simulate waiting for dynamic content to load

def log_scraping_time(start_time):
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Scraping completed in {elapsed_time:.2f} seconds.")