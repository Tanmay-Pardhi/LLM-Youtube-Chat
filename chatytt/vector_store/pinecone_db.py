import os
from typing import List

import pinecone
from langchain.schema import Document
from langchain_community.vectorstores import Pinecone
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
# from langchain.embeddings.openai import OpenAIEmbeddings


class PineconeDB:
    def __init__(self, index_name: str, embedding_source: str):
        # self.initialise_pinecone()
        self.index_name = index_name
        self.vector_store = PineconeVectorStore(
            index=self.get_index(),
            embedding=OpenAIEmbeddings(),
            text_key="text",
        )

    def save_documents_as_embeddings(self, docs: List[Document]):
        self.vector_store.add_documents(documents=docs)

    # def initialise_pinecone(self):
    #     pinecone.init(
    #         api_key=os.environ.get("PINECONE_API_KEY"), environment="gcp-starter"
    #     )
    #     vectorstore = PineconeVectorStore(index_name=index_name, embedding=embeddings)

    def get_index(self, num_pool_threads: int = 4):
        return pinecone.Index(self.index_name, host = 'https://youtube-transcripts-ixb7m88.svc.aped-4627-b74a.pinecone.io', pool_threads=num_pool_threads)

    def get_similar_docs(self, query: str, top_k: int = 3):
        similar_docs = self.vector_store.similarity_search(query=query, k=top_k)

        return similar_docs


def get_embeddings_from_source(source: str):
    embedding_source_map = {"open-ai": OpenAIEmbeddings()}

    return embedding_source_map[source]