"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""


def fn_hack_2(result):
    
    vocales = ["a","e","i","o", "u"]
    for i in vocales:
        result= result.replace(i,"")
    return result