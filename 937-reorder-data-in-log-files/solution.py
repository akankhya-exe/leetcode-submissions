class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        let = []
        dig = []

        for log in logs:
            if log.split()[1].isdigit():
                dig.append(log)
            else:
                let.append(log)

        let.sort(key=lambda x: (x.split(" ", 1)[1], x.split(" ", 1)[0])) # sort by contents first then key, only splitting by first space, everyhting after first space is content and everything before it is an identifier

        return let + dig
