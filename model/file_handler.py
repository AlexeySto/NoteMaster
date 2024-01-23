import json
import os
import datetime
from model.note import Note


class File_handler:

    PATH_FILE = "files\data.txt"

    def save_notes(data):
        data_dict = {}
        data_dict["note"] = []
        i = 1
        for x in data:
            data_dict["note"].append({ "id": i, "datatime": x.data_time, "titel": x.name_note, "text": x.body_note })
            i += 1
        with open(File_handler.PATH_FILE, 'w') as outfile:
            json.dump(data_dict, outfile)

    def load_notes():
        data_list = []
        if (os.path.isfile(File_handler.PATH_FILE)):
            with open(File_handler.PATH_FILE) as json_file:
                data = json.load(json_file)
                for x in data["note"]:
                    name_note = x["titel"]
                    body_note = x["text"]
                    note = Note(name_note, body_note)
                    note.data_time = x["datatime"]
                    data_list.append(note)
        return data_list
