import re,requests,sys
import execjs
print(execjs.get().name)

with open("datadome_encrypt.js", "r", encoding="utf-8") as f:
    jstext = f.read()
ctx = execjs.compile(jstext)
sign = ctx.call("_0x20e5", 343)
print(sign)

# with open("tag-beautify-remove_duplicate.js","r",encoding="utf-8") as f:
#     tagjs = f.read()
#
# def f(match_obj):
#     s = match_obj.group(0)
#     s = s.split("(")[1]
#     s = s.split(")")[0]
#     assert len(s) == 3 and s.isdigit()
#     r = ctx.call("_0x20e5", int(s))
#     return '"' + r.replace('"','\\"') + '"'
#
# pattern = r'_0x20e5\(\d+\)'
# result_tag = re.sub(pattern, f, tagjs)
# with open("tag-beautify-remove_duplicate-strdecrypt.js","w") as f:
#     f.write(result_tag)

