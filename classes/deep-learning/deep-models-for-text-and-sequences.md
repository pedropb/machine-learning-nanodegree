# Deep Models for Text and Sequences

## Challenges for working with texts

In text, usually words that occur with the least frequency are the most important to derive meaning from the text. For example, "do" is a common word and doesn't help a model to classify a document. In contrast, "retinopathy" is a very rare word, that occurs 0.00001% in English, and the document will be most likely a medical document. These rare events are a problem in deep learning, because ideally, we want to have lots of data to train on.

Another problem is that we can use different words that have the same meaning. This means that the model will have to learn about these semantic relations, which means that we'll need to feed more training data to it.

![Challenges](images/dmft/Challenges.png)

