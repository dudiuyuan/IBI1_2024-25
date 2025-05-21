import xml.dom.minidom as minidom
import xml.sax
import time
from datetime import datetime

# DOM Parser
def parse_dom(file_path):
    start = datetime.now()

    doc = minidom.parse(file_path)
    terms = doc.getElementsByTagName('term')

    max_counts = {
        "molecular_function": (None, 0),
        "biological_process": (None, 0),
        "cellular_component": (None, 0)
    }

    for term in terms:
        ns = term.getElementsByTagName('namespace')[0].firstChild.nodeValue
        is_a_tags = term.getElementsByTagName('is_a')
        is_a_count = len(is_a_tags)
        if ns in max_counts and is_a_count > max_counts[ns][1]:
            term_id = term.getElementsByTagName('id')[0].firstChild.nodeValue
            max_counts[ns] = (term_id, is_a_count)

    end = datetime.now()
    dom_time = (end - start).total_seconds()
    print("=== DOM Results ===")
    for ns, (term_id, count) in max_counts.items():
        print(f"{ns}: {term_id} with {count} is_a references")
    print(f"DOM Time: {dom_time:.4f} seconds\n")
    return dom_time

# SAX Parser
class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_tag = ""
        self.name_space = ""
        self.id = ""
        self.is_a_count = 0
        self.max_counts = {
            "molecular_function": ("", 0),
            "biological_process": ("", 0),
            "cellular_component": ("", 0)
        }
        self.collecting_term = False

    def startElement(self, tag, attributes):
        self.current_tag = tag
        if tag == "term":
            self.is_a_count = 0
            self.id = ""
            self.name_space = ""
            self.collecting_term = True

    def characters(self, content):
        if self.current_tag == "id" and self.collecting_term:
            self.id += content.strip()
        elif self.current_tag == "namespace" and self.collecting_term:
            self.name_space += content.strip()
        elif self.current_tag == "is_a" and self.collecting_term:
            self.is_a_count += 1

    def endElement(self, tag):
        if tag == "term":
            if self.name_space in self.max_counts and self.is_a_count > self.max_counts[self.name_space][1]:
                self.max_counts[self.name_space] = (self.id, self.is_a_count)
            self.collecting_term = False
        self.current_tag = ""

def parse_sax(file_path):
    start = datetime.now()
    handler = GOHandler()
    xml.sax.parse(file_path, handler)
    end = datetime.now()
    sax_time = (end - start).total_seconds()

    print("=== SAX Results ===")
    for ns, (term_id, count) in handler.max_counts.items():
        print(f"{ns}: {term_id} with {count} is_a references")
    print(f"SAX Time: {sax_time:.4f} seconds\n")
    return sax_time

# Run
file_path = "D:/IBI/IBI1_2024-25/Practical14/go_obo.xml"

dom_runtime = parse_dom(file_path)
sax_runtime = parse_sax(file_path)

if dom_runtime < sax_runtime:
    print("# DOM parser was faster.")
else:
    print("# SAX parser was faster.")
