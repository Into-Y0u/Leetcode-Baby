class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        n=len(products)
        indices=[i for i in range(n)]
        res=[]
        for idx, c in enumerate(searchWord):
            indices = [i for i in indices if len(products[i])>idx and products[i][idx] == c]                                                                
            res.append(products[i] for i in indices[:3])        
        return res  
