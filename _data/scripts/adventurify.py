import json
import sys
import re

dummypage = {
    "d": 1239537600000,
    "c": "Boggle vacantly at these shenanigans.",
    "b": "It begins to dawn on you that everything you've done may be a colossal waste of time",
    "n": []
}

url = "https://file.garden/aOgKdPFhxWt7Kb9m" # + "/storyfiles/hs2/00002.gif"


# def flashformat(media, bodytext):
#     body = """        <div id='ruffle'></div>
#         <script src='https://nihonstuck.github.io/scripts/ruffle/ruffle.js'></script>
#         <script>
# var swfobject = {};
#
# swfobject.embedSWF = function(url, cont, width, height){
#     var ruffle = window.RufflePlayer.newest(),
#         player = Object.assign(document.getElementById(cont).appendChild(ruffle.createPlayer()), {
#             width: width,
#             height: height,
#             style: 'width: ' + width + 'px; height: ' + height + 'px',
#         });
#
#     player.load({ url: url });
# }"""
#
#     foo = f"swfobject.embedSWF('{url + media[0]}', 'ruffle', 650, 450);</script>"
#     body += foo + bodytext
#     return body



def mediaformat(media, text, opentag, closetag):
    body = ""
    for m in media:
        if opentag == "img":
            # body += f'[{opentag} class="storyPanel"]{url + m}[{closetag}]<br><br>'
            body += f'<img class="storyPanel" src="{url + m}"><br><br>'
        else:
            body += f'[{opentag}]{url + m}[{closetag}]<br><br>'
    body += "<br>"
    if text.startswith("|"):
        match text[0:11]:
            case "|PESTERLOG|":
                text = text.removeprefix("|PESTERLOG|")
                text = '[spoiler open="ペスターログを表示" close="ペスターログを非表示"]' + text + '[/spoiler]'
            case "|SPRITELOG|":
                text = text.removeprefix("|SPRITELOG|")
                text = '[spoiler open="スプライトログを表示" close="スプライトログを非表示"]' + text + '[/spoiler]'
            case "|RECAP LOG|":
                text = text.removeprefix("|RECAP LOG|")
                text = '[spoiler open="マトメログを表示" close="マトメログを非表示"]' + text + '[/spoiler]'
            case "|JOURNALOG|":
                text = text.removeprefix("|JOURNALOG|")
                text = '[spoiler open="日ログを表示" close="日ログを非表示"]' + text + '[/spoiler]'
            case "|SRIOUSBIZ|":
                text = text.removeprefix("|SRIOUSBIZ|")
                text = '[spoiler open="真面目なビジネスを表示" close="真面目なビジネスを非表示"]' + text + '[/spoiler]'
            case _:
                raise Exception("Unhandled case:", text[0:11])
    body += text
    if body.endswith('<br><br>'):
        body = body.removesuffix('<br><br>')

    return body

def flashformat(media, bodytext):
    return mediaformat(media, bodytext, "flash=650x450", "/flash")

def imageformat(media, bodytext):
    return mediaformat(media, bodytext, "img", "/img")

def link_cleanup(body):
    replace = {
        "http://www.mspaintadventures.com/storyfiles/hs2/waywardvagabond/": "/story/waywardvagabond/",
        "http://www.mspaintadventures.com/?s=6&": "/?s=6&",
        "http://www.mspaintadventures.com/sweetbroandhellajeff/": "/sweetbroandhellajeff/",
        "http://www.mspaintadventures.com/": url + "/",
    }
    # TODO: normal pages, e.g. "http://www.mspaintadventures.com/?s=6&amp;p=002069"
    # http://www.mspaintadventures.com/sweetbroandhellajeff/?cid=016.jpg
    # ---> (nihonstuck.github.io)/sweetbroandhellajeff/?p=016

    for u in re.findall("cid=[0-9][0-9][0-9].jpg", body):
        sbahj = u.removesuffix(".jpg").removeprefix("cid=")
        v = "p=" + str(int(sbahj))
        replace[u] = v
        print(f"REPLACE {u} WITH {v}")

    for u in re.findall("s=6&amp;p=[0-9][0-9][0-9][0-9][0-9][0-9]", body):
        sbahj = u.removeprefix("s=6&amp;p=")
        v = "p=" + str(int(sbahj) - 1900)
        replace[u] = v
        print(f"REPLACE {u} WITH {v}")

    for r in replace:
        body = body.replace(r, replace[r])
    return body

    # TODO: page 845, get rid of Gankra thing
    # TODO: also the conair bunny page


def main():
    with open('../translation/mspa.json', 'r') as mspa:
        story = json.load(mspa)["story"]

        final_output = {}
        final_output["n"] = "ホームスタック"
        final_output["o"] = "https://file.garden/aOgKdPFhxWt7Kb9m/nihonstuck2.jpg" # favicon
        final_output["r"] = "少年と友達がゲームをする物語です。約8,000ページ。警告済みです。"
        page_list = []

        translated = ["hsjp", "dz_act3", "dz_intermission", "dz_act4", "dz_act5act1", "a5a2_one", "a5a2_two", "a5a2_three"]
        shouldbe = 1
        for tr in translated:
            with open(f'../translation/{tr}.json', 'r') as tr_json:
                tr_pages = json.load(tr_json)
                for pagenum in tr_pages:
                    newpage = {}
                    newpage["d"] = int(story[pagenum]["timestamp"]) * 1000
                    newpage["c"] = tr_pages[pagenum]["title"]
                    newpage["n"] = [int(n) - 1900 for n in story[pagenum]["next"]]

                    # This is to account for missing pages and to preserve structure
                    if shouldbe < int(pagenum) - 1900:
                        while shouldbe < int(pagenum) - 1900:
                            page_list.append(dummypage)
                            shouldbe += 1

                    # Some translated JSON pages don't have a content field.
                    # It should be blank.
                    try:
                        content = tr_pages[pagenum]["content"]
                    except:
                        content = story[pagenum]["content"]
                        if content and pagenum != "002745" and pagenum != "003750":
                            # raise Exception(f'Missing translation at id {pagenum}, page {int(pagenum) - 1900}')
                            print(f'Potentially missing translation at id {pagenum}, page {int(pagenum) - 1900}')


                    # TODO: clean up content. especially links

                    body = ""
                    if "F" in story[pagenum]["flag"]:
                        body = flashformat(story[pagenum]["media"], content)
                    else:
                        body = imageformat(story[pagenum]["media"], content)

                    body = link_cleanup(body)

                    newpage["b"] = body

                    page_list.append(newpage)
                    shouldbe += 1
        final_output["p"] = page_list
        json_object = json.dumps(final_output, indent=4, ensure_ascii=False).encode("utf8")

        with open('../../assets/json/adventure.json', "wb") as outfile:
            outfile.write(json_object)

if __name__ == "__main__":
    main()
