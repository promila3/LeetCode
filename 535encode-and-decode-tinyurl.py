# https://leetcode.com/problems/encode-and-decode-tinyurl/
class Codec:
    map = {}
    index = 0
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.map[self.index] = longUrl
        temp = self.index
        self.index +=1
        return "http://tinyurl.com/" + str(temp)


    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        outUrl = shortUrl.replace("http://tinyurl.com/", "")
        return self.map[int(outUrl)]
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
