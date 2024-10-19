from langchain_community.document_loaders import PyPDFLoader


async def load_pdf(file_path: str) -> list:
    loader = PyPDFLoader(
        file_path=file_path,
        extract_images=True,
    )

    pages = []
    async for page in loader.alazy_load():
        pages.append(page)

    return pages
