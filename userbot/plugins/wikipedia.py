"""WikiPedia.ORG
Syntax: .wikipedia Query"""
import wikipedia
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="wikipedia (.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Processing ...")
    input_str = event.pattern_match.group(1)
    result = ""
    results = wikipedia.search(input_str)
    for s in results:
        page = wikipedia.page(s)
        url = page.url
        result += f"> [{s}]({url}) \n"
    await event.edit(
        "WikiPedia **Search**: {} \n\n **Result**: \n\n{}".format(input_str, result)
    )
