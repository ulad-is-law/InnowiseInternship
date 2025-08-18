import json

class ResultSaver:
    def save_json(self, data, columns, filepath):
        try:
            result_list = [dict(zip(columns, row)) for row in data]
            json_file = json.dumps(result_list, default=str, indent=4)

            with open(filepath, "w") as f:
                f.write(json_file)
        except Exception as e:
            print(f"error happened during saving: {e}")
