# favourite one 

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        timechart = {i:float('inf') for i in range(1,n+1)}
        
        graph = defaultdict(list)
        
        for u,v,t in times :
            if graph.get(u):
                graph[u].append((v,t))
            else :
                graph[u] = [(v,t)]
        
        st = [(k,0)]
        while st :
            src,time = st.pop(0)
            if timechart[src] > time :
                timechart[src] = time 
                for target,temp in graph[src]:
                    st.append((target , time + temp))
        res = max(timechart.values())
        
        if  res < float('inf'):
            return res
        else :
            return -1
