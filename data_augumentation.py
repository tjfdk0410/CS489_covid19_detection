import pandas as pd
import numpy as np
import nlpaug.augmenter.word as nlpaw
from tqdm import tqdm


##불러올 파일 경로 수정 부탁드려요!!##
train_df = pd.read_csv('/train2.csv', header=None)
train_df = train_df.drop(index=0, axis=0)
train_df.columns=['comment_text', 'isFake']
#train_df.head()

def augment_sentence(sentence, aug, num_threads):
  """

  Input:
    -sentence: A string of text
    -aug: An augmentation object defined by the nplaug library
    -num_threads: Integer controlling the number of threads to use 
                  if augmenting text via cpu
  
  Output:
    - A string of text that been augmented
  """
  return aug.augment(sentence, num_thread=num_threads)


def augment_text(df, aug, num_threads, num_times):
  """

  Takes a pandas DataFrame and augments its text data.

  Input:
    -df: A pandas DataFrame containing the columns:
            -'comment_text' containing strings of text to augent.
            -'isFake' binary target variable containing 0's and 1's.
    -aug: Augmentation object difined by the nlplaug library.
    -num_threads: Integer controlling number of threads to use if augmenting
                  text via CPU
    -num_times: Integer representing the number of times to augment data.

  Output:
    -df: Copy the same pandas DataFrame with augmented data appended to it 
          and with rows randomly shuffled.
    """
  #Get rows of data to augment
  to_augment = df[df['isFake']=='1']
  to_augmentX = to_augment['comment_text']
  to_augmentY = np.ones(len(to_augmentX.index)*num_times, dtype=np.int8)

  #Build up dictionary containing augmented data
  aug_dict = {'comment_text':[], 'isFake': to_augmentY}
  for i in tqdm(range(num_times)):
    augX = [augment_sentence(x, aug, num_threads) for x in to_augmentX]
    aug_dict['comment_text'].extend(augX)

  #Build DataFrame containing augmented data
  aug_df = pd.DataFrame.from_dict(aug_dict)

  return df.append(aug_df, ignore_index = True).sample(frac=1, random_state=42)


#Define nlpaug augmentation object
#aug10p = nlpaw.ContextualWordEmbsAug(model_path='distilbert-base-uncased', action="substitute")
aug10p = nlpaw.ContextualWordEmbsAug(model_path = 'bert-base-uncased', aug_min=1, aug_p=0.1, action="substitute")


#Upsample minority class ('isFake'==1) to create a roughly 50-50 class distribution
balanced_df = augment_text(train_df, aug10p, num_threads=8, num_times=3)


##저장할 파일 경로 수정 부탁드려요###
balanced_df.to_csv("저장할 파일 경로", header=False, index=False)