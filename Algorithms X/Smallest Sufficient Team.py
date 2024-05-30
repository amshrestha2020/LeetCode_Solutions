In a project, you have a list of required skills req_skills, and a list of people. The ith person people[i] contains a list of skills that the person has.

Consider a sufficient team: a set of people such that for every required skill in req_skills, there is at least one person in the team who has that skill. We can represent these teams by the index of each person.

For example, team = [0, 1, 3] represents the people with skills people[0], people[1], and people[3].
Return any sufficient team of the smallest possible size, represented by the index of each person. You may return the answer in any order.

It is guaranteed an answer exists.

 

Example 1:

Input: req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]
Output: [0,2]
Example 2:

Input: req_skills = ["algorithms","math","java","reactjs","csharp","aws"], people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
Output: [1,2]
 

Constraints:

1 <= req_skills.length <= 16
1 <= req_skills[i].length <= 16
req_skills[i] consists of lowercase English letters.
All the strings of req_skills are unique.
1 <= people.length <= 60
0 <= people[i].length <= 16
1 <= people[i][j].length <= 16
people[i][j] consists of lowercase English letters.
All the strings of people[i] are unique.
Every skill in people[i] is a skill in req_skills.
It is guaranteed a sufficient team exists.




class Solution:
    def smallestSufficientTeam(self, req_skills, people):
        from functools import lru_cache
        
        # Map each skill to a bit position
        skill_index = {skill: i for i, skill in enumerate(req_skills)}
        n = len(req_skills)
        
        # Convert each person's skill set to a bitmask
        people_skills = []
        for p_skills in people:
            skill_mask = 0
            for skill in p_skills:
                if skill in skill_index:
                    skill_mask |= 1 << skill_index[skill]
            people_skills.append(skill_mask)
        
        # Initialize DP dictionary
        dp = {0: []}  # Key: bitmask of skills, Value: list of people indices
        
        for i, person_skill in enumerate(people_skills):
            if person_skill == 0:
                continue
            for skill_set, team in list(dp.items()):
                new_skill_set = skill_set | person_skill
                if new_skill_set == skill_set:
                    continue
                if new_skill_set not in dp or len(dp[new_skill_set]) > len(team) + 1:
                    dp[new_skill_set] = team + [i]
        
        # All skills covered is represented by (1 << n) - 1
        return dp[(1 << n) - 1]

