import pandas as pd
import pdfplumber
from docx import Document

def load_file(uploaded_file):
    file_name = uploaded_file.name.lower()

    # CSV
    if file_name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)

    # TXT
    elif file_name.endswith(".txt"):
        df = pd.read_csv(uploaded_file, sep=None, engine="python")

    # Excel
    elif file_name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)

    # PDF
    elif file_name.endswith(".pdf"):
        data = []
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                table = page.extract_table()
                if table:
                    data.extend(table)
        df = pd.DataFrame(data[1:], columns=data[0]) if data else pd.DataFrame()

    # Word
    elif file_name.endswith(".docx"):
        doc = Document(uploaded_file)
        tables = []
        for table in doc.tables:
            for row in table.rows:
                tables.append([cell.text for cell in row.cells])
        df = pd.DataFrame(tables[1:], columns=tables[0]) if tables else pd.DataFrame()

    else:
        raise ValueError("Unsupported file format")

    return df
