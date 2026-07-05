import os


def generate_invitations(template, attendees):
    if not isinstance(template, str) or not isinstance(attendees, list):
        print("Error: Invalid input types.")
        return

    if not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Invalid input types.")
        return

    if len(template.strip()) == 0:
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    placeholders = ['name', 'event_title', 'event_date', 'event_location']

    for index, attendee in enumerate(attendees, start=1):
        processed_template = template

        for placeholder in placeholders:
            val = attendee.get(placeholder)
            if val is None:
                val = "N/A"
            else:
                val = str(val)

            processed_template = processed_template.replace(f"{{{placeholder}}}", val)

        filename = f"output_{index}.txt"

        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(processed_template)
        except Exception as e:
            print(f"An error occurred while writing to {filename}: {e}")
