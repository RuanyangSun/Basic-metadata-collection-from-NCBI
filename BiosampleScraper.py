from bs4 import BeautifulSoup
import requests

# GIMCC_url = "https://www.ncbi.nlm.nih.gov/biosample/?term=SAMN05792026"
# r = requests.get(GIMCC_url)  
# r.encoding = r.apparent_encoding
# GIMCC_soup = BeautifulSoup(r.content, "html.parser")  
#
# items = GIMCC_soup.find_all('th')
# for index, item in enumerate(items):
#     items[index] = item.text.rstrip()  

# with open("C:\\Users\\xrw\\PycharmProjects\\webScraper\\BiosampleScraper\\BiosampleInfo.txt", "w+") as Bioinfo:
#     Bioinfo.writelines("BioSample\tisolation source")
#     Bioinfo.writelines("\tcollection date")
#     Bioinfo.writelines("\tgeographic location")
#     Bioinfo.writelines("\tserovar")
#     Bioinfo.writelines("\n")

GIMCC_url = "https://www.ncbi.nlm.nih.gov/biosample/?term="
with open("./Biosamplenumber_list") as Blst:
    for line in Blst.readlines():
        Search_url = GIMCC_url + line.strip()
        r = requests.get(Search_url)  
        r.encoding = r.apparent_encoding
        GIMCC_soup = BeautifulSoup(r.content, "html.parser")  

        items = GIMCC_soup.find_all('th')
        for index, item in enumerate(items):
            items[index] = item.text.rstrip()  

        # if "isolation source" in items:
        #     i_is = items.index("isolation source")
        if "host" in items:
            i_is = items.index("host")
        else:
            i_is = 999

        if "collection date" in items:
            i_cd = items.index("collection date")
        else:
            i_cd = 999

        if "geographic location" in items:
            i_gl = items.index("geographic location")
        else:
            i_gl = 999

        if "serovar" in items:
            i_s = items.index("serovar")
        else:
            i_s = 999

        subitems = GIMCC_soup.find_all('td')
        for index, item in enumerate(subitems):
            subitems[index] = item.text.rstrip()  
       
        with open("./output", "a+") as Bioinfo:
            Bioinfo.writelines(line.strip())
            Bioinfo.writelines("\t")
            if i_is != 999:
                Bioinfo.writelines(subitems[i_is])
                Bioinfo.writelines("\t")
            else:
                Bioinfo.writelines("Na")
                Bioinfo.writelines("\t")
            if i_cd != 999:
                Bioinfo.writelines(subitems[i_cd])
                Bioinfo.writelines("\t")
            else:
                Bioinfo.writelines("Na")
                Bioinfo.writelines("\t")
            if i_gl != 999:
                Bioinfo.writelines(subitems[i_gl])
                Bioinfo.writelines("\t")
            else:
                Bioinfo.writelines("Na")
                Bioinfo.writelines("\t")
            if i_s != 999:
                Bioinfo.writelines(subitems[i_s])
            else:
                Bioinfo.writelines("Na")
                Bioinfo.writelines("\t")
            Bioinfo.writelines("\n")
