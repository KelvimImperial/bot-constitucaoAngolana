from docling.document_converter import DocumentConverter

source = "../data/constituicao_republica.pdf"  # file path or URL
converter = DocumentConverter()
doc = converter.convert(source).document

print(doc.export_to_markdown())  # output: "### Docling Technical Report[...]"

with open("../data/constituicao_republica.md", "w", encoding="utf-8") as f:
    f.write(doc.export_to_markdown())