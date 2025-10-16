import json
import sys

dummypage = {
    "d": 1239537600000,
    "c": "Boggle vacantly at these shenanigans.",
    "b": "It begins to dawn on you that everything you've done may be a colossal waste of time",
    "n": []
}

def main():
    final_output = {}
    final_output["n"] = "sbahj"
    final_output["o"] = "https://file.garden/aOgKdPFhxWt7Kb9m/nihonstuck2.jpg" # favicon
    final_output["r"] = "it keeps happening but in japanese"
    page_list = []

    curr_page_count = 16
    for pagenum in range(1, curr_page_count + 1):
        newpage = {}
        newpage["d"] = 1232442780000
        newpage["c"] = "8^y"
        newpage["n"] = [pagenum + 1]
        # newpage["b"] = f"[img]https://file.garden/aOgKdPFhxWt7Kb9m/images/sbahj/archive/{pagenum:03}.jpg[/img]"
        # TODO: How do we work with the buttons?
        imgnext = f'<span><a href="/sweetbroandhellajeff/?p={pagenum+1}"><img src="https://file.garden/aOgKdPFhxWt7Kb9m/images/sbahj/next.jpg"></a></span>' 
        imgfirst = f'<span><a href="/sweetbroandhellajeff/?p=1"><img src="https://file.garden/aOgKdPFhxWt7Kb9m/images/sbahj/first.jpg"></a></span>' 
        if pagenum == 1:
            imgback = f'<span><a href="/sweetbroandhellajeff/?p=1"><img src="https://file.garden/aOgKdPFhxWt7Kb9m/images/sbahj/back.jpg"></a></span>' 
        else:
            imgback = f'<span><a href="/sweetbroandhellajeff/?p={pagenum-1}"><img src="https://file.garden/aOgKdPFhxWt7Kb9m/images/sbahj/back.jpg"></a></span>' 
        imglast = f'<span><a href="/sweetbroandhellajeff/?p=24"><img src="https://file.garden/aOgKdPFhxWt7Kb9m/images/sbahj/new.jpg"></a></span>' 
        pagenav = imgfirst + imgback + imgnext + imglast
        mainimg = f'<img src="https://file.garden/aOgKdPFhxWt7Kb9m/images/sbahj/archive/{pagenum:03}.jpg">'
        newpage["b"] = pagenav + "<br><br>" + mainimg + "<br><br>" + pagenav

        page_list.append(newpage)

    final_output["p"] = page_list
    json_object = json.dumps(final_output, indent=4, ensure_ascii=False).encode("utf8")

    with open('./adventure.json', "wb") as outfile:
        outfile.write(json_object)

if __name__ == "__main__":
    main()
