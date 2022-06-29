class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if len(people) <= 1:
            return people
        
        # Between different h, pick person with larger h first
        # Between different k, pick person with smaller k first (in the same h)
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        
        for cur in range(len(people)):
            # Currently picked person
            h, k = people[cur]
            
            # Because h in all processed people are larger than or equal to
            # current person, the k in current people is same as the correct 
            # position
            if k < cur:
                p = people.pop(cur)
                people.insert(k, p)
            
            # If k is larger than or equal to cur, we do nothing 
            # (this people already in the end of the processed people)
        return people
