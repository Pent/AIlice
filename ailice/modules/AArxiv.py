
import arxiv

from ailice.common.lightRPC import makeServer
from ailice.modules.AScrollablePage import AScrollablePage

class AArxiv():
    def __init__(self):
        self.page = AScrollablePage({"SCROLLDOWN": "SCROLLDOWNARXIV"})
        return
    
    def ModuleInfo(self):
        return {"NAME": "arxiv", "ACTIONS": {"ARXIV": {"func": "ArxivSearch", "prompt": "Use arxiv to search academic literatures."},
                                             "SCROLLDOWNARXIV": {"func": "ScrollDown", "prompt": "Scroll down the results."}}}
    
    def ArxivSearch(self, keywords: str) -> str:
        try:
            ret = str(list(arxiv.Search(query=keywords, max_results=40).results()))
        except Exception as e:
            print("arxiv excetption: ", e)
            ret = f"arxiv excetption: {str(e)}"
        self.page.LoadPage(str(ret), "TOP")
        return self.page()

    def ScrollDown(self) -> str:
        self.page.ScrollDown()
        return self.page()

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--addr',type=str, help="The address where the service runs on.")
    args = parser.parse_args()
    makeServer(AArxiv, dict(), args.addr, ["ModuleInfo", "ArxivSearch", "ScrollDown"]).Run()

if __name__ == '__main__':
    main()