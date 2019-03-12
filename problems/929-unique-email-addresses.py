class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        result = set()
        for email in emails:
            result_email = ""
            i = 0
            while i < len(email):
                if email[i] == '.':
                    i += 1
                elif email[i] == '@':
                    break
                elif email[i] == '+':
                    i += 1
                    while email[i] != '@':
                        i += 1
                    break
                else:
                    result_email += email[i]
                    i += 1
            result.add(result_email + email[i:len(email)])
        return len(result)
