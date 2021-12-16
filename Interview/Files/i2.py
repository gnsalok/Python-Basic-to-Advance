'''
Find the overlap of the queue.

Q1 {Name: Q1, country: []string("US", IN), Locale: []string{"english", "hindi"}}
Q2 {Name: Q2, country: []string("US"), Locale: []string{"english", "spanish"}}
Q3 {Name: Q3, country: []string("US"), Locale: []string{"german", "spanish"}}
Q4 {Name: Q4, country: []string("IN"), Locale: []string{"german", "spanish"}}
Q5 {Name: Q5, country: []string("IN"), Locale: []string{"arabic"}}

Q1 <-> Q2 <-> US <-> english
Q2 <-> Q3 <-> US <-> spanish
'''


def parse(d):
    dictionary = dict()
    # Removes cur
    pairs = d.strip('{}').split(', ')
    for i in pairs:
        pair = i.split(': ')
        # Other symbols from the key-value pair should be stripped.
        dictionary[pair[0].strip('\'\'\"\"')] = pair[1].strip('\'\'\"\"')
    return dictionary


try:
    geeky_file = open('file.txt', 'rt')
    lines = geeky_file.read().split('\n')
    for l in lines:
        if l != '':
            dictionary = parse(l)
            print(dictionary)
    geeky_file.close()
except:
    print("Something unexpected occurred!")
