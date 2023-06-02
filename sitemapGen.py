import xml.etree.cElementTree as ET
def registerSiteMaps(jsonItems):
    root = ET.Element('urlset')
    root.attrib['xmlns:xsi']="http://www.w3.org/2001/XMLSchema-instance"
    root.attrib['xsi:schemaLocation']="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd"
    root.attrib['xmlns']="http://www.sitemaps.org/schemas/sitemap/0.9"

    for item in jsonItems['list']:
        uid = item['id']
        dt =  item['date']
        item = ET.SubElement(root, "url")
        ET.SubElement(item, "loc").text = "https://europe.juna-life.ru/indexbase.php?PartNumber="+str(uid)
        ET.SubElement(item, "lastmod").text = dt
        ET.SubElement(item, "changefreq").text = "weekly"
        ET.SubElement(item, "priority").text = "1.0"

    tree = ET.ElementTree(root)
    tree.write('sitemap.xml', encoding='utf-8', xml_declaration=True)
