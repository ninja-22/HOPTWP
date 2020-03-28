#!/usr/local/bin/python

import xml.etree.ElementTree as ET
import sys

class XMLParser():
    def __init__(self, xml):
        self.xml = xml

    def parse(self, parse_type = "doc"):
        if parse_type == "doc":
            root = ET.parse(self.xml).getroot()
        else:
            root = ET.fromstring(self.xml)
        tag = root.tag
        print(f"Root tag is: {tag}")            # root tag of the entire xml document (<employees> in test.xml)
        attributes = root.attrib
        print("Root attributes are: ")          # root attributes are defined in the root tag (department and location, along with the values in test.xml)
        for k, v in attributes.items():          # if we do not know the names of the attributes, use this method to map the attribute and value into a dictionary k-v pair
            print(f"\t {k}: {v}")
        print("\n Printing node details without knowing subtags: ")

        for employee in root:
            print("\n--------------------------------------------")
            for element in employee:
                ele_name = element.tag                  # name of the xml tag/attribute
                ele_value = employee.find(element.tag).text
                print(f"\t\t {ele_name}: {ele_value}")

        print("\n\nPrinting node details specifying subtags: ")
        for employee in root.findall("employee"):               # in employee tag
            print("\n--------------------------------------------")
            print(f'\t\tName: {employee.find("name").text}')        # search for "name" tag that is a subtag of the employee tag, print its value
            print(f'\t\tAge: {employee.find("age").text}')
            print(f'\t\tSalary: {employee.find("salary").text}')
            print(f'\t\tManager ID: {employee.find("manager_id").text}')
            print(f'\t\tDOJ: {employee.find("doj").text}')

obj = XMLParser(sys.argv[1])                # expect an argument (aka the filename passed to the script)
obj.parse()             # access the parse method inside the class



