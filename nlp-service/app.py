import pymupdf as pdf

path_pdf = "nlp-service/sample_resumes/impact-resume.pdf"
doc= pdf.open(path_pdf)

text = ""
for page in doc:
    text += page.get_text()

doc.close()
print(text)
