"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
class Solution:

# Structure is from this post

# IMHO, the above solution cannot handle a few problems:

# if there are lots of read(1) or read(2), the queue becomes increasingly large

# the queue is extend by size of 4 in each call, and "" can be wrote into queue even it doesn't exist in file

# Here is my modified algorithm with commons..

    def __init__(self):
        self.queue = [] # global "buffer"

    def read(self, buf, n):
        idx = 0

        # if queue is large enough, read from queue
        while self.queue and n > 0:
            buf[idx] = self.queue.pop(0)
            idx += 1
            n -= 1

        while n > 0:
            # read file to buf4
            buf4 = [""]*4
            l = read4(buf4)

            # if no more char in file, return
            if not l:
                return idx

            # if buf can not contain buf4, save to queue
            if l > n:
                self.queue += buf4[n:l]

            # write buf4 into buf directly
            for i in range(min(l, n)):
                buf[idx] = buf4[i]
                idx += 1
                n -= 1
        return idx
