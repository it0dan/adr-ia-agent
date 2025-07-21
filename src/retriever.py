from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

def build_retriever(folder_path: str):
    """
    Cria um retriever com base nos arquivos markdown da pasta history/
    """

    # Carrega todos os arquivos .md do diretório especificado
    loader = DirectoryLoader(
        folder_path,
        glob="**/*.md",
        loader_cls=TextLoader,
        show_progress=True
    )
    documents = loader.load()

    # Divide os textos em chunks menores para melhor performance
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100,
    )
    docs_split = text_splitter.split_documents(documents)

    # Cria os embeddings dos textos usando OpenAI
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # Cria o vetorstore FAISS na memória (para PoC)
    vectordb = FAISS.from_documents(docs_split, embeddings)

    # Retorna o retriever configurado para top-3 resultados
    retriever = vectordb.as_retriever(search_type="similarity", search_kwargs={"k": 3})
    return retriever