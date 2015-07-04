#!/usr/bin/python

import wx
import os
import os.path

debug = 1
#debug = 0

#by christopher rehm
#may 25 2015
#a simple program that does word count in a txt document
#will possibly upgrade it to something that does more later
if debug == 1:
    print("hello world")
    print("file to open")

#############################################################
#############################################################
#############################################################
class MyFrame(wx.Frame):

    ###########################################################

    def __init__(self):
        wx.Frame.__init__(self, None, -1, "The Text Analyser", size=(600, 470))
        #create an object instance of the file data analysis class
       # mydatafile = FileDataAnalysis() 

        panel = wx.Panel(self, -1)
      

        self.displayTitles()
        self.updateDataDisplay("00000")
      

    ################################################################################

   

    def ExitProgram(self, event):
        self.Close(True)
        self.Destroy()

    #######################################################################################
    
    def OnAbout(self, event):
        pass

    ######################################################################################
    
    def LoadFile(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.getcwd(), "", "*.*", style=wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename =dlg.GetFilename()
            self.dirname  =dlg.GetDirectory()
            # Open the file, read the contents and set them into
            # the text edit window

            filehandle=os.path.join(self.dirname, self.filename)

           #create signal, there is a new file to analyse

            mydatais.analysedfile =filehandle
            mydatais.analysefile(filehandle)
            #self.displayTitles(self.panel) ####THIS IS WHAT CRASHES; SAYS THERE IS NO PANEL
            #self.updateDataDisplay("0")

    #####################################################################################
           
    def Save(self, event):
        pass
 #########################################################################
    def displayTitles(self):
        txt11 =wx.StaticText(self.panel, -1, "name of file analysed",       pos=(20,20))
        txt12 =wx.StaticText(self.panel, -1,"total number of words in file",pos=(20,60))
        txt19 =wx.StaticText(self.panel, -1,"unique words in file",         pos=(20,100))
        txt13 =wx.StaticText(self.panel, -1, "average number of letters per word", pos=(20,140))
        txt14 =wx.StaticText(self.panel, -1, "average sentence length",            pos=(20,180))
        txt15 =wx.StaticText(self.panel, -1, "average clauses per sentence",       pos=(20,220))
       # txt16 =wx.StaticText(self.meframe, -1, "0",                           pos=(320,260))
        #txt17 =wx.StaticText(self.meframe, -1, "0",                           pos=(320,300))
        #txt18 =wx.StaticText(self.meframe, -1, "0",                           pos=(320,340))


    ########################################################################
    def updateDataDisplay(self, mydataloc):
        pass
            #output
        txt11 =wx.StaticText(self.panel, -1, mydataloc,             pos=(320,20))
       # txt12 =wx.StaticText(onpanel, -1, str(mydatais.rawwordcount) ,       pos=(320,60))
        #txt19 =wx.StaticText(onpanel, -1, str(mydatais.uniquewordcount),     pos=(320,100))
        #txt13 =wx.StaticText(self.meframe, -1, str(self.avgwordcount),        pos=(320,140))
        #txt14 =wx.StaticText(self.meframe, -1, str(self.avgsentencelength),   pos=(320,180))
        #txt15 =wx.StaticText(self.meframe, -1, str(self.avgnumberofwordspara),pos=(420,220))
       # txt16 =wx.StaticText(self.meframe, -1, "0",                           pos=(320,260))
        #txt17 =wx.StaticText(self.meframe, -1, "0",                           pos=(320,300))
        #txt18 =wx.StaticText(self.meframe, -1, "0",                           pos=(320,340))
 
    #####################################################################################  


#######################################################################################


class FileDataAnalysis(object):
    def __init__(self):
        aframe = MyFrame()
        self.analysedfile ="none currently"
        self.rawwordcount = 0
        self.uniquewordcount = 0
        self.lettersperword = 0
        self.wordspersentence = 0
        self.clausespersentence = 0
        self.clausesintext = 0
        self.wordsperparagraph = 0
        self.numberofparagraphs = 0
        self.datafromfile = ""
        self.datafromfileunique = ""
        aframe.Show(True)
        

    ################ 
    # get file to be analysed
    ################
   
    ################################################################################

    def analysefile(self, filehandle):
        myfile =open(filehandle, "rb")
        newstring = myfile.read()
        #now count sentences, clauses first

        #now pull out all the punctuation, and sort the words.
        newstring = str.replace(str(newstring),"."," ")
        newstring = str.replace(str(newstring),","," ")
        newstring = str.replace(str(newstring),":"," ")
        newstring = str.replace(str(newstring),";"," ")
        newstring = str.replace(str(newstring),"\""," ")
        newstring = str.replace(str(newstring),","," ")
        newstring = str.lower(newstring)

        list =  str.split(newstring)
        print(list)
        list2 = sorted(list)
        length = len(list2)
        if debug == 1:
            print(list2)  #debug tool

        self.numberofwords = len(list2)
        if debug == 1:
            print("The length of your text in words is ", len(list2))
        a = 1
        ulength =length
        while (a < ulength-1):
            if debug == 1:
                print(list2[a],list2[a+1]) #debug tool
                print("\n") #debug tool
            if list2[a] == list2[a+1]:
                list2.remove(list2[a+1])
                ulength = ulength - 1
            else:
                a = a+1

        #print("The number of unique words in your text is ", ulength
        #self.updatedataresults()
        #print list2

   


###############################################################
##############################################################        


#######################################################################################
#######################################################################################

if __name__ == '__main__':
    app = wx.App()
    mydatais = FileDataAnalysis()
   
    app.MainLoop()
