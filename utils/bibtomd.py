import bibtexparser
import os
import re

def parse_bibtex_to_text(bibtex_file, output_dir):
    # Read the BibTeX file
    with open(bibtex_file, 'r') as bib_file:
        bib_database = bibtexparser.load(bib_file)

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Process each entry in the BibTeX file
    for entry in bib_database.entries:
        # Extract required fields
        key = entry.get('ID', '')
        title = entry.get('title', 'Untitled')
        paperurl = entry.get("url", "None")
        journal = entry.get('journal', 'Unknown Venue')
        year = entry.get('year', 'Unknown Year')
        authors = entry.get('author', 'Unknown Authors')
        date = entry.get('urldate', year)  # Fall back to year if no explicit date
        if len(date.split("-"))==1:
            date += "-01-01"

        title = title.replace("{","")
        title = title.replace("}","")

        # Format the citation
        authors = authors.replace(" and", ";")
        citation = f"{authors}. \"{title}\". {journal}, {year}."

        # Create the text content
        text_content = f"""\
---
title: '{title}'
collection: publications
category: manuscripts
paperurl: '{paperurl}' 
date: {date}
venue: '{journal}'
citation: '{citation}'
---
"""

        author, word, pubyear = key.split("_")
        # Generate the filename with year at the start
        new_filename = f"{pubyear}_{author}_{word}.md"

        # Save the text file
        text_path = os.path.join(output_dir, new_filename)
        with open(text_path, 'w') as text_file:
            text_file.write(text_content)

        print(f"Created: {text_path}")

parse_bibtex_to_text('ExportedItems.bib', '../_publications')
