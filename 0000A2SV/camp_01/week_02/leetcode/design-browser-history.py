class DoublyLinkedList:
    def __init__(self,page,prev_=None,next_=None):
        self.page = page
        self.prev = prev_
        self.next = next_

class BrowserHistory:
    def __init__(self, homepage: str):
        self.current_page = DoublyLinkedList(homepage,None,None)
        
    def visit(self, url: str) -> None:
        new_page = DoublyLinkedList(url,self.current_page,None)
        self.current_page.next = new_page
        self.current_page = new_page
        
    def back(self, steps: int) -> str:
        while self.current_page.prev and steps > 0:
            steps -= 1
            self.current_page = self.current_page.prev 
        return self.current_page.page

    def forward(self, steps: int) -> str:
        while self.current_page.next and steps > 0:
            steps -= 1
            self.current_page = self.current_page.next
        return self.current_page.page

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)