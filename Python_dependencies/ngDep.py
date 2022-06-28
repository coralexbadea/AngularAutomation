import sys
import json 
import os
import glob
import re 

def getDependenciesForHTMLFile(path_to_file):
    #path_to_file = sys.argv[1]

    jsonFile = open("./MyHero.json", 'r')

    htmlFile = open(path_to_file, 'r')

    jsonDict = json.loads(jsonFile.read())
    htmlContent = htmlFile.read()

    jsonFile.close()
    htmlFile.close()

    finalDependencies = []

    for jsonKey in jsonDict.keys():
        if(jsonKey in htmlContent):
            finalDependencies += jsonDict[jsonKey]["dependencies"]
       
    return finalDependencies


def parse_tree_files(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + parse_tree_files(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles


def getDepsForHTMLFiles(htmlFilesPaths):
    total_dependencies = []
    for filePath in htmlFilesPaths:
        deps = getDependenciesForHTMLFile(filePath)
        total_dependencies += deps
    total_dependencies = list(set(total_dependencies))
    return total_dependencies
"""
def getDeclarationsFromModule(module_path):
    with open(module_path, 'r') as f:
        content = f.read()
        regex = "declarations"+ "(.*)"+"\[" + "(.*)" + "\]";
        body = re.search(regex, content)
        
        deps_string = body.group(2)
        deps = re.findall("[^\s\t\n\r]+Component",  deps_string);
        dep_list = [dep for dep in deps]
        return dep_list
"""  

def getBeginEndCustomModule(name, paranthesis, content):
    regex = name + "(.*)"+paranthesis[0]+"[\s]*[\n\r]+"
    m_function_head = re.search(regex, content)
    count = 1
    for i,c in enumerate(content[m_function_head.end():]):
        if c == paranthesis[0]:
            count += 1
        elif c == paranthesis[1]:
            count -= 1
        if count == 0:
            end = m_function_head.end() + i 
            break
    return (m_function_head.end(), end)


def getImportsFromModule(module_path):
    with open(module_path, 'r') as f:
        content = f.read()
        begin,end = getBeginEndCustomModule("imports", ['[', ']'], content)
        
        deps_string = content[begin: end]
        deps = re.findall("[^\s\t\n\r]+Module", deps_string);
        dep_list = [dep for dep in deps]
        return dep_list


if __name__ == "__main__":
    module_path = sys.argv[1]

    root_module_path = os.path.dirname(module_path)
    filesPaths = parse_tree_files(root_module_path)
    htmlFilesPaths = [file for file in filesPaths if (".html" in file)]
    total_deps = getDepsForHTMLFiles(htmlFilesPaths)
    print("Total Deps: ", ", ".join(total_deps))
    module_deps = getImportsFromModule(module_path)
    print("Module Deps: ", ", ".join(module_deps))
    
    onlyHtml_deps = [dep for dep in total_deps if dep not in module_deps]
    print("Dependencies Only In HTML: " + ", ".join(onlyHtml_deps))
    onlyModule_deps = [dep for dep in module_deps if dep not in total_deps]
    print("Dependencies Only In Module: " + ", ".join(onlyModule_deps))
