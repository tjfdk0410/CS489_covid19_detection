from transformers import (
    AutoConfig,
    AutoModelForSequenceClassification,
    AutoModel,
    AutoTokenizer)
import torch
import numpy 

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
                

        
    def inference(self, texts):
        txt_split = texts.split('\n')
        results= []

        for txt in txt_split:
            #print(txt)
            encoded_input = self.tokenizer(txt, return_tensors='pt')
            labels = torch.tensor([1]).unsqueeze(0)
            outputs = self.model(**encoded_input, )
            
            is_fake = bool(outputs[0].softmax(1).argmax())
            if is_fake:
                confidence = float(outputs[0].softmax(1)[0][1])
                
                print("sentence: " + txt )
                print("confidence: " + str(float(outputs[0].softmax(1)[0][1])) + " isFake : " + str(bool(outputs[0].softmax(1).argmax())))
                results.append((float(outputs[0].softmax(1)[0][1]) ,is_fake))

        return results