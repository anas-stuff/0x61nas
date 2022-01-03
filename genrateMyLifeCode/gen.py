import yaml
import random
import os

# Constants
codeFilePath = "./lang/codes/MyLifeCode"
readmeFilePath = "./README.md"  # To test
lineCode = "<!-- codeHear -->"
start = "<!-- START -->"

reCode = "<h2>\n\n```LANG\nSTR\n```\n</h2>\n" + start

# Open list.ymal file and generate code
with open(r"./lang/list.yaml") as f:
    yamlFile = yaml.load(f, Loader=yaml.FullLoader)

    list = yamlFile.get("lang")

    # print type(list)
    print(type(list))

    # Test
    print(list)

    # Get current language from cache file
    currentLang = ""
    try:
        cf = open("./cache", "r")
        currentLang = cf.readline()
        currentLangIndex = int(str(cf.readline()))
        cf.close()
    except:
        currentLang = ""

    # Get random language
    while True:
        index = int(random.randint(0, len(list) - 1))
        lang = list[index]
        if lang.get('name') != currentLang:
            break

    # Open the cache file and write the new language
    cf = open("./cache", "w")
    # Write to cache file
    cf.write(lang.get('name'))
    cf.write("\n")
    cf.write(str(index))

    # close files
    cf.close()
    f.close()

    # Get code
    code = lang.get('print')
    code = code.replace("STR",
                        "Hi there!")

    reCode = reCode.replace("LANG", lang.get('name')).replace("STR", code)

    # Write code to README.md
    # Open readme file to read and write
    with open(readmeFilePath, "r", encoding="utf-8") as rf:
        readmeText = rf.read()
        rf.close()

        # Remove old code
        startIndex = readmeText.index(start) + len(start)

        readmeText = readmeText[startIndex:]
        #print(readmeText)

        # Write new code
        readmeText = reCode + readmeText

        # delete old readme file
        os.remove(readmeFilePath)

        # Write new readme file
        with open(readmeFilePath, "w", encoding="utf-8") as rf:
            rf.write(readmeText)
            rf.close()
