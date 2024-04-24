from django.shortcuts import render
from .forms import DocumentForm
from .models import Document
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tag import pos_tag
from nltk.tokenize.treebank import TreebankwordDetokenizer
import nltk

def Diminution_document(content):
    sentences = sent_tokenize(content)
    tagged_sentences = [pos_tag(word_tokenize(sentence)) for sentence in sentences]
    stop_words = set(stopwords.words('english'))
    filtered_sentences = [
        [word for word, pos in tagged_sentences if word.lower() not in stop_words and pos in {'NN','VB','JJ'}]
        for tagged_sentence in tagged_sentences
    ]
    words = [word for sentence in filtered_sentences for word in sentence]
    freq_dist = FreqDist(words)
    top_words = [word for word, freq in freq_dist.most_common(10)]
    Diminution_sentences = [
        sentence for sentence in sentences
        if any(word in sentence for word in top_words)
    ]
    Diminution_content = TreebankwordDetokenizer().detokenize(Diminution_sentences)
    return Diminution_content
def home(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST,request.FILES)
        if form.is_valid():
            document = form.save()
            Diminution_content = Diminution_document(document.content)
            return render(request, 'Diminution_app/result.html',{'document':document,'Diminution_content':Diminution_content})
        else:
            form = DocumentForm()
        return render(request, 'Diminution_app/index.html',{'form':form})
# Create your views here.
