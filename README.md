# PDF Largest Number Extractor

Extracts the largest numerical value from any PDF. 
If the document mentions **“in millions”**, the script automatically **scales** appropriately (e.g., `3.25` becomes `3,250,000`).

---

## 📦 Requirements

- Python 3.13

Install dependencies using `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Usage
```bash
python extract_max_number.py path/to/document.pdf
```
