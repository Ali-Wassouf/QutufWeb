'''
Created on ٢٩‏/٠٥‏/٢٠١٠

@Created by: Muhammad Altabba
'''
from .....ALP.Models.Tagging.POSTags.CliticlessPOS import CliticlessPOS, CliticlessPOSConstants
from .....ALP.Models.Tagging.POSTags.POS import POSConstants
from .....ALP.Models.Tagging.POSTags.NominalPOS import NominalPOSConstants, NominalPOS
from .....ALP.Controllers.Morphology.Entities.UnderivedCliticless import UnderivedCliticless


class ProperNoun(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_hUBlqI34Ed-gg8GOK1TmhA
    """
    '''
    classdocs
    '''

    VoweledForm = ''

    UnvoweledForm = ''

    POS = NominalPOS()

    def __init__(self, unvoweled, voweled):
        '''
        Constructor
        '''
        self.VoweledForm = voweled
        self.UnvoweledForm = unvoweled

        self.POS = NominalPOS()
        self.POS.SubClass = NominalPOSConstants.SubClass.Proper_Noun
        self.POS.Definiteness = NominalPOSConstants.Definiteness.Definite_by_Itself
        self.POS.Number = CliticlessPOSConstants.Number.Singular

    pass

    def ReturnAsUnderivedCliticless(self):
        underivedCliticless = UnderivedCliticless(self.UnvoweledForm, self.VoweledForm)
        underivedCliticless.POS = self.POS.Clone()

        return underivedCliticless

    pass
