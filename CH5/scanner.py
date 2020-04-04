#!/usr/local/bin/python3.7

import subprocess as sp
import os
import xml.etree.ElementTree as ET

class NmapPy():
    def __init__(self, command=[]):
        self.command = command

    def scan(self):
        try:
            p = sp.Popen(self.command, shell=False, stdout=sp.PIPE, stderr=sp.PIPE)
            out, err = p.communicate()
            print("\n The NMAP scan is complete.")
            xml_str = str(out)
            root = ET.fromstring(xml_str)
            tag = root.tag
            hosts = []
            for host in root.findall("host"):
                details = {"address":host.find("address").attrib.get("addr"), "name":host.find("hostnames").find("hostname").attrib.get("name")}
                port_list = []
                print(str(host))
                ports = host.find("ports")
                for port in ports:
                    port_details = {"port":port.attrib.get("portid"), "protocol":port.attrib.get("protocol")}
                    service = port.find("service")
                    state = port.find("state")
                    if service is not None:
                        port_details.update({"service":service.attrib.get("name"), "product":service.attrib.get("product", ""), "version":service.attrib.get("version", ""), "extrainfo":service.attrib.get("extrainfo", ""), "ostype":service.attrib.get("ostype", ""), "cpe":service.attrib.get("cpe", "")})
                        if state is not None:
                            port_details.update({"state":state.attrib.get("state"), "reason":state.attrib.get("reason", "")})
                        port_list.append(port_details)
                    details["ports"] = port_list
                    hosts.append(details)
                for host in hosts:
                    print("----------------------------------")
                    print(f'Name: {str(host.get("name",""))}')
                    print(f'IP: {str(host.get("address", ""))}')
                    print("Services: ")
                    for port in host["ports"]:

                        print("\t Service: ")
                        print("\t ----------------------------")
                        for k, v in port.items():
                            print(f'\t\t {str(k)}: {str(v)}')
                    print("----------------------------------")
        except Exception as ex:
            print(f"Exception caught: {ex}")

nmap = NmapPy(["nmap", "-Pn", "-sV", "127.0.0.1", "-oX", "test"])
nmap.scan()