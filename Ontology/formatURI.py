
def formatURI(text):
    for ch in [".", "-", ")", "(", ":", "| ", '"', "[", "]", "> ", "{", "}", "#"]:
        if ch in text:
            text = text.replace(ch, "")

    for ch in ["/", "\\", "'", "`", "^", ">", "&", "   "]:
        if ch in text:
            text = text.replace(ch, " ")

    if "& " in text:
        text = text.replace("& ", "and ")

    if "%" in text:
        text = text.replace("%", "_percent")

    text = text.replace(" ", "_")
    return "#" + text
