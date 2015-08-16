'''One way of solving the exercise is listed below. There are couple of things to note about this solution:

since the names and email for authors are unique for each author, we use "find". The text method can be used to get the value of the tag.
since "insr" can contain several values, we use "findall" and iterate the returned list.
we access the attributes of a tag by method "attrib" and using the attribute name "iid" '''




def get_authors(root):
    authors = []
    for author in root.findall('./fm/bibl/aug/au'):
        data = {
                "fnm": None,
                "snm": None,
                "email": None,
                "insr": []
        }
        data["fnm"] = author.find('./fnm').text
        data["snm"] = author.find('./snm').text
        data["email"] = author.find('./email').text
        insr = author.findall('./insr')
        for i in insr:
            data["insr"].append(i.attrib["iid"])
        authors.append(data)

    return authors
