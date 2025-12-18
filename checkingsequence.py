with open('human_data.txt','r') as f:
    seq=f.read()
    print('lets check if this human had diabetes !!ONLY FOR EDUCATIONAL PURPOSES IDK IF ITS REAL LOL!!')
    daib = 'AACTGGG'
    if daib in seq:
        print('yayy , daibetes detected ')
    else:
        print("nah mate you ain't got that dawg in you")
    