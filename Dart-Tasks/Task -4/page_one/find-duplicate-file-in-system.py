class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        content_map = {}
        
        for path in paths:
            directory, *files = path.split()
            for file in files:
                file_name, file_content = file.split('(')
                if file_content in content_map:
                    content_map[file_content].append(directory + '/' + file_name)
                else:
                    content_map[file_content] = [directory + '/' + file_name]
        
        result = [group for group in content_map.values() if len(group) > 1]
        return result
