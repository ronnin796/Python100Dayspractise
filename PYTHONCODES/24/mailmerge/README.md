# Mail Merge

## Description

Automated mail merge utility that generates personalized letters from a template. Reads recipient names from a file and creates individual letters with custom placeholders replaced.

## Features

- Batch letter generation
- Template-based customization
- Automatic filename generation
- Organized file structure (Input/Output)
- String replacement automation

## Learning Outcomes

- File I/O operations
- String manipulation and replacement
- Batch processing with loops
- Path management with pathlib
- Content templating concepts
- Directory structure organization

## How It Works

1. Reads base letter template from Input/Letters
2. Reads list of names from Input/Names
3. For each name, creates personalized copy
4. Replaces placeholders with actual values
5. Saves completed letters to Output folder

## Usage

```bash
python main.py
```

## File Structure

```
Input/
  Letters/
    starting_letter.txt
  Names/
    invited_names.txt
Output/
  ReadyToSend/
```

## Template Placeholders

- [name] - replaced with recipient name

## Technologies Used

- Python 3
- pathlib for path handling
- String operations
