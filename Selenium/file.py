"""Selenium Test"""
import csv
import json

class File:
    """
    This class defines a method to be able to create files
    """
    @staticmethod
    def save_csv(data):
        """
        This method will create and write data in a csv file
        """
        file = open("data.csv", 'w', encoding="utf-8")
        with file:
            writer = csv.writer(file)
            writer.writerows(data)

    @staticmethod
    def save_json(data):
        """
        This method will create and write data in a JSON file
        """
        with open('bonus.json', 'w', encoding="utf-8") as file:
            json.dump(data, file, indent=4)
