class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.live_time = timeToLive
        self.tokens = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = self.live_time + currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens and currentTime < self.tokens[tokenId]:
            self.tokens[tokenId] = currentTime + self.live_time

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for each_time in self.tokens.values():
            if currentTime < each_time:
                count += 1
        return count
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)