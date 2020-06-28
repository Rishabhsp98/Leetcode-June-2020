class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        if not tickets:
            return 
        
        tickets_dict = collections.defaultdict(list)
        
        for src, dest in tickets:
            tickets_dict[src].append(dest)
        
        routes = ['JFK']
        
        def dfs(src):
            if len(routes) == len(tickets) + 1:
                return True
            
            destinations = sorted(tickets_dict[src])
            
            for destination in destinations:
                routes.append(destination)
                tickets_dict[src].remove(destination)
                
                if dfs(destination):
                    return True
                tickets_dict[src].append(destination)
                routes.pop()
        
        dfs('JFK')
        return routes
                
        