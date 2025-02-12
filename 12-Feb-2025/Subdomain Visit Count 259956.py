# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def getSubDomains(self,pair):
        c_d = pair.split(" ")
        visits,domain = int(c_d[0]),c_d[1]

        domains = domain.split(".")
        split_domains = []
        for i in range(len(domains)):
            sub_domain = ""
            for j in range(i,len(domains)):
                sub_domain += (domains[j]+".")

            split_domains.append(sub_domain[:-1])

        return split_domains,visits

    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visit_counter = defaultdict(int)
        for pair in cpdomains:
            split_domains,visits = self.getSubDomains(pair)
            for domain in split_domains:
                visit_counter[domain] += visits

        solution = []
        
        for domain,visit in visit_counter.items():
            solution.append(str(visit)+" "+domain)

        return solution

        