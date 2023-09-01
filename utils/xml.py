PARS_xml  = ['perm_u', 'poro_u', 'alpha_u', 'm_u', 'sr_u', 'r_hist', 'r_mid']

def findperm_u(xmltree):
    return xmltree.find("./materials/material[@name='Soil_5: Upper_aquifer']/permeability").get('x') 

def findporo_u(xmltree):
    return xmltree.find("./materials/material[@name='Soil_5: Upper_aquifer']/mechanical_properties/porosity").get('value') 

def findalpha_u(xmltree):
    return xmltree.find("./materials/material[@name='Soil_5: Upper_aquifer']/cap_pressure/parameters").get('alpha') 

def findm_u(xmltree):
    return xmltree.find("./materials/material[@name='Soil_5: Upper_aquifer']/cap_pressure/parameters").get('m') 

def findsr_u(xmltree):
    return xmltree.find("./materials/material[@name='Soil_5: Upper_aquifer']/cap_pressure/parameters").get('sr') 

def findr_hist(xmltree):
    return xmltree.find("./boundary_conditions/boundary_condition[@name='BC 3: Mass Flux']/liquid_phase/liquid_component/inward_mass_flux[@start='0.0']").get('value') 

def findr_mid(xmltree):
    return xmltree.find("./boundary_conditions/boundary_condition[@name='BC 3: Mass Flux']/liquid_phase/liquid_component/inward_mass_flux[@start='6.16635504e+10']").get('value') 

def xml_parser(xmltree, element):
    return globals()[f'find{element}'](xmltree)
