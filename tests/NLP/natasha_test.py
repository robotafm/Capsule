import io
from natasha import (
    Segmenter,
    MorphVocab,
    
    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    NewsNERTagger,
    
    PER,
    NamesExtractor,

    Doc
)

# Constants:
input_file = r'D:\Data\testdata\text\news.txt'

segmenter = Segmenter()
morph_vocab = MorphVocab()
emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)
syntax_parser = NewsSyntaxParser(emb)
ner_tagger = NewsNERTagger(emb)
names_extractor = NamesExtractor(morph_vocab)

with io.open(input_file, 'r', encoding='utf-8') as outf:
    text = outf.read()
doc = Doc(text)
doc.segment(segmenter)
print(doc.tokens[:5])
print(doc.sents[:5])
doc.tag_morph(morph_tagger)
print(doc.tokens[:5])
doc.sents[0].morph.print()
for token in doc.tokens:
    token.lemmatize(morph_vocab)
print(doc.tokens[:5])
{_.text: _.lemma for _ in doc.tokens}
doc.parse_syntax(syntax_parser)
print(doc.tokens[:5])
doc.sents[0].syntax.print()
doc.tag_ner(ner_tagger)
print(doc.spans[:5])
doc.ner.print()
for span in doc.spans:
    span.normalize(morph_vocab)
print(doc.spans[:5])
{_.text: _.normal for _ in doc.spans if _.text != _.normal}
{_.text: _.normal for _ in doc.spans if _.text != _.normal}
for span in doc.spans:
    if span.type == PER:
        span.extract_fact(names_extractor)
print(doc.spans[:5])
{_.normal: _.fact.as_dict for _ in doc.spans if _.type == PER}