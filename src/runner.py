thonimport json
import os
from extractors.facebook_parser import FacebookParser
from outputs.exporters import Exporter

def main():
    # Load settings
    with open('src/config/settings.example.json', 'r') as file:
        settings = json.load(file)
    
    # Initialize Facebook parser and exporter
    parser = FacebookParser(settings['keyword'], settings['max_groups'])
    exporter = Exporter()

    # Scrape the data
    groups = parser.scrape_groups()

    # Export the data
    exporter.export_to_json(groups, 'data/sample.json')

if __name__ == "__main__":
    main()