import pandas as pd
import re
import json
import logging
from constraints import *


def generate_email(name):
    clean_name = re.sub(r'[^a-zA-Z\s]', '', name)
    name_parts = clean_name.lower().split()

    if len(name_parts) >= 2:
        email = f"{name_parts[0][0]}{name_parts[-1]}@{EMAIL_DOMAIN}"
    else:
        email = f"{name_parts[0]}@{EMAIL_DOMAIN}"

    return email


def generate_unique_emails(df):
    emails = set()
    unique_emails = []

    for _, row in df.iterrows():
        name = row['Student Name']
        email = generate_email(name)

        base_email = email.split('@')[0]
        counter = 1
        while email in emails:
            email = f"{base_email}{counter}@{EMAIL_DOMAIN}"
            counter += 1

        emails.add(email)
        unique_emails.append(email)

        logging.info(f"Generated email for {name}: {email}")

    return unique_emails


def separate_students_by_gender(df):
    male_students = df[df['Gender'] == 'M']
    female_students = df[df['Gender'] == 'F']

    logging.info(f"Number of male students: {len(male_students)}")
    logging.info(f"Number of female students: {len(female_students)}")

    return male_students, female_students


def find_students_with_special_chars(df):
    special_char_pattern = re.compile(r'[^a-zA-Z\s]')
    special_char_students = df[df['Student Name'].apply(lambda x: bool(special_char_pattern.search(x)))]

    logging.info(f"Number of students with special characters in their names: {len(special_char_students)}")

    return special_char_students


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, pd.Timestamp):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")


def shuffle_and_save_json(df):
    shuffled_df = df.sample(frac=1).reset_index(drop=True)

    # Convert DataFrame to JSON-serializable format
    json_data = shuffled_df.to_dict(orient='records')

    # Save as JSON
    with open(SHUFFLED_STUDENTS_JSON, 'w') as f:
        json.dump(json_data, f, default=json_serial, indent=2)

    # Save as JSONL
    with open(SHUFFLED_STUDENTS_JSONL, 'w') as f:
        for record in json_data:
            json_record = {
                "student_number": record['Student Number'],
                "additional_details": {
                    "dob": record['DoB'],
                    "gender": record['Gender'],
                    "special_character": "yes" if bool(re.search(r'[^a-zA-Z\s]', record['Student Name'])) else "no",
                    "name_similar": "TBD"  # This would be filled after running the similarity matrix
                }
            }
            f.write(json.dumps(json_record, default=json_serial) + '\n')

    logging.info(f"Shuffled and saved {len(shuffled_df)} student records as JSON and JSONL")

# Note: LaBSE similarity matrix function would be implemented here if required