# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_parent = {}  
        email_to_name = {}

        def find(email):
            if email_parent[email] != email:
                email_parent[email] = find(email_parent[email])

            return email_parent[email]

        def union(email1, email2):
            root1 = find(email1)
            root2 = find(email2)

            if root1 != root2:
                email_parent[root1] = root2

        for account in accounts:
            name = account[0]
            emails = account[1:]

            for email in emails:
                email_to_name[email] = name

                if email not in email_parent:
                # email is not a email_parent
                # initialize it as a email_parent of it's own
                    email_parent[email] = email

                # union every email to the first email in the list 
                # this should give the same value since they are 
                # in the same component
                union(account[1], email)

        # merge ever account with it's parent
        merged_accounts = defaultdict(list)
        for email in email_parent:
            # find parent
            root = find(email)
            # add the email to the list of emails 
            # in the same parent
            merged_accounts[root].append(email)

        result = []
        for root, emails in merged_accounts.items():
            email_owner = email_to_name[root]
            result.append([email_owner] + sorted(emails))

        return result