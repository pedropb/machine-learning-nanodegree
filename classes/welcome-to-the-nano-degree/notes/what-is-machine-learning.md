# Introduction

What is machine learning?

"In the world there are humans and machines. Humans learn from past experiences. Machines need to be programmed. Machine learning is programming a machine to learn from past experiences. And past experiences for machines are *data*"

# Decision Trees

Decision trees are a series of questions you ask at one's data to come to a decision. In the example, we built the questions about the features that had a nice split over the data. The data is below, and so is the compiled decision tree.

| Gender | Age | App Downloaded|
|--------|-----|---------------|
| F | 15 | Pokemon Go |
| M | 12 | Pokemon Go |
| F | 25 | WhatsApp |
| M | 32 | Snapchat |
| F | 40 | WhatsApp |
| M | 14 | Pokemon Go |

![Alt text](http://g.gravizo.com/g?
  digraph G {
    aize ="4,4";
    "Ask age";
    "Ask age" -> "suggest Pokemon Go" [label="<20"];
    "Ask age" -> "Ask gender" [label=">=20"];
    "Ask gender" -> "suggest WhatsApp" [label="F"];
    "Ask gender" -> "suggest Snapchat" [label="M"];
  }
)