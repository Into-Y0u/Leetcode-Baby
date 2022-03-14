class Solution:
    def simplifyPath(self, path: str) -> str:
        '''
        /home//foo/    =>  [ "home" , "foo" , ".."]
        ext = 
        '''
        my = path.split("/")
        ext = [""," " , "."]
        res = []
        # print(my)
        for n in my :
            if n in ext :
                continue
            if n == "..":
                if  res:
                    res.pop()
            else :
                res.append(n)
        # print(res)
        return "/"+"/".join(res)
