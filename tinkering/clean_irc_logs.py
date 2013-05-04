f = open("../references/IRC-Games/seeds/testgradius.log")
w = open("parsed_testgradius_logs.txt", 'w')
for line in f:
    w.write(' '.join(line.split()[3:]) + '\n')