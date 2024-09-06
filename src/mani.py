import pandas as pd
import logging
import os
import sys
from functions import (
    generate_unique_emails,
    separate_students_by_gender,
    find_students_with_special_chars,
    shuffle_and_save_json
)
from constraints import *

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        logger.info(f"Created directory: {directory}")

def main():
    try:
        logger.info("Starting Grooking Python 101 project")

        # Create necessary directories
        create_directory(os.path.dirname(EMAIL_OUTPUT_CSV))
        create_directory(LOG_DIR)

        # Print current working directory and full path of input file
        current_dir = os.getcwd()
        full_input_path = os.path.abspath(INPUT_FILE)
        logger.info(f"Current working directory: {current_dir}")
        logger.info(f"Full path of input file: {full_input_path}")

        # Check if the input file exists
        if not os.path.exists(full_input_path):
            raise FileNotFoundError(f"Input file not found: {full_input_path}")

        # Load the data
        logger.info(f"Loading data from {full_input_path}")
        df = pd.read_excel(full_input_path)

        # Generate unique emails
        logger.info("Generating unique emails")
        df['Email'] = generate_unique_emails(df)

        # Save the updated dataframe with emails
        logger.info(f"Saving students with emails to {EMAIL_OUTPUT_CSV} and {EMAIL_OUTPUT_TSV}")
        df.to_csv(EMAIL_OUTPUT_CSV, index=False)
        df.to_csv(EMAIL_OUTPUT_TSV, sep='\t', index=False)

        # Separate students by gender
        logger.info("Separating students by gender")
        male_students, female_students = separate_students_by_gender(df)
        male_students.to_csv(MALE_STUDENTS_CSV, index=False)
        female_students.to_csv(FEMALE_STUDENTS_CSV, index=False)

        # Find students with special characters in their names
        logger.info("Identifying students with special characters in their names")
        special_char_students = find_students_with_special_chars(df)
        special_char_students.to_csv(SPECIAL_CHAR_STUDENTS_CSV, index=False)

        # Shuffle names and save as JSON and JSONL
        logger.info("Shuffling names and saving as JSON and JSONL")
        shuffle_and_save_json(df)

        logger.info("Grooking Python 101 project completed successfully")

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()