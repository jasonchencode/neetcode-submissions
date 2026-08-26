class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        addresses = set()
        for email in emails:
            email_sent = ""
            i = 0
            while email[i] != '@':
                if email[i] == '.':
                    i += 1
                    continue
                if email[i] == '+':
                    while email[i] != '@':
                        i += 1
                    break
                email_sent += email[i]
                i += 1
            email_sent += email[i:]
            addresses.add(email_sent)
        return len(addresses)