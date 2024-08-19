import mwxml

# Path to the WikiDump XML file
dump_file = '[17]MileStoneProject\\wiki.xml'

# Path to the output cleaned XML file
cleaned_file = '[17]MileStoneProject\\cleaned.txt'

# Function to clean the XML file
def clean_xml(input_file, output_file):
    with open(output_file, 'w', encoding='utf-8') as out_file:
        dump = mwxml.Dump.from_file(input_file)
        for page in dump:
            if page.namespace == 0:  # Filter only main namespace pages
                revisions = [rev.text for rev in page]
                cleaned_text = '\n'.join(revisions)
                out_file.write(cleaned_text + '\n')

# Clean the XML file
clean_xml(dump_file, cleaned_file) 