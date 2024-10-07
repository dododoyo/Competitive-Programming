# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count/description/

class Solution:
    def getSubDomains(self,pair):
        c_d = pair.split(" ")
        visits,domain = int(c_d[0]),c_d[1]
        words,sub_domains = domain.split("."), []
        for i in range(len(words)):
            sub_domain = ""
            for j in range(i,len(words)):
                sub_domain += (words[j]+".")
            sub_domains.append(sub_domain[:-1])
        return sub_domains,visits
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visit_counter = defaultdict(int)
        for pair in cpdomains:
            sub_domains,visits = self.getSubDomains(pair)
            for domain in sub_domains:
                visit_counter[domain] += visits
        solution = [str(value)+" "+key  for key,value in visit_counter.items()]
        return solution

        