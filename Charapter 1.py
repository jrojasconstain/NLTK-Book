import nltk
from nltk.book import *
import matplotlib

"""
*** Introductory Examples for the NLTK Book ***
Loading text1, ..., text9 and sent1, ..., sent9
Type the name of the text or sentence to view it.
Type: 'texts()' or 'sents()' to list the materials.
text1: Moby Dick by Herman Melville 1851
text2: Sense and Sensibility by Jane Austen 1811
text3: The Book of Genesis
text4: Inaugural Address Corpus
text5: Chat Corpus
text6: Monty Python and the Holy Grail
text7: Wall Street Journal
text8: Personals Corpus
text9: The Man Who Was Thursday by G . K . Chesterton 1908
"""

# 1.3 Searching text
# Concordance: every ocurrence of a word with some context
text1.concordance("monstrous")
text4.concordance("America")
text7.concordance("investment")

# Similar: other words that appear in a similar range of contexts
text1.similar("monstrous")
text2.similar("monstrous")
text7.similar("investment")

# Common contexts: examine the contexts that are shared by two or more words
text2.common_contexts(["monstrous", "very"])
text7.common_contexts(["investment", "market"])

# Dispersion plot: positional information about location of a word in the text 
text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
