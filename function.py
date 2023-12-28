def readparagraph(string):
    string = string.replace("。", "。\n")
    paragraphs = string.split("\n")
    cleaned_paragraphs = [p.strip() for p in paragraphs if p.strip()]
    return cleaned_paragraphs
  
def printlist(list,waitingtime):
    for i in list:
        print(i)
        time.sleep(waitingtime)
