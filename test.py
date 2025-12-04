import nltk
from nltk.corpus import stopwords
# nltk.download('stopwords')
# nltk.download('punkt_tab')
import os
import spacy
import en_core_web_md
import gensim
from gensim import corpora
from gensim.models import CoherenceModel
import string
import src.loader as loader
# import pyLDAvis.gensim_models as gensimvis
# import pyLDAvis


def get_slide_data():
    datadir="data/generative-ai/"

    tylers_notes=[]
    slides=[]
    for folder in os.listdir(datadir):
        try:
            tylers_notes.append(loader.load_text(os.path.join(datadir,folder,"tylers-notes.md")))
            # slides.append(loader.load_pdf(os.path.join(datadir,folder,"slides.pdf"))[0])
        except:
            pass
    # slides=[]
    # for s in os.listdir(datadir):
        # if os.path.isfile(os.path.join(datadir,s)):
            # try:
                # slides.append(loader.load_pdf(os.path.join(datadir,s))[0])
                # print(f'finished: {s}')
            # except KeyboardInterrupt as e:
                # raise e
            # except:
                # print(f"failed: {s}")
    # return slides
    return tylers_notes+slides

class dirichlet:

    def __init__(self,texts,num_topics=10,random_state=100,chunksize=1000,passes=50,iterations=100):
        self.stop_words = stopwords.words('english')
        self.nlp=spacy.load("en_core_web_md")
        self.texts=texts
        self.texts_clean=[]
        for text in self.texts:
            self.texts_clean.append(self.clean_text(text))
        self.lemmas=self.lemmatization(self.texts_clean)
        self.dictionary = corpora.Dictionary(self.lemmas)
        print(self.dictionary)
        if len(self.dictionary) > 0:
            self.doc_term_matrix = [self.dictionary.doc2bow(rev) for rev in self.lemmas]
        else:
            self.doc_term_matrix = []
        
        if self.doc_term_matrix:
            self.LDA = gensim.models.ldamodel.LdaModel
            self.lda_model = self.LDA(
                corpus=self.doc_term_matrix,
                id2word=self.dictionary,
                num_topics=num_topics,
                random_state=random_state,
                chunksize=chunksize,
                passes=passes,
                iterations=iterations
            )
            for topic in self.lda_model.print_topics():
                print(topic)
                print('---')
        else:
            print("Document term matrix is empty, cannot build LDA model.")
        
    def remove_stopwords(self,text):
        textArr = text.split(' ')
        rem_text = " ".join([i for i in textArr if i not in self.stop_words])
        return rem_text

    def clean_text(self,text):
        delete_dict = {sp_char: ' ' for sp_char in string.punctuation}
        delete_dict[' '] = ' '
        table = str.maketrans(delete_dict)
        text1 = text.translate(table)
        textArr = text1.split()
        text2 = ' '.join([w for w in textArr if not w.isdigit() and len(w) > 1])
        return self.remove_stopwords(text2.lower())

    def lemmatization(self,texts, allowed_postags=['NOUN','ADJ']):
        output = []
        for sent in texts:
            doc = self.nlp(sent)
            # print([token for token in doc if token.pos_ == 'VERB'])
            output.append(
                [token.lemma_ for token in doc if token.pos_ in allowed_postags])
        return output

# print(tylers_notes_cleaned['lecture-3'])
# print(lemmatization(tylers_notes_cleaned.values()))
# print('---')
# print(lemmatization(tylers_notes_cleaned.values(),['VERB']))

# text_list = yelp_review['text'].tolist()
# tokenized_reviews = lemmatization(text_list)
if __name__=='__main__':
    slides=get_slide_data()
    print('starting LDA')
    d=dirichlet(slides,num_topics=5)

    # print(d.clean_text(list(slides.values())[0]))
    # print(slides)
    total_docs = len(d.doc_term_matrix)
    if total_docs > 0:
        print('\nPerplexity:', d.lda_model.log_perplexity(
            d.doc_term_matrix, total_docs=total_docs))
        coherence_model_lda = CoherenceModel(
            model=d.lda_model,
            texts=d.lemmas,
            dictionary=d.dictionary,
            coherence='c_v'
        )
        coherence_lda = coherence_model_lda.get_coherence()
        print('Coherence:', coherence_lda)

        topic_dict={}
        for doc in d.doc_term_matrix:
            topic_weights=d.lda_model[doc]
            for topic,weight in topic_weights:
                if topic in topic_dict:
                    topic_dict[topic]+=weight
                else:
                    topic_dict[topic]=weight
        print(topic_dict)
    else:
        print("No documents to evaluate coherence or perplexity.")
