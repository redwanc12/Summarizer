from Tkinter import *
import ttk
from ScrolledText import *

DiscoverKeywords = [
'found', 'reveals', 'shows', 'discovered', 'detected', 'identified', 'invented', 'revealed', 'learned',
'unveils', 'tells', 'main', 'realized', 'confirm', 'confirms', 'confirmed', 'new research', 'figured out', 
'observed', 'noticed', 'new studies', 'recent studies','new evidence', 'witnessed', 'presented', 'announced',
'theorize', 'theorized'
]

speakingKeywords = [
'says', 'wrote', 'said', 'claimed', 'stated', 'reported', 'say', 'told'
]
def summarizer(): #finds main sentance of the article
  mainpointlist = []
  article = articleTB.get()
  article = article.replace('\n',' ') #removes line formatting
  article = article.replace('? ', '. ')
  article = article.replace('! ', '. ')
  article = article.replace('"', '')
  sentances = article.split('. ') #splits the article into a list a sentances
  for sents in sentances:
      for keys in speakingKeywords:
          if keys in sents:
              mainpointlist.append(sents)
      for keys in DiscoverKeywords: #checks each sentance to see if it contains DiscoverKeywords
          if keys in sents:
            mainpointlist.append(sents)
  finalSummary = '. '.join(mainpointlist)
  resultPad.delete('1.0', END)
  resultPad.insert(INSERT, finalSummary)
  global newtext
  newtext = finalSummary
                   
def reduceCalc():
    original = articleTB.get()
    new = newtext
    decimal = float(len(new))/float(len(original))
    percent = round(decimal * 100)
    percent = int(percent)
    reducedPercent = 100 - percent
    differenceText.set('Reduced by ' + str(reducedPercent) +'%')
    
def both():
    summarizer()
    reduceCalc()

    
app = Tk()
app.title('Summarizer')
app.geometry('450x300+200+200')


enterTextString = StringVar()
enterTextString.set('Enter you article:')
label1 = Label(app, textvariable = enterTextString, height = 4)
label1.pack()
articleInput = StringVar(None)
articleTB = Entry(app, textvariable=articleInput)
articleTB.pack()
summarizerButton = Button(app, text='Summarize now!', width=20, command=both)
summarizerButton.pack()
'''resultText = StringVar()
result = Label(app, textvariable = resultText, height = 4, wraplengt=400)
result.pack()'''
differenceText = StringVar()
difference = Label(app, textvariable = differenceText, height = 4)
difference.pack()
resultPad = ScrolledText(app, width=50, height=1500)
resultPad.pack()

app.mainloop()