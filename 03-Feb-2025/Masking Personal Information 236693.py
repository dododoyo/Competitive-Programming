# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        # is email 
        if '@' in s:
            first, after = s.split('@')
            return (f"{first[0]}*****{first[-1]}@{after}").lower()

        # is phone number
        else: 
            digits = []

            # filter digits only 
            for x in s:
                if x.isdigit():
                    digits.append(x)

            local = f"***-***-{''.join(digits[-4:])}"

            # the last 10 digits signify only local numbers 
            # if all the digits have length of 10
            # it means country code wasn't specified
            if len(digits) == 10:
                return local.lower()


            # country code was specified
            return (f"+{'*' * (len(digits) - 10)}-" + local).lower()