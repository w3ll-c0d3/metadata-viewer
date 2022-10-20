from PyPDF2 import PdfReader

def get_pdf():
    draw_line()
    file = PdfReader(input("Path: "))
    return file

def get_metadata(file):
    meta = file.metadata
    return meta

def read_metadata(meta, file):
    content = f"""
    \033[1;32mPages: {len(file.pages)}
    \033[1;32mAuthor: {meta.author}
    \033[1;32mCreator: {meta.creator}
    \033[1;32mProducer: {meta.producer}
    \033[1;32mSubject: {meta.subject}
    \033[1;32mTitle: {meta.title}
    """
    print(content)

def draw_line():
    print("\n------------------------------")

def main():
    pdf = get_pdf()
    metadata = get_metadata(pdf)
    read_metadata(metadata, pdf)


if __name__ == '__main__':
    main()