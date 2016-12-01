oses = ('mac', 'windows', 'linux')
interps = ('python', 'python3', 'pypy', 'ipy')

print('\t'.join(('program', 'os', 'interpreter', 'time')))
for os in oses:
    for interp in interps:
        with open('{}/{}.results.txt'.format(os, interp)) as f:
            for l in f:
                if l[0] != '#':
                    cols = l.strip().split()
                    p = int(cols[1][:-1])
                    for t in cols[2:]:
                        print('\t'.join(map(str, (p, os, interp, t))))

