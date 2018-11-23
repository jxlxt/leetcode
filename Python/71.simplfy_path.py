class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split('/')
        path = filter(lambda x: x != '' and x != '.', path)
        res = []
        
        for elem in path:
            if elem != '..':
                res.append(elem)
            elif res and elem == '..':
                res.pop()
        return '/' + '/'.join(res)
