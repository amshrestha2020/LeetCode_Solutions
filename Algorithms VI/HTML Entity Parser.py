HTML entity parser is the parser that takes HTML code as input and replace all the entities of the special characters by the characters itself.

The special characters and their entities for HTML are:

Quotation Mark: the entity is &quot; and symbol character is ".
Single Quote Mark: the entity is &apos; and symbol character is '.
Ampersand: the entity is &amp; and symbol character is &.
Greater Than Sign: the entity is &gt; and symbol character is >.
Less Than Sign: the entity is &lt; and symbol character is <.
Slash: the entity is &frasl; and symbol character is /.
Given the input text string to the HTML parser, you have to implement the entity parser.

Return the text after replacing the entities by the special characters.

 

Example 1:

Input: text = "&amp; is an HTML entity but &ambassador; is not."
Output: "& is an HTML entity but &ambassador; is not."
Explanation: The parser will replace the &amp; entity by &
Example 2:

Input: text = "and I quote: &quot;...&quot;"
Output: "and I quote: \"...\""
 

Constraints:

1 <= text.length <= 105
The string may contain any possible characters out of all the 256 ASCII characters.






class Solution:
    def entityParser(self, text: str) -> str:
        # Mapping of HTML entities to their respective characters
        entities = {
            "&quot;": '"',
            "&apos;": "'",
            "&amp;": "&",
            "&gt;": ">",
            "&lt;": "<",
            "&frasl;": "/"
        }
        
        # Result list to collect parts of the parsed string
        result = []
        i = 0
        n = len(text)
        
        while i < n:
            if text[i] == '&':
                # Look for the end of the entity
                semicolon_pos = text.find(';', i)
                if semicolon_pos != -1:
                    entity = text[i:semicolon_pos + 1]
                    if entity in entities:
                        result.append(entities[entity])
                        i = semicolon_pos + 1
                    else:
                        result.append('&')
                        i += 1
                else:
                    result.append('&')
                    i += 1
            else:
                result.append(text[i])
                i += 1
        
        return ''.join(result)

# Example usage:
# solution = Solution()
# print(solution.entityParser("&amp; is an HTML entity but &ambassador; is not.")) 
# # Output: "& is an HTML entity but &ambassador; is not."
# print(solution.entityParser("and I quote: &quot;...&quot;")) 
# # Output: "and I quote: \"...\""
# print(solution.entityParser("&amp;gt;")) 
# # Output: "&gt;"

