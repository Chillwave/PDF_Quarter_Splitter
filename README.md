# PDF_Quarter_Splitter
Takes a PDF file, splits each page into four quarters (NW, NE, SW, SE), and then combines all these quarters into a single PDF file. This is especially useful for detailed analysis of documents or preparing them for a specific type of presentation or printing requirement.

## Features

- **Splitting**: Each page of the input PDF is split into four quarters.
- **Combining**: All quarters from all pages are combined into a single PDF file.
- **Timestamping**: The output PDF file is timestamped to indicate the generation time.

## Prerequisites

Ensure you have Python installed on your system. The script has been tested with Python 3.8 and higher. Additionally, the script uses the `PyPDF2` library, which needs to be installed:

```bash
pip install PyPDF2
```

## Setup

1. Clone this repository or download the script to your local machine.
2. Place the PDF files you want to process in the same directory as the script, or modify the `pdf_path` in the script to point to the correct file location.

## Usage

To use the script, follow these steps:

1. Open your terminal or command line interface.
2. Navigate to the directory containing the script.
3. Run the script by executing:

```bash
python split_pdf_into_quarters_and_combine.py
```

## Output

The script will generate a combined PDF file in the specified output folder (`output_quarters` by default). The filename will include a timestamp to differentiate it from other outputs. For example: `combined_quarters_20230701-120000.pdf`.
