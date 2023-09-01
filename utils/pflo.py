AT_SEEPAGE = False

PARS_pflo = ['ph_seepage', 'al_seepage', 'tri_seepage', 'uran_seepage']
keys = {'ph_seepage': 'H+', 'al_seepage': 'Al+++', 'tri_seepage': 'Tritium', 'uran_seepage': 'UO2++'}

def pflo_parser(f, parameter):

    # read the file until it reaches the section for 'CONSTRAINT seepage'
    global AT_SEEPAGE
    if not AT_SEEPAGE:
        line = f.readline()
        while 'CONSTRAINT seepage' not in line:
            line = f.readline()

        for i in range(7):
            f.readline()
        AT_SEEPAGE = True

    # read the file until it reaches the line including the parameter value
    line = f.readline()
    while keys[parameter] not in line:
        line = f.readline()
    
    # output the parameter value
    for elem in line.split():
        try:
            val = float(elem)
            if parameter == 'uran_seepage': AT_SEEPAGE = False
            return val
        except ValueError:
            pass
    return 
