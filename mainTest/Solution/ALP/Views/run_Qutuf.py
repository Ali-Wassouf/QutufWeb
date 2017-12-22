'''
Created on ١١‏/٠٥‏/٢٠١٠

@author: Muhammad Altabba
'''

import codecs
from ....root import ROOT_DIR
import os
print(ROOT_DIR)

from ...ALP.Controllers.TextEntities.TextEncapsulator import *
#from .....mainTest import  root

#Set Files Locations Variables:
'''
Change the next few parameters as appropriate.
'''

baseDirectory = ROOT_DIR
baseDirectoryOfQutufDB = os.path.join(baseDirectory,'Data')
inputTextFile = os.path.join(baseDirectoryOfQutufDB,'test_Qutuf.txt')
baseDirectoryOfAlKhalilDB = os.path.join(baseDirectory,'AlKhalil_V1_Modified','db')
ouputXmlFile = os.path.join(baseDirectory,'Output','test.xml')
ouputHtmlFile = os.path.join(baseDirectory,'Output','test.html')


#Set Operations Variables:
prematureTaggingPositiveThreshold = 0.0
prematureTaggingNegativeThreshold = -0.0

overdureTaggingThreshold  = None
overdureTaggingTopReservants  = None




'''
The next few parameters are fixed do not change them.
'''
procliticsXmlFile = baseDirectoryOfQutufDB + 'MorphologyTransducers\\Proclitics.xml'
encliticsXmlFile = baseDirectoryOfQutufDB + 'MorphologyTransducers\\Enclitics.xml'
prematureTaggingRulesXmlFile = baseDirectoryOfQutufDB + 'TaggingRepository\\PrematureTaggingRules.xml'
overdueTaggingRulesXmlFile = baseDirectoryOfQutufDB + 'TaggingRepository\\OverdueTaggingRules.xml'
rootsFolder = 'roots2'

def runit(phrase):
    # Initialize:
    text = TextEncapsulator()

    # Load Data from Files:
    text.LoadFromFiles(baseDirectoryOfAlKhalilDB, rootsFolder,
                       procliticsXmlFile, encliticsXmlFile,
                       prematureTaggingRulesXmlFile,
                       overdueTaggingRulesXmlFile)

    # Read input text into Qutuf:
    f = codecs.open(inputTextFile, 'r', 'utf-8')
    string = phrase#f.read()
    f.close()
    text.String = phrase #string

    # Operate:
    text.Tokenize()

    text.Normalize(2)

    text.CompoundParsing()

    text.PrematureTagging()

    text.ParseClitics()

    text.PatternMatching(prematureTaggingPositiveThreshold, prematureTaggingNegativeThreshold)

    text.OverdueTagging(overdureTaggingThreshold, overdureTaggingTopReservants)

    # Print:
    print('---------------------------------------------------------------------------')
    text.Print()
    print('---------------------------------------------------------------------------')
    outputDict = {}
    # Write Output Files:
    xmlStreamWriter = io.StringIO()
    text.RenderHtml(xmlStreamWriter)
    writer = codecs.open(ouputHtmlFile, 'w', 'utf-8')
    writer.write(xmlStreamWriter.getvalue())
    writer.close()
    outputDict['HTML'] = xmlStreamWriter.getvalue()

    xmlStreamWriter = io.StringIO()
    text.RenderXml(xmlStreamWriter)
    writer = codecs.open(ouputXmlFile, 'w', 'utf-8')
    writer.write(xmlStreamWriter.getvalue())
    writer.close()
    outputDict['xml'] = xmlStreamWriter.getvalue()

    return outputDict
