import collections
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = collections.Counter()
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count = int(count)
            frags = domain.split(".")
            for i in range(len(frags)):
                ans[".".join(frags[i:])] += count
        return ["{} {}".format(cnt, item) for item, cnt in ans.items()]
