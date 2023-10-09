import asyncio

from langchain.tools import BaseTool, PubmedQueryRun


class PubMed(BaseTool):
    name = "PubMed® search"
    description = "useful for answering question about medical publications"
    return_direct = False

    def _run(self, search_query: str) -> str:
        pubmed = PubmedQueryRun(args_schema=self.args_schema)
        return pubmed.run(search_query)

    async def _arun(self, search_query: str) -> str:
        pubmed = PubmedQueryRun(args_schema=self.args_schema)
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, pubmed.run, search_query)
