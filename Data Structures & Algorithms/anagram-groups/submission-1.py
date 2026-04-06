class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        # For every word in strs
        for word in strs:
            # sort the words letters so eat -> a,e,t
            key = "".join(sorted(word))
            # if the word is not already in groups add the word as a key to the group
            # then append the word into the group 
            if key not in groups:
                groups[key] = []
            groups[key].append(word)

        return list(groups.values())