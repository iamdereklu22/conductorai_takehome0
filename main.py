import fitz
import re
import sys

def extract_text_from_pdf(pdf_path):
    text = fitz.open(pdf_path)
    res = []
    for page in text:
        res.extend(page.get_text().splitlines())
    return res

def find_million_contexts(lines):
    res = set()
    for i, line in enumerate(lines):
        if 'million' in line.lower():
            for j in range(i, min(i + 10, len(lines))):
                res.add(j)
    return res

def extract_numbers(lines):
    million_context_lines = find_million_contexts(lines)

    numbers = []
    for i, line in enumerate(lines):
        # regex to find numbers with(?) commas and decimal points
        found = re.findall(r'\b\d{1,3}(?:,\d{3})*(?:\.\d+)?\b', line) 
        
        for val in found:
            num = float(val.replace(",", ""))
            if i in million_context_lines:
                num *= 1000000
            numbers.append(num)
    return numbers

def find_largest_number(pdf_path):
    lines = extract_text_from_pdf(pdf_path)
    numbers = extract_numbers(lines)
    return max(numbers) if numbers else None

if __name__ == "__main__":
    try:
        pdf_path = sys.argv[1]
        result = find_largest_number(pdf_path)

        print("Largest number found:", result) if result else print("No numbers found.")
    except:
        print("Usage: python extract_max_number.py <path_to_pdf>")

    
