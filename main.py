import inference
import os 

from transformers import (
    AutoConfig,
    AutoModelForSequenceClassification,
    AutoModel,
    AutoTokenizer)
import torch
import numpy as np
import pandas as pd

model_path = 'result/maxseq140_batch64_ep12_aug/'
tokenizer_path = ''

class detect_fake_news:
    
    def __init__(self, device ):
        if device == 'gpu':
            self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        else: self.device = 'cpu'

        config = AutoConfig.from_pretrained(model_path, local_files_only=True)
        self.tokenizer = AutoTokenizer.from_pretrained( model_path, local_files_only=True)
        self.model = AutoModelForSequenceClassification.from_pretrained( model_path,config=config, local_files_only=True)
        

        
    def inference(self, text):
        encoded_input = self.tokenizer(text, return_tensors='pt')
        print(encoded_input)
        labels = torch.tensor([1]).unsqueeze(0)
        result = self.model(**encoded_input, labels=labels)
        
        return (list(result[-2]),result[-1])
    
    





config = AutoConfig.from_pretrained(model_path, local_files_only=True)
tokenizer = AutoTokenizer.from_pretrained( model_path, local_files_only=True)
model = AutoModelForSequenceClassification.from_pretrained( model_path,config=config, local_files_only=True)
        
texts =""

df=pd.read_csv('test.csv', usecols=['text'], low_memory = True)
for d in df.text:
    texts += d + '\n'
    

texts= """For the past week virologist Sarah Palmer and her colleagues at The Westmead Institute’s Centre for Virus Research in Sydney have been working overtime to unlock the secrets of COVID-19's Omicron variant.
Like detectives solving a crime, Professor Palmer and post-doctoral fellow Eunok Lee have gathered evidence from a collection of Omicron sequences taken from patients across the globe since November. Their mission is to try to understand the variant and to predict what it is likely to do next.
For anyone who is screaming that this next step should be "shut the borders!", Palmer believes Australia’s newly relaxed border settings remain appropriate. (More on why, later).
Professor Catherine Bennett, the chair in epidemiology at Deakin University agrees, but adds "the timing is terrible". "We've got so many things changing [as borders open for the first time], the last thing you need is Omicron."
South Australia grappled with precisely this dilemma as Premier Steven Marshall announced yesterday that the state's just-opened borders would stay that way albeit with additional testing requirements for those hoping to enter.
Yet it is clear we are about to discover for the first time what living with coronavirus really feels like.
The next step is to understand more about what's going on inside the virus. Researchers have already reported that Omicron features a huge number of mutations on its spike protein when compared with previous variants of SARS-CoV-2.
Palmer's research team hopes to take that understanding further. In the past week they have turned up more information about the nature of some of these mutations that help explain the anecdotal data emerging from South Africa.
"Omicron includes a spike protein mutation that makes it more infectious, but also includes a mutation on the spike protein that may allow it to reduce vaccine effectiveness," Palmer says.
It's important to emphasise that these discoveries are brand new, and further investigations are essential, however the latest clues about the nature of Omicron include a concerning finding.
When the virus is studied from another direction — by exploring the nucleocapsid, another viral protein which contributes to viral replication, rather than the spike protein — Palmer says her team found Omicron may have been created by what's called a "recombination" – a supercharged love child of the early Alpha variant plus Delta, something that has not been found in SARS-CoV-2 until now.
"We're very, very concerned," Palmer says, relaying the discovery with a calm and measured voice that belies its seriousness. "It indicates that possibly we could see that variants can recombine and if somebody is infected with two variants there could be a recombination that could lead to a more pathogenic and infectious virus."
With Omicron now found in 40 countries, including Australia where cases have hit the teens, the seriousness of Palmer's investigation requires little elaboration.
In South Africa, with very low vaccination rates, cases have also surged five or six-fold in the days since that first swab of Omicron was taken on November 8.
The level of concern Australians should be feeling ebbs and flows depending on how you look at it.
On the one hand scientists in South Africa believe the Omicron variant spreads twice as fast as Delta but there is also evidence that hospitalisation rates have not surged at the same pace.
Shabir Madhi, a South African vaccinologist, has argued this is "a positive signal".
Deakin's Catherine Bennett agrees that the fact the virus was found because of a "pattern of arising cases that also showed a pattern of reinfection”, rather than a spike in hospitalisations, is "reassuring news”.
Early data from South Africa shows positive cases found through testing have risen from 1 per cent on average to more than 15 per cent despite a modest rise in those seeking tests, Bennett says.
"This tends to suggest that the rise in cases is not just because more people are getting tested but it is actually a concentration of positive results that fits with a surge in new infections" she says.
And if, as Palmer suspects, the virus is learning to combine the strengths of different variants into new ones then this could prove to be a very dangerous skill-set.
There is another way of looking at this dilemma, according to Bennett, that offers a slightly more positive spin. It may be that so many mutations improve our understanding of the virus or represent the "full flush" of what it's capable of. Maybe so many mutations are catastrophic and the virus can't survive.
"The question is when do we reach a point where there are no new mutations, just new combinations? We will then have a bit of a handle on this virus in terms of its evolution," Bennett says.
Yet to truly understand the meaning of these discoveries more and more virus sequences need to be studied.
When Omicron is researched in large numbers, Palmer explains, it will become clearer whether these mutations are rare or common – "low frequency" or "high frequency" in scientific language. Virologists like Palmer can then create "phylogenetic trees", COVID-19's equivalent of a family tree, that will show how variants relate to each other, as well as within and across patients.
"This allows us to do a little detective work to say, OK, when did this [mutation] first originate and where did it originate," she says.
This understanding will also inform a picture of who is most vulnerable to the Omicron variant and how best to protect the population.
"We need to know where this virus is going? How is it changing? What does that mean for vaccines and boosters?" Palmer says.
Yet lab work can only go so far in predicting how Omicron will behave in a human population and it could be another month before patterns become evident as this variant spreads, Palmer says.
"We know Delta can be less severe when you're younger but how this Omicron variant will affect people who are elderly or those not protected by vaccination or immunocompromised, we don't know that yet" she says.
It may be tempting for some to advocate for a return to Australia's reflex of closed internal and external borders to keep COVID out.
Yet Palmer believes we need to accept that "this is what viruses do, they mutate".  
"Omicron won't be the only new variant we see because mutations make perfect evolutionary sense," she says. "The virus is changing in response to our immune systems to give itself a benefit."
Instead, Palmer warns that now is the time to double down on strategies known to reduce transmission. She is a proponent of masks, particularly on public transport, and admits she prefers outdoor dining and avoids eating indoors at restaurants.
Bennett – who promotes testing as a key method of keeping control of COVID spread – argues that Australia has taken the right approach allowing the return of citizens and permanent who have homes to isolate in but delaying opening borders to foreign nationals for a few more weeks.
"It takes pressure off the system so it's pragmatic but it's also precautionary," she says. "By pushing back our international border opening we get a couple more weeks to get a more complete picture of Omicron."
"""    

txt_split = texts.split('\n')
results= []

for txt in txt_split:
    #print(txt)
    encoded_input = tokenizer(txt, return_tensors='pt')
    labels = torch.tensor([1]).unsqueeze(0)
    outputs = model(**encoded_input, )
    
    is_fake = bool(outputs[0].softmax(1).argmax())
    if is_fake:
        confidence = float(outputs[0].softmax(1)[0][1])
        
        print("sentence: " + txt )
        print("confidence: " + str(float(outputs[0].softmax(1)[0][1])) + " isFake : " + str(bool(outputs[0].softmax(1).argmax())))
        results.append((float(outputs[0].softmax(1)[0][1]) ,is_fake))
