import re
import ast

def replace_variables(input_string, data):   

    def replacer_meta(match):
        content = match.group(1)
        if content.startswith("var:"):
            _, name, quoted_default = content.split(":", 2)
            if name in data:
                return str(data[name])
            return str(ast.literal_eval(quoted_default))
        # Pass other content through as-is
        return match.group(0)

    return re.sub(r"{{(.+?)}}", replacer_meta, input_string)


s1 = replace_variables("Hey, {{var:ninja_name:'Ninja'}} show me your justu !!!", {'ninja_name': 'Kakashi'})
s2 = replace_variables("Hard work is worthless for those that don't believe in themselves. – {{var:ninja_name:'Ninja'}}", {'ninja_name': 'Naruto Uzumaki'})

print(s1)
print(s2)

'''
Hey, Kakashi show me your justu !!!
Hard work is worthless for those that don't believe in themselves. – Naruto Uzumaki
'''


