# import from built-in modules 
from argparse  import ArgumentParser, RawTextHelpFormatter as RT
from pathlib   import Path
from re        import match
from xml.etree import ElementTree as ET

import numpy  as np
import pandas as pd

# import from personal modules 
from utils.xml  import xml_parser, PARS_xml
from utils.pflo import pflo_parser, PARS_pflo

FPATH = Path(__file__)
DIR = FPATH.parent

def getArguments():
    ''' parse the command-line interface
        the command line takes four required arguments  

        tpl: the file path to a .xml template
        ipt: the directory including the .xml files where we can extract the values of parameters
        opt: the file path to output the parameter values as a .csv file  
    '''  
    parser = ArgumentParser(formatter_class=RT)
    parser.add_argument('ipt',      type = str, help="the directory to the .xml files")
    parser.add_argument('opt',      type = str, help="the file path to output the parameter values")

    return parser.parse_args()

def main():
    args = getArguments()

    ipt = DIR.joinpath(args.ipt)
    opt = DIR.joinpath(args.opt)

    # plot simulated data 
    paras = {"files_num": []}
    for parameter in PARS_xml:
        paras[parameter] = []
    for parameter in PARS_pflo:
        paras[parameter] = []

    files = Path(ipt).glob('sim*.xml') # glob only supports wild cards: *, ?

    for f in files: 
        if match(r'^sim\d{1,3}.xml', f.name):

            fnum = int( ''.join(list(filter(str.isdigit, f.name))) )
            paras['files_num'].append(fnum)

            # extract data from .xml files 
            tree = ET.parse(f)
            for parameter in PARS_xml: 
                val = xml_parser(tree, parameter)
                paras[parameter].append(val)

            # extract data from .in geochemistry database 
            fname_geo = f.parent.joinpath(f'farea-full_nem{fnum}.in')

            with open(fname_geo, 'r') as f_geo:
                for parameter in PARS_pflo:
                    val = pflo_parser(f_geo, parameter)
                    paras[parameter].append(val)
    
    paras = pd.DataFrame.from_dict(data=paras)
    paras.sort_values(by=['files_num'], inplace=True)
    paras.to_csv(opt, header=True, index=False)

if __name__ == "__main__":
    main()
