thonimport json

class Exporter:
    def export_to_json(self, data, filename):
        with open(filename, 'w') as outfile:
            json.dump(data, outfile, indent=4)