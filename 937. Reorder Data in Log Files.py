class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        let = []
        dig = []
        res = []

        for i in logs:
            if i[-1].isalpha():
                let.append(i)
            else:
                dig.append(i)

        # sort letter lexicographically first, then by id
        let.sort(key=lambda x: (x.split()[1:],x.split()[0]))

        res = let+ dig

        return res
